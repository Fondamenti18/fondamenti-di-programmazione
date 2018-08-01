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
    percorso = ""
    i = 0
    j = 0
    p = 0
    stallo = 0
    while stallo != 5:
        mossa = 0
        coloraDiVerde(img, i,j)
        if p == 0:
            if inside(img, i,j+40) and img[i][j+40] != (255,0,0) and img[i][j+40] != (0,255,0):
                percorso += "0"
                j += 40
                mossa += 1
                stallo = 0
        elif p == 1:
            if inside(img, i+40,j) and img[i+40][j] != (255,0,0) and img[i+40][j] != (0,255,0):
                percorso += "1"
                i += 40
                mossa += 1
                stallo = 0
        elif p == 2:
            if inside(img, i,j-40) and img[i][j-40] != (255,0,0) and img[i][j-40] != (0,255,0):
                percorso += "2"
                j -= 40
                mossa += 1
                stallo = 0
        elif p == 3:
            if inside(img, i-40,j) and img[i-40][j] != (255,0,0) and img[i-40][j] != (0,255,0):
                percorso += "3"
                i -= 40
                mossa += 1
                stallo = 0
        if mossa == 0:
            p = (p+1)%4
            stallo += 1

    for k in range(i, i+40):
        for h in range(j, j+40):
            img[k][h] = (0,0,255)
    save(img, fname1)
    return percorso

def coloraDiVerde(img, i, j):
    for k in range(i, i+40):
        for h in range(j, j+40):
            img[k][h] = (0,255,0)

def inside(img, i, j):
    imgWidth, imgHeight = width(img), height(img)
    if(0 <= i < imgWidth and 0 <= j < imgHeight): return True
    else: return False

def width(img): return len(img[0]) #Larghezza -------------------------------
def height(img): return len(img) #Altezza -----------------------------------
