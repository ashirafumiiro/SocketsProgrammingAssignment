from socket import *


server_address = ('127.0.0.1', 8000)
client_socket = socket(AF_INET, SOCK_STREAM)
try:
    client_socket.connect(server_address)
    message = input("Enter the message to send: ")
    client_socket.send(message.encode('utf-8'))
    print("Sent: ", message)
    response = client_socket.recv(4096)
    print("Received:", response.decode('utf-8'))
    client_socket.close()

except Exception as ex:
    print(ex)