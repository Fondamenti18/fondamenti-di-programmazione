
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
    lstImg = load(filename)
    dizCol = Analize(lstImg,c)
    
    lato,coord = FindSquare(dizCol)
    
    return lato,coord

def insideImg(img,x,y):
    return 0 <= y < rows(img) and 0<=x<columns(img)

def rows(img):
    return len(img)

def columns(img):
    return len(img[0])

def Analize(lst,col):
    ris = {}
    counth = 0
    for y in lst:
        countr = 0
        for x in y:
            if counth not in ris.keys():
                ris[counth]=[]
                
            if x == col:
                ris[counth].append(countr)
                
            countr+=1
        counth+=1
    return ris

def FindSquare(diz):
    # prendo adiacenti
    lmax,maxTot,lx,x,ly,y=0,0,0,0,0,0 
    keyx = 0
    lacc=[]

    for key in diz.keys():
        
        if len(lacc) > maxTot: # possibile quadrato maggiore
                lmax,lx,ly = trova_quad(lacc,key-1,diz)  
                
                if lmax > maxTot:
                    maxTot=lmax
                    x = lx
                    y = ly
                lacc = []
        
        for value in diz[key]:
            if lacc == []:
                lacc.append(value)
                keyx = key
            elif value-1 in diz[key]:
                lacc.append(value)
            elif len(lacc) > maxTot: # possibile quadrato maggiore
                lmax,lx,ly = trova_quad(lacc,key,diz)  
                
                if lmax >= maxTot:
                    maxTot=lmax
                    x = lx
                    y = ly
                lacc = [value]
            else:
                lacc = [value]
    if maxTot == 0 and len(lacc) > 0:
        return 1,(lacc[0],keyx)
    else:
        return maxTot,(x,y)

def trova_quad(lst,key,diz):
    i = len(lst) 

    while(i>0):
        lstAcc = lst
        x=0
        while x < i-1:
            x+=1
            
            if key+x not in diz.keys():
                break 

            lstAcc = list(set(lstAcc).intersection(set(diz[key+x])))

#            if set(lstAcc) != set(lst):
#                i-=1
#                break 

        if len(lstAcc)== i:
            
            return i,min(lstAcc),key
        
        i-=1
    return 0,0,0
