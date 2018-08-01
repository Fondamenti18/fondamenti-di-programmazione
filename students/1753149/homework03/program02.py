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

import png
from immagini import *
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)

def cammino(fname, fname1):
    img=load(fname)
    x=0
    y=0
    h=40
    a=img[x][y]
    c=colore(img,x,y)
    stringa=''
    b=len(img)
    for i in img:
        while y+h<=599 and img[x][y+h] and img[x][y+h]!=rosso and img[x][y+h]!=verde:
            a=img[x][y+h]
            c=colore(img,x,y)
            y=y+h
            stringa+='0'
        while x+h<=599 and img[x+h][y] and img[x+h][y]!=rosso and img[x+h][y]!=verde:
            a=img[x+h][y]
            c=colore(img,x,y)
            x=x+h
            stringa+='1'
        while y-h>=0 and img[x][y-h] and img[x][y-h]!=rosso and img[x][y-h]!=verde:
            a=img[x][y-h]
            c=colore(img,x,y)
            y=y-h
            stringa+='2'
        while x-h>=0 and img[x-h][y] and img[x-h][y]!=rosso and img[x-h][y]!=verde:
            a=img[x-h][y]
            c=colore(img,x,y)
            x=x-h
            stringa+='3'
    c=coloreB(img,x,y)
    save(img, fname1)
    return stringa
        
def colore(img,x,y):
    h=40
    w=40
    c=verde
    for j in range(y,y+h):
        for i in range(x,x+w):
            img[i][j]=c
    return img

def coloreB(img,x,y):
    h=40
    w=40
    c=blu
    for j in range(y,y+h):
        for i in range(x,x+w):
            img[i][j]=c
    return img