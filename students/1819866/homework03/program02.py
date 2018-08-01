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
    img = load(fname)
    stringa = ''
    traccia = []
    posx = 0
    posy = 0
    img = colora40(img, posy, posx, (0, 255, 0))
    traccia += [(posy, posx)]
    a = 1
    while a != 0:
        a = 0
        while inside(img, posy, posx + 40) and img[posy][posx + 40] != (255, 0, 0) and (posy, posx + 40) not in traccia:
            posx = posx + 40
            img = colora40(img, posy, posx, (0, 255, 0))
            stringa += '0'
            traccia += [(posy, posx)]
            a = 1
        while inside(img, posy + 40, posx) and img[posy + 40][posx] != (255, 0, 0) and (posy + 40, posx) not in traccia:
            posy = posy + 40
            img = colora40(img, posy, posx, (0, 255, 0))
            stringa += '1'
            traccia += [(posy, posx)]
            a = 1
        while inside(img, posy, posx - 40) and img[posy][posx - 40] != (255, 0, 0) and (posy, posx - 40) not in traccia:
            posx = posx - 40
            img = colora40(img, posy, posx, (0, 255, 0))
            stringa += '2'
            traccia += [(posy, posx)]
            a = 1
        while inside(img, posy - 40, posx) and img[posy - 40][posx] != (255, 0, 0) and (posy - 40, posx) not in traccia:
            posy = posy - 40
            img = colora40(img, posy, posx, (0, 255, 0))
            stringa += '3'
            traccia += [(posy, posx)]
            a = 1
    img = colora40(img, posy, posx, (0, 0, 255))
    save(img, fname1)
    return stringa
    
    

def inside(lista_di_liste, y, x):
    h = len(lista_di_liste)
    l = len(lista_di_liste[0])
    if 0 <= y < h and 0 <= x < l: 
        return True
    else: return False
    
def colora40(img, posy, posx, c):
    for riga in range(posy, posy + 40):
        for pixel in range(posx, posx + 40):
            img[riga][pixel] = c
    return img
    

    