from pwn import *
print(bytearray.fromhex("270f").decode()[::-1])
