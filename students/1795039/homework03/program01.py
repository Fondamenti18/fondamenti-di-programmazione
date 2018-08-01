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

def trovapixel(img, c, riga, colonna, altezza, larghezza):

    finito = False
    
    while riga < altezza:
        
        while colonna < larghezza:
           
            if  img[riga][colonna] == c:
                break
            
            colonna += 1    
        if  img[riga][colonna] == c:
            break
        riga += 1
        colonna = 0
        

    if riga == altezza and colonna == larghezza:
        finito = True


    return riga, colonna, finito
    

def quadpotenziale(img, c, pxriga, pxcolonna, altezza, larghezza):
    
    maxpxriga = pxriga
    
    while maxpxriga < altezza:
        if img[maxpxriga][pxcolonna] == c:
            maxpxriga += 1
        
        else:
            maxpxriga -= 1
            break
    maxpxcolonna = pxcolonna

    while maxpxcolonna < larghezza:
        if  img[pxriga][maxpxcolonna] == c:
            maxpxcolonna += 1
        else:
            maxpxcolonna -= 1
            break
    
    lungquad = (maxpxcolonna - pxcolonna)+1
    altquad = (maxpxriga - pxriga)+1
    
    if lungquad < altquad:
        altquad = lungquad
        maxpxriga =(pxriga + altquad) -1
        
    elif lungquad > altquad:
        lungquad = altquad
        maxpxcolonna = pxcolonna + (lungquad -1)
      
    #print("Partenza: ", pxcolonna, pxriga, "Arrivo: ", maxpxcolonna, maxpxriga, "Lung: ", lungquad, altquad)
    
    return lungquad, altquad, maxpxriga, maxpxcolonna

def checkquad(img, c, pxriga, pxcolonna, maxpxcolonna, maxpxriga):

    checkriga = pxriga
    checkcolonna = pxcolonna
    
 
    
    stop = False
    
    while checkriga < maxpxriga:
        checkcolonna = pxcolonna+1
        checkriga += 1
        while checkcolonna < maxpxcolonna:
            checkcolonna += 1
            
            if img[checkriga][checkcolonna] == c:
                stop = False
                
            else:
                stop = True
                break
        
        if stop == True: break
   
        
    
    
    return checkriga, checkcolonna


    
def quadrato(filename,c):

    img = load(filename)
    larghezza = len(img[0])-1
    altezza = len(img)-1
    quad = (0,(0,0))
    riga = 0
    colonna = 0
    pxriga = riga
    pxcolonna = colonna

    while True:
        
        pxriga, pxcolonna, finito = trovapixel(img, c, pxriga, pxcolonna, altezza, larghezza)
        
        
        lungquad, altquad, maxpxriga, maxpxcolonna = quadpotenziale(img, c, pxriga, pxcolonna, altezza, larghezza)
        
        checkriga, checkcolonna = checkquad(img, c, pxriga, pxcolonna, maxpxcolonna, maxpxriga)
    
        if checkriga == maxpxriga and checkcolonna == maxpxcolonna:
            tmpquad = (altquad, (pxcolonna, pxriga))
            
            if tmpquad[0] > quad[0]:
                quad = tmpquad
       
        if finito == False:
            pxcolonna += 1
        else: break


    return quad


    
   
    


       
    

    



                                               





