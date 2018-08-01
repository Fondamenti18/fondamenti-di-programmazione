'''
Un robottino deve muoversi su di una scacchiera di 15 col 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.priga .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra (col crescente). 
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
    '0' per un passo verso destra (col crescenti)
    '1' per un passo verso il basso (riga crescenti)
    '2' per un passo verso sinistra (col decrescenti)
    '3' per un passo verso l'alto (riga decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.tcolt 

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
'''

from immagini import *

def width(img):
    return len(img[0])

def height(img):
    return len(img)

def colora_quadro(col, riga, l, img, c):
    for i in range(riga, riga+l):
        for j in range(col, col+l):
            img[i][j] = c
    
def check_right(col, riga, l, img):
    return img[riga][col+l] != (255, 0, 0) if is_inside(col+l, riga, img) else False

def check_down(col, riga, l, img):
    return img[riga+l][col] != (255, 0, 0) if is_inside(col, riga+l, img) else False

def check_left(col, riga, l, img):
    if is_inside(col-l, riga, img):
        return img[riga][col-l] != (255, 0, 0)
    return False

def check_up(col, riga, l, img):
    return img[riga-l][col] != (255, 0, 0) if is_inside(col, riga-l, img) else False

def is_inside(col, riga, im):
    return 0 <= col < width(im) and 0 <= riga < height(im)  
 
def cammino(fname,  fname1):
    im = load(fname)
    lato = len(im)//15
    visited = [(0, 0)]
    col = riga = 0
    codice = ""

    colora_quadro(col, riga, lato, im, (0, 255, 0))

    for _ in range(lato*2):
        while check_right(col, riga, lato, im) and (col+lato, riga) not in visited:
            codice += '0'
            col += lato
            colora_quadro(col, riga, lato, im, (0, 255, 0))
            visited.append((col, riga))

        while check_down(col, riga, lato, im) and (col, riga+lato) not in visited:
            codice += '1'
            riga += lato
            colora_quadro(col, riga, lato, im, (0, 255, 0))
            visited.append((col, riga))
           
        while check_left(col, riga, lato, im) and (col-lato, riga) not in visited:
            codice += '2'
            col -= lato
            colora_quadro(col, riga, lato, im, (0, 255, 0))
            visited.append((col, riga))
                
        while check_up(col, riga, lato, im) and (col, riga-lato) not in visited:
            codice += '3'
            riga -= lato
            colora_quadro(col, riga, lato, im, (0, 255, 0))
            visited.append((col, riga))

    colora_quadro(visited[-1][0], visited[-1][1], lato, im, (0, 0, 255))
 
    save(im, fname1)
    return codice
