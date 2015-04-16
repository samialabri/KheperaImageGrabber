import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 2015

listen_addr = ("",port)

ip_adder = raw_input("enter the ip address of whom you want to contact : ")

s.bind(listen_addr)

while 1:
	data , addr = s.recvfrom(1024)
	if data == "hello":
		s.sendto("thank you",("192.168.1.113",port))
	else:
		s.sendto("try again and send the correct message",("192.168.1.113",port))
