'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra (x crescente). 
Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o verticale. 
Le regole di movimento del robottino sono le seguenti: 
- al generico step, si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci e' gia transitato in passato. 
- se invece la cella risulta occupata o e' una cella su cui ha gia transitato, ruota di 90 gradi in senso orario ed aspetta lo step successivo. 
- dopo aver ruotato  di 360 gradi senza essere riuscito a spostarsi si ferma. 

Progettare la funzione  percorso(fname, fname1) che presi in input:
- il percorso di un file (fname) contenente l'immagine in formato .png di una scacchiera con ostacoli
- il percorso di un file di tipo .png (fname1) da creare
legge l'immagine della scacchiera in fname, colora di verde le celle della scacchiera percorse dal robottino prima di fermarsi, 
colora di blu la cella in cui il robottino si ferma e registra l'immagine ricolorata nel file fname1. 
Inoltre restituisce una stringa dove in sequanza sono codificati i passi effettuati dal robottino prima di fermarsi. 
La codifica e' a seguente: 
    '0' per un passo verso destra (x crescenti)
    '1' per un passo verso il basso (y crescenti)
    '2' per un passo verso sinistra (x decrescenti)
    '3' per un passo verso l'alto (y decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt 

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
'''

from immagini import *


def colora(dax,ax,day,ay,colore,scacchiera):
	
	for x in range(dax, ax+1):
		for y in range(day, ay+1):
			scacchiera[y][x]=colore
	return scacchiera



def cammino(fname,  fname1):
	cammino=[[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
	x=0
	y=0
	xpixel=0
	ypixel=0
	facciaRivolta=0
	scacchiera=load(fname)
	percorso=""
	rosso=(255, 0, 0)
	verde=(0, 255, 0)
	blu=(0, 0, 255)
	size=40
	isFermo=0
	scacchiera=colora(xpixel,xpixel+size-1,ypixel,ypixel+size-1,verde,scacchiera)
	esci=0
	while esci==0:
		 
		if facciaRivolta==0 and isFermo<4:
			 
			if  x<14 and scacchiera[ypixel][xpixel+size]!=rosso and (cammino[y][x+1]==0)  :
				scacchiera=colora(xpixel+size,xpixel+(2*size)-1,ypixel,ypixel+size-1,verde,scacchiera)
				percorso=percorso+str(facciaRivolta)
				x=x+1
				cammino[y][x]=1
				xpixel=xpixel+size
				isFermo=0
				
			else:
				facciaRivolta=facciaRivolta+1
				if facciaRivolta ==4:
					facciaRivolta=0
				isFermo=isFermo+1	
		elif facciaRivolta==1 and isFermo<4:
			
			if  y<14 and scacchiera[ypixel+size][xpixel]!=rosso and (cammino[y+1][x]==0):
				scacchiera=colora(xpixel,xpixel+size-1,ypixel+size,ypixel+(2*size)-1,verde,scacchiera)
				percorso=percorso+str(facciaRivolta)
				y=y+1
				cammino[y][x]=1
				ypixel=ypixel+size
				isFermo=0
			else:
				facciaRivolta=facciaRivolta+1
				if facciaRivolta ==4:
					facciaRivolta=0
				isFermo=isFermo+1
		elif facciaRivolta==2 and isFermo<4:
			
			if  x>0 and scacchiera[ypixel][xpixel-size]!=rosso and (cammino[y][x-1]==0)  :
				scacchiera=colora(xpixel-size,xpixel,ypixel,ypixel+size-1,verde,scacchiera)
				percorso=percorso+str(facciaRivolta)
				x=x-1
				cammino[y][x]=1
				xpixel=xpixel-size
				isFermo=0
			else:
				facciaRivolta=facciaRivolta+1
				if facciaRivolta ==4:
					facciaRivolta=0
				isFermo=isFermo+1
		elif facciaRivolta==3 and isFermo<4:
			
			if  y>0 and scacchiera[ypixel-size][xpixel]!=rosso and (cammino[y-1][x]==0) :
				scacchiera=colora(xpixel,xpixel+size-1,ypixel-size,ypixel,verde,scacchiera)
				percorso=percorso+str(facciaRivolta)
				y=y-1
				cammino[y][x]=1
				ypixel=ypixel-size
				isFermo=0
			else:
				facciaRivolta=facciaRivolta+1
				if facciaRivolta ==4:
					facciaRivolta=0
				isFermo=isFermo+1
		else:
			
			scacchiera=colora(xpixel,xpixel+size-1,ypixel,ypixel+size-1,blu,scacchiera)
			esci=1
	'''print(percorso)'''
	save(scacchiera,fname1)
	
	return percorso
	
