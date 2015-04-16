import socket
from time import sleep
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 2015

listen_addr = ("",port)

s.bind(listen_addr)

while 1:
	data , addr = s.recvfrom(1024)
	if data == "hello":
		print "yes"
	else:
		print "no"
	sleep (1)
