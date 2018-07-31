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
import time


''' FUNZIONE CHE COMPATTA L'IMMAGINE DA 600X600 A 15X15'''
def compatta(img):
    img2 = [ [ None for c in range(15) ] for r in range(15) ]
    for i in range(0,15):
        for j in range(0,15):
            img2[i][j]=img[i*40][j*40]
    return img2

''' RIALLARGA L'IMMAGINE A 600X600 '''
def allarga(img):
    img2 = [ [ None for c in range(600) ] for r in range(600) ]
    for i in range(0,600):
        for j in range(0,600):
            img2[i][j]=img[i//40][j//40]
    return img2

'''FUNZIONE 'PASSO' '''
def step(img,x,y,d):
    s=0
    
    
    '''
    i successivi if iniziano con 'd' indica la direzione
    
    '0' per un passo verso destra (x crescenti)
    '1' per un passo verso il basso (y crescenti)
    '2' per un passo verso sinistra (x decrescenti)
    '3' per un passo verso l'alto (y decrescenti)
    
    le funzioni sono tutte pressoche uguali
    '''
    
    
    if d==0:
        if y+1>14:
            '''se esce fuori dalla scacchiera'''
        else:
            if img[x][y+1]!=(255,0,0) and img[x][y+1]!=(0,255,0):
                '''se non trova ne verde ne rosso'''
                img[x][y+1]=(0,255,0) 
                '''imposta la cella successiva a verde'''
                x,y=x,y+1 
                '''cambia le coordinate'''
                    
                    
                    
    elif d==1:
        if x+1>14:
            '''se esce fuori dalla scacchiera'''
        else:
            if img[x+1][y]!=(255,0,0) and img[x+1][y]!=(0,255,0):
                img[x+1][y]=(0,255,0)
                x,y=x+1,y
                    
                    
    elif d==2:
        if y-1<0:
            '''se esce fuori dalla scacchiera'''
        else:
            if img[x][y-1]!=(255,0,0) and img[x][y-1]!=(0,255,0):
                img[x][y-1]=(0,255,0)
                x,y=x,y-1
    
    
    elif d==3:
        if x-1<0:
            '''se esce fuori dalla scacchiera'''
        else:
            if img[x-1][y]!=(255,0,0) and img[x-1][y]!=(0,255,0):
                img[x-1][y]=(0,255,0)
                x,y=x-1,y
                
    return img,x,y

def cammino(fname,  fname1):
    img=load(fname) 
    ''' carica immagine '''
    imgc=compatta(img) 
    ''' compatta l'immagine '''
    string=''
    stop=0 
    '''flag di stop'''
    t=0 
    '''tentativi'''
    
    x,y,d=0,0,0
    imgc[x][y]=(0,255,0)
    
    
    while stop==0:
        imgc,xx,yy=step(imgc,x,y,d) 
        '''fa un passo'''
        if x==xx and y==yy:
            ''' se le coordinate cambiano '''
            t=t+1 
            ''' incrementa i tentativi effettuati '''
            
            ''' incrementa la direzione '''
            d=d+1
            if d==4:
                d=0
        else:
            t=0
            x=xx
            y=yy
            string=string+str(d) 
            '''stringa da dare in output, accoda la direzione'''
            
        if t==4:    
            ''' ultima casella '''
            imgc[x][y]=(0,0,255)
            stop=1 
            ''' attiva il flag di stop '''
    
    img=allarga(imgc) 
    ''' riallarga l'immagine '''
    save(img,fname1) 
    '''salva '''
    return string
