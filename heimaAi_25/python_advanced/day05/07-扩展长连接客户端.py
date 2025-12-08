import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("10.1.68.179",12306))

while True:
    data = input("请输入文字: ")

    client_socket.send(data.encode())

    if data == "exit":
        break

client_socket.close()