import socket


def main():
    while True:
        address = input("Enter host name and get the ip or press 'q' to quit: ")  # get address from user console
        if address == "q":  # if user supplies 'q', terminate the loop
            break

        try:
            address_info = socket.gethostbyname(address)
            print("The ip address is", address_info)
            print()
        except socket.gaierror:
            print("The address does not exits or check your internet connection")
            print()  # print new line


if __name__ == "__main__":
    main()
