'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo 
monocolore rettangoli di vari colori i cui assi sono sempre parallei agli 
assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo 
preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contine un immagine in formato png 
  della  tipologia appena descritta.
- una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0 
  e 255 compresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e colore C 
  interamente visibile nell'immagine. 
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla 
  posizione all'interno dell'immagine del punto in alto a sinistra del 
  quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il 
cui punto in alto a sinistra occupa la riga minima  (e a parita' di riga la 
colonna minima) all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del 
colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del 
grader).
'''

from immagini import *

def quadrato(filename,c):    
    img = load(filename)
    matrice = []
    for _ in range(len(img)): 
        riga = [0] 
        for _ in range(len(img[0])-1): 
            riga+=[0] 
        matrice+=[riga]
    for i in range(len(matrice[0])):
        matrice[0][i] = 0             
        
    for px in range(len(img[0])): 
        for py in range(len(img)): 
            if img[py][px] == c:
                matrice[py][px] = 1 + min(matrice[py][px-1], matrice[py-1][px], matrice[py-1][px-1])
                    
    newArray = []
    for subarray in matrice:
        maxItem = 0
        for item in subarray:
            if item > maxItem:
                maxItem = item
        newArray.append(maxItem)
        massimo = max(newArray)
    f = massimo - 1

    for px in range(len(img[0])): 
        for py in range(len(img)): 
            if matrice[py][px] == massimo:
                tupla = px-f,py-f
                return (massimo, tupla)