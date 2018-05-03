from socket import *


client_socket = socket(AF_INET, SOCK_DGRAM)
while True:
    try:
        address = input("Enter Server Address: ")
        server_address = (address.strip(), 3310)
        message = input("Enter Message to send or q to quit: ")
        if message == "q":
            break
        client_socket.sendto(message.encode('utf-8'), server_address)
        received_message, server_address = client_socket.recvfrom(100)  # maximum buffer size is 100
        print(received_message.decode('utf-8'))  # Print received message
    except Exception as ex:
        print("An Error occurred in communication")
        print(ex)
client_socket.close()
