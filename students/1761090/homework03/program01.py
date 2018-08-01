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
    altezza = len(img)
    larghezza = len(img[0])

    diz = {}
    for y in range(altezza):
        for x in range(larghezza):
            diz[(y,x)]=0

    for y in range(altezza -1, -1, -1):
        for x in range(larghezza -1, -1, -1):
            if y == altezza - 1:
                if img[y][x] == c:
                    diz[(y,x)]=1
                else:
                    diz[y,x]=0
            if x == larghezza -1:
                if img[y][x] == c:
                    diz[(y,x)]=1
                else:
                    diz[(y,x)]=0
            if img[y][x] == c:
                diz[(y,x)]=(1+min(diz[(y, x+1)], diz[(y+1, x)], diz[(y+1, x+1)])) if (y < altezza-1) and (x<larghezza-1) else 1

    massimo = max(list(diz.values()))
    lista=[]
    for k, v in diz.items():
        if v == massimo:
            lista.append(k)

    minl = min(lista)
    return (massimo, (minl[1], minl[0]))





