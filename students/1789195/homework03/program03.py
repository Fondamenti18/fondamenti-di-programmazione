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

rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255) 

bordo=[]
area=[]
    
def ricolora(fname, lista, fnameout):
	img = load(fname)	#carica immagine
	lst=[]
	global bordo
	global area
	for x, y, c1, c2 in lista:	#unpacking della lista in input
		colore=img[y][x]	#mette nella variabile colore il colore presente nell'immagine nelle coordinate indicate
		x=xPrimoPixel(img, x, y, colore)	#richiama la funzione xPrimoPixel che trova il primo pixel in posizione x
		y=yPrimoPixel(img, x, y, colore)	#richiama la funzione yPrimoPixel che trova il primo pixel in posizione y
	
		img=coloraBordo(img, x, y, colore, c2)		#richiama funzione coloraBordo
		img=coloraArea(img, x+1, y+1, c1, colore)	#richiama funzione coloraPos che colora tutti i pixel x+1 e y+1 dalle coordinate date	
	
	for i in range(0, len(bordo)):
		lst+=[(area[i], bordo[i])]
		
	save(img, fnameout)		#salva l'immagine img con il nome in input fnameout	
	bordo=[]
	area=[]
	return(lst)	#ritorna una lista che contiene tuple con all'interno l'area e il bordo dei pixel ricolorati
	
	
def coloraArea(img, x, y, c1, colore):
	'''Funzione che prende in input l'immagine, la posizione x, la posizione y, il colore c1 e il colore originale del quadrato da ricolorare 
	controlla se le coordinate x e y di volta in volta aumentate di 1 sono del colore richiesto in input, finché lo sono colora il pixel presente
	in quelle coordinate con il colore c1 e aumenta il contatore di 1. Richiama la variabile globale area e gli assegna il valore del contatore.
	'''
	i=0
	j=0
	count=0
	try:
		while(img[y+i][x+j]==colore):
			while(img[y+i][x+j]==colore):
				img[y+i][x+j]=c1
				j+=1
			count+=j			
			j=0
			i+=1
	except:
		pass
	global area
	area.append(count)
	return(img)
	
def coloraBordo(img, x, y, colore, c2):
	'''Funzione che prende in input l'immagine, la posizione x, la posizione y, il colore in input e c2. Controlla se nella coordinata x,y è presente il un pixel di colore
	colore, se si ricolora il pixel con il colore c2 e aumenta il count di 1, quando raggiunge un pixel diverso ruota di 90 gradi ripetendo l'operazione. Richiama la variabile globale
	bordo e gli assegna il valore di count.
	'''
	count=0
	try:
		
		while(img[y][x]==colore and y+1<len(img) and img[y+1][x]==colore):
			img[y][x]=c2
			y+=1
			count+=1
		
		while(img[y][x]==colore and x+1<len(img[0]) and img[y][x+1]==colore):
			img[y][x]=c2
			x+=1
			count+=1
		while(img[y][x]==colore and y-1>=0 and img[y-1][x]==colore):
			img[y][x]=c2
			y-=1
			count+=1	
		while(img[y][x]==colore and x-1>=0):
			img[y][x]=c2
			x-=1
			count+=1
	except:
		pass
		
	global bordo
	bordo.append(count)	
	return(img)
	
def yPrimoPixel(img, x, y, colore):
	'''Funzione che prende in input l'immagine, la posizione x, la posizione y e il colore passato in input, cerca il primo pixel x.
	'''
	while(img[y-1][x]==colore and y-1>=0):		#posizione al primo pixel x
		y-=1
	return(y)

def xPrimoPixel(img, x, y, colore):
	'''Funzione che prende in input l'immagine, la posizione x, la posizione y e il colore passato in input, cerca il primo pixel y.
	'''
	while(img[y][x-1]==colore and x-1>=0):		#posizione al primo pixel x
		x-=1
	return(x)			

	
if __name__=='__main__':
	
	print(ricolora('I1.png',[(10,10,rosso,blu)],'test1.png'))
	print(ricolora('I1.png',[(10,10,rosso,blu),(90,10,nero,verde)],'test2.png'))
	


