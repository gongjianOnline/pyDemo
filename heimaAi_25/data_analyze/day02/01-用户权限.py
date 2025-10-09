"""
查看全部用户
    getent passwd
创建普通用户
    useradd -m itheima
    passwd itheima
切换用户
    su itheima
---
查看所有组
    getent group
创建用户组
    groupadd [-g -d] 用户组名
    -g 指定用户的组,不指定 -g , 会创建同组名并自动加入,指定 -g 需要组已经存在,如已存在着同组名,必须使用 -g
    -d 指定用户 HOME 路径,不指定HOME目录默认在: /home/用户名
删除用户组
    groupdel [-r] 用户组名
    -r 删除用户HOME目录
查看用户所属组
    id [用户名]
    不写则查自身
修改用户所属组
    usermod -aG 用户组 用户名
        将指定用户加入到指定用户组中

---
chmod 修改文件和文件夹权限
    语法: chmod u=rwx,g=rx,o=x 1.txt  将文件权限修改为 rwxr-x--x
        chmod -R u=rwx,g=rx,o=x test 将文件夹 test 以及里面全部内容改成 rwxr-x--x
    语法糖: 0:无权限 4:只读 2:只写 1:可执行
        chmod -R 777 文件名/目录名

chown 修改属主权限
    只能通过root账号修改
    chown [-R] 用户:用户组 文件或文件夹


"""