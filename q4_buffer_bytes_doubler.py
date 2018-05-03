from socket import *
from pprint import pprint


client_socket = socket(AF_INET, SOCK_STREAM)
try:
    source_url = input("Enter the source url: ")
    client_socket.connect((source_url, 80))
    client_socket.send("GET / HTTP/1.0\r\n\r\n".encode('utf-8'))
    received_bytes = client_socket.recv(4096)
    doubled_bytes = received_bytes * 2
    pprint(doubled_bytes)  # print the doubled bytes
    client_socket.close()

except Exception:
    print("Server not found")
