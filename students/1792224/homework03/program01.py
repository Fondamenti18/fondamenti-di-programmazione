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
    img, colonne, righe = creaquadra(filename, c)
    tris = (0, (0, 0))
    l = ni = 0
    while l == 0:
        ni += 1
        ttmp = qrig(img, tris[1][1], tris[1][0], ni, colonne, righe)
        if ttmp[0] == 0:
            l = 1
        else:
            tris = ttmp
    return tris

def qrig(imr, rpart, cpart, lqua, lcol, lrig):
    rigc = ""
    lquaq = "1" * lqua * lqua
    for i1 in range(rpart, lrig):
        for i2 in range(cpart, lcol):
            cpart = 0
            rigc = ""
            for i3 in range(lqua):
                if i1 + lqua > lrig:
                    lqua = 0
                    break
                else:
                    rigc += imr[i1+i3][i2:i2+lqua]
            if rigc == lquaq:
                rpart = i1
                cpart = i2
                break
        if rigc == lquaq:
            break
    return (lqua, (cpart, rpart))

def creaquadra(filename, c):
    with open(filename, mode='rb') as f:
        reader = png.Reader(file=f)
        colonne, righe, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l01 = ""
            for i in range(0, len(line), 3):
                if (line[i], line[i+1], line[i+2]) == c:
                    l01 += "1"
                else:
                    l01 += "0"
            img += [l01]
    return img, colonne, righe
