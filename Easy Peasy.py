
encrypted_file='5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c'

origin='a'*32
encrypted_a='0346483f243d1959563d1907563d1903543d190551023d1959073d1902573d19'
encrypted_a=[encrypted_a[i:i+2] for i in range(0,len(encrypted_a),2)]
encrypted_file=[encrypted_file[i:i+2] for i in range(0,len(encrypted_file),2)]
print(encrypted_a)
key=[]
for i in encrypted_a:
	for j in range(256):
		if '{:02x}'.format(ord('a')^j)==i:
			key.append(j)
			break

flag=''

for i,o in enumerate(encrypted_file):
	for j in [chr(k) for k in range(256)]:
		if '{:02x}'.format(ord(j)^key[i])==o:
			flag+=j
			break

print(flag)