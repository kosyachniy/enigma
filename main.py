def alpha(alphabet,text):
	return int(alphabet.index(text))

def beta(alphabet,number):
	return alphabet[number]

def there(inp,shift,alphabet):
	return beta(alphabet,(alpha(alphabet,inp)+shift)%len(alphabet))

def here(inp,shift,alphabet):
	return beta(alphabet,(alpha(alphabet,inp)-shift)%len(alphabet))

#key=(int(i) for i in input())
key=[]
nom=input()
for i in nom:
	key.append(int(i))
text=input()
n=len(text)
#йцукенгшщзхъёфывапролджэячсмитьбю
alphabet=tuple(i for i in set(j for j in text+'qwertyuiopasdfghjklzxcvbnm'))
text=list(text)

for i in key:
	for j in range(n):
		text[j]=there(text[j],i,alphabet)
for j in range(n//2):
	text[j],text[n-1-j]=text[n-1-j],text[j]
#Изменить структуру валов / роторов и поставить here
for i in key[::-1]:
	for j in range(n):
		text[j]=there(text[j],i,alphabet)

for i in text:
	print(i,end='')
print()