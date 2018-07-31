# -*- coding: utf-8 -*-
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

import png 
import numpy

def load(filename):
    with open(filename,mode='rb') as f:
        r=png.Reader(file=f)
        iw,ih,png_img,_=r.asRGB8()
        img=[]
        for png_row in png_img:
            row=[]
            for i in range(0,len(png_row),3):
                row.append((png_row[i+0],
                            png_row[i+1],
                            png_row[i+2]))
            img.append(row)
    return img,iw,ih

def create(iw,ih):
    matrix=[]
    for _ in range(ih+1):
        row=[]
        for _ in range(iw+1):
            row.append(0)
        matrix.append(row)
    return matrix

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    img,iw,ih=load(filename)
    matrix=create(iw,ih)
    for i in range(ih):
        for j in range(iw):
            if img[i][j]!=c:
                matrix[i+1][j+1]=0
            if img[i][j]==c:
                a=matrix[i][j]
                b=matrix[i][j+1]
                d=matrix[i+1][j]
                e=min(a,b,d)
                matrix[i+1][j+1]=1+e
    MAX=numpy.amax(matrix)
    for i in range(ih+1):
        for j in range(iw+1):
            if matrix[i][j]==MAX:
                return MAX,(j-MAX,i-MAX)
            