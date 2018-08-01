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
    '''Implementare qui la funzione'''
    img = load(filename)
    side=0
    coords=(0,0)
    y=0
    x=0
    w=0
    

    for y,row in enumerate(img): #For every row in the image
        if c in row: #Check if the color is in the row
            i=0
            for item in row[i:len(row)-side]: #For every item in the row from the index i to the side's length
                if item == c: #Check if the item is the color
                    x=i
                    w=1
                    square=True
                    
                    for foll_item in row[i+1:]: #For every following item in the row
                        
                        if not foll_item == c: #Check if the current item is not the color
                            break
                        w+=1
                    if w <= len(img[y:]): #Check if the remaining rows are enough for the width found
                        for foll_row in img[y+1:y+w]: #For as many following rows as the width found is 
                            for item in foll_row[x:x+w]: #For as many items in the folloing row as the width found is
                                if not item == c: #Check if the item is not the color
                                    square=False
                                    
                                    break
                            if not square:
                                break
                    else:
                        square= False
                        ############
                    
                    if square:
                        #print('x',x,'y',y,'side',side)

                        if w == side:
                            if y == coords[1]:
                                if x < coords[0]:
                                    side=w
                                    coords=(x,y)
                            if y < coords[1]:
                                side=w
                                coords=(x,y)
                        if w > side:
                            side=w
                            coords=(x,y)
                            



                i+=1



    '''
    print(img)
    print('#########################\n#########################')
    print(img2)'''
    
    return side,coords

#quadrato('Ist1.png',(255,0,0))