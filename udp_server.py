from socket import *


server_port = 3310
host_name = ""
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((host_name, server_port))
print("Server listening for incoming connections")

while True:
    try:
        message, client_address = server_socket.recvfrom(2048)
        print("Connection received from, %s on port %d" % client_address)
        modified_message = "Your message has been received"  # message.decode('utf-8').upper()

        server_socket.sendto(modified_message.encode('utf-8'), client_address)

    except Exception as ex:
        print(ex)
