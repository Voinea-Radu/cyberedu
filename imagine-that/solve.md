If I connect to it asks me for a starting and enging point I just added **a** and I got an error 

![img](https://raw.githubusercontent.com/L1ghtDream/cyberedu/master/imagine-that/images/1.png?raw=true)

If I entered 1 and 10 I got something that looks like a png

![img](https://raw.githubusercontent.com/L1ghtDream/cyberedu/master/imagine-that/images/2.png?raw=true)


So I wanted to create a script that takes the output from the terminal and stores it into a file but because I am not very googd with python a got one from the web and modified it with remote connect to tit my purpose

```
from pwn import *

host, port = ("34.107.22.248", 31048)

def get_bytes(start):
	end = start + 1
	r = remote(host,port)
	r.recvuntil(": ")
	r.sendline(str(start).encode())
	r.recvuntil(": ")
	r.sendline(str(end).encode())
	r.recvuntil(str(end).encode() + b'\r\n')
	file = r.recvuntil("Enter")
	r.close()
	file = file[1:-7]
	if len(file) == 1:
		return file
	else:
		if file == b'\r\n':
			return b'\n'
		else:
			print('You can stop the program now')
			return b'\x00'


p = 0
f = open("saveme", "wb")
f.write(b'\x89')
while True:
	new_bytes = get_bytes(p + 1)
	f.write(new_bytes)
	f.flush()
	p = p + 1
	print(new_bytes)

f.close()
```

After 10 minutes I got a file and because I knew it was a PNG I tryed renaming it to a PNG and I got a QR code

![img](https://raw.githubusercontent.com/L1ghtDream/cyberedu/master/imagine-that/images/3.png?raw=true)

I tryed scaning it and I got **asdsdgbrtvt4f5678k7v21ecxdzu7ib6453b3i76m65n4bvcx**. I entered this as a password and here is the flag **ctf{1e894e796b65e40d46863907eafc9acd96c9591839a98b3d0c248d0aa23aab22}**

