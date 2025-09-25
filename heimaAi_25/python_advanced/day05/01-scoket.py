"""
socket


"""

import socket
"""
参数1: Address Family,地址族,即: 表示用何种IP规则来解析,例如: IPV4,IPV6..., AF_INEF 代表 IPV4
参数2: 表示传输方式,Stream(流),用字节流(二进制形式)传输数据
"""
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_socket.connect(('127.0.0.1', 3000))


cli_socket.close()



