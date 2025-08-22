import os
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple
from functools import lru_cache
from sqlalchemy import create_engine, MetaData, Table, select, insert, update, delete, text
from sqlalchemy.engine import Engine, Result,URL
from contextlib import contextmanager

# 从环境变量读取（生产更安全）
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3307"))
DB_NAME = os.getenv("DB_NAME", "vote")

def sqlalchemy_url():
    return URL.create(
        drivername="mysql+pymysql",
        username=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        query={"charset": "utf8mb4"},  # 防止乱码
    )

# --- 1) Engine 全局单例 ---
@lru_cache(maxsize=1)
def get_engine() -> Engine:
    return create_engine(
        sqlalchemy_url(),
        pool_pre_ping=True,     # 探活，避免 “MySQL server has gone away”
        pool_recycle=3600,      # 回收时间（秒）
        future=True,            # 使用 2.0 风格 API
        echo=False,             # 调试时可设 True
    )

# --- 2) 元数据与表缓存（反射已存在表结构） ---
_metadata = MetaData()
@lru_cache(maxsize=128)
def get_table(table_name: str) -> Table:
    eng = get_engine()
    return Table(table_name, _metadata, autoload_with=eng)

# --- 3) 上下文：读用 connect，写用 begin（带事务） ---
@contextmanager
def connect():
    conn = get_engine().connect()
    try:
        yield conn
    finally:
        conn.close()

@contextmanager
def begin():
    with get_engine().begin() as conn:  # 自动 commit/rollback
        yield conn

# --- 4) 通用 CRUD（无模型类，按表名操作） ---
def create_row(table: str, values: Dict[str, Any]) -> int:
    t = get_table(table)
    with begin() as conn:
        res: Result = conn.execute(insert(t).values(**values))
        # MySQL 下可用 lastrowid；跨库可返回受影响行数或主键查询
        return res.lastrowid or 0

def get_by_id(table: str, pk_name: str, pk_value: Any) -> Optional[Dict[str, Any]]:
    t = get_table(table)
    stmt = select(t).where(getattr(t.c, pk_name) == pk_value)
    with connect() as conn:
        row = conn.execute(stmt).mappings().first()
        return dict(row) if row else None

def query_rows(
    table: str,
    where: Optional[List[Tuple[str, str, Any]]] = None,  # [(col, op, val)], 如 [("name","=", "Tom")]
    order_by: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> List[Dict[str, Any]]:
    t = get_table(table)
    stmt = select(t)
    # 动态 where
    if where:
        from sqlalchemy import and_, or_
        conds = []
        for col, op, val in where:
            col_expr = getattr(t.c, col)
            if op == "=":
                conds.append(col_expr == val)
            elif op == "!=":
                conds.append(col_expr != val)
            elif op == ">":
                conds.append(col_expr > val)
            elif op == "<":
                conds.append(col_expr < val)
            elif op.lower() == "like":
                conds.append(col_expr.like(val))
            elif op.lower() == "in" and isinstance(val, (list, tuple, set)):
                conds.append(col_expr.in_(list(val)))
            else:
                raise ValueError(f"Unsupported operator: {op}")
        from sqlalchemy import and_
        stmt = stmt.where(and_(*conds))

    # 排序
    if order_by:
        # 支持 "id desc" / "name asc"
        parts = order_by.split()
        col = getattr(t.c, parts[0])
        if len(parts) > 1 and parts[1].lower() == "desc":
            col = col.desc()
        stmt = stmt.order_by(col)

    # 分页
    if limit is not None:
        stmt = stmt.limit(limit)
    if offset is not None:
        stmt = stmt.offset(offset)

    with connect() as conn:
        rows = conn.execute(stmt).mappings().all()
        return [dict(r) for r in rows]

def update_by_id(table: str, pk_name: str, pk_value: Any, values: Dict[str, Any]) -> int:
    t = get_table(table)
    with begin() as conn:
        res: Result = conn.execute(
            update(t).where(getattr(t.c, pk_name) == pk_value).values(**values)
        )
        return res.rowcount

def delete_by_id(table: str, pk_name: str, pk_value: Any) -> int:
    t = get_table(table)
    with begin() as conn:
        res: Result = conn.execute(
            delete(t).where(getattr(t.c, pk_name) == pk_value)
        )
        return res.rowcount

# --- 5) 如需直接写 SQL（可选） ---
def exec_sql(sql: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    with connect() as conn:
        rows = conn.execute(text(sql), params or {}).mappings().all()
        return [dict(r) for r in rows]