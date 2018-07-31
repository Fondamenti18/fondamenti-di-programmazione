'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, c) che prende in input:
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
    img=load(filename)
    lista=[]
    lista_diag=[]
    for x in range(0, len(img[0])):
        for y in range(0, len(img)):
            cont=0
            diag=0
            if img[y][x]==c:
                diag+=1
                while 0<=y+1<len(img) and 0<=x+1<len(img[0]):
                    y+=1
                    x+=1
                    cont+=1
                    if img[y][x]==c:
                        for py in range(y-cont, y+1):
                            for px in range(x-cont, x+1):
                                if img[py][x]==c and img[y][px]==c:
                                    pass
                                else:
                                    break
                    else:
                        break
                    diag+=1
                lista+=[(diag, ((x-cont), (y-cont)))]
                lista_diag+=[diag]
            y-=cont
            x-=cont
    lun_max=max(lista_diag)
    for el in lista:
        if el[0]==lun_max:
            return el