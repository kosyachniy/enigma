#Энигма

def enigma(text,key,alphabet,n,m,patch=''):
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
