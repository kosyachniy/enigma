def alpha(text):
	return text

#Коммутационную панель
def panel(patch,text):
	for i in patch:
		if i[0]==text:
			return i[1]

#Роторы
def there(inp,shift,alphabet,patch):
	print(inp)
	return panel(patch,alphabet[(int(alphabet.index(inp)+shift)%len(alphabet))])

def here(inp,shift,alphabet,patch):
	return panel(patch,alphabet[(int(alphabet.index(inp)-shift)%len(alphabet))])

#key=(int(i) for i in input())
key=[]
nom=input()
for i in nom:
	key.append(int(i))
patch=[(i[0],i[1]) for i in input().split()]
text=input()
n=len(text)
alphabet=tuple(i for i in set(j for j in text+'йцукенгшщзхъёфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm'))
text=list(text)

for i in key:
	for j in range(n):
		text[j]=there(text[j],i,alphabet,patch)
for j in range(n//2):
	text[j],text[n-1-j]=text[n-1-j],text[j]
#Изменить структуру валов / роторов и поставить here
for i in key[::-1]:
	for j in range(n):
		text[j]=there(text[j],i,alphabet,patch)

for i in text:
	print(i,end='')
print()