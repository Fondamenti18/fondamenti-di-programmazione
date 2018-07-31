'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista (nell'ordine), 
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1, 
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *
import png
import sys


rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)


def isThisColor(c1, c2):
	return c1[0] == c2[0]and  c1[1] == c2[1] and c1[2] == c2[2]



def converti(img, c):

	limit = sys.getrecursionlimit()
	#print('LIMIT = ',limit)
	sys.setrecursionlimit(4000)
	limit = sys.getrecursionlimit()
	#print('LIMIT = ',limit)
	n = len(img) #altezza
	m = len(img[0])#larghezza

	Matrix = [[0 for g in range(m)] for r in range(n)]
	#print(Matrix)
	for i in range(n):
		for j in range(m):
			if isThisColor(img[i][j], c):
				Matrix[i][j] = 1
	return Matrix

    
def ricolora(fname, lista, fnameout):
	img=load(fname)
	result = []
	for BOH in lista:
		x=BOH[0]
		y=BOH[1]
		c1=BOH[2]
		c2=BOH[3]
		c=img[x][y]
		Matrix=converti(img,c)

		
		n = len(Matrix) #altezza
		m = len(Matrix[0])#larghezza
		Matrix_adiacenti= [[0 for g in range(m)] for r in range(n)]
		Matrix_adiacenti[x][y]=1
		
		trova_adiacenti(Matrix,Matrix_adiacenti,x,y)
		result.append(colora(img, fnameout, Matrix_adiacenti,c1,c2))
	return result
	

	
def can_go(x,y,Matrix):
	n = len(Matrix) #altezza
	m = len(Matrix[0])#larghezza
	if x<0 or y<0 or x>=n or y>=m:
		
		return False
	else:
		return True
	
	
def trova_adiacenti(Matrix,Matrix_adiacenti,x,y):
	Xsu=x
	Ysu=y-1
	Xgiu=x
	Ygiu=y+1
	Xdx=x+1
	Ydx=y
	Xsx=x-1
	Ysx=y
	coordinate=[(Xsu,Ysu),(Xgiu,Ygiu),(Xdx,Ydx),(Xsx,Ysx)]
	for i in range(0,4):
	
		xx = coordinate[i][0]
		yy=coordinate[i][1]
		
		if can_go(xx, yy, Matrix):
			if Matrix_adiacenti[xx][yy]==0:
				if Matrix[xx][yy]==1:
					Matrix_adiacenti[xx][yy]=1
					
					trova_adiacenti(Matrix,Matrix_adiacenti,xx,yy)
				else:
					#bordo
					Matrix_adiacenti[x][y]=2
		else:
			Matrix_adiacenti[x][y]=2
			
				
	
	
	
def colora(img,fname1, Matrix_adiacenti, c1,c2):
	
	
	area = 0
	perimetro = 0
	n = len(Matrix_adiacenti) #altezza
	m = len(Matrix_adiacenti[0])#larghezza
	for i in range(n):
		for j in range(m):
			if Matrix_adiacenti[i][j]==1:
				img[j][i]=c1
				area+=1
			if Matrix_adiacenti[i][j]==2:
				img[j][i]=c2
				perimetro+=1
	save(img,fname1)
	return (area,perimetro)
	
	
	
	
	

	
	
	

