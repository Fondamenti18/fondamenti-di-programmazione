'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso colonna (x crescente). 
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
    '0' per un passo verso colonna (x crescenti)
    '1' per un passo verso il riga (y crescenti)
    '2' per un passo verso sinistra (x decrescenti)
    '3' per un passo verso l'alto (y decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt 

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
'''

from immagini import *
import png
movimento=""
def cammino(fname, fname1):
        global movimento
        movimento=""
        green=(0,255,0)
        colonna=40
        riga=0
        controllo=0
        img=load(fname)
        img=colora(green,0,0,img)
        cammino_verso_destra(img,colonna,riga,controllo,fname1)
        return movimento
		
def salvataggio(fname,img):
	save(fname,img)

def colora(c,riga,colonna,img):
	for i in range(riga,riga+40):
		for d in range(colonna,colonna+40):
			img[i][d]=c
	return img
    
def cammino_verso_destra(img,colonna,riga,controllo,fname):
        global movimento
        white=(255,255,255)
        black=(0,0,0)
        red=(255,0,0)
        green=(0,255,0)
        blue=(0,0,255)
        if controllo!=4:
            while colonna<width(img):
                if img[riga][colonna]==white or img[riga][colonna]==black:
                    movimento=movimento+"0"
                    controllo=0
                    img=colora(green,riga,colonna,img)
                    colonna+=40
                else: break
            controllo+=1
            colonna-=40
            riga+=40
            cammino_verso_il_basso(img,colonna,riga,controllo,fname)
        else:
            colonna-=40
            img=colora(blue,riga,colonna,img)
            salvataggio(img,fname)
            
            

def cammino_verso_il_basso(img,colonna,riga,controllo,fname):
	global movimento
	white=(255,255,255)
	black=(0,0,0)
	red=(255,0,0)
	green=(0,255,0)
	blue=(0,0,255)
	if controllo!=4:
		while riga<height(img):
			if img[riga][colonna]==white or img[riga][colonna]==black:
				movimento=movimento+"1"
				controllo=0
				img=colora(green,riga,colonna,img)
				riga+=40
			else: break
		controllo+=1
		riga-=40
		colonna-=40
		cammino_verso_sinistra(img,colonna,riga,controllo,fname)
	else:
		riga-=40
		img=colora(blue,riga,colonna,img)
		salvataggio(img,fname)
		

def cammino_verso_sinistra(img,colonna,riga,controllo,fname):
	global movimento
	white=(255,255,255)
	black=(0,0,0)
	red=(255,0,0)
	green=(0,255,0)
	blue=(0,0,255)
	if controllo!=4:
		while colonna>=0:
			if img[riga][colonna]==white or img[riga][colonna]==black:
				movimento=movimento+"2"
				controllo=0
				img=colora(green,riga,colonna,img)
				colonna-=40
			else: break
		controllo+=1
		colonna+=40
		riga-=40
		cammino_verso_alto(img,colonna,riga,controllo,fname)
	else:
		colonna+=40
		img=colora(blue,riga,colonna,img)
		salvataggio(img,fname)
			
def cammino_verso_alto(img,colonna,riga,controllo,fname):
	global movimento
	white=(255,255,255)
	black=(0,0,0)
	red=(255,0,0)
	green=(0,255,0)
	blue=(0,0,255)
	if controllo!=4:
		while riga>=0:
			if img[riga][colonna]==white or img[riga][colonna]==black:
				movimento=movimento+"3"
				controllo=0
				img=colora(green,riga,colonna,img)
				riga-=40
			else: break
		controllo+=1
		riga+=40
		colonna+=40
		cammino_verso_destra(img,colonna,riga,controllo,fname)
	else:
		riga+=40
		img=colora(blue,riga,colonna,img)
		salvataggio(img,fname)
			
def width(img):
	'''Ritorna la larghezza dell'immagine img.'''
	return len(img[0])

def height(img):
	'''Ritorna l'altezza dell'immagine img.'''
	return len(img)
