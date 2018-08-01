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
    colonne = [[]]
    righe = []
    match = []
    for i in range(len(img[0])):
        if img[0][i] == c:
            colonne[0] += [1]
        else:
            colonne[0] += [0]
    for j in range(1, len(img)):
        r = []
        for i in range(len(img[0])):
            if img[j][i] == c:
                r += [colonne[j-1][i] +1]
            else:
                r += [0]
        colonne += [r]
    for j in range(len(img)):
        righe += [[]]
        if img[j][0] == c:
            righe[j] += [1]
        else:
            righe[j] += [0]
    for i in range(1, len(img[0])):
        for j in range(len(img)):
            if img[j][i] == c:
                righe[j] += [righe[j][i-1] +1]
            else:
                righe[j] += [0]
    for j in range(len(img)):
        r = []
        for i in range(len(img[0])):
            if colonne[j][i] < righe[j][i]:
                r += [colonne[j][i]]
            else:
                r += [righe[j][i]]
        match += [r]
    maxi = 0
    n = 0
    for j in range(len(img)):
        for i in range(len(img[0])):
            if match[j][i] > n:
                value = n+1
                while value in range(n+1, match[j][i]+1):
                    if verifica(j, i, colonne, righe, value):
                        maxi = value
                        coppia = (i-n, j-n)
                        n = maxi
                        value += 1
                    else:
                        value = match[j][i]+1
    return (maxi, coppia)

def verifica(j, i, colonne, righe, n):
    for x in range(i, i-n, -1):
        if colonne[j][x] < n:
            return False
    for y in range(j, j-n, -1):
        if righe[y][i] < n:
            return False
    return True
                
                
                
                
                