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

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    imag=load(filename)
    x,y,maxlenght=0,0,0
    rowmat,globmat=[],[]
    
    for i in imag:
        y+=1
        
        for j in i:
            x+=1
            rowmat=conditio(x,y,j,c,rowmat,globmat)
        
        globmat.append(rowmat)
        rowmat=[]    
        x=0
    
    maxlenght=[max(i) for i in globmat]
    y=maxlenght.index(max(maxlenght))
    maxlenght=max(maxlenght)
    x=globmat[y].index(maxlenght)
    
    return maxlenght,(x+1-maxlenght,y+1-maxlenght)

def conditio(x,y,j,c,rowmat,globmat):
    
    if y==1 or x==1: 
        if j==c: rowmat.append(1)
        else:rowmat.append(0)
    
    else:
        if j==c: rowmat.append(min(rowmat[x-2],globmat[y-2][x-1],globmat[y-2][x-2])+1)
        else: rowmat.append(0)
    
    return rowmat
    
    
    
   