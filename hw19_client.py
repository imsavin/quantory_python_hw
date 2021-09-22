from socket import *
import sys
host = 'localhost'
port = 5353
addr = (host,port)
while True:
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    data = input('Enter hostname: ')
    if not data :             #При получении пустого ввода закрывается сокет и программа.
        udp_socket.close()
        sys.exit(1)
#encode - перекодирует введенные данные в байты, decode - обратно
    data = str.encode(data)
    udp_socket.sendto(data, addr)
    data = udp_socket.recvfrom(1024)

    print(bytes.decode(data[0]))
    udp_socket.close()


