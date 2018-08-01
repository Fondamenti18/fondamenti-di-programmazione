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

def check_lato(img, rig, j, lun, c):
    for i in range (rig, rig+lun):
        if img[rig][j]==c:
            continue
        else:
            return None
    return "Ok"

def find_quad(img, rig, col, c):
    lun=0
    riga_ok=0
    for j in range(col, len(img[rig])): #trovo la lunghezza iterando su questa riga
        if img[rig][j]==c:
            lun+=1
            lato_dx = check_lato(img, rig, j, lun, c)
            if lato_dx == None:
                lun-=1
                break
        else:
            break
    if lun>2:
        x=0
        k=0
        z=lun/2
        while x != lun: #diagonale da sinistra
            try:
                if img[rig+x][col+x]!=c:
                    return None
            except Exception as e:
                break
            x+=1
        while k != lun/2: #diagonale da destra
            try:
                if img[rig+k][col+lun-2-k]!=c:
                    return None
            except Exception as e:
                break
            k+=1
    for i in range(rig, rig+lun): #itero sulle righe
        count=0
        try:
            for j in range(col, col+lun): #itero sulle colonne
                if img[i][j] ==c:
                    count+=1
                    continue
                else:
                    break
        except Exception as e:
            break
        if count==lun: #se ogni pixel nella riga è del colore c allora la riga ha "lun"*pixels
            riga_ok +=1
        else:
            return None
    if riga_ok==lun: #se "lun"*righe sono del colore c, allora il quadrato è ok
        return (lun, (col,rig))
    else:
        return None

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    img=load(filename)
    x = None
    y= None
    max_quad=()
    for i in range (0, len(img)):
        for j in range (0, len(img[i])):
            if img[i][j]==c:
                quad=find_quad(img, i, j, c)
                if quad!= None:
                    if max_quad == () or max_quad[0]<quad[0] or (max_quad[0] == quad[0] and max_quad[1]>quad[1]):
                        max_quad=quad
                    #else:
                    #    if max_quad[0]<quad[0] or (max_quad[0] == quad[0] and max_quad[1]>quad[1]):
                    #        max_quad = quad
    return max_quad
#quadrato('Ist0.png',(255,255,255))
