import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("10.1.68.179",12306))

recv_data_bytes = client_socket.recv(1024)
recv_data = recv_data_bytes.decode()
print("客户端收到",recv_data)

client_socket.send("卷起来".encode())

client_socket.close()