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

import immagini
from math import hypot


def quadrato(filename,c):
    immagine = immagini.load(filename)
   
    quadrato_massimo=[0, (0,0)]
    
    w=width(immagine)
    h=height(immagine)
    x = 0
    y = 0
    start_y=0
    old_start_y= 0
    while y < h-quadrato_massimo[0]:
        
        start_x = 0
        x=0
        old_start_x=0
        #print("y: ", y)
        while x < w-quadrato_massimo[0]:
            if immagine[y][x] == c:
                start_x, start_y = genera_square(immagine, x, y, quadrato_massimo[0], c, quadrato_massimo, start_x, start_y)
                if old_start_x!=start_x:
                    x=start_x+1
                    old_start_x=start_x
                else: x+=1    
            else:
                x+=1
        if old_start_y!=start_y:
            y=start_y
            old_start_y=start_y
        else:
            y+=1
  
    quadro=tuple(quadrato_massimo)
    return quadro

"""funzione genera quadrati nel vicinato sempre piu grandi"""
def genera_square(immagine, x, y, lato, c, quadrato_massimo, start_x, start_y):
        
    while True:
    
        if not inside(immagine, x+lato, y+lato): return start_x, start_y 
    
        # controllo delle righe che contengano tutte il colore c
        for j in range(y, y+lato):
            if immagine[j][x:x+lato].count(c) != lato: # ha beccato un pixel diverso
                for i in range(x, x+lato):
                    if immagine[j][i] != c:
                        break                                              # voglio sapere coordinate punto au cui ho beccato qualcosa di diverso.
                set_quadrato_massimo(x, y, lato-1, quadrato_massimo)
                return i, j # ritorno la x di rottura.
    
        lato+=1
        #genera_square(immagine, trasposta, x, y, lato+1, c, quadrato_massimo)

    
def inside(img, x , y):
    '''Verifica se il pixel di coordinate x,y è contenuto nella immagine'''
    return 0 <= x < width(img) and 0 <= y < height(img)

                
""" funzione che ritorna la larghezza dell'immagine"""  
def width(img):
    return len(img[0]) # è la prima riga mi da le colonne e dunque la larghezza

""" funzione che ritorna l'altezza dell'immagine"""  
def height(img):
    return len(img) # numero di righe quindi l'altezza della matrice

        

""" funzione che confronta i lati trovati lasciando nella lista quello piu grande e vicino alla minima coordinata"""
def set_quadrato_massimo(x, y, lato, quadrato_massimo):

        
    if len(quadrato_massimo) == 2: # la lista contiene già un quadrato
    
        if lato > quadrato_massimo[0]:
            # te sovrascrivo
            quadrato_massimo[0]=lato
            quadrato_massimo[1]=(x, y)
        elif lato == quadrato_massimo[0]:
            # verifico la coordinata più prossima all'origine (0, 0)
            p1=(x, y)
            p2=quadrato_massimo[1]
            quadrato_massimo[1] = distanza_minore(p1, p2) # mi torna il più vicino
    else:  # lista vuota quindi scrivo e basta      
            quadrato_massimo.append(lato)
            quadrato_massimo.append((x, y))
        
""" funzione che trova il piu vicino allo spigolo iniziale dell immagine"""
def distanza_minore(p1, p2):
    
    x1, y1 = p1
    x2, y2 = p2
    
    dist1 = hypot(x1 - 0, y1 - 0)
    dist2 = hypot(x2 - 0, y2 - 0)

    if dist1 < dist2: return p1
    else: return p2
    
if __name__ == '__main__':
    args       = ('Ist4.png',(0,0,255))
    #args        = ('Ist3.png',(255,0,0))
    #args        = ('Ist2.png',(255,0,0))
    #args        = ('Ist1.png',(255,0,0))
    #args        = ('Ist0.png',(255,255,255))
    returned    = quadrato(*args)
    print(returned)