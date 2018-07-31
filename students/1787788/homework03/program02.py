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

def calculatedirection(direzione):
	if direzione == (0,1):
		return (1,0)
	elif direzione == (1,0):
		return (0, -1)
	elif direzione == (0, -1):
		return (-1, 0)
	else:
		return (0,1)

		
def buildFinalString(direzione):
	if direzione == (0, 1):
		return '0'
	elif direzione == (1, 0):
		return '1'
	elif direzione == (0, -1):
		return '2'
	else:
		return '3'
		
def Creamappa(image, matrice):
	riga = 0
	for row in range(40,601,40):
		colonna = 0
		for column in range(40,601,40):
			colore(image[row-1][column-1], riga, matrice)
		riga += 1
	return matrice
	
		
def direction(matrice, direzione, prossimaposizione):
	if(matrice[prossimaposizione[0]][prossimaposizione[1]] != 1):
		direzione = calculatedirection(direzione)
	return direzione
		
def clamp(n, smallest, largest): 
  return max(smallest, min(n, largest))
  
		
def canYouMove(matrice,posizione):
	return int(matrice[posizione[0]][clamp(posizione[1]-1, 0, 14)] == 1) or int(matrice[clamp(posizione[0]-1, 0, 14)][posizione[1]] == 1) or int(matrice[clamp(posizione[0]+1, 0, 14)][posizione[1]] == 1) + int(matrice[posizione[0]][clamp(posizione[1]+1, 0, 14)] == 1) 

def colore(colore, riga, matrice):
	if(colore==(255,255,255) or colore==(0,0,0)):
		matrice[riga] += [1]
	elif(colore == (255,0,0)):
		matrice[riga] += [0]

def drawRect(img, pos, color):
  for x in range(pos[0]*40, clamp( (pos[0]*40)+40, 0, len(img))):
    for y in range(pos[1]*40, clamp( (pos[1]*40)+40, 0, len(img[0]))):
      img[x][y] = color
	  
def cammino(fname,  fname1):
	image = load(fname)
	matrice = [[], [], [], [], [], [], [],[], [], [],[], [], [], [], [] ]
	cronologia = list()
	posizione = (0,0)
	direzione = (0,1)
	cammino = ""
	matrice = Creamappa(image, matrice)
	cronologia += [posizione]
	while canYouMove(matrice,posizione) >0:
		prossimaposizione = (clamp(posizione[0]+direzione[0],0,14), clamp(posizione[1]+direzione[1],0,14))
		direzione = direction(matrice, direzione, prossimaposizione)
		if matrice[prossimaposizione[0]][prossimaposizione[1]] == 1:
			matrice[posizione[0]][posizione[1]] = 0
			posizione = (clamp(posizione[0]+direzione[0],0,14), clamp(posizione[1]+direzione[1],0,14))
			matrice[posizione[0]][posizione[1]] = 0
			cronologia += [posizione]
			cammino += buildFinalString(direzione)
	for pos in cronologia:
		drawRect(image, pos, (0,255,0))
	drawRect(image, cronologia[-1],(0,0,255))
	save(image, fname1)
	return cammino
	
		
        
