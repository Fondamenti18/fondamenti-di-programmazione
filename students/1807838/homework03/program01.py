from immagini import *
#import time
def quadrato(filename,c):
	global img
	img=load(filename)
	ret=(0,(0,0))
	h=len(img)-1#ALTEZZA DELL'IMMAGINE REALE: DA 0 A H-1(=1000)
	w=len(img[0])-1#LARGHEZZA DELL'IMMAGINE REALE: DA 0 A W-1(=1000)
	row=0
	while row<h-1:
		col=0
		while col<w-1:
			lato=0
			col2=col
			flag=False
			while img[row][col2]==c:
				lato+=1
				#print(row,'da',col,'a',col2,lato,ret[0])
				if lato>ret[0] and col+lato-1<=w and row+lato-1<=h:
					skip = checkquadrato(row,col,lato,c)
					if skip==True:
						#print('è un quadrato')
						skip=checkpieno(row,col,lato,c)
						if skip==True:
							#print('è pieno')
							ret=(lato,(col,row))
						else:
							flag=True
					else:
						flag=True
						
				if flag:
					col=skip
					#print('\n\n					SKIP		\n',skip)
					break
				else:
					if col2<w-1:
						col2+=1
					else:break
			col+=1
		row+=1
	print(ret)
	return ret

def checkquadrato(row,col,lato,c):
	up={stop for stop in range(col,col+lato-1) if img[row][stop]!=c}
	left={ col for stop in range(row,row+lato-1) if img[stop][col]!=c}
	down={ stop for stop in range(col,col+lato-1) if img[row+lato-1][stop]!=c}
	right={ col+lato-1 for stop in range(row,row+lato-1) if img[stop][col+lato-1]!=c}
	diag={ col+i for i in range(lato) if img[row+i][col+i]!=c}
	diag2={ col+lato-1-i for i in range(lato) if img[row+i][col+lato-1-i]!=c}
	if up==set() and left==set() and down==set() and right==set() and diag==set() and diag2==set():
		return True
	return max(left.union(up,right,down,diag,diag2))

def checkpieno(row,col,lato,c):
	in1={x for y in range(row,row+lato-1) for x in range(col,col+lato-1) if img[y][x]!=c}
	if in1==set():
		return True
	return max(in1)
'''
####				TESTS				####
ret=quadrato('Ist3.png',(255,0,0))
print(ret==(60, (100, 50)))
'''
