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

from immagini import *
def inside(img,x,y):
    return 0<=x<len(img[0]) and 0<=y<len(img)

def verificaquadrato(img,x,y,l,c): 
    for i in range(y,y+l-1):
        for j in range(x,x+l-1):    
            if(inside(img,j,i) and img[i][j]!=c):
                return False
    return True        
            
def calcolabase(img,c,i,j):
    base=0
    while(inside(img,j,i)and img[i][j]==c):
        base+=1
        j+=1
    return base

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    img=load(filename)
    massimo=0
    minimo=()
    for riga in range(len(img)):
        for colonna in range(len(img[0])):
            if (inside(img,colonna,riga) and img[riga][colonna]==c ):
                vertice=(colonna,riga)
                base=calcolabase(img,c,riga,colonna)
                if(verificaquadrato(img,colonna,riga,base,c)): 
                    if (base>massimo):
                        massimo=base 
                        minimo=vertice
    return massimo,minimo
                    
                
                
            
    
