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

def pixinim(x,y,hi,wi):
    return 0 <= y <hi and 0<= x < wi

def colorize(x,y,img,c):
    for yy in range(y,y+40):
        for xx in range(x,x+40):
            img[yy][xx]=c
            
def orient(x,y,move):
    moves={0:[40,0],1:[0,40],2:[-40,0],3:[0,-40]}
    return x+moves[move][0],y+moves[move][1]

def gira(d):
    if d<3:
        return d+1
    else:
        return 0

def cammino(fname,  fname1):
    imm=load(fname)
    turncount=0
    direction=0
    x=0
    y=0
    nxtx=0
    nxty=0
    hi=len(imm)
    wi=len(imm[0])
    red=(255,0,0)
    green=(0,255,0)
    blue=(0,0,255)
    stringamovimenti=""
    
    while turncount<4:        
        nxtx,nxty = orient(x,y,direction)
        if pixinim(nxtx,nxty,hi,wi):
            if imm[nxty][nxtx]==red or imm[nxty][nxtx]==green:
                direction=gira(direction)
                turncount+=1
            else:
                colorize(x,y,imm,green)
                stringamovimenti=stringamovimenti+str(direction)
                x=nxtx
                y=nxty
                turncount=0
        else:
            direction=gira(direction)
            turncount+=1
    else:
        colorize(x,y,imm,blue)
    save(imm,fname1)            
    return stringamovimenti            























    
