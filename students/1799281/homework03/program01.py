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
"C:/Users/john/Desktop/homework3/es1/Ist0.png"
if im[j+k][temp-u]!=im[j][i-u]:    #ok temp-u: coordinata colonna j+k coordinata riga sotto
                controllo=0
                return(0)                     # se non è un quadrato partendo da destra
            elif im[j+k][temp-u]==im[j][i-u]:
                continue
'''

from immagini import *


im= 0


def quadrato(filename,c):
    global im
    im=load(filename)
    j=0
    i=0
    a=0
    b=0
    ocont=0 #contatore orizzontale
    quadrati=[]  #lista con dentro le coordinate dei quadrati
    x=0    #ocont
    f=[]
    y=0
    dizio={}
    temp=()
    tempo=0
    finale=[]
    contro=1
    l=0
    while j != len(im):
       y=0
       x=0
       i=0
       ocont=0
       while i != len(im[j]):
           #print(j)
           r,g,b=im[j][i]
           #print(r,g,b)
           if (c==(r,g,b)):
               #print("ue")
               if i<len(im[j]):    #serve a vedere se finisce l'immagine  if im[j].index(im[j][i])!= len(im[j])+1:
                   #print(i,len(im[j])+1)
                   if im[j][i]==im[j][i+1]:                
                       ocont=ocont+1
                       if y==0:
                           m=j
                           n=i
                          # print("asfab")
                       contro=controllo(n,m,ocont)
                       #print(ocont,i,j,"primo",contro,n,m)
                       if contro==1 and y==0:
                           #print(temp)
                           #temp=i,j
                           #print(j,i,x)
                            temp=i,j
                            finale = finale + [temp]
                            y=1
                       elif contro== 0 and y==1:
                           #print(ocont,i,j,"secondo")
                           f=f+[ocont]
                           #print(len(im),j+ocont-1)
                           ocont=0
                           x=0
                           y=0
                   elif (im[j][i])!=(im[j][i+1]):   #it works! monopixel
                        if y==1:
                            ocont = ocont+1
                            #print(ocont,i,j,"ultimo")
                            f=f+[ocont]
                            ocont=0
                            y=0
                        elif y==0:
                            temp=i,j
                            finale = finale + [temp]
                            f=f+[1]
                            y=0
                        #print("cane")
               elif i==len(im[j]):
                    if y==1:
                        temp=i,j
                        finale = finale + [temp]
                        print(ocont,i,j,"beh")
                        f=f+[ocont]
                        ocont=0
                        y=0
                    elif y==0:
                        finale = finale + [temp]
                        f=f+[1]
           i=i+1
       j=j+1
    #finale=set(finale)
   #print(type(a))
    a,b=fi(finale,f)

    #p=(30,20)
    #print(finale.index(p))
    return(a,b)















def controllo(i,j,ocont):
    o=i
    l=j
    for k in range (ocont-1):
        #l=k
        l=l+1
        #print(k,l)
        o=i
        while o !=(ocont+i):      # while o !=(ocont+i-1):
            #print("entro", o, l)
            if im[j][i]==im[l][o]:
                #print(i,j,o,l)
                #print(l)
                o=o+1
                continue
            else:
               return(0)
    return(1)
            
    #return(ocont)
def fi(finale,f):
    a=max(f)
    #a=0
    b=0
    i=0
    #while i != len(f):
        #if f[i]==a:
           #b=i
       # i=i+1
    #return(b,finale[b])
    while i != len(f):
        if f[i]==a:
            b=i
            break
        i=i+1
            
    return(a,finale[b])
