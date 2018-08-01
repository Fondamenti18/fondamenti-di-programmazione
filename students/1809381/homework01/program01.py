
import math
def modi(ls,k):
	finale=[]
	n_primi=[]
	for i in ls:
		primi=True
		b=2
		divisore=0
		if (int(math.sqrt(i)))*(int(math.sqrt(i)))==i:
			divisore+=1
			primi=False
		else:
			while b<(int(math.sqrt(i)+1)):
				if i%b==0:
					divisore+=2
					primi=False
				b+=1
		if divisore==k:
			finale+=[i]
		elif primi:
			n_primi+=[i]
	ls[:]=list(finale)
	return n_primi
