import base64

str='11101000 + 101010000 + 100110011 + 110111010 + 11000100'
r = 0
for n in str.replace(' ', '').split('+'):
   r+=int(n)
print(r)
print(base64.b64decode('7oYnXzWt9Bcm4Z1JtDLoj7spwxvxJWBXA6iCTxl34DdPLlVjm0i-lGsOZGuy67l40Ow='))


