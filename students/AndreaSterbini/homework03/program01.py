'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.png .

Scrivere una  funzione quadrato(filename,c) che prende in input:
- il percorso di un file (filename) che contine un immagine in formato png della  tipologia appena descritta.
- una tupla di colori in formato RGB

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato di dimensione massima e colore c interamente visibile 
  nell'immagine. 
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
all'interno dell'immagine del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) 
all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del 
colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''

from immagini import *

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    M=load(filename)
    # per ogni punto in ordine x, y
    # se di colore diverso si salta
    # altrimenti potrebbe essere l'angolo UPSX di un quadrato
    # lo si allarga
    # se maggiore del max trovato si aggiorna il max

    mq = 0
    posx  = None
    posy  = None
    h = len(M)
    w = len(M[0])
    for y in range(h):
        M[y][0] = 1 if M[y][0] == c else 0
    for x in range(w):
        M[0][x] = 1 if M[0][x] == c else 0
    for y in range(1, h):
        for x in range(1, w):
            if M[y][x] != c:
                M[y][x] = 0
            else:
                q = min(M[y][x-1], M[y-1][x], M[y-1][x-1])+1
                M[y][x] = q
                if q > mq:
                    mq = q
                    posx, posy = x, y
    return mq, (posx-mq+1,posy-mq+1)

