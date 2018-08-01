'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre paralleli agli assi dell'immagine.

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
        
def getLenLato(image, colonna, riga, imageLen, c):
    #Ottiene la lunghezza massima del lato dello stesso colore
    index=colonna+1
    size=1
    while colonna<index<imageLen:
        if image[riga][index]==c:
            size+=1
            index+=1
        else:
            return size

def getLenAltezza(image, colonna, riga, imageHeight, c):
    #Ottiene la lunghezza massima dell'altezza dello stesso colore
    index=riga+1
    size=1
    while riga<index<imageHeight:
        if image[index][colonna]==c:
            size+=1
            index+=1
        else:
            return size
    
def quadrato(filename,c):
    image=load(filename)
    Dictlen={}
    imageHeight=len(image)
    imageLen=len(image[0])
    altezzaIMG=range(0,imageHeight)
    lunghezzaIMG=range(0,imageLen)
    for riga in altezzaIMG:
        for colonna in lunghezzaIMG:
            if image[riga][colonna]==c:
                if getLenLato(image, colonna, riga, imageLen, c)<=getLenAltezza(image, colonna, riga, imageHeight, c):
                    myLength=getLenLato(image,colonna,riga,imageLen,c)
                    if myLength not in Dictlen:
                        Dictlen[myLength]=(colonna, riga)
    lung=max(Dictlen)
    myCoor=Dictlen.get(lung)
    return lung, myCoor
   
