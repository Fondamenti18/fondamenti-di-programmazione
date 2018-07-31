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


# advance = [[0, 40], [40, 0], [0, -40], [-40, 0]]
advancey = [0, 40, 0, -40]
advancex = [40, 0, -40, 0]


def step(x,y, w,h, direction, visitedSpots, img):
    nx = x + advancex[direction]
    ny = y + advancey[direction]

    if (0 <= nx < w) & (0 <= ny < h) & ((nx, ny) not in visitedSpots):
        return img[ny][nx] != (255, 0, 0)
    else:
        return False


def fillVisitedQuad(x, y, img):
    # global img 

    for i in range(40):
        c = [(0, 255, 0) for x in range(40)]
        img[y + i][x: x + 40] = c

def fillLastVisitedQuad(x, y, img):
    # global img 

    for i in range(40):
        c = [(0, 0, 255) for x in range(40)]
        img[y + i][x: x + 40] = c

def recolorPicture(visitedSpots, lastVisited, img):
    for spot in visitedSpots:
        fillVisitedQuad(spot[0], spot[1], img)
    
    fillLastVisitedQuad(lastVisited[0], lastVisited[1], img)
    
def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    # i posti dov'è già stato si registrano in un set così è veloce controllare se è già stato o meno in un posto
    # si riscrive direttamente sul risultato ritornato da fname per diminuire il più possibile il tempo di esecuzione
    # global img


    img = load(fname)
    h = len(img)
    w = len(img[0])
    
    visitedSpots = set()
    visitedSpots.add((0,0))
    lastVisited = (-1, -1)

    state = 0
    statechange = 0

    percorso = ""

    x = 0
    y = 0

    while statechange != 4:
        # returns true if we can step in this direction
        result = step(x, y, w,h, state, visitedSpots, img)

        if result:
            x += advancex[state]
            y += advancey[state]
            visitedSpots.add((x, y))
            statechange = 0
            percorso += str(state)
            continue
        else:
            statechange += 1
            state = (state + 1) % 4

    lastVisited = (x, y)


    recolorPicture(visitedSpots, lastVisited, img)

    save(img, fname1)    

    return percorso
    # debug = 0


# cammino("I2.png", "IRES.png")