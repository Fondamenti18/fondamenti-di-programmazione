'''
Un robottino deve muoversi su di una scacchiera  15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli 
(queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.png .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra. 
Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o verticale. 
Le regole di movimento del robottino sono le seguenti: 
al generico step, si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci e' gia transitato in passato. 
Se invece la cella risulta occupata o e' una cella su  cui ha gia transitato,  ruota di 90 gradi in senso 
orario ed aspetta lo step successivo. Dopo aver ruotato  di 360 gradi senza essere riuscito a spostarsi si ferma. 

progettare la funzione  percorso(fname, fname1) che presi in output:
- il percorso di un file (fname) contenente l'immagine in formato .png di una scacchiera con ostacoli
- il percorso di un file di tipo .png(fname1)
legge l'immagine della scacchiera in fname, colora di verde le celle della scacchiera percorse dal robottino prima di fermarsi, 
colora di blu la cella in cui il robottino si ferma e registra l'immagine ricolorata nel file fname1. 
Inoltre restituisce una stringa dove in sequanza sono codificati i passi effettuati dal robottino prima di fermarsi. 
La codifica e' a seguente: '0' per un passo verso destra, '1' per un passo verso il basso, '2' per un passo 
verso sinistra e '3' per un passo verso l'alto.

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 


Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt 

'''

from immagini import *

rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
    
h = 15
w = 15
l = 40
direzioni = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    img=load(fname)
    x,y = 0, 0
    percorso = ''
    direzione = 0
    svoltato = 0
    vai = True
    while vai:
        vai, x, y, direzione, percorso, svoltato = step(img, x, y, direzione, percorso, svoltato, vai)
    save(img, fname1)
    return percorso

def step(img, x, y, direzione, percorso, svoltato, vai):
    dx, dy = direzioni[direzione]
    nx, ny = x+dx, y+dy
    if 0 <= nx < w and 0 <= ny < h and img[ny*l][nx*l] != rosso and img[ny*l][nx*l] != verde:
        svoltato = 0
        percorso += str(direzione)
        colora(img, x, y, l, verde)
        x, y = nx, ny
    else:
        direzione = (direzione+1)%4
        svoltato += 1
        if svoltato > 3:
            colora(img, x, y, l, blu)
            vai = False
    return vai, x, y, direzione, percorso, svoltato


def colora(img, x, y, l, colore):
    for X in range(0, l):
        for Y in range(0, l):
            img[y*l+X][x*l+Y] = colore



if __name__ == '__main__':
    print(cammino('I1.png', 't1.png'))

