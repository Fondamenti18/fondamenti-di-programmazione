'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contine un immagine in formato png della  tipologia appena descritta.
- una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0 e 255 compresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e colore C interamente visibile nell'immagine. 
- le cordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
all'interno dell'immagine del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''
'''
from immagini import *

def quadrato(filename,c):
    img=load(filename)
    ris=set()
    altezza=len(img)
    lunghezza=len(img[0])
    lmx=0
    cmx=(0,0)
    for i in range(lunghezza): 
        for j in range(altezza):
            if[i]==c and ((i,j) not in ris):
                lato,cordinate=quad(img,i,j,c,lunghezza,altezza,ris)
                lmx,cmx=diag(lato,cordinate,lmx,cmx)
    return lmx,cmx



def canc(x,y,ym,xm,ris):
    for i in range(x,xm+1):
        for l in range(y,ym+1):
            ris.add((i,l))			

def cercaO(img,x,y,c,n,ris):
    if img[y+n][x+n] != c:		
        canc(x,y,y+n,x+n,ris)
    return True


def blocco(img,x,y,c,n,ris):
    for i in range(n-1,-1,-1):
        if img[y+n][x+i] != c:
            canc(x,y,y+n,x+i,ris)
            return True
        if img[y+i][x+n] !=c:
               canc(x,y,y+i,x+n,ris)
               return True
    return False


    


def quad(img,x,y,c,lunghezza,altezza,ris):
    n = 1
    while ((0<= x+n and x+n<lunghezza) & (0<= y+n and y+n <altezza)) and not blocco(img,x,y,c,n,ris) and not cercaO(img,x,y,c,n,ris):
        n+=1
    return n,(x,y)



def diag(lato,cordinate,lmx,cmx):
    if lato>lmx:
        return lato,cordinate
    else:
        return lmx,cmx
 '''   
from immagini import *

def quadrato(filename,c):
    img = load(filename)
    altezza = len(img)
    lunghezza = len(img[0])
    M = 0
    mxc = (0,0)
    quad=[]
    ris = set()
    for x in range(lunghezza):
        for y in range(altezza):
            if (img[y][x] == c) and ((x,y) not in ris):
                lato, cordinate = creaq(img,x,y,c,lunghezza,altezza,ris)
                quad=slista(x,y,lunghezza,altezza)
                M,mxc = diag(lato,cordinate,M,mxc,quad)
    return M, mxc

def diag(lato,cordinate,M,mxc,quad):
    if lato > M:
        return lato,cordinate
    else:
        return M,mxc

def slista(x,y,lunghezza,altezza):
    x=[]
    for i in range(lunghezza) :
        
            x.append((i))
    return x

def blocco(img,x,y,c,n,ris):
    for i in range(n-1,-1,-1):
        if img[y+n][x+i] != c:
            canc(x,y,y+n,x+i,ris)
            return True
        if img[y+i][x+n] !=c:
            canc(x,y,y+i,x+n,ris)
            return True
    return False

def canc(x,y,yd,xd,ris):
    for i in range(x,xd+1):
        for j in range(y,yd+1):
            ris.add((i,j))			
    return

def creaq(img,x,y,c,lunghezza,altezza,ris):
    n=1
    while ((0<= x+n and x+n <lunghezza) & (0<= y+n and y+n <altezza)) and not trovablocco(img,x,y,c,n,ris) and not blocco(img,x,y,c,n,ris):
        n += 1
    return n,(x,y)

def trovablocco(img,x,y,c,n,ris):
    if img[y+n][x+n] != c:		
        canc(x,y,y+n,x+n,ris)
        return True



