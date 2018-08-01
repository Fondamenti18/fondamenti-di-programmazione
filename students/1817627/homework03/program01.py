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

from immagini import load

def quadrato(filename,c):
    img=load(filename)
    righe=len(img)
    colonne=len(img[0])
    start=0
    for k in range(righe):
        for p in range (colonne):
            if not img[k][p] == c:
                continue
            par=1
            Bool=True
            for x in range(p+1,colonne):
                if not img[k][x] != c:
                    par+=1
                else:
                    break
            if par>start:
                for y in range(k+1,k+par):
                    for x in range(p,p+par):
                        if img[y][x] != c:
                            Bool=False
                            break
                    if Bool==False: 
                        break
                if Bool and par>start:
                        pixel=(p,k)
                        start=par
    return start,pixel