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
    '''Implementare qui la funzione'''
    
    img = load(fname)
    global dimCasella 
    dimCasella = 40
    global dimensions
    dimensions = int (len(img[0])/40)
    
    fullDim = len(img)
    
    rosso = (255,0,0)
    verde = (0,255,0)
    blu = (0,0,255)
    row = 0
    passi = ''
    cantMove = 0
    direction = 0
    position = (0,0)
    
    while (cantMove != 360):
        row, col = directionToMove(position[0], position[1], direction)
        
        while (row >= fullDim or col >= fullDim or row < 0 or col < 0 or img[row][col] == rosso or img[row][col] == verde):
            direction = netxDirection(direction)
            row, col = directionToMove(position[0], position[1], direction)
            cantMove += 90
            
            if(cantMove == 360):
                coloraCasella(blu, position[0], position[1], img)
                save(img, fname1)
                #print(passi)
                return passi
        cantMove = 0
        passi += str(direction)
        coloraCasella(verde, position[0], position[1], img)
        position = (row,col)
    
def directionToMove(row,col,direction):
    if direction == 0:
        return row , col+dimCasella
    elif direction == 1:
        return row+dimCasella, col
    elif direction == 2:
        return row, col-dimCasella
    elif direction == 3:
        return row-dimCasella, col

def netxDirection(direction):
    if(direction == 3):
        direction = 0
    else:
        direction += 1
    return direction  

def coloraCasella(color, row, col, img):
     for x in range(0, dimCasella):
            for y in range(0, dimCasella):
                img[row+x][col+y] = color

#cammino('I1.png','t1.png')
