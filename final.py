import socket
import os
from time import sleep
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 2015

listen_addr = ("",port)



s.bind(listen_addr)

while 1:
	data , addr = s.recvfrom(1024)
	if data == "hello":
		os.system("v4l2grab -d /dev/video1 -o image.jpg -W 1280 -H 720 -q 100")
