from math import sqrt
def modi(ls,k):
	primils=[]
	rem=[]
	for x in ls:
		tot=0
		a=2
		b=1
		if x%2!=0:
			a=3
			b=2
		for d in range (a,round(sqrt(x)),b):
			if x%d==0:
				tot+=1
		tot*=2
		if sqrt(x)==round(sqrt(x)):
			tot-=1
		if tot==0:
			primils.append(x)
		if tot!=k:
			rem.append(x)
	for x in rem:
		ls.remove(x)
	return primils
