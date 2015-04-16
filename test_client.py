import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


port = 2015

server_ip = raw_input()

listen_addr = ("",port)

s.bind(listen_addr)



while 1:

    data = raw_input("enter the data you want to send : ")
    s.sendto(data,(server_ip,port))

    recv_data , addr = s.recvfrom(1024)
    print recv_data
