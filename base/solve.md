The chalange is trowing random numbers in the console and we have to covert the value in hex but we need to be fast

![img](https://raw.githubusercontent.com/L1ghtDream/cyberedu/master/base/images/1.png?raw=true)

So I gone ahead and created a script

```
from pwn import *
from ptrlib import *

def getOct(s):
    octdata = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #           0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25

    idOct = s

    if(s>=150):
        idOct = idOct - 2
    if(s>=160):
        idOct = idOct - 2
    if(s>=170):
        idOct = idOct - 2
        
    return octdata[idOct-141]


sock = Socket('35.198.183.125', 31648)

#------------------Number To Hex------------------
resp = sock.recv().decode("utf-8")
print("[S] " + resp)

#Calculate hex
var1 = resp.split(" ")
no = ""
for i in range(2,len(var1[5])-2):
    no = no + var1[5][i]
answer1 = hex(int(no))

#Send response
sock.sendline(answer1)
print("[S] Input: " + answer1)

#------------------Hex To Text------------------
resp = sock.recv().decode("utf-8")
print("[S] " + resp)

#Calculate string
var1 = resp.split(" ")
text = ""
for i in range(2,len(var1[5])-2):
    text = text + var1[5][i]
answer2 = bytearray.fromhex(text).decode()
    
#Send response
sock.sendline(answer2)
print("[S] Input: " + answer2)

#------------------Oct To Text------------------

resp = sock.recv().decode("utf-8")
print("[S] " + resp)

#Calculate string
var = resp.split(" ")

text = ""
text = text + var[5][3]
text = text + var[5][4]
text = text + var[5][5]

j=6;
repeat = 1
answer3 = ""
answer3 = answer3 + getOct(int(text))

while repeat == 1:
    if(var[j][len(var[j])-1] == ">"):
        text = ""
        text = text + var[j][0]
        text = text + var[j][1]
        text = text + var[j][2]
        text = text + var[j][3]
        answer3 = answer3 + getOct(int(text))
        break
        
    answer3 = answer3 + getOct(int(var[j]))
    
    j=j+1;


#Send response
sock.sendline(answer3)
print("[S] Input: " + answer3)



print(sock.recv().decode("utf-8"))
print(sock.recv().decode("utf-8"))
print(sock.recv().decode("utf-8"))
print(sock.recv().decode("utf-8"))




sock.close()
```

and sure enough here is the flag **DCTF{55cdfe07fae36a30c2c8d0738fdcd3f7718e4898f8585b142f7eaf2f269a0deb}**