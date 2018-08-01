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


from copy import copy
def cambia_dir(d):
    if d==[40,0]:
        d1=[0,40]
    elif d==[0,40]:
        d1=[-40,0]
    elif d==[-40,0]:
        d1=[0,-40]
    elif d==[0,-40]:
        d1=[40,0]
    return d1
    
def seq(d):
    s=''
    if d==[40,0]:
        s+='0'
    elif d==[0,40]:
        s+='1'
    elif d==[-40,0]:
        s+='2'
    elif d==[0,-40]:
        s+='3'
    return s

def interno(img, x, y):
    return 0 <= y < len(img) and 0 <= x < len(img[0])

def boole(scac,pos,direz,passato):
    if interno(scac,pos[0]+direz[0],pos[1]+direz[1]) and scac[pos[1]+direz[1]][pos[0]+direz[0]]!=(255,0,0) and [pos[0]+direz[0],pos[1]+direz[1]] not in passato:
        return True
    else:
        return False

def disegna(img, x, y, w, h, c):
    img1=copy(img)
    for px in range(x, x+w):
        for py in range(y, y+h):
            if interno(img1,px,py):
                img1[py][px] = c
    return img1


def cammino(fname,  fname1):
    scac=load(fname)
    sequenza=''
    pos=[20,20]
    direz=[40,0]
    passato=[[20,20]]
    
    cont=0
    
    scac=disegna(scac,0,0,40,40,(0,255,0))
    
    while True:
        
        
        if cont==4:
            scac=disegna(scac,pos[0]-20,pos[1]-20,40,40,(0,0,255))
            break
        
        if boole(scac,pos,direz,passato):
            pos[0]=pos[0]+direz[0]
            pos[1]=pos[1]+direz[1]
            if [pos[0],pos[1]] not in passato:
                passato.append([pos[0],pos[1]])
            scac=disegna(scac,pos[0]-20,pos[1]-20,40,40,(0,255,0))
            cont=0
            sequenza+=seq(direz)
        else:
            
            direz=cambia_dir(direz)
            cont+=1
        
    
    
    save(scac,fname1)
    return sequenza
                
                
                
                
        
    
