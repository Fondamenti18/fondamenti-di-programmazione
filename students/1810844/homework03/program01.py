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

def controllo_pixel(pixel,colore):
    vero = False
    if pixel == colore:
        vero = True
    return vero

def controllo_quadrato(img,colore,lun,R,C,l):
    vero = False
    r = R
    c = C
    nuovac = c
    if lun <= l - r:
        while c > C - lun:
            if img[r][c] == colore:
                if r < R + (lun -1):
                    r += 1
                else:
                    c -= 1
            else:
                nuovac = c
                c = C -(lun+1)
    if c == C - lun:
        vero = True
    return vero,nuovac

def quadrato(filename,C):
    '''Implementare qui la funzione'''
    img = load(filename)
    lun = 0
    r = 0
    c = 0
    lun_max = 0
    rig = -1
    col = -1
    primo = True
    l = len(img)
    L = len(img[0])
    while r < l:
        c = 0
        while c < L:
            app = controllo_pixel(img[r][c],C)
            if lun_max >= l - r:
                r = l
                c = L
                app = False
            if app == True:
                lun += 1
                if primo == True:
                    lun_max = lun
                    rig = r
                    col = c
                    primo = False
                    
                if lun > 1:
                    a,b = controllo_quadrato(img,C,lun,r,c,l)
                    if a == True:
                        if lun_max < lun:
                            lun_max = lun
                            rig = r
                            col = c - (lun - 1)
                    else:
                        lun = 0
                        c = b
            else:
                lun = 0
            c += 1
        r += 1
    return lun_max,(col,rig)
    
