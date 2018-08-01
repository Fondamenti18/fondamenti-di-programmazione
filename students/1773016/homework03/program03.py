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
cordControllate = []
def prendiQuadrato(x,y,img):
    tempX = x
    tempY = y
    y0 = 0
    latoArea = 0
    while img[tempY][tempX] == img[y][x]:
        if tempX == 0:
            tempX -= 1
            break
        tempX -= 1
    x0 = tempX + 1
    tempX = x
    while img[tempY][tempX] == img[y][x]:
        if tempX == len(img[0])-1:
            tempX += 1
            break
        tempX += 1
    if (x-1>0 and x+1<len(img[0])) or img[y][x-1] == img[y][x]:
        latoArea = tempX - x0 - 1
    else:
        latoArea = 1
    latoPer = tempX - x0 - 1
    tempX = x
    while img[tempY][tempX] == img[y][x]:
        if tempY == 0:
            tempY -= 1
            break
        tempY -= 1
    y0 = tempY + 1
    return latoArea,latoPer,x0,y0
def coloraInterno(x,y,img,lato,cIn):
    for riga in range(y+1,y+lato):
        for colonna in range(x+1,x+lato):
            img[riga][colonna] = cIn
def coloraEsterno(x0,y0,img,lato,cOut):
    for colonna in range(x0,x0+lato+1):
        img[y0][colonna] = cOut
    for colonna in range(x0, x0 + lato+1):
        img[y0+lato][colonna] = cOut
    for riga in range(y0+1,y0+lato):
        img[riga][x0] = cOut
    for riga in range(y0+1,y0+lato):
        img[riga][x0+lato] = cOut
def coloraQuadrato(x,y,cIn,cOut,img):
    latoArea,latoPerimetro, x0, y0 = prendiQuadrato(x, y, img)
    if (x,y) in cordControllate:
        area = (latoArea-1)**2
    else:
        area = (latoPerimetro-1)**2
    perimetro = (latoPerimetro)*4
    coloraInterno(x0,y0,img,latoPerimetro,cIn)
    coloraEsterno(x0,y0,img,latoPerimetro,cOut)
    return area,perimetro
def ricolora(fname, lista, fnameout):
    img = load(fname)
    altezza = len(img)
    larghezza = len(img[0])
    #print('altezza: %s larghezza: %s' %(altezza,larghezza))
    listaRis = []
    for elem in lista:
        x = elem[0]
        y = elem[1]
        c1 = elem[2]
        c2 = elem[3]
        areaElem,periElem = coloraQuadrato(x,y,c1,c2,img)
        cordControllate.append((x, y))
        listaRis.append((areaElem,periElem))
    save(img,fnameout)
    return listaRis
#lista=[(0,0,(0,0,0),(0,5*i,5*i)) for i in range(1,25)]
#print(ricolora('I1.png',lista,'test7.png'))
'''
    risultato = [(2304, 196)] + [(0, 196)] * 23
'''