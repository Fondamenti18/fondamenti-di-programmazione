from enum import Enum
from immagini import *


class Direction(Enum):
	SU= (-1,0,3,3)
	GIU= (1,0,1,1)
	DX = (0,1,0,0)
	SX= (0,-1,2,2)


def cammino(fname,  fname1):

	print(' sto elaborando fname = ',fname)
	Matrix=converti(fname)
	Matrix[0][0]=2
	i = 0
	j = 0
	d = Direction.DX
	ris=[]
	
	while True:
		(i2,j2,d2) = avanza(Matrix,i,j,d)
		i = i2
		j = j2
		d = d2
		#print('i2 = ',i2,'  j2 = ',j2,'   d2 = ',d2, '    MATRIX Value = ',Matrix[i][j], ' MATRIX 0 0 = ',Matrix[0][0])
		#input('contento ? ')

			
		if Matrix[i][j] == 3:
			#img[i*40][j*40]==(0,0,255)
			
			break;

		ris.append(str(d.value[3]))
		#print(ris)
		#print ('----------------- w ------------')
	colora(fname,fname1, Matrix)
	stringResult = ''
	for s in ris:
		stringResult+=s
	return stringResult
        #
	
def avanza(Matrix,i,j,d):
    n = len(Matrix) #altezza
    m = len(Matrix[0])#larghezza
    #print(i,j,d)
    giricount= 0
    if i==n-1 and d==Direction.GIU:
        giricount+=1
        d=Direction.SX
    if i==0 and d==Direction.SU:
        giricount+=1
        d=Direction.DX
    if j==m-1 and d==Direction.DX:
        giricount+=1
        d=Direction.GIU
    if j==0 and d==Direction.SX:
        giricount+=1
        d=Direction.SU
    i2=i+d.value[0]
    j2=j+d.value[1]
    free= isFree(Matrix, i2,j2)
    if free:
        i=i2
        j=j2
        Matrix[i][j]=2
		
#        print ('Matrix [',i,'][',j,'] = ',Matrix[i][j])
#        input('spetta')
    else:
#        print(' ELSE  la cella non e libera: [',i2,', ',j2,']')
        
        while giricount < 4:
  
#            print('CURRENT DIRECTION = ',d)
            d = nextDirection(d)
            #d = nextD
#            print('NEXT DIRECTION = ',d)
#            print('ora sono qui : [',i,', ',j,']')
#            print('e mi sto spontando del vettore: [',d.value[0],', ',d.value[1],']')
            i2=i+d.value[0]
            j2=j+d.value[1]
            giricount+=1
#            print('sto per controllare la cella: [',i2,', ',j2,']')
#            input('WW')
            if isFree(Matrix,i2,j2):
                
                i = i2
                j = j2
                #d = nextD
                Matrix[i][j]=2
#                print ('Matrix [',i,'][',j,'] = ',Matrix[i][j])
#                input('spetta')
                break
#            else:
#                print('not free!')
                
        
    
    if giricount==4:
        Matrix[i][j] = 3
        return (i,j, d)    #via senza uscita
        
    return (i,j,d)
	
def nextDirection(d):
	giri=[Direction.DX,Direction.GIU,Direction.SX,Direction.SU]
	return giri[(d.value[2]+1)%4]
	
def isFree(Matrix,i,j):
    n = len(Matrix) #altezza
    m = len(Matrix[0])#larghezza
    if(i < 0 or j < 0 or i >= n or j >= m):
        return False
    return (Matrix[i][j] == 0)
	
def converti(fname):
	img=load(fname)
	n = len(img) #altezza
	m = len(img[0])#larghezza
	c=(255,0,0)
	

	Matrix = [[0 for g in range(15)] for r in range(15)]
	#print(Matrix)
	for i in range(n):
		if i == 0:
			i = 10
		for j in range(m):
			if j==0:
				j = 10
			if isThisColor(img[i][j], c):
				Matrix[i//40][j//40] = 1
			j+=40
		i+=40
	return Matrix
	
def colora(fname,fname1, Matrix):
	#print(Matrix)
	img=load(fname)
	n = len(Matrix) #altezza
	m = len(Matrix[0])#larghezza
	for i in range(n):
		for j in range(m):
			if Matrix[i][j]==3:
				for ii in range(i*40,(i+1)*40):
					for jj in range(j*40,(j+1)*40):
						img[ii][jj]=(0,0,255)
			if Matrix[i][j]==2:
				#print('TROVATO UN DUE AT: i=',i,', j= ',j)
				for ii in range(i*40,(i+1)*40):
					for jj in range(j*40,(j+1)*40):
						img[ii][jj]=(0,255,0)
	#img[20:100][20:100]=(0,0,255)

	save(img,fname1)
	
	
	
	
def isThisColor(c1, c2):
	return c1[0] == c2[0]and  c1[1] == c2[1] and c1[2] == c2[2]

	
#print(cammino('I1.png','prova1.png'))