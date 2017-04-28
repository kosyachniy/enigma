#Мой шифратор

from math import log,ceil

def my(text,alphabet,n,m):
	dim=ceil(log(m,2))

	def bin(word):
		x=[0]*dim
		i=dim-1
		num=alphabet.index(word)
		while num>0:
			x[i]=num%2
			num//=2
			i-=1
		return x

#Добавляет лишний бит 0 в начале
	def debin(text):
		x=[]
		j=0
		text=[0]+text
		num=0
		text.append((text[len(text)-1]+1)%2)
		for i in text:
			if i==j:
				num+=1
			else:
				x.append(num-1)
				num=1
				j=(j+1)%2
		return x

#Добавляет 1 размерность | Есть ограничение максимальным количеством подряд | С любыми строками
	def de(text,di,ma):
		x=[]
		j=0
		while j<=len(text)-1:
			for i in range(di):
				k=0
				while (j<=len(text)-1) and (text[j]==i):
					if k>=ma:
						x.append(k)
						x.append([0]*(di-1))
						k=1
					else:
						k+=1
					j+=1
				x.append(k)
		return x

	def ass(text):
		st=[]
		for i in text:
			st+=bin(i)
		st=debin(st)
		for i in range(len(st)):
#!Проблема с превышением словаря -> de(text,m-1,m)
			st[i]=alphabet[st[i]%m]
		return st

	return ass(ass(text))