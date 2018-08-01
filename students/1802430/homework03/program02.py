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
    prova=load(fname)
    cod='' 
    str(cod)
    
    y=0
    x=0

    while ins(prova, x+40, y)!=False and ((prova[y][x+40]==(255,255,255) or prova[y][x+40]==(0,0,0)))or ins(prova, x, y+40)!=False and ((prova[y+40][x]==(255,255,255) or prova[y+40][x]==(0,0,0)))\
    or  ins(prova, x-40, y)!=False and ((prova[y][x-40]==(255,255,255) or prova[y][x-40]==(0,0,0))) or  ins(prova, x, y-40)!=False and ((prova[y-40][x]==(255,255,255) or prova[y-40][x]==(0,0,0))):
          
        x,y,cod=destra(prova,x,y,cod)
        rect(prova,x,y, 40, 40,(0,255,0) )
        x,y,cod=giu(prova,x,y,cod)
        rect(prova,x,y, 40, 40,(0,255,0) )    
        x,y,cod=sinistra(prova,x,y,cod)
        rect(prova,x,y, 40, 40,(0,255,0) )
        x,y,cod=su(prova,x,y,cod)
    
    rect(prova,x,y, 40, 40,(0,0,255) )
    
    save(prova,fname1)
    #display(Image(fname1))
    return cod
    
def ins(img, x, y):
    return 0 <= y < len(img[0]) and 0 <= x < len(img)

def destra(prova,x,y,cod):
    while ins(prova, x+40, y)!=False and (prova[y][x+40]==(255,255,255) or prova[y][x+40]==(0,0,0)):
            rect(prova,x,y, 40, 40,(0,255,0) )
            x+=40
            cod+='0'
    return x,y,cod
    
def giu(prova,x,y,cod):
    while ins(prova, x, y+40)!=False and(prova[y+40][x]==(255,255,255) or prova[y+40][x]==(0,0,0)):
            rect(prova,x,y, 40, 40,(0,255,0) )
            y+=40
            cod+='1'
    return x,y,cod

def sinistra(prova,x,y,cod):
     while ins(prova, x-40, y)!=False and (prova[y][x-40]==(255,255,255) or prova[y][x-40]==(0,0,0)):
            rect(prova,x,y, 40, 40,(0,255,0) )
            x-=40
            cod+='2'
     return x,y,cod

def su(prova,x,y,cod):
    while ins(prova, x, y-40)!=False and (prova[y-40][x]==(255,255,255) or prova[y-40][x]==(0,0,0)):
            rect(prova,x,y, 40, 40,(0,255,0) )
            y-=40
            cod+='3'
    return x,y,cod
    

def rect(img, x, y, w, h, c):
    '''disegna sull'immagine img un rettangolo di colore c, ampiezza w e altezza h a partire dal pixel (y,x)'''
    for px in range(x, x+w):
        for py in range(y, y+h):
            if ins(img,px,py):
                img[py][px] = c