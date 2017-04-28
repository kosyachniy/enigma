#Расшифровка=шифрование (в обе стороны одинаково)
#Бесконечное количество роторов
#Использование любых символов - динамический алфавит
#!При использовании особого словаря - дешифровка невозмона

from enigma import enigma
from my import my

#Создание словаря
#1234567890йцукенгшщзхъёфывапролджэячсмитьбю
alpha=lambda text: tuple(sorted([i for i in set(j for j in text+'qwertyuiopasdfghjklzxcvbnm')]))

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
	print(i,end='')
print()
text=my(text,alphabet,n,m)
print(text)