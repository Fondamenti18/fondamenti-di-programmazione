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
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
all'interno dell'immagine del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''

from immagini import save, load
from IPython.display import Image, display

def quadrato(filename,c):
    img=load(filename)
    h=len(img)
    b=len(img[0])
    print(h)
    x=0
    y=0
    l=0
    dev=0
    L=0
    pr=0
    pc=0
    while x<h and y<b:
        if img[x][y]==c and dev==0:
            R=x
            C=y
            l=l+1
            dev=1
            if l>L:
                pr=R
                pc=C
                L=l
            y=y+1
            if y==b:
                y=0
                dev=0
                l=0
                x=x+1
                
        elif img[x][y]!=c and dev==0:
            y=y+1
            if y==b:
                y=0
                x=x+1
                l=0
                
        elif img[x][y]==c and dev==1:
            l=l+1
            if l>L and l+R<h:
                z,w=check(C,R,l,img,c)
                if z==1:
                    pr=R
                    pc=C
                    L=l
                    y=y+1
                else:
                    y=w+1
                    dev=0
                    l=0
            elif l>L and l+R>=h:
                x=h
            else:
                y=y+1              
                if y==b:
                    y=0
                    dev=0
                    l=0
                    x=x+1
                
        elif img[x][y]!=c and dev==1:
            l=0
            dev=0
            y=y+1
            if y==b:
                y=0
                x=x+1
    
    return (L,(pc,pr))
            
                    
                
def check(C,R,l,img,c):    
    for px in range(R+1, R+l):
        for py in range(C, C+l):
            if img[px][py]!=c:
                return 0,py
    return 1,py           
                
        