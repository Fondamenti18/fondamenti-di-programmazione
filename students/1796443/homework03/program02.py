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

def col(img,x,y,c):
    for i in range(y,y+40):
        for j in range(x,x+40):
            img[i][j]=c

def p0(img,x,y,s,p,c):
    if x+40<600:
        if img[y][x+40]!=(255,0,0) and img[y][x+40]!=(0,255,0):
            s+=p
            x+=40
            c=0
            col(img,x,y,(0,255,0))
        else:
            p='1'
            c+=1
    else:
        p='1'
        c+=1
    return (x,y,s,p,c)

def p1(img,x,y,s,p,c):
    if y+40<600:
        if img[y+40][x]!=(255,0,0) and img[y+40][x]!=(0,255,0):
            s+=p
            y+=40
            c=0
            col(img,x,y,(0,255,0))
        else:
            p='2'
            c+=1
    else:
        p='2'
        c+=1
    return (x,y,s,p,c)

def p2(img,x,y,s,p,c):
    if x>0:
        if img[y][x-40]!=(255,0,0) and img[y][x-40]!=(0,255,0):
            s+=p
            x-=40
            c=0
            col(img,x,y,(0,255,0))
        else:
            p='3'
            c+=1
    else:
        p='3'
        c+=1
    return (x,y,s,p,c)

def p3(img,x,y,s,p,c):
    if y>0:
        if img[y-40][x]!=(255,0,0) and img[y-40][x]!=(0,255,0):
            s+=p
            y-=40
            c=0
            col(img,x,y,(0,255,0))
        else:
            p='0'
            c+=1
    else:
        p='0'
        c+=1
    return (x,y,s,p,c)

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    img=load(fname)
    s=''
    p='0'
    c=0
    x=0
    y=0
    col(img,x,y,(0,255,0))
    while c<5:
        if p=='0':
            x,y,s,p,c=p0(img,x,y,s,p,c)
        if p=='1':
            x,y,s,p,c=p1(img,x,y,s,p,c)
        if p=='2': 
            x,y,s,p,c=p2(img,x,y,s,p,c)
        if p=='3':
            x,y,s,p,c=p3(img,x,y,s,p,c)
    col(img,x,y,(0,0,255))
    save(img,fname1)
    return s
