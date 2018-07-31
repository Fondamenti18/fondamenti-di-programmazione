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

def pixinim(x,y,hi,wi):
    return 0 <= y <hi and 0<= x < wi

def quadrato(filename,c):
    img=load(filename)
    hi=len(img)
    wi=len(img[0])
    flag=0
    flag2=0
    contx=0
    conty=0
    contlato=0
    maxtillnow=[0,0,0]
    
    ispossible=1
    possibles=[]
    
    for y in range(hi):
        for x in range(wi):

            if img[y][x]==c:
                x1=x
                y1=y
                contx+=1
                conty+=1
                while flag==0:
                    if pixinim(x1+1,y,hi,wi):
                        if img[y][x1+1]==c:
                            x1+=1
                            contx+=1
                        else:
                            flag=1
                    if pixinim(x,y1+1,hi,wi):
                        if img[y1+1][x]==c:
                            y1+=1
                            conty+=1
                        else:
                            flag=1

                    if img[y1][x1]!=c:
                        flag=1
                        ispossible=0

 
                if contx<conty:
                    contlato=contx
                else:
                    contlato=conty
                #a questo punto abbiamo che x,y sono le cordinate dello spigolo in alto a sinistra e contlato e' il lato del possibile quadrato
                #controlliamo la diagonale dall' angolo in basso a sinistra a quello in alto a destra 
                if contlato<maxtillnow[2]:
                    ispossible=0

                
                x1=x+contlato-1
                y1=y+contlato-1
                
                if ispossible==1:
                    if contlato > 2:
                        for z in range(contlato):
                            if img[y+z][x1]!=c:
                                ispossible=0
                                break
                            if img[y1][x+z]!=c:
                                ispossible=0
                                break
                            
                if ispossible==1:
                    for yy in range(y,y+contlato):
                        if ispossible==0:
                            break
                        for xx in range(x,x+contlato):
                            if img[yy][xx]!=c:
                                ispossible=0
                                break
                            
                if ispossible==1:
                    if contlato>maxtillnow[2]:
                        maxtillnow=[x,y,contlato]

                    if contlato==maxtillnow[2]:
                        if y<maxtillnow[1]:
                            maxtillnow=[x,y,contlato]
                        if y==maxtillnow[1]:
                            if x<maxtillnow[0]:
                                maxtillnow=[x,y,contlato]

                    
                contlato=0    
                ispossible=1
                contx=0
                conty=0
                flag=0

            

    return maxtillnow[2],(maxtillnow[0],maxtillnow[1])



"""
hello=quadrato('PROVA.png',(255,0,0))    
print(hello)
"""
