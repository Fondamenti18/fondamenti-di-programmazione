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

import math

from immagini import *
def quadrato (filename, c):
    global col,img, w,h,diz_pos_l
    col=c
    diz_pos_l=dict()
    img=load(filename)
    w=len(img[0])
    h=len(img)
    global lista_pos
    lista_pos=trova_pixel_colore(img, c)  
    a=itera_quadrati(img, max(diz_pos_l.values()))
    return a

def trova_pixel_colore (immagine, c):
    posizioni=list()
    for y in range(len(immagine)):
        for x in range(len(immagine[0])):
            if (immagine[y][x]==c):
                posizioni.append((x,y))
                diz_pos_l[(x,y)]=max_l(x,y)
    return posizioni 

def max_l(x,y):
    cont=1
    while(inside(x+cont,y+cont)):
        if(img[y+cont][x+cont]==col and img[y+cont][x]==col and img[y][x+cont]==col):
            cont+=1
        else:   break
    return cont
def inside(x,y):
    return 0<=x<w and 0<=y<h

def itera_quadrati(img, l_max):
    l=l_max
    verifiche=0
    for i in range(l, 0, -1):
        for j in lista_pos:
            if(diz_pos_l[j]>=i):
                if inside(j[0]+i-1,j[1]+i-1):
                    verifiche+=1
                    if verifica_quadrato(j,i,img):
                        return (i,j)
                
def verifica_quadrato(coord, l, img):
    #print(l, coord)
    a=coord[0]+l
    b=coord[1]+l
    if a>len(img[0]) or b>len(img):
        return False
    i=coord[1]
    while (i<b):
        j=coord[0]
        while (j<a):
            if(img[i][j]!=col):
                return False
            else:
                j=j+1
        i=i+1
    return True
def verifica_diagonale(x,y,l,img):
    i=y
    j=x
    while i<y+l:
        while j<x+l:
            #print(i,j)
            if(img[i][j]!=col):
                return False
            i+=1
            j+=1
        diz_pos_l[(i,j)]=max((j-x),(i-y))
    return True
def verifica_colonna(x,y,l,img):
    j=x
    i=y
    while i<y+l:
        if(img[i][j]!=col):
            return False
        i+=1
    return True
def verifica_riga(x,y,l,img):
    i=y
    j=x
    while j<x+l:
        if(img[i][j]!=col):
            return False
        j+=1
    return True