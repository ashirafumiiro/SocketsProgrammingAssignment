from socket import *


server_address = ("0.0.0.0", 8000)  # receive from all ips and on port 8000
server_sock = socket(AF_INET, SOCK_STREAM)
server_sock.bind(server_address)
server_sock.listen(1)
print("[*] Server Listening on port 8000")
while True:
    connection_sock, address = server_sock.accept()
    message = connection_sock.recv(2084)  # buffer size is 2048
    print("Received:", message.decode('utf-8'))
    if message.decode('utf-8') == "ping":  # if received ping, send pong
        connection_sock.send("pong".encode('utf-8'))
    connection_sock.close()
