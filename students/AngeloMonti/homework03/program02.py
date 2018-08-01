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
def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    img=load(fname)
    w=h =15
    lista =[(1,0),(0,1),(-1,0),(0,-1)]
    s=40
    x=y=0
    quadrato(img,x*s,y*s,s,(0,255,0))
    f=d=step=0
    stringa=''
    dx,dy=lista[d]
    while f<4:
        if 0<=x+dx<w and 0<=y+dy<h and \
        img[(y+dy)*s][(x+dx)*s]!=(255,0,0) and  img[(y+dy)*s][(x+dx)*s]!=(0,255,0):
            f=0
            x=x+dx
            y=y+dy
            img[y][x]=(0,255,0)
            quadrato(img,x*s,y*s,s,(0,255,0))
            stringa+=str(d)
        else:
            f+=1
            d=(d+1) % 4
            dx,dy=lista[d]
        step+=1
    quadrato(img,x*s,y*s,s,(0,0,255))
    save(img, fname1)
    return stringa
    
def quadrato(img, x, y, s, c):
    '''disegna sull'immagine img un quadrato di colore c e lato s a partire dal pixel (x,y)''' 
    for px in range(x, x+s):
        for py in range(y, y+s):
            img[py][px] = c

