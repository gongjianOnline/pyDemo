"""
服务端端口复用
    当客户端和服务端建立连接后,服务端退出后端口号不会立即释放,需要等待大概1-2分钟
    格式:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ...
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    细节:
        SOL_SOCKET      当前的 scoket 对象
        SO_REUSEADDR    端口重用(属性名)
        True 成立(属性值)
"""
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定 IP 和 端口号
server_socket.bind(("10.1.68.179",12306))
# 设置最大监听数(允许挂载,挂起的数量)
server_socket.listen(5)
# 具体的监听动作,接受客户端信息,并获取 1 个socket对象,负责和客户端交互
# accept_socket 负责和客户端交互的对象
# client_info 客户端的IP信息
print(1)
accept_socket,client_info = server_socket.accept()
print(2,client_info)
# 给客户端法一句话,二进制形式
accept_socket.send("干啥呢".encode('utf-8'))
# 接受客户端信息
# 一次性接受客户端数据的1024字节,超出则无法接受
recv_data_bytes = accept_socket.recv(1024)
recv_data = recv_data_bytes.decode('utf-8')
print("服务器端打印",recv_data)

# 和客户端交互的 scoket 关闭
accept_socket.close()

# 设置端口号适用
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)