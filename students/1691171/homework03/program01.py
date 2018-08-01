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

from immagini import load,save


def convert_to_matrix(image, c):
    mat = []
    for row in image:
        riga = []
        for v in row:
            if v == c:
                riga.append(True)
            else:
                riga.append(False)
        mat.append(riga)
    return mat


def stesso_colore(matrix, riga, colonna, size):
    i = riga
    while i < riga + size:
        j = colonna
        while j < colonna + size:
            if not matrix[i][j]:
                return False
            j += 1
        i += 1
    return True

def grande(matrix, x, y, minsize):
    w, h = len(matrix), len(matrix[0])
    width = x
    heigth = y
    while width < w and matrix[width][y]: width += 1
    while heigth < h and matrix[x][heigth]: heigth += 1
    width -= x
    heigth -= y
    size = 0
    if width > heigth:
        size = heigth
    else:
        size = width
    co = 0
    sb = size
    if not stesso_colore(matrix, x, y, sb):
        while sb - co != 1:
            size = (co + sb)//2
            if stesso_colore(matrix, x, y, size):
                co = size
            else:
                sb = size
    return sb


def maggiore(a, b):
    if a == None:
        return b
    if b[0] > a[0] or (b[0] == a[0] and b[1] < a[1]) or (b[0] == a[0] and b[1] == a[1] and b[2] < a[2]):
        return b
    return a


def quadrato(filename,c):
    image = load(filename)
    mat = convert_to_matrix(image, c)
    width = len(mat[0])
    heigth = len(image)
    i = 0
    found = [0, 0, 0]
    while i < heigth:
        j = 0
        while j < width:
            if mat[i][j]:
                s = grande(mat, i, j, found[0])
                found = maggiore(found, [s, i, j])
            j += 1
        i += 1
    return (found[0], (found[2], found[1]))

