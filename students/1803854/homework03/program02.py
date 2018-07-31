'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto direz destra (x crescente). 
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
    '0' per un passo direz destra (x crescenti)
    '1' per un passo direz il basso (y crescenti)
    '2' per un passo direz sinistra (x decrescenti)
    '3' per un passo direz l'alto (y decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt 

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
'''

from immagini import *

rosso = (255, 0, 0)
verde = (0, 255, 0)
blu = (0, 0, 255)

def width(image):
	return len(image[0])

def colora(image, puntox, puntoy, colore):
	for i in range(puntox, puntox+40):
		for m in range(puntoy, puntoy+40):
			image[m][i] = colore

def cammino(fname,  fname1, x = 0, y = 0):
	'''
	'''
	img = load(fname)
	dir_count = 0
	contatore_blu = 0
	percorso = ''
	while contatore_blu != 1:
		colora(img, x, y, verde)
		if dir_count == 0:
			temp = cammino_right(img, x, y, dir_count, contatore_blu)
			x = temp[0]
			y = temp[1]
			dir_count = temp[2]
			contatore_blu = temp[3]
		elif dir_count == 1:
			temp = cammino_down(img, x, y, dir_count, contatore_blu)
			x = temp[0]
			y = temp[1]
			dir_count = temp[2]
			contatore_blu = temp[3]
		elif dir_count == 2:
			temp = cammino_left(img, x, y, dir_count, contatore_blu)
			x = temp[0]
			y = temp[1]
			dir_count = temp[2]
			contatore_blu = temp[3]
		elif dir_count == 3:
			temp = cammino_up(img, x, y, dir_count, contatore_blu)
			x = temp[0]
			y = temp[1]
			dir_count = temp[2]
			contatore_blu = temp[3]
		percorso += str(dir_count)
	colora(img, x, y, blu)
	percorso = percorso[:-1]
	save(img, fname1)
	return percorso

def cammino_right(image, x, y, direz, contatore):
	if not (x == 560 or image[y][x+40] == rosso or image[y][x+40] == verde):
		x += 40
	elif not (y == 560 or image[y+40][x] == rosso or image[y+40][x] == verde):
		y += 40
		direz = 1
	elif not (y == 0 or image[y-20][x] == rosso or image[y-20][x] == verde):
		y -= 40
		direz = 3
	else:
		contatore += 1
	return x, y, direz, contatore


def cammino_down(image, x, y, direz, contatore):
	if not (y == 560 or image[y+40][x] == rosso or image[y+40][x] == verde):
		y += 40
	elif not (x == 0 or image[y][x-20] == rosso or image[y][x-20] == verde):
		x -= 40
		direz = 2
	elif not (x == 560 or image[y][x+40] == rosso or image[y][x+40] == verde):
		x += 40
		direz = 0
	else:
		contatore += 1
	return x, y, direz, contatore
	
def cammino_left(image, x, y, direz, contatore):
	if not (x == 0 or image[y][x-20] == rosso or image[y][x-20] == verde):
		x -= 40
	elif not (y == 0 or image[y-20][x] == rosso or image[y-20][x] == verde):
		y -= 40
		direz = 3
	elif not (y == 560 or image[y+40][x] == rosso or image[y+40][x] == verde):
		y += 40
		direz = 1
	else:
		contatore += 1
	return x, y, direz, contatore

def cammino_up(image, x, y, direz, contatore):
	if not (y == 0 or image[y-20][x] == rosso or image[y-20][x] == verde):
		y -= 40
	elif not (x == 560 or image[y][x+40] == rosso or image[y][x+40] == verde):
		x += 40
		direz = 0
	elif not (x == 0 or image[y][x-20] == rosso or image[y][x-20] == verde):
		x -= 40
		direz = 2
	else:
		contatore += 1
	return x, y, direz, contatore
				
if __name__ == '__main__':
	cammino('I3.png', 'sas.png')
			
