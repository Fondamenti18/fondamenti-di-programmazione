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
rettangolometro=dict()
h,w = 0,0

def quadrato(filename,c):
    global h,w
    pixels=load(filename)
    h, w = len(pixels), len(pixels[0])
    calcola_rettangoli(pixels,c)
    p_max=(0,0)
    l_max = 0
    for i in range(h):
        for j in range(w):
            while check_quadrato(i, j, l_max+1):
                l_max=l_max+1
                p_max = (i+1,j+1)
    return  l_max,(p_max[1], p_max[0])
    
def calcola_rettangoli(pixels,c):
    for i in range(h):
        for j in range(w):
            if i==0:
                sopra = 0
            else:
                sopra = rettangolometro[i-1,j]
            if j==0:
                sinistra = 0
            else:
                sinistra = rettangolometro[i,j-1]
            if i==0 or j==0:
                diagonale = 0
            else:
                diagonale = rettangolometro[i-1,j-1]
            check = int(pixels[i][j] != c)
            rettangolometro[i,j] = sopra+sinistra-diagonale+check

def ostacoli(i1,j1,i2,j2):
    if i1>=h or i2>=h or j1>=w or j2>=w:
        return 1
    if j1==0:
        sopra = 0
    else:
        sopra=rettangolometro[i2,j1-1+1]
    if i1==0:
        sinistra = 0
    else:
        sinistra=rettangolometro[i1-1+1,j2]
    if i1==0 or j1==0:
        diagonale = 0
    else:
        diagonale=rettangolometro[i1-1+1,j1-1+1]
    totale=rettangolometro[i2,j2]
    return totale-sopra-sinistra+diagonale

def check_quadrato(i, j, l):
    return ostacoli(i, j, i+l, j+l) == 0    
