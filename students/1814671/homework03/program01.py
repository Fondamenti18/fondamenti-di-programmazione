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
    h = height(img)
    w = width(img)

    maxQuad = (0,0)

    for i in range(h):
        for j in range(w):
            if img[i][j] == c:
                lunghezza = littleWidth(img, i, j, c)
                altezza = littleHeight(img, i, j, c)
                actualStart = (j, i)
                for q in range(i, i+min(altezza, lunghezza)):
                    for w in range(j, j+min(altezza, lunghezza)):
                        if img[q][w] != c:
                            r = littleWidth(img, i, j, img[q][w])
                            i = 0
                            j += r
                            break


                maxQuad = min(altezza, lunghezza)


    print(maxQuad, )

#Controllo coordinate pixel nell'immagine ----------------------------------
def inside(img, i, j):
    imgWidth, imgHeight = width(img), height(img)
    if(0 <= i < imgWidth and 0 <= j < imgHeight): return True
    else: return False

#Salva immagine -------------------------------------------------------------
def save(filename, img):
    pyimg = png.from_array(img, 'RGB')
    pyimg.save(filename)

def width(img): return len(img[0]) #Larghezza -------------------------------
def height(img): return len(img) #Altezza -----------------------------------
def littleWidth(img, i, j, c):
    littleLen = 0
    for k in range(j, width(img)):
        if img[i][k] == c:
            littleLen += 1
        else:
            break
    return littleLen#, (k, j)
def littleHeight(img, i, j, c):
    littleLen2 = 0
    for k in range(i, height(img)):
        if img[k][j] == c:
            littleLen2 += 1
        else:
            break
    return littleLen2
#Caricamento immagine da file (libro) ---------------------------------------


#quadrato('Ist1.png',(255,0,0))
q = 1
w = 1
for i in range(q, 7):
    for j in range(w, 7):
        print(i,j)
        if i == 2:
            i += 5
            j += 3
