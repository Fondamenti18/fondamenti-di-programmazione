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

def drawSquare(img, x1, y1, len, color):
    for x in range(x1, x1+len):
        for y in range(y1, y1+len):
            img[y][x] = color

def getW(img):
    return len(img[0])

def getH(img):
    return len(img)

def canGo(img, x, y, dx, dy, LC, W, H):
    return 0 <= (x + dx) * LC < W and 0 <= (y + dy) * LC < H and\
           img[(y + dy) * LC][(x + dx) * LC] != (255, 0, 0) and img[(y + dy) * LC][(x + dx) * LC] != (0, 255, 0)

def cammino(fname, fname1):
    newDir = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0):(0, -1), (0, -1):(1, 0)}
    code = {(1, 0):'0', (0, 1):'1', (-1, 0):'2', (0, -1):'3'}

    img = load(fname)
    W, H = getW(img), getH(img)
    x, y, dx, dy, LC = 0, 0, 1, 0, 40
    path = ''
    goOn = True
    while goOn:
        drawSquare(img, x*LC, y*LC, LC, (0, 255, 0))
        times = 0
        while times < 4 and (not canGo(img, x, y, dx, dy, LC, W, H)):
            dx, dy = newDir[(dx, dy)]
            times += 1
        goOn = (times != 4)
        if goOn:
            path += code[(dx, dy)]
            x += dx
            y += dy

    drawSquare(img, x*LC, y*LC, LC, (0, 0, 255))
    save(img, fname1)
    return path

if __name__=='__main__':
    print(cammino('I4.png', 'out.png'))
