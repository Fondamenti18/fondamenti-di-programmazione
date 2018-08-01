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
    img = load(filename)
    return findquad(c,img)

def findquad(c,img):
    minn = 99999999999999999999999999999999999999999999
    maxx = 0
    coo = ()
    prova = []
    for y,i in enumerate(img):
        if c in i:
            for x, j in enumerate(i):
                if j == c:
                    cy = 0
                    cc = 0
                    minn = 999999999999999999999999999999999999999999999999
                    while dentro(img, x, y+cy) and img[y+cy][x] == c:
                        while dentro(img, x+cc, y+cy) and img[y+cy][x+cc] == c:
                            cc +=1
                        cy +=1
                        if cc < maxx:
                            break
                        minn = min(minn,cc)
                        cc = 0
                        if minn <= cy:
                            if maxx < minn:
                                maxx = minn
                                coo = (x,y)
                            break
    return (maxx,coo)
                            
                        
                        
def dentro(img, x, y):
    return 0 <= y < len(img) and 0 <= x < len(img[0])