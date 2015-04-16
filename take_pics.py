import os
from time import sleep

while 1:
	os.system("v4l2grab -d /dev/video1 -o image.jpg -W 1280 -H 720 -q 100")
	sleep(2)
