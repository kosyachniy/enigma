#Расшифровка=шифрование (в обе стороны одинаково)
#Бесконечное количество роторов
#Использование любых символов - динамический алфавит
#!При использовании особого словаря - дешифровка невозмона

from enigma import enigma

#Создание словаря
def alpha(text):
#1234567890йцукенгшщзхъёфывапролджэячсмитьбю
	alphabet=list(i for i in set(j for j in text+'qwertyuiopasdfghjklzxcvbnm'))
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

text=enigma(text,key,alphabet,n,m,patch)
for i in text:
	print(alphabet.index(i),end='')
print()

for i in text:
	print(i,end='')
print()