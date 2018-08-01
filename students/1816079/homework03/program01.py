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
    square = {}
    x = y = l = 0
    while(x >= 0 and y >= 0):
        x,y = coordinates(img,c,(x+l,y))
        for k in square.keys():
            if k[0] <= x and x < k[0]+square.get(k):
                if k[1] <= y and y < k[1]+square.get(k):
                    l = k[0]+square.get(k)-x
                    break
        else:
            l = dim_square(img,(x,y))
            if l:
                square[(x,y)] = l
                
    lmax_square = 0
    xymax_square = (0,0)
    for k,v in square.items():
        if v == lmax_square:
            if k < xymax_square:
                xymax_square = k
                lmax_square = v
        elif v > lmax_square:
            lmax_square = v
            xymax_square = k
    
    return (lmax_square,xymax_square)
        
        
def coordinates(arr2d, element, start = (0,0)):
    rowp = start[0]
    for y in range(start[1], len(arr2d)):
        while(element in arr2d[y][rowp:]):
            x = arr2d[y].index(element,rowp)
            if y > 0:
                if arr2d[y-1][x] == element:
                    while(arr2d[y][x] != element):
                        x += 1
                    rowp += x
                    continue
            return x, y
        rowp = 0
    return -1,-1
            
        

def dim_square(img, coord):
    color = img[coord[1]][coord[0]]
    w = h = 0
    for _ in range(coord[0], len(img[0])):
        if img[coord[1]][coord[0]+w] != color:
            break
        w += 1
    for _ in range(coord[1], len(img)):
        if img[coord[1]+h][coord[0]] != color:
            break
        if img[coord[1]+h][coord[0]:coord[0]+w].count(color) < w:
            break 
        h += 1
    if w <= h:
        return w
    if w > h:
        return h
    return None
