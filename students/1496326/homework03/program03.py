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
    
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    img = load(fname)
    listaCoppie = []
    dimY = len(img)
    dimX = len(img[0])
   
    for tupla in lista:
        x = tupla[0]
        y = tupla[1]
        color1 = tupla[2]
        color2 = tupla[3]
        c = img[y][x]
        listaCord = []
        img[y][x] = color1
        listaCord.append((y,x))
        visited = set()
        visited.add((y,x))
        perimetro = 0
        area = 0
        i = 0
        while i < len(listaCord):
            pixel = listaCord[i]
            row = pixel[0]
            col = pixel[1]
            isBorder = False
            
            rowDown = row-1
            rowUp = row+1
            colUp = col+1
            colDown = col-1
            
            newPixel1 = (rowDown,col)
            newPixel2 = (rowUp,col)
            newPixel3 = (row,colDown)
            newPixel4 = (row,colUp)
            
            
            if newPixel1 not in visited :
                if rowDown >= 0 and c == img[rowDown][col]:
                    img[rowDown][col] = color1
                    visited.add(newPixel1)
                    listaCord.append(newPixel1)
                elif rowDown < 0 or c != img[rowDown][col]:
                     img[row][col] = color2
                     isBorder = True
            
            if newPixel2 not in visited:
                if rowUp < dimY and c == img[rowUp][col]:
                    img[rowUp][col] = color1
                    visited.add(newPixel2)
                    listaCord.append(newPixel2)
                elif rowUp >= dimY or c != img[rowUp][col]:
                     img[row][col] = color2
                     isBorder = True
                
            if newPixel3 not in visited:
                if colDown >= 0 and c == img[row][colDown]:
                    img[row][colDown] = color1
                    visited.add(newPixel3)
                    listaCord.append(newPixel3)
                elif colDown < 0 or c != img[row][colDown]:
                     img[row][col] = color2
                     isBorder = True
                     
            if newPixel4 not in visited:   
                if colUp < dimX and c == img[row][colUp]:
                    img[row][colUp] = color1
                    visited.add(newPixel4)
                    listaCord.append(newPixel4)
                elif colUp >= dimX or c != img[row][colUp]:
                     img[row][col] = color2
                     isBorder = True
                
            if(isBorder):
                perimetro += 1
            else:
                area += 1
            
            i += 1
        #print('len:' + str(len(listaCord)))
        listaCoppie.append((area, perimetro))
    save(img, fnameout)
    return listaCoppie
      

