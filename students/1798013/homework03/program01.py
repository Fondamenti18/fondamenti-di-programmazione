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
import png
def trovala(img,c,x,y):
    esci = False
    x_inizios = len(img) + 1
    y_inizios = len(img[0]) + 1
    for xx in range(x,len(img)-1):
        for yy in range(y,len(img[0])-1):
            if img[xx][yy] == c:
                x_inizios,y_inizios = xx,yy
                esci = True
                break
        y = 0
        if esci:
            break
    return x_inizios,y_inizios

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    img = load(filename)
    larghezza = len(img[0])
    altezza = len(img)
    lato_buono = 0
    for x in range(altezza):
        for y in range(larghezza):
            xs,ys = trovala(img,c,x,y)
            if xs >= larghezza:
                break
            x = xs
            y = ys
            x_inizio = x
            y_inizio = y
            while True:
                y += 1
                x += 1
                if x >= len(img)-1 or y >= len(img[0])-1 or img[x][y] != c:
                    x -= 1
                    y -= 1
                    break
            x_fine,y_fine = x,y
            lato = (x_fine - x_inizio + 1)
            if lato > 1:
                while True:
                    buono = True
                    if x_fine > x_inizio:
                        for x in range(x_inizio,x_fine+1):
                            for y in range(y_inizio,y_fine+1):
                                if img[x][y] != c:
                                    buono = False
                                    break
                            if not buono:
                                break
                        if not buono:
                            x_fine -= 1
                            y_fine -= 1
                        else:
                            break
                    else:
                        break
            lato = (x_fine - x_inizio + 1)
            if lato > lato_buono:
                lato_buono = lato
                x_buono = x_inizio
                y_buono = y_inizio
            if y_inizio < larghezza-1:
                y = y_inizio + 1
                x = x_inizio
            elif x_inizio < altezza-1:
                y = 0
                x = x_inizio + 1
            else:
                break
    return lato_buono,(y_buono,x_buono)
