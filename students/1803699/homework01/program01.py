from math import *

def num_divisori(x):
	lista_div=[]
	for i in range(1,floor(sqrt(x))+1):
			if x%i == 0:
				if x/i==i:
					lista_div+=[i]
				else:
					lista_div+=[i, x/i]
	return len(lista_div)-2

    
def modi(ls,k):
	primi=[]
	rimuovi=[]
	for i in ls:
		n = num_divisori(i)
		if n==0:
			primi+=[i]
		if n!=k:
			rimuovi+=[i]
	for i in rimuovi:
		ls.remove(i)
	return primi
