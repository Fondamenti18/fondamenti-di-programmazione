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

def get_square(img,y,x,c):
    counter = 0
    start_x = x
    start_y = y
    try:
        while(img[y][x] == c):
            counter+=1
            y+=1
            x+=1
    except:
        pass
    return counter,(start_x,start_y)

def is_max(max_square,square):
    if(max_square == None): return True
    if(square[0] > max_square[0]): return True
    if(square[0] == max_square[0]):
        if(square[1] < max_square[1]): return True
    return False


def quadrato(filename,c):
    img = load(filename)
    max_y = len(img)
    max_x = len(img[0])
    x = 0
    y = 0
    max_square = None
    try:
        while(y < max_y):
            while(x < max_x):
                pixel = img[y][x]
                if(pixel == c):
                    square = get_square(img,y,x,c)
                    if(square == None): continue
                    if(is_max(max_square,square)):
                        max_square = square
                x+=1
            y+=1
            x=0
    except:
        pass
    return max_square
