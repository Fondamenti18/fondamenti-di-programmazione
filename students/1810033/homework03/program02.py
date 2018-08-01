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
def colora(a,e,b,c,d):
    for i in range(a-20,e+20):
        for l in range(b-20,c+20):
            d[i][l]=(0,255,0)
    return d
def colorag(a,b,d):
    for i in range(a-20,a+20):
        for l in range(b-20,b+20):
            d[i][l]=(0,0,255)
    return d
def destra(a,b,d,e):
    f=set()
    w=(a,b)
    for l in range(b+40,len(d[0]),40):
            if d[a][l]!=(255,0,0) and d[a][l]!=(0,255,0):
                w=(a,l)
                d=colora(a,a,b,l,d)
                e=e+'0'
            else :
                
                break
    
    return d,w,e
def basso(a,b,d,e):
    f=set()
    w=(a,b)
    for i in range(a+40,len(d),40):
            if d[i][b]!=(255,0,0) and d[i][b]!=(0,255,0):
                w=(i,b)
                d=colora(i,i,b,b,d)
                e=e+'1'
            else :
              break
    
    return d,w,e
def sinistra(a,b,d,e):
    f=set()
    w=(a,b)
    for l in range(b-40,19,-40):
            if d[a][l]!=(255,0,0) and d[a][l]!=(0,255,0):
                w=(a,l)
                d=colora(a,a,l,l,d)
                e=e+'2'
            else :
                
                break
    
    return d,w,e
def alto(a,b,d,e):
    f=set()
    w=(a,b)
    for i in range(a-40,19,-40):
            if d[i][b]!=(255,0,0) and d[i][b]!=(0,255,0):
                w=(i,b)
                d=colora(i,i,b,b,d)
                e=e+'3'
            else :
                
                break
    
    return d,w,e
def cammino(fname,  fname1):
    x=load(fname)
    pos=(20,20)
    cam=''
    for i in range(0,40*15*15):
        a=0
        b=0
        c=0
        d=0 
        if pos[1]==580 or x[pos[0]][pos[1]+40]==(255,0,0) or x[pos[0]][pos[1]+40]==(0,255,0)  :
            a=1
        if pos[1]==20 or x[pos[0]][pos[1]-40]==(255,0,0) or x[pos[0]][pos[1]-40]==(0,255,0)  :
             b=1
        if pos[0]==580 or x[pos[0]+40][pos[1]]==(255,0,0) or x[pos[0]+40][pos[1]]==(0,255,0) :
            c=1
        if pos[0]==20 or x[pos[0]-40][pos[1]]==(255,0,0) or x[pos[0]-40][pos[1]]==(0,255,0) : 
            d=1
        e = (a,b,c,d)
        if e == (1,1,1,1):
            x= colorag(pos[0],pos[1],x)
            break
        x,pos,cam=destra(pos[0],pos[1],x,cam)
        x,pos,cam=basso(pos[0],pos[1],x,cam)
        x,pos,cam=sinistra(pos[0],pos[1],x,cam)
        x,pos,cam=alto(pos[0],pos[1],x,cam)
        
    save(x,fname1)
    return cam
    '''Implementare qui la funzione'''
