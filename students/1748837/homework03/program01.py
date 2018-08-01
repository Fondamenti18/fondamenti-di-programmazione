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
    image=load(filename)
    result=findSquares(image,c)
    return (result[0],(result[1],result[2]))



def checkAllSquare(image,start,line,diagonal,c):
    side=diagonal
    flag=True
    while flag:
        check=checker(image,start,line,side,c)
        if check==-1:
            flag=False
        else:
            side=check
    return side        

def checker(image,start,line,diagonal,c):
    for i in range(line,line+diagonal):
        for x in range(start,start+diagonal):
            if image[i][x]!=c:
                return x-start
    return -1
       
def areaSquares(image,startPixel,line,c):
    highVertex=[line,startPixel]
    currentPixel=highVertex
    diagonal=0
    while currentPixel[0]<len(image)-1 and image[currentPixel[0]][currentPixel[1]]==c and currentPixel[1]<len(image[line])-1:
        currentPixel=[currentPixel[0]+1,currentPixel[1]+1]
        diagonal+=1
    return diagonal


def findSquares(image,c):
    topSquare=[0,0,0]
    for indexLine in range(len(image)):
        line=image[indexLine]
        for indexColumn in range(len(line)):
            column=image[indexLine][indexColumn]
            if (len(line)-indexColumn)<topSquare[0]:
                break
            if indexLine==topSquare[2] and indexColumn<topSquare[1]+topSquare[0]:
                break
            if column==c and areaSquares(image,indexColumn,indexLine,c)>topSquare[0]:
                checked=checkAllSquare(image,indexColumn,indexLine,areaSquares(image,indexColumn,indexLine,c),c)
                topSquare=([checked,indexColumn,indexLine] if checked>topSquare[0] else topSquare)
    return topSquare


