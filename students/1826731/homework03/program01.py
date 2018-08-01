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

def cerca_quadrato(imm, x, y, c):
    x_copia, y_copia = x, y
    lista = [imm[y_copia][x_copia]]
    while imm[y_copia][x_copia + 1] == c and imm[y_copia + 1][x_copia] == c:
        lista.append(imm[y_copia][x_copia + 1])
        x_copia, y_copia = x_copia + 1, y_copia + 1
    lunghezza = len(lista)
    for riga in range(y, lunghezza):
        for colonna in range(x, lunghezza):
            if imm[riga][colonna] != c:
                return False
    return lunghezza
    
def quadrato(filename, c):
    immagine = load(filename)
    lato = 0
    x, y = 0, 0
    for riga in range(len(immagine)):
        for colonna in range(len(immagine[0])):
            if immagine[riga][colonna] == c:
                mis_lato = cerca_quadrato(immagine, colonna, riga, c)
                if mis_lato == False:
                    continue
                elif mis_lato > lato:
                    lato = mis_lato
                    x, y = colonna, riga
                elif mis_lato == lato:
                    if riga < y:
                        y = riga
                    elif riga == y:
                        if colonna < x:
                            x = colonna
    return lato, (x, y)
