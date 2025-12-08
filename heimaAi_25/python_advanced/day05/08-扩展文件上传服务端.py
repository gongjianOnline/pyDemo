import socket
import os
from itertools import count

# 确保目录存在
os.makedirs("./file", exist_ok=True)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("10.1.68.179", 12306))
server_socket.listen(5)

accept_socket, client_info = server_socket.accept()
count =  0
with open(f"./file/serveFile{count}.txt", "wb") as f:
    count += 1
    while True:
        recv_data = accept_socket.recv(1024)
        if not recv_data:
            break
        f.write(recv_data)

accept_socket.close()
# server_socket.close()