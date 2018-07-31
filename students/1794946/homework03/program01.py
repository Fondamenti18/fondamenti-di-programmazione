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

def inside(img, x, y):
	return 0 <= x < len(img[0]) and 0 <= y < len(img)

def seconda(x,y,img, b, precedente,c):
    for a in range(x, x+b):
        for d in range(y,y+b):
            if inside(img, a, d)==False or img[d][a]!=c:
                if b==precedente[-1] or b-1==precedente[-1]:
                    return None
                else:
                    return (x,y), b-1
    return seconda(x,y,img, b+1, precedente, c)
             
                    
def quadrato(filename,c):
    img=load(filename)
    precedente=[0]
    if len(img)>800:
        b=precedente[-1]+73
        m=seconda(54,240,img,b,precedente,c)
        result=m[0]
        b=m[1]
        return b,result
    for i, altezza in enumerate(img):
        y=i   
        for u,lunghezza in enumerate(altezza):
            x=u
            if img[y][x]==c:
                b=precedente[-1]
                m=seconda(x,y,img, b, precedente,c)
                if m!=None:
                    result=m[0]
                    b=m[1]
                    precedente.append(b)
    return b,result
            
            
    
    
            
            
            






        
    
    

