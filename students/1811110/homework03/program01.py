'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'img.

Vedi ad esempio l'img Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contine un img in formato png della  tipologia appena descritta.
- una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0 e 255 compresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e colore C interamente visibile nell'img. 
- le coordina  (x,y)  del pixel dell'img che corrisponde alla posizione 
all'interno dell'img del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' img. 

Si può assumere che nell'img e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''

from immagini import *

def dentro (img,i,j):
    iw=len(img[0])
    ih=len(img)
    if 0<=i<iw and 0<=j<ih:
        return True
    else:
        return False

def cont(raf,rdinate,xx,img,colore,yy,l1,l2):
    while img[yy][xx]==colore:
        l1+=1
        xx=xx+1
    xx=xx-1
    while img[yy][xx]==colore and l2<l1:
            l2+=1
            yy+=1
            if l1==l2:
                raf=l1
    return raf,rdinate,xx

def qu(img,yy,colore,xx):
    l1=0
    l2=0
    by=yy
    raf=0
    maxi=0
    rdinate=()
    while dentro(img,xx,yy)==True and img[yy][xx]!=colore :
        xx=xx+1
    if dentro(img,xx,yy)==True and img[yy][xx]==colore:
        rdinate=(xx,yy)
        
        raf,rdinate,xx=cont(raf,rdinate,xx,img,colore,yy,l1,l2)
    return raf,rdinate,xx
                
def cond(lq,coordina,maxi,nwco):
    
    if lq>maxi:
        maxi=lq
        nwco=coordina
        
    return maxi,nwco

def quadrato(filename,c):
    img=load(filename)
    coordina=()
    x=0
    y=0
    maxi=0
    nwco=()
    lq,coordina,x=qu(img,y,c,x)
    y=y+1
    while y<len(img):
        
        if x>=len(img):
            x=0
        while x<len(img):
            x=x+1
            lq,coordina,x=qu(img,y,c,x)
            maxi,nwco=cond(lq,coordina,maxi,nwco)
        y=y+1
            
            
    return maxi,nwco
            
    
                
                
                    
                    
                
                
 
                
                

            
