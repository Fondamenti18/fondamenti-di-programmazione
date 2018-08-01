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
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione all'interno dell'immagine del punto in alto a sinistra del quadrato.

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine.

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''

from immagini import *

def getW(img):
    return len(img[0])

def getH(img):
    return len(img)

def buildPrefixSum(psum, img, c):
    W, H = getW(img), getH(img)
    for i in range(H+1):
        psum.append([])
        for j in range(W+1):
            if i == 0 or j == 0:
                psum[i].append(0)
            else:
                psum[i].append((0 if img[i-1][j-1] != c else 1) + psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1])

def queryPrefixSum(psum, i1, j1, i2, j2):
    return psum[i2+1][j2+1] - psum[i2+1][j1] - psum[i1][j2+1] + psum[i1][j1]

def updateBestAnsw(img, i, j, c, bestLen, bestX, bestY, psum, H, W):
    if img[i][j] == c:
        while i+bestLen<H and j+bestLen<W and queryPrefixSum(psum, i, j, i+bestLen, j+bestLen) == (bestLen+1)*(bestLen+1): #eseguito alla peggio min(N, M) volte
            bestLen += 1
            bestX = j
            bestY = i
    return bestLen, bestX, bestY

def quadrato(filename, c):
    img = load(filename)
    W, H = getW(img), getH(img)
    psum = []
    buildPrefixSum(psum, img, c)
    bestLen, bestX, bestY = 0, W, H
    for i in range(H): #O(NM) ammortizzato
        if i + bestLen >= H:
            break
        for j in range(W):
            if j + bestLen >= W:
                break
            bestLen, bestX, bestY = updateBestAnsw(img, i, j, c, bestLen, bestX, bestY, psum, H, W)
    return (bestLen, (bestX, bestY))

if __name__=='__main__':
    print(quadrato('test.png', (0,0,0)))
