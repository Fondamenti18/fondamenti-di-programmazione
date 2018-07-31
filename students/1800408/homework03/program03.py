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
    global immagine
    immagine = load(fname)
    global colonne
    colonne = len(immagine[0])
    global righe
    righe = len(immagine)
    
    
    lista_finale = []
    for elemento in lista:
        x = elemento[0]
        y = elemento[1]
        c1 = elemento[2]
        c2 = elemento[3]
        c0 = immagine[y][x]
        risultato = filler(x, y, c0, c1, c2)
        area = risultato[0]
        perimetro = risultato[1]
#        print ("Perimentro=", perimetro, "Area=", area)
        lista_finale.append(risultato)
        #print(lista_finale)
    save(immagine, fnameout)
    return lista_finale
    
def verso_ovest(c0, x, y):
    n = x
    while (n >= 0):
        if immagine[y][n] == c0:
            n -= 1
        else:
            x_e = n + 1
            break
        if (n == -1):
            x_e = 0
    return x_e

def verso_est(c0, x, y):
    n = x
    while (n < colonne):
        if immagine[y][n] == c0:
            n += 1
        else:
            x_w = n - 1
            break
        if (n == colonne):
            x_w = colonne - 1
    return x_w

def filler(x, y, c0, c1, c2):

    area = 0
    perimetroH = 0
    perimetroV = 0
    if immagine[y][x] == c1:
        return ((0,0)) 
    coda = []
    coda.append([x,y])
    pixels = 0
    while pixels < len(coda):
        pixel = coda[pixels]
        pixels +=1
        px = pixel[0]
        py = pixel[1]
        x_w = verso_ovest(c0, px, py)
        x_e = verso_est(c0, px, py)
        if x_w <= x_e:
            for raster in range(x_w, x_e + 1):
                immagine[py][raster] = c1
                area += 1
                if py > 0: #non stiamo a fine immagine superiore
                    if (immagine[py-1][raster]) == c0:
                        coda.append([raster,py-1]) #accoda pixel superiore
                    else:
                        if (immagine[py-1][raster] != c1) and (raster > x_w) and (raster < x_e):
                            immagine[py][raster] = c2 #bordo superiore
                            perimetroH += 1  
                else: #stiamo a fine immagine superiore
                    if (raster > x_w) and (raster < x_e):
                        immagine[py][raster] = c2 #bordo superiore
                        perimetroH += 1
                if py < (righe - 1): #non stiamo a fine immagine inferiore
                    if (immagine[py+1][raster]) == c0:
                        coda.append([raster,py+1]) #accoda pixel inferiore
                    else:
                        if (immagine[py+1][raster] != c1) and (raster > x_w) and (raster < x_e):
                            immagine[py][raster] = c2 #bordo inferiore
                            perimetroH += 1
                else: #stiamo a fine immagine inferiore
                    if (raster > x_w) and (raster < x_e):
                        immagine[py][raster] = c2 #bordo inferiore
                        perimetroH += 1
            immagine[py][x_w] = c2 #bordo sinistro
            perimetroV +=1      
            immagine[py][x_e] = c2 #bordo destro
            perimetroV +=1
            #print ("perimetroH=",perimetroH)
            perimetro = perimetroV + perimetroH
    return ((area - perimetro,perimetro))




    
    
    