from functools import wraps
from flask import request, jsonify


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')  # 可以从 headers 中获取
        if not token:
            return jsonify({"code": 401, "message": "Missing token"}), 401
        # 你也可以加 token 的合法性验证逻辑
        return f(*args, **kwargs)
    return decorated_function