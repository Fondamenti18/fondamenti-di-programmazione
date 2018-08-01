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

    global lista_immagine
    lista_immagine = load(filename)
    altezza , larghezza = len(lista_immagine) , len(lista_immagine[0])
    longest = 0
    
    for riga in range(altezza):
        for pixel in range(larghezza):
            if lista_immagine[riga][pixel] == c:
                tmp = verifica(riga , pixel , c)
                if tmp > longest:
                    longest = tmp
                    coordinate = pixel , riga
                elif tmp > longest and tmp == 1:
                    #questa elif serve se il pixel e' uguale a uno
                    longest = tmp
                    coordinate = pixel , riga
    
    return longest , coordinate

def verifica(riga , pixel , colore):
    lunghezza = 1

    try:
        #se e' un quadrato con interruzioni
        while lista_immagine[riga + lunghezza][pixel + lunghezza] == colore:
            for check_riga in range(lunghezza):
                for check_pixel in range(lunghezza):
                    if lista_immagine[riga + check_riga][pixel + check_pixel] != colore:
                        return lunghezza - 1
            lunghezza += 1
        else:
            #se e' un pixel o un quadrato senza interruzioni (il quadrato senza interruzioni funziona perche'
            #a lista_immagine[riga + lunghezza][pixel + lunghezza] prende la lunghezza-esima posizione, compreso lo 0)
            return lunghezza
    except IndexError:
        return lunghezza - 1


if __name__ == '__main__':
    print( quadrato ( 'Ist2.png',(255,0,0) ) )
