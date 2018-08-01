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

def cammino(fname, fname1):
    verde=(0,255,0)
    blu=(0,0,255)
    chessboard=load(fname) 
    mosse=[[0,0], [1,0], '']      
    passo=0        
    direzioni={0: [1,0], 1: [0,1], 2: [-1,0], 3: [0,-1]}     
    while True:
        for rotazione in range(4):
            if rotazione!=4 and mossePossibili(chessboard, mosse[0][0]+mosse[1][0], mosse[0][1]+mosse[1][1]):
                colora(chessboard, mosse[0][0], mosse[0][1], verde)
                mosse[0][0]+=mosse[1][0]
                mosse[0][1]+=mosse[1][1]
                mosse[2]+=str(passo)
                break
            else:
                passo=(passo+1)%4
                mosse[1]=direzioni[passo]
        else:
            colora(chessboard, mosse[0][0], mosse[0][1], blu)
            break
    save(chessboard, fname1)
    return mosse[2]

def colora(chessboard, x, y, c):
	for w in range(x*40,(x+1)*40):
		for h in range(y*40,(y+1)*40):
			chessboard[h][w]=c

def inside(chessboard, x, y):
    return 0<=x<len(chessboard[0]) and 0<=y<len(chessboard)

def mossePossibili(chessboard, x, y,):
    bianco=(255,255,255)
    nero=(0,0,0)
    if inside(chessboard, x*40+20, y*40+20):
        return chessboard[y*40+20][x*40+20]==bianco or chessboard[y*40+20][x*40+20]==nero
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    