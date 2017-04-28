#Расшифровка=шифрование (в обе стороны одинаково)
#Бесконечное количество роторов
#Использование любых символов - динамический алфавит
#!При использовании особого словаря - дешифровка невозмона

def enigma(text,key,alphabet,n,m):
#Коммутационная панель
	def panel(text):
		for i in patch:
			if i[0]==text:
				return i[1]
			elif i[1]==text:
				return i[0]
		return text

#Роторы
#!Автоматический поворот роторов
	there=lambda word,shift: alphabet[(alphabet.index(word)+shift)%m]
	here=lambda word,shift: alphabet[(alphabet.index(word)-shift)%m]

	for i in range(n):
#Обход роторов в одну сторону
		word=text[i]
		for j in key:
			word=there(word,j)
#Рефлектор
		word=alphabet[m-1-alphabet.index(word)]
#Обход роторов в обратную сторону
		for j in key[::-1]:
			word=here(word,j)
		text[i]=panel(word)
	return text

#Создание словаря
def alpha(text):
#1234567890йцукенгшщзхъёфывапролджэячсмитьбю
	text+='qwertyuiopasdfghjklzxcvbnm'
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
#patch=[(i[0],i[1]) for i in input('Структура коммутационной панели: ').split()]
patch=''
#!Изменить структуру валов / роторов
alphabet=alpha(text)
m=len(alphabet)
text=list(text)

text=enigma(text,key,alphabet,n,m)

for i in text:
	print(i,end='')
print()