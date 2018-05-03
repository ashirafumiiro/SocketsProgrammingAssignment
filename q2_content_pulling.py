import socket


def main():
    server_address = ('www.cedat.mak.ac.ug', 80)  # socket address of the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client socket with ipv4 and tcp protocol

    try:
        client_socket.connect(server_address)
        client_socket.send("GET / HTTP/1.0\r\n\r\n".encode('utf-8'))  # convert data to bits
        received_data = client_socket.recv(10240000)
        print(received_data.decode('utf-8'))
        client_socket.close()

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()  # run main function if executed directly
