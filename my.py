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

	def de(text):
		j=1
		num=0
		x=[]
		text.append((text[len(text)-1]+1)%2)
		for i in text:
			if i==j:
				if num>=m:
					x.append(num)
					num=1
				else:
					num+=1
			else:
				x.append(num)
				num=1
				j=(j+1)%2
		return x

	st=[1]
	for i in text:
		st+=bin(i)
	st=de(st)
	new=''
	for i in st:
		new+=alphabet[i-1]

	return new