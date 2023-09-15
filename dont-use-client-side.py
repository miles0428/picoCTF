import requests

url='https://jupiter.challenges.picoctf.org/problem/37821/'

r=requests.get(url)
# print(r.text)
text='''    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == 'a3c8') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_1') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == '9}') {
                  alert("Password Verified")'''


text=text.split('\n')
a=[]
b=[]
#get element between 'ing(' and ','
for i in text:
    if 'substring' in i:
        a.append(i[i.find('ing(')+4:i.find(',')])
        b.append(i[i.find('==')+4:i.find('\')')])
aa=[]
for i in a:
    #get the number of split
    if i == '0':
        aa.append(i)
    else:
        if i.find('*') == -1:
            aa.append('1')
        #get the number after *
        else:
            aa.append(i[i.find('*')+1:])

bb={}
for i in range(len(aa)):
    bb[aa[i]]=b[i]

f=''
for i in range(8):
    f+=bb[str(i)]
print(f)
