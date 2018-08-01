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



def destra(a,x,y):
    s=''
    while y<=560 and (a[x][y]==(0,0,0) or a[x][y]==(255,255,255)):#mi muovo verso destra, y<=560 così mi evito indexerror
        creaquadrato(a,y,x,40,(0,255,0))
        y+=40
        s+='0'
    
    y-=40
    return (s,x,y)
def giu(a,x,y):
    s=''
    while x<=560 and (a[x][y]==(0,0,0) or a[x][y]==(255,255,255)):#mi muovo verso giu, x<=560 così mi evito indexerror
        creaquadrato(a,y,x,40,(0,255,0))
        x+=40
        s+='1'
    
    x-=40
    return (s,x,y)
def sinistra(a,x,y):
    s=''
    while y>=0 and (a[x][y]==(0,0,0) or a[x][y]==(255,255,255)): #mi muovo verso sinistra, y>=560 così mi evito indexerror
        creaquadrato(a,y,x,40,(0,255,0))
        y-=40
        s+='2'
        if y<0:
            break
    
    y+=40
    return (s,x,y)
def su(a,x,y):
    s=''
    while x>=0 and (a[x][y]==(0,0,0) or a[x][y]==(255,255,255)):#mi muovo verso sopra, y>=560 così mi evito indexerror
        creaquadrato(a,y,x,40,(0,255,0))
        x-=40
        s+='3'
        if x<0:
            break
    
    x+=40
    return (s,x,y)

def creaquadrato(img,x,y,lato,c):
    for i in range(lato):
        for j in range(lato):
            img[y+j][x+i]=c

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    a=load(fname)
    right=destra(a,0,0)
    right1=right[0]
    cr=right1[1:]
    stringa=''
    stringa+=cr
    for i in range(100000000000000000000000):
        down=giu(a,right[1]+40,right[2])
        
        left=sinistra(a,down[1],down[2]-40)
        
        up=su(a,left[1]-40,left[2])
        
        right=destra(a,up[1],up[2]+40)
        
        stringa+=down[0]+left[0]+up[0]+right[0]          
        if down[0]=='' and left[0]=='' and up[0]=='' and right[0]=='':
            creaquadrato(a,up[2],up[1],40,(0,0,255))
            break
    save(a,fname1)
    return stringa