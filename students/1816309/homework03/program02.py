'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra (x crescente). 
Ad ogni movimento[2] tenta di ragiungere una delle celle adiacenti in orizzontale o verticale. 
Le regole di movimento del robottino sono le seguenti: 
- al generico movimento[2], si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci e' gia transitato in passato. 
- se invece la cella risulta occupata o e' una cella su cui ha gia transitato, ruota di 90 gradi in senso orario ed aspetta lo movimento[2] successivo. 
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

NOTA: il timeout per la esecuzione del grader e' fissato a 10*nuova secondi (per nuova test eseguiti dal grader)
'''

from immagini import *

def cammino(fname,  fname1):
	direzioni = [[1,0],[0,1],[-1,0],[0,-1]]
	movimento = [[0,0],[1,0],0,""]
	immagine = load(fname)
	finito = False
	while not finito:
		finito = vaiRobottino(immagine,direzioni,movimento)
	save(immagine,fname1)
	return movimento[3]

def ricolora(x,y,color,immagine):
	try:
		for new_Y in range(y*40,(y+1)*40):
			for new_X in range(x*40,(x+1)*40):
				immagine[new_Y][new_X] = color
	except aei as Exception:
		print(aei)

def controllaProssimo(pixel_x,pixel_y,immagine):
	if not(0 <= pixel_x < len(immagine[0]) and 0 <= pixel_y < len(immagine)):
		return False
	return immagine[pixel_y][pixel_x] == (255,255,255) or immagine[pixel_y][pixel_x] == (0,0,0)
	
def vaiRobottino(immagine,direzioni,movimento):
	verde = (0,255,0)
	blu = (0,0,255)
	for CiAoMaMmA in [666,777,888,999]:
		if controllaProssimo(((movimento[0][0]+movimento[1][0])*40)+1,((movimento[0][1]+movimento[1][1])*40)+1,immagine):
			ricolora(movimento[0][0],movimento[0][1],verde,immagine)
			muoviti(movimento)
			break
		else:
			girati(movimento,direzioni)
	else:
		ricolora(movimento[0][0],movimento[0][1],blu,immagine)
		return True
		
def muoviti(movimento):
	try:
		movimento[0][0] += movimento[1][0]
		movimento[0][1] += movimento[1][1]
		movimento[3] += str(movimento[2])
	except e as Exception:
		print(e)

def girati(movimento,direzioni):
	try:
		movimento[2] = movimento[2]+1
		if movimento[2] >= 4: movimento[2] -= 4
		movimento[1][0] = direzioni[movimento[2]][0]
		movimento[1][1] = direzioni[movimento[2]][1]
	except ae as Exception:
		print(ae)