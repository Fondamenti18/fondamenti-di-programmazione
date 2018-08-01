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

def width(img):
    return len(img[0])
def heigth(img):
    return len(img)
def cammino(fname,  fname1):
    img=load(fname)
    percorso=''
    x=0
    y=0
    controllo=0
    img=colora(img,x,y,x+40,y+40,(0,255,0))
    while controllo<5:
        img,x,percorso,controllo=destra(img,x,y,percorso,controllo)
       # print('c=',controllo)
        img,y,percorso,controllo=basso(img,x,y,percorso,controllo)
        #print(controllo)
        img,x,percorso,controllo=sinistra(img,x,y,percorso,controllo)
      #  print(controllo)
        img,y,percorso,controllo=alto(img,x,y,percorso,controllo)
    img=colora(img,x,y,x+40,y+40,(0,0,255))
    img=save(img,fname1)
    return percorso
 
def destra(img,x,y,percorso,controllo):
    try:
        while img[y][x+40]!=(255,0,0) and img[y][x+40]!=(0,255,0) and x+40<width(img):
            controllo=0
            img=colora(img,x+40,y,x+80,y+40,(0,255,0))
            x+=40
            percorso+='0'
        controllo+=1
        return img,x,percorso,controllo
    except IndexError:
        return img,x,percorso,controllo
def basso(img,x,y,percorso,controllo):
    try:
        while img[y+40][x]!=(255,0,0) and img[y+40][x]!=(0,255,0) and y+40<heigth(img):
            controllo=0
            img=colora(img,x,y+40,x+40,y+80,(0,255,0))
            y+=40
            percorso+='1'
        controllo+=1
        return img,y,percorso,controllo
    except IndexError:
        return img,y,percorso,controllo
def sinistra(img,x,y,percorso,controllo):
    try:
        while img[y][x-40]!=(255,0,0) and  img[y][x-40]!=(0,255,0) and (x-40)>=0:
            controllo=0
            img=colora(img,x-40,y,x,y+40,(0,255,0))
            x-=40
            percorso+='2'
        controllo+=1
        return img,x,percorso,controllo
    except IndexError:
        print('SUPERBIMBO')
        return img,x,percorso,controllo

def alto(img,x,y,percorso,controllo):
    try:
        while img[y-40][x]!=(255,0,0) and  img[y-40][x]!=(0,255,0) and y-40>=0:
            controllo=0
            img=colora(img,x,y-40,x+40,y,(0,255,0))
            y-=40
            percorso+='3'
        controllo+=1
        return img,y,percorso,controllo
    except IndexError:
        return img,y,percorso,controllo

def colora(img,x,y,w,h,c):
    for py in range(y,h):
        for px in range(x,w):
            img[py][px]=c
    return img