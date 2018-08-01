'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista (nell'ordine), 
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1, 
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *

def disegna(img, x, y, w, h, c):
    
    for colonna in range(y, y+h):
        for riga in range(x, x+w):
                img[riga][colonna] = c
            

def disegnasurface(img, x, y, w, h, c):
    
    for colonna in range(y, y+h):
        for riga in range(x, x+w):
                img[riga][colonna] = c
    
def ricolora(fname, lista, fnameout):

    img = load(fname)
    listRow = []
    listColumn = []
    listHeight = []
    listCs = []
    ordine = []
    listCp = []

    i=-1
    
    while i!= len(lista)-1:

        i+=1
        
        column = lista[i][0]
        row = lista[i][1]
        
        surfaceColor = lista[i][2]
        perimeterColor = lista[i][3]
        baseColor = img[row][column]        
        newRow = row
        newColumn = column 
        originRow = row
        originColumn = column
        height = 0
        width = 0
        
        while newRow > 0:
            newRow -= 1
            if img[newRow][column] == baseColor:
                originRow -= 1
            else: break
                             
        while newColumn  > 0:
            newColumn -= 1
            if img[row][newColumn] == baseColor:
                originColumn -= 1
            else: break
    
        newRow = originRow
        newColumn = originColumn
        
        while newRow < len(img) and img[newRow][newColumn] == baseColor:
            height += 1
            newRow += 1    
        
        listRow.append(originRow)
        listColumn.append(originColumn)
        listHeight.append(height)
        listCs.append(surfaceColor)
        listCp.append(perimeterColor)
    
        disegna(img, listRow[i],listColumn[i],listHeight[i],listHeight[i], listCp[i])
        disegnasurface(img, listRow[i]+1,listColumn[i]+1,listHeight[i]-2,listHeight[i]-2, listCs[i])
            
        heightp = height -1
        heighta= height-2
        
        if i>= 1 and listRow[i] == listRow[i-1] and listColumn[i] == listColumn[i-1] and listCs[i] == listCs[i-1]:
            heighta = 0
        
        misure = ((heighta)*(heighta),((heightp)*4))      
        ordine.append(misure)
        
    save(img,fnameout)
    
    return ordine

        
    

    


