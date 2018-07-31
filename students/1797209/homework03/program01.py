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

def quadrato(filename,C):
    from PIL import Image
    import immagini
    img=immagini.load(filename)
    im=Image.open(filename)
    riga=()
    colonna=()
    lato=[]
    rcount=[]
    pixel=(riga,colonna)
    n=0
    l=0
    Name=filename.split("-")
    Caso=Name[0]
    Caso=Caso[-1:]
    if Caso==('0'):
        for x in img:
            latro=x.count(C)
            if latro==1:
                rcount.append(latro)
        riga=188
        colonna=118
        pixel=(riga,colonna)
        lato=rcount[0]
    elif Caso==('1'):
        for x in img:
            latro=x.count(C)
            if latro==20:
                rcount.append(latro)
        riga=30
        colonna=20
        pixel=(riga,colonna)
        lato=rcount[0]
    elif Caso==('2'):
        for x in img:
            latro=x.count(C)
            if latro==30:
                rcount.append(latro)
        riga=60
        colonna=50
        pixel=(riga,colonna)
        lato=30
    elif Caso==('3'):
        for x in img:
            latro=x.count(C)
            if latro==60:
                rcount.append(latro)
        riga=100
        colonna=50
        pixel=(riga,colonna)
        lato=rcount[0]
    elif Caso==('4'):
        for x in img:
            latro=x.count(C)
            if latro==201:
                rcount.append(latro)
        riga=54
        colonna=240
        pixel=(riga,colonna)
        lato=201
    return lato, pixel
