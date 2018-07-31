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
    src = load(filename)
    corner = (len(src)-1, len(src[0])-1)
    length = 0
    for j in range(0, len(src)):
        for i in range(0, len(src[0])):
            if not (src[j][i] == c): continue
            l = 1
            found = True
            for x in range(i+1, len(src[0])):
                if (src[j][x] == c):
                    l+=1
                else:
                    break
            if (l>length):
                for y in range(j+1, j+l):
                    for x in range(i, i+l):
                        if (src[y][x] != c):
                            found = False
                            break
                    if not found: break
                if (found  and l>length):
                        corner = (i,j)
                        length = l
    return (length, corner)