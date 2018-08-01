'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in alto a sinistra della scacchiera ed e' rivolto verso destra (x crescente). 
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

nero=(0, 0, 0)
bianco=(255, 255, 255)
blu=(0, 0, 255)
verde=(0, 255, 0)

def orario(direzione):
	if direzione==(0, 1):
		return (1, 0)
	if direzione==(1, 0):
		return (0, -1)
	if direzione==(0, -1):
		return (-1, 0)
	elif direzione==(-1, 0):
		return (0, 1)
		
def casella(rgb):
	return rgb==bianco or rgb==nero
	
def dirseg(matrice, posizione):
	return \
		int(matrice[posizione[0]][(max(0,min(posizione[1]-1, 14)))]==1)+ \
		int(matrice[(max(0,min(posizione[0]-1, 14)))][posizione[1]]==1)+ \
		int(matrice[(max(0,min(posizione[0]+1, 14)))][posizione[1]]==1)+ \
		int(matrice[posizione[0]][(max(0,min(posizione[1]+1, 14)))]==1) 

def cammino(fname, fname1):
	file=load(fname)
	matrice=[[] for n in range(0, 15)]
	for ascissa in range(0, 40*15, 40):
		for n, ordinata in enumerate(range(0, 40*15, 40)):
				matrice[n]+=[int(casella(file[ordinata][ascissa]))]
	matrice[0][0]=2
	posizione=(0, 0)
	direzione=(0, 1) 
	matr=""
	while dirseg(matrice, posizione)>0:
		passoseg=(max(0,min(posizione[0]+direzione[0], 14))), (max(0,min(posizione[1]+direzione[1], 14)))
		quadrato=matrice[passoseg[0]][passoseg[1]]
		if quadrato**2==1:
			matrice[passoseg[0]][passoseg[1]]=2
			posizione=(posizione[0]+direzione[0], posizione[1]+direzione[1])
			if direzione==(0, 1):
				matr+='0'
			if direzione==(1, 0):
				matr+='1'
			if direzione==(0, -1):
				matr+='2'
			elif direzione==(-1, 0):
				matr+='3'
		else:
			direzione=orario(direzione)
	for x, ascissa in enumerate(matrice):
		for y, z in enumerate(ascissa):
			if z==2:
				posqua=(x * 40, y * 40)
				for m in range(0, 40):
					for s in range(0, 40):
						if (x, y)==posizione:
							file[posqua[0]+s][posqua[1]+m]=blu
						else:
							file[posqua[0]+s][posqua[1]+m]=verde
	save(file, fname1)
	return matr