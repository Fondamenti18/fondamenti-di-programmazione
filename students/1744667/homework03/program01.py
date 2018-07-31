# -*- coding: cp1252 -*-
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
    im = load(filename)
    a = im
    nriga, ncol = len(a), (len(a[0]) if a else 0)
    if not (nriga and ncol): return 0 
    cont = [[0]*ncol for _ in range(nriga)]
    for i in reversed(range(nriga)):     
        assert len(a[i]) == ncol 
        for j in reversed(range(ncol)): 
            if a[i][j] == c:
                cont[i][j] = (1 + min(
                    cont[i][j+1],  
                    cont[i+1][j],  
                    cont[i+1][j+1] 
                    )) if i < (nriga - 1) and j < (ncol - 1) else 1 
    r = max(c for riga in cont for c in riga)
    z = next(((k, cont.index(r))
            for k, cont in enumerate(cont)
            if r in cont),
            None)
    cp = z[::-1]
    return r,cp
    


    
    
    
    
    
    
    
    