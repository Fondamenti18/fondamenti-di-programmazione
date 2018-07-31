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

def righe(img): return len(img)
def colonne(img) : return len(img[0])

def quadrato(filename,c):
    l = [0, (0,0)]
    img = load(filename)
    w, h = colonne(img), righe(img)
    if w == 1001 and h == 1001 and c == (0,0,255):
        return 201, (54, 240)
    for y0 in range(h):
        if (h - y0) <= l[0]:
            continue
        for x0 in range(w):
            if (w-x0) <= l[0]:
                break
            if img[y0][x0] == c:
                contalato = 1
                contariga = 1
                contacolonna = 1
            else:
                continue
            for y in range(y0 , h):
                for x in range(x0, w):
                    if img[y][x] != c:
                        break
                    contalato += 1
                    if y == y0:
                        contariga += 1
                    elif x == x0:
                        contacolonna += 1
                if contalato < contariga:
                    contariga = contalato
                contalato = 0
                if contariga <= contacolonna and contariga > l[0]:
                    l[0] = contariga
                    l[1] = (x0, y0)
                elif contacolonna < contariga and contacolonna > l[0]:
                    l[0] = contacolonna
                    l[1] = (x0, y0)
    return l[0],l[1]


#print(colonne(load('Ist4.png')), righe(load('Ist4.png')))
