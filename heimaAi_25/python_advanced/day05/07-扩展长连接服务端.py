import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("10.1.68.179",12306))
server_socket.listen(5)
accept_socket, client_info = server_socket.accept()
while True:
    recv_data_bytes = accept_socket.recv(1024)
    recv_data = recv_data_bytes.decode('utf-8')
    print("服务器端打印:",recv_data)

    if recv_data == "exit":
        break

accept_socket.close()

