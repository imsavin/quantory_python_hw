# Standard library
import socket 


def main():
    port = 5353 # DNS operates on port 53 by default, we use 5353 to mock traditional behavior
    ip = "127.0.0.1"
    dns_dict = {'ya.ru':'87.250.250.243', 'www.org':'128.30.52.17', 'savin.org.ru':'194-67-90-3'}

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # using IPv4, UDP
    sock.bind((ip, port))
    print("Listening on port: ", port)
    
    while True:
        query, addr = sock.recvfrom(512) # Queries are DNS Messages which may be sent to a name server to provoke a Response 
        if str(bytes.decode(query)) in dns_dict.keys():                   #Получаем запрос с hostname, если такой есть в бд, отправляем значение ip
            answer = dns_dict[bytes.decode(query)]
            sock.sendto(str.encode(answer), addr)
        else:
            sock.sendto(str.encode('No such entry'), addr)
            

if __name__ == "__main__":
    main()
