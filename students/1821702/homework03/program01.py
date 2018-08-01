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

def trovacolore(file,controllo):
    colore = []
    for y in range(0,len(file)):
        for x in range(0,len(file[y])):
            if file[y][x] == controllo:
                colore.append([x,y])
    return colore

def trovabase(lcolori,pos):
    b = 0
    i = lcolori.index(pos)
    while i<len(lcolori):
        if pos == lcolori[i]:
            pos = [pos[0]+1,pos[1]]
            b +=1
            i += 1
        else:
            break
    return b

def trovaaltezza(lcolori,b,pos):
    h = b
    i = 0
    posizione = [pos[0],pos[1]+i]
    while i < h and posizione in lcolori:
        y = trovabase(lcolori,posizione)
        if y < h:
            h = y
        i += 1
        posizione = [pos[0],pos[1]+i]
    h = i
    return h

def costruisciquadrato(pos,lcolori,quadrato):
    b = 0
    h = 0
    b = trovabase(lcolori,pos)
    if b < quadrato[0]:
        return quadrato
    h = trovaaltezza(lcolori,b,pos)
    if b > h:
        b = h
    if b < quadrato[0]:
        return quadrato
    q = (b,(pos[0],pos[1]))
    quadrato = maxquadrato(q,quadrato)
    return quadrato
                            
def maxquadrato(quadrati,massimo):
    lato = massimo[0]
    xmin = quadrati[1][0]
    ymin = quadrati[1][1]
    if quadrati[0] > lato:
        massimo = quadrati
    elif quadrati[0] == lato:
        if quadrati[1][1] < ymin:
            massimo = quadrati
        elif quadrati[1][1] == ymin:
            if quadrati[1][0] < xmin:
                massimo = quadrati
    return massimo

def quadrato(filename,c):
    f = load(filename)
    lcol = trovacolore(f,c)
    quadrato = (0,(0,0))
    for i in lcol:
        quadrato = costruisciquadrato(i,lcol,quadrato)
    return quadrato



