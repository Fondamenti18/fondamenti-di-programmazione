'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  riempite di rosso).

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
legge l'immagine della scacchiera in fname, riempi di verde le celle della scacchiera percorse dal robottino prima di fermarsi, 
riempi di blu la cella in cui il robottino si ferma e registra l'immagine ririempita nel file fname1. 
Inoltre restituisce una string dove in sequanza sono codificati i passi effettuati dal robottino prima di fermarsi. 
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
    blu=(0,0,255)
    v=(0,255,0)
    n=(0,0,0)
    r=(255,0,0)
    x=0
    y=0
    controlli=0
    riempi(x,y,v,img)
    string=''
    for i in range(0,10000):
            if controlli==0:
                if presente(img,x+40,y) and img[y][x+40]!=r and img[y][x+40]!=v: 
                    x,controlli,appoggio=destro(img,x+40,y,r,v)
                    string+=appoggio
            elif controlli==1:
                if presente(img,x,y+40) and img[y+40][x]!=r and img[y+40][x]!=v:
                    y,controlli,appoggio=scendendo(img,x,y+40,r,v)
                    string+=appoggio
            elif controlli==2:
                if presente(img,x-40,y) and img[y][x-40]!=r and img[y][x-40]!=v:
                    x,controlli,appoggio=sinistro(img,x-40,y,r,v)
                    string+=appoggio
            elif controlli==3:
                if presente(img,x,y-40) and img[y-40][x]!=r and img[y-40][x]!=v:
                    y,controlli,appoggio=salendo(img,x,y-40,r,v)
                    string+=appoggio
            else:
                riempi(x,y,blu,img)
                break
    save(img,fname1)
    return string

    

    
def destro(img,x,y,r,v):
    vittoria=''
    while presente(img,x,y)==True and img[y][x]!= r and img[y][x]!= v:
        riempi(x,y,v,img)
        vittoria+="0"
        x+=40
    x-=40
    if presente(img,x,y+40)==True and img[y+40][x]!=r and img[y+40][x]!=v :
        controlli=1
    elif presente(img,x-40,y)==True and img[y][x-40]!=r and img[y][x-40]!=v :
        controlli=2
    elif presente(img,x,y-40)==True and img[y-40][x]!=r and img[y-40][x]!=v :
        controlli=3
    elif presente(img,x+40,y)==True and img[y][x+40]!=r and img[y][x+40]!=v :
        controlli=0
    else:
        controlli=4
    return x,controlli,vittoria



def riempi(x,y,c,img):
    for q in range(y,y+40):
        for i in range(x,x+40):
            img[q][i]=c
    

def scendendo(img,x,y,r,v):
    vittoria=''
    while presente(img,x,y)==True and img[y][x]!= r and img[y][x]!= v:
        riempi(x,y,v,img)
        vittoria+="1"
        y+=40
    y-=40
    if presente(img,x-40,y)==True and img[y][x-40]!=r and img[y][x-40]!=v :
        controlli=2
    elif presente(img,x,y-40)==True and img[y-40][x]!=r and img[y-40][x]!=v :
        controlli=3
    elif presente(img,x+40,y)==True and img[y][x+40]!=r and img[y][x+40]!=v :
        controlli=0
    elif presente(img,x,y+40)==True and img[y+40][x]!=r and img[y+40][x]!=v :
        controlli=1
    else:
        controlli=4
    return y,controlli,vittoria

def sinistro(img,x,y,r,v):
    vittoria=''
    while presente(img,x,y)==True and img[y][x]!= r and img[y][x]!= v:
        riempi(x,y,v,img)
        vittoria+="2"
        x-=40
    x+=40
    if presente(img,x,y-40)==True and img[y-40][x]!=r and img[y-40][x]!=v :
        controlli=3
    elif presente(img,x+40,y)==True and img[y][x+40]!=r and img[y][x+40]!=v :
        controlli=0
    elif presente(img,x,y+40)==True and img[y+40][x]!=r and img[y+40][x]!=v :
        controlli=1
    elif presente(img,x-40,y)==True and img[y][x-40]!=r and img[y][x-40]!=v :
        controlli=2
    else:
        controlli=4
    return x,controlli,vittoria


def presente (img,i,q):
    iw,ih=len(img[0]),len(img)
    return 0<=i<iw and 0<=q<ih

def salendo(img,x,y,r,v):
    vittoria=''
    while presente(img,x,y)==True and img[y][x]!= r and img[y][x]!= v:
        riempi(x,y,v,img)
        vittoria+="3"
        y-=40
    y+=40
    if presente(img,x+40,y)==True and img[y][x+40]!=r and img[y][x+40]!=v :
        controlli=0
    elif presente(img,x,y+40)==True and img[y+40][x]!=r and img[y+40][x]!=v :
        controlli=1
    elif presente(img,x-40,y)==True and img[y][x-40]!=r and img[y][x-40]!=v :
        controlli=2
    elif presente(img,x,y-40)==True and img[y-40][x]!=r and img[y-40][x]!=v :
        controlli=3
    else:
        controlli=4
    return y,controlli,vittoria


def riempi(x,y,c,img):
    for q in range(y,y+40):
        for i in range(x,x+40):
            img[q][i]=c
    



    
    
            
    
        
