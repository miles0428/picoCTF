url='https://jupiter.challenges.picoctf.org/problem/36474'
import requests
robots = requests.get(url+'/robots.txt')
print(robots.text)

Disallowed = robots.text.split('\n')[1].split(':')[1].strip()
print(Disallowed)

flag = requests.get(url+Disallowed)

for i in flag.text.split('\n'):
    if 'pico' in i:
        print(i)
        break



