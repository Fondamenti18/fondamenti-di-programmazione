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

def cammino(fname,  fname1):
	scacchiera = load(fname)
	percorso = ''
	h, b = (len(scacchiera), len(scacchiera[0]))
	x, y, n, d = (0, 0, 0, 0)
	direzione = [(40, 0), (0, 40), (-40, 0), (0, -40)]
	colore = {'bianco' : (255, 255, 255),
	'nero' : (0, 0, 0),
	'verde' : (0, 255, 0),
	'blu' : (0, 0, 255)}
	scacchiera = ricolora(scacchiera, x, y, colore['verde'])
	while n != 4:
		scacchiera, x, y, d, n, percorso = step(scacchiera, x, y, direzione, n, d, h, b, colore, percorso)
	scacchiera = ricolora(scacchiera, x, y, colore['blu'])
	save(scacchiera, fname1)
	return percorso
	
def step(scacchiera, x, y, direzione, n, d, h, b, colore, percorso):
	tx = x + direzione[d][0]
	ty = y + direzione[d][1]
	if ((tx >= 0 and tx < b) and (ty >= 0 and ty < h)) and (scacchiera[ty][tx] == colore['nero'] or scacchiera[ty][tx] == colore['bianco']):
		x = tx
		y = ty 
		n = 0
		percorso += str(d)
		scacchiera = ricolora(scacchiera, x, y, colore['verde'])
	else:
		n += 1
		d = (d+1)%4
	return scacchiera, x, y, d, n, percorso
	
def ricolora(scacchiera, x, y, colore):
	for i in range(40):
		for j in range(40):
			scacchiera[y+i][x+j] = colore
	return scacchiera
	