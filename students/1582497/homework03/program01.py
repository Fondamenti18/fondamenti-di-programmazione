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
    x_y = ()
    image = load(filename)
    lati_quadrati = []
    
    def square_side(x,y):
        side = 0
        if image[y][x] == c:
            for n in range(len(image[y:])):
                if image[y+n][x] == c:
                    side += 1
                    n += 1
                else:
                    break
        return side
    
    def is_square(x,y):    
        for n in range(square_side(x,y),0,-1):
            square = True
            for k in range(n):    
                if any(x != c for x in image[y+k][x:n+x]):
                    square = False
            if square == True:
                return n
                break
    
    for y in range(len(image)):
        for x in range(len(image[y])):
            if image[y][x] == c:
                lati_quadrati.append(is_square(x,y))
                
    for y in range(len(image)):
        for x in range(len(image[y])):  
            if image[y][x] == c:             
                if is_square(x,y) == max(lati_quadrati):
                    if x_y == ():
                        x_y = (x,y)
    
    return max(lati_quadrati),x_y

#print (quadrato('Ist2.png',(255,0,0)))