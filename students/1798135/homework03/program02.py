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

#def cammino(fname,  fname1):
def cammino(fname,fname1):
	img=load(fname)
	tabellina=[]
	rosso=(255,0,0)
	verde=(0,255,0)
	blu=(0,0,255)
	for ii in range(15):
		i=ii*40
		riga=[]
		for jj in range(15):
			j=jj*40
			riga.append(img[i][j])
		tabellina.append(riga)

	y=0
	x=0
	risultato=""
	faccia=0
	contatore=0
	while (True):
		if faccia==0:
			if (x+1)<15:
				if tabellina[y][x+1]!=rosso and  tabellina[y][x+1]!=verde:
					tabellina[y][x]=verde
					x=x+1
					risultato=risultato+"0"
					contatore=0
					continue
			contatore+=1
			faccia+=1

		elif faccia==1:
			if (y+1)<15:
				if tabellina[y+1][x]!=rosso and  tabellina[y+1][x]!=verde:
					tabellina[y][x]=verde
					y=y+1
					risultato=risultato+"1"
					contatore=0
					continue
			contatore+=1
			faccia+=1

		elif faccia==2:
			if (x-1)>=0:
				if tabellina[y][x-1]!=rosso and  tabellina[y][x-1]!=verde:
					tabellina[y][x]=verde
					x=x-1
					risultato=risultato+"2"
					contatore=0
					continue
			contatore+=1
			faccia+=1

		elif faccia==3:
			if (y-1)>=0:
				if tabellina[y-1][x]!=rosso and  tabellina[y-1][x]!=verde:
					tabellina[y][x]=verde
					y=y-1
					risultato=risultato+"3"
					contatore=0
					continue
			contatore+=1
			faccia=0

		#print(contatore,"  faccia ",faccia)
		if contatore==5:
			tabellina[y][x]=blu
			break
	for i in range(15):
		ii=i*40
		for j in range(15):
			jj=j*40
			if tabellina[i][j]!=img[ii][jj]:
				colore=tabellina[i][j]
				for y in range(40):
					for x in range(40):
						img[ii+y][jj+x]=colore
	save(img,fname1)
	return risultato

