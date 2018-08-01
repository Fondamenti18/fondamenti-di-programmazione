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

verde=(0,255,0)
blu=(0,0,255)
rosso=(255,0,0)
nero=(0,0,0)
bianco=(255,255,255)

def cammino(fname, fname1):
    img=load(fname)
    h=len(img)
    w=len(img[0])
    passi=''
    lquad=40 #numero di pixel dello stesso colore
    x=0
    y=0
    #print(img[y][x],'start')
    colora_quad(x,y,img,verde)
    z=0
    n=0
    listapY=[y, y+lquad, y, y-lquad]
    listapX=[x+lquad, x, x-lquad, x]
    codifica=['0','1','2','3']
    provay=listapY[n%4]
    provax=listapX[n%4] 
    while z<4:
        if provay in range(h) and provax in range(w):
            if img[provay][provax]==bianco or img[provay][provax]==nero:
                y=provay
                x=provax
                passi+=codifica[n%4]
                listapY=[y, y+lquad, y, y-lquad]
                listapX=[x+lquad, x, x-lquad, x]
                provay=listapY[n%4]
                provax=listapX[n%4] 
                #print(img[y][x], 'if1', y,x, provay, provax)
                colora_quad(x,y,img,verde)
                z=0
            else:
                z=z+1
                n=n+1
                provay=listapY[n%4]
                provax=listapX[n%4]
            
        else:
            z=z+1
            n=n+1
            provay=listapY[n%4]
            provax=listapX[n%4]
    colora_quad(x,y,img,blu)
    save(img,fname1)
    return passi
    
    
        
    
        
            


def colora_quad(x,y,img,c): #dato un vertice in alto a sn, colora del colore c il quadrato che parte da quel punto finchè sulle x non trova un punto di colore diverso da quello del vertice. 
    img[y][x]=c
    f=1
    
    while f<40:
        for j in range (y,y+f):
            img[j][x+f]=c
        for i in range (x,x+f+1):
            img[y+f][i]=c
        f+=1
    #print(x,y,c, 'print', img[y][x])
    
    
    

















#che carino questo programma! ci ho picchiato di nuovo la testa, ma meno forte che su altri... quante cose ho sbagliato via via? tante. tipo:
    #

