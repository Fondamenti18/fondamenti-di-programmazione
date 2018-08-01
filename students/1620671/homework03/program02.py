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
    p = '0'
    x = 0
    y = 0
    colora(img,0,0,(0,255,0))
    while True:
        vialibera =guarda(img, y, x, p[-1], 0)[0]
        mod = guarda(img, y, x, p[-1], 0)[1]
        if vialibera == True:
            if mod == '0':
                x += 40
                colora(img,y,x,(0,255,0))
                p += '0'
            elif mod == '1':
                y += 40
                colora(img, y,x,(0,255,0))
                p += '1'
            elif mod == '2':
                x -= 40
                colora(img, y,x,(0,255,0))
                p += '2'
            elif mod == '3':
                y -= 40
                colora(img,y,x,(0,255,0))
                p += '3'
        elif vialibera == False:
            colora(img,y,x,(0,0,255))
            break
    save(img, fname1)
    p = p[1:]
    return p



def colora(img, y0, x0, c):
    for y in range(y0, y0+40):
        for x in range(x0, x0+40):
            if inside(img,x,y):
                img[y][x] = c

def inside(img, x, y):
    return 0 <= y < righe(img) and 0 <= x < colonne(img)

def righe(img) : return len(img)
def colonne(img) : return len(img[0])


def guarda(img, y0, x0, mod , count):
    ver = [(0,255,0),(255,0,0)]
    vialibera = False
    if mod == '0' and count <= 5:
        if x0 == 560:
            count += 1
            mod = '1'
            return guarda(img, y0, x0, mod, count)
        if img[y0][x0+40] in ver or not inside(img, x0+40, y0):
            count += 1
            mod = '1'
            return guarda(img, y0, x0, mod, count)
        else:
            vialibera = True
    elif mod == '1' and count <= 5:
        if y0 == 560:
            count += 1
            mod = '2'
            return guarda(img, y0, x0, mod, count)
        if img[y0+40][x0] in ver or not inside(img, x0, y0+40):
            count += 1
            mod = '2'
            return guarda(img, y0, x0, mod, count)
        else:
            vialibera = True
    elif mod == '2' and count <= 5:
        if x0 == 0:
            count += 1
            mod = '3'
            return guarda(img, y0, x0, mod, count)
        if img[y0][x0-40] in ver or not inside(img, x0-40, y0):
            count += 1
            mod = '3'
            return guarda(img, y0, x0, mod, count)
        else:
            vialibera = True
    elif mod == '3' and count <= 5:
        if y0 == 0:
            count += 1
            mod = '0'
            return guarda(img, y0, x0, mod, count)
        if img[y0-40][x0] in ver or not inside(img, x0, y0-40):
            count += 1
            mod = '0'
            return guarda(img, y0, x0, mod, count)
        else:
            vialibera = True
    elif count > 5:
        vialibera = False
    return vialibera, mod