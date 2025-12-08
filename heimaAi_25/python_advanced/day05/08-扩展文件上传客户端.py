import socket

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cli.connect(("10.1.68.179", 12306))

with open(r"./file/xxx.txt", "rb") as f:
    while True:
        data = f.read(1024)
        if len(data) <= 0:
            break
        cli.send(data)
print("断了")
cli.close()
