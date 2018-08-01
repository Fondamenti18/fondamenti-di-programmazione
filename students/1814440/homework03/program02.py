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

def height(imm):
    return len(imm)

def width(imm):
    return len(imm[0])

def inside(imm,y,x):
    return 0<=x<width(imm) and 0<=y<height(imm)

def controllo(imm,x,y,direzione):
    ''' ritorna la prossima casella di movimento'''
    try:
        if((imm[y][x+40]==(0,0,0) or imm[y][x+40]==(255,255,255)) and direzione=='0' and inside(imm,y,x+40)): return x+40,y,'0'
    except: pass
    try:
        if((imm[y+40][x]==(0,0,0) or imm[y+40][x]==(255,255,255)) and (direzione=='1' or direzione=='0') and inside(imm,y+40,x)): return x,y+40,'1'
    except: pass
    try:
        if((imm[y][x-40]==(0,0,0) or imm[y][x-40]==(255,255,255)) and (direzione=='1' or direzione=='0' or direzione=='2') and inside(imm,y,x-40)): return x-40,y,'2'
    except: pass
    try:
        if((imm[y-40][x]==(0,0,0) or imm[y-40][x]==(255,255,255)) and inside(imm,y-40,x)): return x,y-40,'3'
    except: pass
    try:
        if((imm[y][x+40]==(0,0,0) or imm[y][x+40]==(255,255,255)) and inside(imm,y,x+40)): return x+40,y,'0'
    except: pass
    try:
        if((imm[y+40][x]==(0,0,0) or imm[y+40][x]==(255,255,255)) and inside(imm,y+40,x)): return x,y+40,'1'
    except: pass
    try:
        if((imm[y][x-40]==(0,0,0) or imm[y][x-40]==(255,255,255)) and inside(imm,y,x-40)): return x-40,y,'2'
    except: pass
    return -1,-1,'0'

def colora(imm,y,x,colore):
    '''colora lo scacco'''
    for a in range(y,y+40):
        for b in range(x,x+40):
            imm[a][b]=colore
    return imm

def calcola(imm):
    direzione='0' # i valori sono quelli attesi nella stringa di ritorno
    ret='' #stringa di ritorno
    x=0 # x attuale
    y=0 # y attuale
    while(True):
        nx,ny,direzione=controllo(imm,x,y,direzione)
        if nx==-1: # se è -1 non mi posso muovere
            imm=colora(imm,y,x,(0,0,255)) # coloro lo scacco di blu
            return imm,ret
        imm=colora(imm,y,x,(0,255,0)) # coloro lo scacco di verde
        ret+=direzione
        x=nx
        y=ny
        
def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    imm=load(fname).copy() # carico l'immagine in memoria
    imm,ret=calcola(imm)
    save(imm,fname1)
    return ret
