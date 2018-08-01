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

def pieno(img,x,y,lato,c): #funzione che ritorna il lato effetivo del quadrato che ha tutte le righe piene dello stesso colore
    l=lato
    i=0
    j=0
    while i<l:
        while j<l:
            if img[y+i][x+j]!=c:
                l=max(j,i)     #il lato e' il maggiore tra le x e y
            j+=1
        i+=1
        j=0
    return l

def diag(img,x,y,c): #funzione che scorre la diagonale fino a trovare l'angolo in basso a destra
    py=y
    px=x
    if inside(img,px+1,py+1):
        d=img[py+1][px+1]
        while d==c:
            py+=1
            px+=1
            if inside(img,px+1,py+1):
                d=img[py+1][px+1]
            else:break
    lato=px-x+1
    return lato

def inside(img,x,y): #funzione che indica se un pixel e' nell immagine
    return 0<=y<len(img) and 0<=x<len(img[0])

def quadrato(filename,c):
    img=load(filename)
    y=0
    x=0
    px=len(img[0])
    py=len(img)
    ris=0
    while y<len(img):
        while x<len(img[0]): #doppio while che scorre i pixel
            if y>len(img)-ris: #se le y mancanti sono minori del lato termina
                x=len(img[0])
                y=len(img)
            else:
                if x > len(img[0]) - ris and y + 1 < len(img): #se le x mancanti sono minori del lato salta la riga
                    y += 1
                    x = 0
                else:
                    if img[y][x] == c: #se il colore del pixel e' uguale a c
                        d = diag(img, x, y, c)
                        if d > ris: #se la diagonale e' maggiore del lato continua altrimenti salta
                            lato = pieno(img, x, y, d, c)
                            if lato > ris: #se il lato e' maggiore di quello trovato fin ora
                                ris = lato
                                px = x
                                py = y
                                if (len(img[0]) - (x + ris)) < ris: #se le x mancanti sono minori del lato
                                    y += round(d/2)
                                    x = 0
                                else:
                                    x = x + d
                            elif lato == ris: #nel caso siano uguali
                                if y < py:
                                    py = y
                                    px = x
                                    if (len(img[0]) - (x + ris)) < ris:
                                        y += round(d/2)
                                        x = 0
                                    else:
                                        x = x + d
                                elif y == py and x < px:
                                    px = x
                                    if (len(img[0]) - (x + ris)) < ris:
                                        y += round(d/2)
                                        x = 0
                                    else:
                                        x = x + d
                            else:
                                if (len(img[0]) - (x + lato)) < ris:
                                    y += lato
                                    x = 0
                        else:
                            x+=d
                    x+=1
        y+=1
        x=0
    return ris,(px,py)

