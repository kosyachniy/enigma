#Создание словаря
def alpha(text):
	text+='йцукенгшщзхъёфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm'
	alphabet=list()
	for i in text:
		if not any(i==j for j in alphabet):
			alphabet.append(i)
	alphabet.sort()
	return tuple(alphabet)

#Ввод данных
#!key=(int(i) for i in input())
key=[]
nom=input()
for i in nom:
	key.append(int(i))
text=input()
n=len(text)
patch=[(i[0],i[1]) for i in input('Структура коммутационной панели: ').split()]
#!Изменить структуру валов / роторов
alphabet=alpha(text)
m=len(alphabet)
text=list(text)

#Коммутационная панель
def panel(text):
	for i in patch:
		if i[0]==text:
			return i[1]
	return text

#Роторы
def there(inp,shift):
	return alphabet[(int(alphabet.index(inp)+shift)%len(alphabet))]
def here(inp,shift):
#!Правильно ли работает в отрицательных числах
	return alphabet[(int(alphabet.index(inp)-shift)%len(alphabet))]

for i in range(n):
#Обход роторов в одну сторону
	for j in key:
		text[i]=there(text[i],j)
#Рефлектор
	text[i]=alphabet[m-1-alphabet.index(text[i])]
#Обход роторов в обратную сторону
	for j in key[::-1]:
		text[i]=here(text[i],j)
	text[i]=panel(text[i])

for i in text:
	print(i,end='')
print()