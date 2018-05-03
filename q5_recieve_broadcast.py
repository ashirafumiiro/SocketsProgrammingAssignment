import select
import socket

port = 3310
bufferSize = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', port))
s.setblocking(0)

while True:
    result = select.select([s], [], [])
    msg = result[0][0].recv(bufferSize) 
    print(msg)