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

    img = load(filename)
    coordinate = (0, 0)
    lato = 0
    larghezza_attuale = 0
    altezza_attuale = 0
    quadrato = True

    for i in range(len(img)):
        for j in range(len(img[i])):
            if(img[i][j][0] == c[0] and img[i][j][1] == c[1] and img[i][j][2] == c[2]):
                for h in range(j, len(img)):
                    if(img[i][h][0] == c[0] and img[i][h][1] == c[1] and img[i][h][2] == c[2]):
                        larghezza_attuale += 1
                    else:
                        break
                for k in range(i, len(img[i])):
                    if(img[k][j][0] == c[0] and img[k][j][1] == c[1] and img[k][j][2] == c[2]):
                        altezza_attuale += 1
                    else:
                        break
                if(larghezza_attuale == altezza_attuale):
                    for i_1 in range(i, larghezza_attuale + 1):
                        for j_1 in range(j, larghezza_attuale + 1):
                            if(img[i_1][j_1][0] != c[0] and img[i_1][j_1][1] != c[1] and img[i_1][j_1][2] != c[2]):
                                quadrato = False
                    if(quadrato and larghezza_attuale > lato):
                        coordinate = (j, i)
                        lato = larghezza_attuale
                quadrato = True
                larghezza_attuale = 0
                altezza_attuale = 0


    return (lato, coordinate)

#print(quadrato("Ist1.png", (255,0,0)))
#print(quadrato("Ist0.png", (255,255,255)))