For this chalange I met something that I never done before it was something encrypted into a audio file
First I tryed to google for tools and I stumbled across **foremost** I run this with **-i rain.wav** and got nothing good so I continuated my research and got an idea to just open it in an audio editor like **Audacity** but no luck. I opened it then in a visual spectogram app like **sonic visualizer** and got something interesting. There are 2 spikes in the middle. There must be the flag

![img](https://raw.githubusercontent.com/L1ghtDream/cyberedu/master/tsunami-researcher/images/1.png?raw=true)

After adding a spectografic filter I got this

![img](https://raw.githubusercontent.com/L1ghtDream/cyberedu/master/tsunami-researcher/images/2.png?raw=true)

If your are blind and you can not see this there is writen **SecretCode: spectrogram** so i encoded **spectrogram** in **sha256** and got **cc3a329919391e291f0a41b7afd3877546f70813f0c06a8454912e0a92099369** so here is the flag **ctf{cc3a329919391e291f0a41b7afd3877546f70813f0c06a8454912e0a92099369}**

```
import hashlib

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
hash_string = 'spectrogram'
sha_signature = encrypt_string(hash_string)

print(sha_signature)
```