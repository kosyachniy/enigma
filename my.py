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

	def de(text,di):
		j=text[0]
		num=0
		x=[]
		text.append((text[len(text)-1]+1)%di)
		for i in text:
			if i==j:
				if num>=m:
					x.append(num-1)
					num=1
				else:
					num+=1
			else:
				x.append(num-1)
				num=1
				j=(j+1)%di
		return x

	st=[0]
	for i in text:
		st+=bin(i)
	st=de(st,2)
	new=''
	for i in st:
		new+=alphabet[i]

	return new