import requests
url = 'http://mercury.picoctf.net:34561/index.php'

r=requests.head(url)
print(r.headers)
