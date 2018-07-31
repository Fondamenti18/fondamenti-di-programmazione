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

def is_square(image, x, y, min_lenght):
    c = image[x][y]
    height = len(image)
    lenght = len(image[0])
    side_lenght_x = 0
    side_lenght_y = 0
    x_temp = x
    y_temp = y

    while image[x_temp][y] == c:
        if x_temp+1 < height:
            x_temp += 1
            side_lenght_x += 1
        else:
            break
    while image[x][y_temp] == c:
        if y_temp+1 < lenght:
            y_temp += 1
            side_lenght_y += 1
        else:
            break

    if side_lenght_x == 1 and side_lenght_y == 1:
        return 1

    if side_lenght_x < min_lenght or side_lenght_y < min_lenght:
        return False

    if side_lenght_y < side_lenght_x:
        for i in range(side_lenght_y):
            for j in range(side_lenght_y):
                if x+i < height or j+y < lenght:
                    if image[x+i][y+j] == c:
                        continue
                    else:
                        return False
                else:
                    return False
        return side_lenght_y
    else:
        for i in range(side_lenght_x):
            for j in range(side_lenght_x):
                if x+j < height or j+i < lenght:
                    if image[x+j][y+i] == c:
                        continue
                    else:
                        return False
                else:
                    return False
        return side_lenght_x

def quadrato(filename,c):
    img = load(filename)
    height = len(img)
    lenght = len(img[0])

    square_vertices = list()
    square_sides_lenght = list()

    for x in range(height):
        for y in range(lenght):
            if img[x][y] == c:
                if len(square_sides_lenght) < 1:
                    min_lenght = 0
                else:
                    min_lenght = max(square_sides_lenght)
                side_lenght = is_square(img, x, y, min_lenght)
                if side_lenght:
                    square_vertices.append((x, y))
                    square_sides_lenght.append(side_lenght)

    return max(square_sides_lenght), square_vertices[square_sides_lenght.index(max(square_sides_lenght))][::-1]
