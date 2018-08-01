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
    img=load(fname)
    blue=(0,0,255)
    green=(0,255,0)
    red=(255,0,0)
    white=(255,255,255)
    black=(0,0,0)
    x=0
    y=0
    ctr=0
    colora(x,y,green,img)
    stringa=''
    for i in range(0,7000):
            if ctr==0:
                    x,ctr,appoggio=right(img,x+40,y,red,green)
                    stringa+=appoggio
            elif ctr==1:
                    y,ctr,appoggio=bottom(img,x,y+40,red,green)
                    stringa+=appoggio
            elif ctr==2:
                    x,ctr,appoggio=left(img,x-40,y,red,green)
                    stringa+=appoggio
            elif ctr==3:
                    y,ctr,appoggio=top(img,x,y-40,red,green)
                    stringa+=appoggio
            else:
                colora(x,y,blue,img)
                break
    save(img,fname1)
    return stringa

    

    
def right(img,x,y,red,green):
    risultato=''
    while inside(img,x,y)==True and img[y][x]!= red and img[y][x]!= green:
        colora(x,y,green,img)
        risultato+="0"
        x+=40
    x-=40
    if inside(img,x,y+40)==True and img[y+40][x]!=red and img[y+40][x]!=green :
        ctr=1
    elif inside(img,x,y-40)==True and img[y-40][x]!=red and img[y-40][x]!=green :
        ctr=3
    else:
        ctr=4
    return x,ctr,risultato

def bottom(img,x,y,red,green):
    risultato=''
    while inside(img,x,y)==True and img[y][x]!= red and img[y][x]!= green:
        colora(x,y,green,img)
        risultato+="1"
        y+=40
    y-=40
    if inside(img,x-40,y)==True and img[y][x-40]!=red and img[y][x-40]!=green :
        ctr=2
    elif inside(img,x+40,y)==True and img[y][x+40]!=red and img[y][x+40]!=green :
        ctr=0
    else:
        ctr=4
    return y,ctr,risultato

def left(img,x,y,red,green):
    risultato=''
    while inside(img,x,y)==True and img[y][x]!= red and img[y][x]!= green:
        colora(x,y,green,img)
        risultato+="2"
        x-=40
    x+=40
    if inside(img,x,y-40)==True and img[y-40][x]!=red and img[y-40][x]!=green :
        ctr=3
    elif inside(img,x,y+40)==True and img[y+40][x]!=red and img[y+40][x]!=green :
        ctr=1
    else:
        ctr=4
    return x,ctr,risultato

def top(img,x,y,red,green):
    risultato=''
    while inside(img,x,y)==True and img[y][x]!= red and img[y][x]!= green:
        colora(x,y,green,img)
        risultato+="3"
        y-=40
    y+=40
    if inside(img,x+40,y)==True and img[y][x+40]!=red and img[y][x+40]!=green :
        ctr=0
    elif inside(img,x-40,y)==True and img[y][x-40]!=red and img[y][x-40]!=green :
        ctr=2
    else:
        ctr=4
    return y,ctr,risultato

def inside (img,i,j):
    iw,ih=len(img[0]),len(img)
    return 0<=i<iw and 0<=j<ih

def colora(x,y,c,img):
    for j in range(y,y+40):
        for i in range(x,x+40):
            img[j][i]=c
    



    
    
            
    
        
