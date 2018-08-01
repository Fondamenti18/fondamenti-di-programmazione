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

def isValidLast(img, c, start, end):
    #Contiene solo il giusto colore

    if (len(img) - 1) < end[0]:
        return False
    
    if (len(img[start[0]]) - 1) < end[1]+1:
        return False

    if len(set(img[end[0]][start[1]:end[1]])) is not 1:
        return False

    valid = True

    for line in img[start[0]:end[0]]:
        if line[end[1]] != c:
            valid = False
            break

    return valid
        
def quadrato(filename,c):
    squares = []
    side = 0
    img = load(filename)

    for (y, line) in enumerate(img):
        for (x, pixel) in enumerate(line):
            if pixel != c:
                continue
    
            end = (y, x)
            while (isValidLast(img, c, [y, x], [end[0]+1, end[1]+1])):
                end = (end[0]+1, end[1]+1)


            if side > (end[0]-y+1):
                continue
            if (end[0]-y+1) > side:
                squares = []
            
            #Salva il valore del lato
            side = (end[0]-y+1)
            squares.append([x, y])

    squares.sort()
    return (side, (squares[0][0], squares[0][1]))
