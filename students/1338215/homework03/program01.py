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
    '''Implementare qui la funzione'''
    img=load(filename)
    x=0
    y=0
    lato=0
    tx=0
    ty=0
    for colonna in range(len(img)):
        for riga in range(len(img[0])):
            if(img[colonna][riga]==c):
                tx=riga
                ty=colonna
                latox=0
                for i in range(tx,len(img[0])):
                    if(img[colonna][i]==c):
                        latox+=1
                    else:
                        break
               
                if(latox>=lato):
                    latoy=0
                    for i in range(ty,len(img)):
                        if(img[i][tx]==c):
                            latoy+=1
                        else:
                            break
                   
                    minima=min(latox,latoy)
                    if(minima>=lato):
                        contX=tx+minima
                        contY=ty+minima
                        a=minima
                        check=True
                        for col in range(ty,contY):
                            for ri in range(tx,contX):
                                if(img[col][ri]!=c):
                                    b=contX-ri
                                    ta=b-a
                                    if(ta<a):
                                        a=ta
                               
                                if(col==a):
                                   
                                    minima=a
                                    break
                                if(a<lato):
                                    check=False
                                    break
                               
                        if(minima>lato and check):
                           
                            lato=minima
                            x=tx
                            y=ty
                        if(minima==lato and check):
                            if(x>tx):
                                x=tx
                                y=ty
                            elif(x==tx):
                                if(y>ty):
                                    y=ty
                         
   
    l1=[lato,(x,y)]
    return tuple(l1)
     
 
 
 
def load(fname):
   
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
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)