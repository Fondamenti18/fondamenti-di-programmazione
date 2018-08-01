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
	image = load(fname)
	dir = 0
	path = []
	position = [0, 0]
	move(image, dir, path, position)
	save(image, fname1)
	return ''.join(path)
	
def move(image, dir, path, position):
	green = (0, 255, 0)
	blue = (0, 0, 255)
	i = 0
	recolor(image, position, green)
	while i < 4:
		if in_borders(image, dir, position) and not block(image, dir, position):
			i = 0
			position[0] += y_step(dir)
			position[1] += x_step(dir)
			recolor(image, position, green)
			path += [str(dir)]
		else:
			dir = change_dir(dir)
			i += 1
	recolor(image, position, blue)
			
def recolor(image, position, color):
	step = 40
	for r in range(position[0], position[0] + step):
		for c in range(position[1], position[1] + step):
			image[r][c] = color
			
def change_dir(dir):
	if dir == 3:
		dir = 0
	else:
		dir += 1
	return dir
		
def block(image, dir, p):
	red = (255, 0, 0)
	green = (0, 255, 0)
	x = x_step(dir)
	y = y_step(dir)
	return image[p[0] + y][p[1] + x] == red or image[p[0] + y][p[1] + x] == green
	
def in_borders(image, dir, p):
	x = x_step(dir)
	y = y_step(dir)
	return p[0] + y >= 0 and p[0] + y < len(image) and p[1] + x >= 0 and p[1] + x < len(image[0])
	
def y_step(dir):
	step = 40
	if dir == 0 or dir == 2:
		step = 0
	if dir == 3:
		step *= -1
	return step
	
def x_step(dir):
	step = 40
	if dir == 1 or dir == 3:
		step = 0
	if dir == 2:
		step *= -1
	return step
	
	
