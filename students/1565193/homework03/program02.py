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
    
    move=""
    ridmat,extmat=[],[]
    imag=load(fname)    
    ridmat=reduct(imag,ridmat)
    ridmat,move=movement(ridmat,move)
    extmat=extend(ridmat)
    save(extmat,fname1)
    
    return move


def movement(ridmat,move):
    
    was,wasdir=[],[]
    ost,ok,stop=(255,0,0),(0,255,0),(0,0,255)
    direz=0
    x,y=1,1
    ridmat[y-1][x-1]=ok
    was.append((x,y))
    k=len(ridmat)*len(ridmat[0])*4
    
    for i in range(k):

        if len(wasdir)==4:
            ridmat[y-1][x-1]=stop
            break
        
        if direz==0:            
            try:               
                if ridmat[y-1][x]!=ost and (x+1,y) not in was and x+1 <= 15 and direz not in wasdir:
                    x+=1
                    ridmat[y-1][x-1]=ok
                    was.append((x,y))
                    move+="0"
                    wasdir=[]
                else:
                    wasdir.append(0)
                    direz=1
                    continue
            
            except IndexError: 
                wasdir.append(0)
                direz=1
                continue
            
        if direz==1:
            try:
                if ridmat[y][x-1]!=ost and (x,y+1) not in was and y+1<= 15 and direz not in wasdir:
                    y+=1
                    ridmat[y-1][x-1]=ok
                    was.append((x,y))
                    move+="1"
                    wasdir=[]
                else:
                    wasdir.append(1)
                    direz=2
                    continue
                
            except IndexError:
                wasdir.append(1)
                direz=2
                continue

        if direz==2:            
            try:
                if ridmat[y-1][x-2]!=ost and (x-1,y) not in was and x-1 >=1 and direz not in wasdir:
                    x-=1
                    ridmat[y-1][x-1]=ok
                    was.append((x,y))
                    move+="2"
                    wasdir=[]
                else:
                    wasdir.append(2)
                    direz=3
                    continue
                
            except IndexError: 
                wasdir.append(2)
                direz=3
                continue

        if direz==3:            
            try:
                if ridmat[y-2][x-1]!=ost and (x,y-1) not in was and y-1 >=1 and direz not in wasdir:
                    y-=1
                    ridmat[y-1][x-1]=ok
                    was.append((x,y))
                    move+="3"
                    wasdir=[]
                else:
                    wasdir.append(3)
                    direz=0
                    continue
                
            except IndexError: 
                wasdir.append(3)
                direz=0
                continue

    return ridmat,move


def reduct(imag,ridmat):
    
    x,y=0,0
    rid=[]
    
    for i in imag:
        y+=1
        
        if y%40!=0: continue
        
        for j in i:
            x+=1
            
            if x%40==0: rid.append(j)
        
        ridmat.append(rid)
        rid=[]
        
    return ridmat


def extend(ridmat):
    
    ext,extmat=[],[]
    x=0
    
    for i in ridmat:
        s=0

        for j in i:
            x+=1
            j=[j]*40
            ext.extend(j)

        while s<40:
            s+=1
            extmat.append(ext)
        
        ext=[]
    
    return extmat

#def right(x,y,move,ridmat,ost,was,ok):
    
