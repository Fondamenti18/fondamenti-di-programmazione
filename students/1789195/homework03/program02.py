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
La codifica e' la seguente: 
    '0' per un passo verso destra (x crescenti)
    '1' per un passo verso il basso (y crescenti)
    '2' per un passo verso sinistra (x decrescenti)
    '3' per un passo verso l'alto (y decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt 

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
'''

from immagini import *

rosso  = (255,   0,   0)
verde  = (  0, 255,   0)
blu    = (  0,   0, 255)
nero   = (  0,   0,   0)
bianco = (255, 255, 255)
	
def cammino(fname,  fname1):
	img=load(fname)    #carica immagine	
	stringa=''
	x=0
	y=0
	count=0
	direzione='dx'

	while(count<400):
	   img=colora(img, y, x)	   
	   if(direzione=='dx'):
	       if(x+40<600):
	           if(img[y][x+40]!=rosso and img[y][x+40]!=verde ):
	               x+=40
	               stringa+='0'
	           else:
	               direzione='bs'
	       else:
	           direzione='bs'	           
	   if(direzione=='bs'):
	       if(y+40<600):
	           if(img[y+40][x]!=rosso and img[y+40][x]!=verde ):
	               y+=40
	               stringa+='1'
	           else:
	               direzione='sx'
	       else:
	           direzione='sx'	   
	   if(direzione=='sx'):
	       if(x-40>=0):
	           if(img[y][x-40]!=rosso and img[y][x-40]!=verde ):
	               x-=40
	               stringa+='2'
	           else:
	               direzione='al'
	       else:
	           direzione='al'	               
	   if(direzione=='al'):
	       if(y-40>=0):
	           if(img[y-40][x]!=rosso and img[y-40][x]!=verde ):
	               y-=40
	               stringa+='3'
	           else:
	               direzione='dx'
	       else:
	           direzione='dx'
	   count+=1
	   img=colora(img, y, x, blu)
	
	save(img, fname1)
	return(stringa)
    

def colora(img, y, x, colore=verde):
	i=0
	j=0
	try:			
		while(i<40):
			while(j<40):
				img[y+i][x+j]=colore
				j+=1			
			j=0
			i+=1		
	except:
		pass

	return(img)
	
if __name__ == '__main__':	
    print(cammino('I1.png','t1.png'))