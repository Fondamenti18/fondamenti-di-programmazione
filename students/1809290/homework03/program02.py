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

def cammino(fname,fname1):
    img=load(fname)
    w,h=len(img[0]),len(img)
    x,y=0,0
    percorso=''
    quadrato(img,x,y)
    blu=0
    while blu!=4:
        blu=0
        #print(y,x,blu)
        while y+40<w and (img[x][y+40]!=(255,0,0) and img[x][y+40]!=(0,255,0)):
            y+=40
            #print(img[x][y],x,y)
            quadrato(img,x,y)
            percorso+='0'
        #print(y,x)
        while x+40<w and (img[x+40][y]!=(255,0,0) and img[x+40][y]!=(0,255,0)):
            x+=40
            #print(img[x][y],x,y)
            quadrato(img,x,y)
            percorso+='1'
        #print(y,x)
        while y-40>=0 and (img[x][y-40]!=(255,0,0) and img[x][y-40]!=(0,255,0)):
            y-=40
            #print(img[x][y],x,y)
            quadrato(img,x,y)
            percorso+='2'
        #print(y,x)
        while x-40>=0 and (img[x-40][y]!=(255,0,0) and img[x-40][y]!=(0,255,0)):
            x-=40
            #print(img[x][y],x,y)
            quadrato(img,x,y)
            percorso+='3'
        #print(y,x,blu)
        #blu+=1
        '''controllo per uscire dal while'''
        #save(img,fname1)
        #save(img,fname1)
        if y+40>=w or img[x][y+40]==(255,0,0) or img[x][y+40]==(0,255,0):
            blu+=1
            #print(blu,'1')
        if y-40<=0 or img[x][y-40]==(255,0,0) or img[x][y-40]==(0,255,0):
            blu+=1
            #print(blu,'2')
        if x+40>=h or img[x+40][y]==(255,0,0) or img[x+40][y]==(0,255,0):
            blu+=1
            #print(blu,'3')
        if x-40<=0 or img[x-40][y]==(255,0,0) or img[x-40][y]==(0,255,0):
            blu+=1
            #print(blu,'4')
    quadratob(img,x,y)
    #print(percorso)
    save(img,fname1)
    return percorso


def quadrato(img,x,y,w=40,c=(0,255,0)):
    for px in range (x,x+w):
        for py in range (y,y+w):
            img[px][py]=c
def quadratob(img,x,y,w=40,c=(0,0,255)):
    for px in range (x,x+w):
        for py in range (y,y+w):
            img[px][py]=c
#Image(fname1)''' 