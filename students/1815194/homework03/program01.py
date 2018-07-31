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
def studia_oriz(img,c,x,y,l):
    bol=True
    if x+l<len(img[0]) and y+l<len(img):
        for y1 in range(y,y+l):
            if img[y1][x+l]!=c:
                bol=False
                break
        for x1 in range(x,x+l):
            if img[y+l][x1]!=c:
                bol=False
                break
    return bol


def quadrato(filename,c):
    img=load(filename)
    l_max=0
    coord_max=tuple()
 
    for y in range(len(img)-1):
        for x in range(len(img[0])-1):
            coord=tuple()
            if img[y][x]==c:
                l=1
                
                while studia_oriz(img,c,x,y,l)==True:                      
                    l+=1
                    
            
                if l>l_max:
                   
                    l_max=l
                    coord_max=(x,y)
                
    return l_max,coord_max             
                
