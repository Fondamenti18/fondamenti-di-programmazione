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
    cord = None
    #listWrong = []
    size = 0
    dimY = len(img)
    dimX = len(img[0])
    
    for row in range(dimY):
        #print(row)
        for col in range(dimX):
            #trovo il pixel di colore c
            if(c == img[row][col]):
                
                #se non c'e' size la setto a 1
                if(size == 0):
                    cord = (col, row)
                    size = 1
                
                #controllo che sia un possibile candidato controllando
                #che alla distanza 'size+1' ci sia ancora lo stesso colore
                newSize = size+1
                if(size > 0):
                    
                    #spigoli
                    if(row + newSize >= dimY or col + newSize>= dimX or c != img[row+newSize][col] or c != img[row][col+newSize] or c != img[row+newSize][col+newSize]):
                        continue
                    toSkip = False
                    metaLato = int ((size+1)/2)
                    rowMezzi = row+metaLato
                    colMezzi = col+metaLato
                    
                    #lati e diagonali
                    for q in range(0, newSize):
                        newRow = row+q
                        newCol = col+q
                        reverseCol = col + newSize -q
                        if(newRow >= dimY  or newCol >= dimX or reverseCol >= dimX or c != img[newRow][col] or c != img[row][newCol] or c != img[newRow][newCol] 
                        or c != img[newRow][reverseCol] or colMezzi >= dimX or rowMezzi >= dimY or c != img[rowMezzi][newCol] or c != img[newRow][colMezzi]):
                            toSkip = True
                            break
                    #rombo
                    for q in range (0, metaLato):
                        if(c != img[rowMezzi+q][col+q] or c != img[rowMezzi-q][col+q] or c != img[rowMezzi-q][col+newSize-q] or c != img[rowMezzi+q][col+newSize-q]):
                            toSkip = True
                            break
                    if(toSkip):
                        continue
                    
                    for f in range(row, row+newSize):
                        for h in range(col, col+newSize):
                            if(c != img[f][h]):
                                toSkip = True
                                break;
                        if(toSkip):
                            break
                    if(toSkip):
                        continue
                
                #ciclo da 1 alla fine dell'immagine
                for i in range(newSize, dimX-col):
                    flag = True
                    #se il pixel a distanza i e' giusto controllo se forma un quadrato
                   
                    if(c == img[row][col+i]):
                        
                        
                        for x in range (1, i):
                            #controllo tutte le colonne sotto la nuova colonna fino a row + i
                            if(row+x >= dimY or c != img[row + x][col+i]):
                                flag = False
                                break
                            #controllo se row+i e' di colore c
                            for y in range(0, i):
                                if(row+x >= dimY or c != img[row+x][col + y]):
                                    flag = False
                                    break
                            if(not flag):
                                break
                        
                        if(flag):
                            if(size < i+1):
                                cord = (col, row)
                                size = i+1
                    if(not flag):
                        break
    print('size quadrato:' + str(size))
    print('coord:' + str(cord))
    
    return size, cord

#quadrato('Ist4.png', (0,0,255))