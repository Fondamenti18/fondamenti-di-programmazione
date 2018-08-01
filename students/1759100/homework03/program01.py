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
from math import sqrt
def heigth(img):
    return len(img)
def width(img):
    return len(img[0])

def cerca_lato(img,x,y,c):#devo cercare dei quadrati.
    lato1=0
    lato2=0
    for px in range(x,width(img)):
        if img[y][px]==c:
            lato1+=1
    for py in range(y,heigth(img)):
        if img[py][x]==c:
            lato2+=1 
    if lato1<lato2:
        for py in range(y,y+lato1):
            for px in range(x,x+lato1):
                if img[py][px]!=c:
                    lato1=px-x
                    lato2=py-y
    else:
        for py in range(y,y+lato2):
            for px in range(x,x+lato2):
                if img[py][px]!=c:
                    lato1=px-x
                    lato2=py-y
    if lato1<=lato2 :
        return lato1,x,y
    else:return lato2,x,y
               
def quadrato(filename,c):
    img=load(filename)
    dizionario={}
    dizionario['l']=0

    #print(heigth(img),width(img))
    for y in range(heigth(img)):
        for x in range(width(img)):
            if img[y][x]==c:
                l,xx,yy=cerca_lato(img,x,y,c)
                if l!=0 and l!=None:
                    if l>dizionario['l']:
                        print('   ')
                        dizionario['l']=l
                        dizionario['cord']=(xx,yy)
    return (dizionario['l'],dizionario['cord'])
    save(img,'ris:'+filename+'.png')
