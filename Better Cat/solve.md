First thing that I tryed was editing the file as it is with RightClick and edit. But no luck it is a binary.
I quickly chnaged to Binary Ninja and disassambled the binary. 
I have gone to the main and took a look on ther. 
![alt text](https://ibb.co/jfLjmNG)

I realized that the input that we are requested with is data_c18 so  i renamed it to password.
![alt text](https://ibb.co/kXmgCGV)

Now we can see that the input what we privide is used in a strcpm (it checks if the inpit is correct)
![alt text](https://ibb.co/Z6Rhfxb)

And we see that is is compared to a variable name it to realPassword
![alt text](https://ibb.co/c2M02V9)

And we see that it is defined to 0x3231616c6f726170
So we pop into a python script and we create a decoder

```
from pwn import *
print(bytearray.fromhex("3231616c6f726170").decode())
```

and we get **21alorap** but I quickly realized that this is in reverse so I added the tag 

```
from pwn import *
print(bytearray.fromhex("3231616c6f726170").decode()[::-1])
```

and we got **parola12** if we enter it we got the flag **ctf{a818778ec7a9fc1988724ae3700b42e998eb09450eab7f1236e53bfdcd923878}**