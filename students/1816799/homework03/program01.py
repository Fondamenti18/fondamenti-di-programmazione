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
from collections import deque

def quadrato(filename,c):
    
    img, w, h=load2(filename,c)
    
    return build_m(img, w, h)  
    
    
def build_m(img, width, height):

    l=0
    angolo=()
    for y in range(height-1):

        for x in range(width-1):
            pos=img[y+1][x+1]

            if pos==1:
                img[y+1][x+1]= min(img[y][x], img[y+1][x], img[y][x+1])+pos

    for i in range(height):

        if l<max(img[i]):
            l=max(img[i])
            a1=img[i].index(l)-l+1
            a2=i-l+1
            angolo=(a1, a2)
    
    return (l ,angolo)
            
def load2(fname,c):
    
    img, width, height=load1(fname)
       
    lst=deque()
        
    for line in img:

        l = deque()
        for tupla in line:

            if tupla==c: l.append(1)
            else: l.append(0)    

        lst.append(l)

    return lst, width, height 
            
def load1(fname):

    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []

        for line in png_img:

            l = []
            for i in range(0, len(line), 3):

                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]

        return img, w, h
    
if __name__=='__main__':

    print(quadrato('Ist0.png',(255,255,255)))
    print(quadrato('Ist1.png',(255,0,0)))
    print(quadrato('Ist2.png',(255,0,0)))
    print(quadrato('Ist3.png',(255,0,0)))
    print(quadrato('Ist4.png',(0,0,255)))

    
