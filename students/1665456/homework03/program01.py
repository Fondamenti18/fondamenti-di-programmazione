# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:12:00 2017

@author: samue
"""

'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo 
immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contine un immagine in formato png della  tipologia appena 
descritta.
- una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0 e 255 compresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e colore C interamente visibile 
nell'immagine. 
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
all'interno dell'immagine del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' 
immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''

from immagini import *
import png

def load(fname):
    """ Carica la immagine PNG dal file fname.
        Torna una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return img

def save(img, filename):
    """ Salva la immagine img  nel file filename in formato PNG8.
        Img e' una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)



def calcolaLato(immagine, x, y, c):
    trovato=True
    xx=x
    yy=y
    latoT=1
    
    while trovato and  xx < len(immagine)-1 and yy < len(immagine[xx])-1:
        xx=xx+1
        yy=yy+1
        i=xx
        j=yy
        while i>=x and trovato:
            if immagine [i][yy]!=c:
                trovato=False
            else:
                i=i-1
        while j>=y and trovato:
            if immagine [xx][j]!=c:
                trovato=False
            else:
                j=j-1
        if trovato==0:
            latoT=xx-x
    return latoT   
            
            
            
            
    

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    immagine=load(filename)
    
    lato=0
    
    poX=0
    poY=0
    
    for x in range(len(immagine)):
        for y in range(len(immagine[x])):
            
            
            latoT=0
            if immagine[x][y]==c:
                latoT=calcolaLato(immagine, x, y, c)
            if lato < latoT:
                lato=latoT
                poX=x
                poY=y
            
    return(lato, (poY, poX))
                
                
                
#quadrato('Ist0.png',(255,255,255))
#quadrato('Ist1.png',(255,0,0))
#quadrato('Ist2.png',(255,0,0))
#quadrato('Ist3.png',(255,0,0))
#quadrato('Ist4.png',(0,0,255))
