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
    
def checkRiga(image, colonna, riga, imageLen, imageHeight, c):
    #Controlla ogni riga relativa al pixel dell'altezza della colonna ottenuta
    #con checkColonna, ritorna un dizionario con associata ad ogni riga, la 
    #lunghezza del lato ottenuto e la coordinata y del primo pixel del lato
    
    DataDiction={}
    altezzaITER=range(riga, imageHeight)
    if colonna==0:                           #Caso altezza su bordo sinistro
        lunghezzaITER=range(0, imageLen)
        LenLato=0
        CoorY=0
        for rig in altezzaITER:
            for col in lunghezzaITER:
                if image[rig][col]==c:
                    LenLato+=1
                else:
                    LenLato=0
                    break
                DataDiction[rig]=LenLato
                
                
    elif colonna==imageLen-1:
        lunghezzaITER=range(colonna,-1,-1)   #Caso altezza su bordo destro
        LenLato=0
        for rig in altezzaITER:
            for col in lunghezzaITER:
                if image[rig][col]==c:
                    LenLato+=1
                    CoorY=col
                else:
                    LenLato=0
                    break
                DataDiction[rig]=LenLato
                
    else:                                     #Caso generale
        LatoDX=range(colonna, imageLen)
        LatoSX=range(colonna,-1,-1)
        LenLatoDX=0
        LenLatoSX=0
        for rig in altezzaITER:
            for col in LatoDX:
                if image[rig][col]==c:
                    LenLatoDX+=1
                else:
                    break
            for col in LatoSX:
                if image[rig][col]==c:
                    LenLatoSX+=1
                    CoorY=col
                else:
                    break
            MyLato=LenLatoDX+LenLatoSX-1
            if MyLato>0:
                DataDiction[rig]=MyLato
            LenLatoDX=0
            LenLatoSX=0
    return DataDiction, CoorY
        
        
        
def checkColonna(image, colonna, riga, imageHeight, c):
    #Dato un pixel, controlla tutta la colonna cercando quanto può andare avanti con
    #pixel dello stesso colore c in input. Ritorna l'altezza del lato ottenuto
    #e le coordinate del pixel più in alto
    if riga==0:                             #Caso pixel su bordo superiore
       altezzaIMG=range(0, imageHeight) 
       LenAltezza=0
       MyCoor=(colonna, 0)
       for rig in altezzaIMG:
           if image[rig][colonna]==c:
               LenAltezza+=1
           else:
               return LenAltezza, MyCoor
    
    elif riga==imageHeight-1:               #Caso pixel su bordo inferiore             
        altezzaIMG=range(riga,-1,-1)
        LenAltezza=0
        for rig in altezzaIMG:
            if image[rig][colonna]==c:
                LenAltezza+=1
                MyCoor=(colonna, rig)
            else:
                return LenAltezza, MyCoor
            
    else:                                   #Caso generale
        altezzaSUP=range(riga,-1,-1)
        altezzaINF=range(riga,imageHeight)
        LenAltezzaSUP=0
        LenAltezzaINF=0
        for rig in altezzaSUP:
            if image[rig][colonna]==c:
                LenAltezzaSUP+=1
                MyCoor=(colonna, rig)
            else:
                break
        for rig in altezzaINF:
            if image[rig][colonna]==c:
                LenAltezzaINF+=1
            else:
                break
        
        MyAltezza=LenAltezzaSUP+LenAltezzaINF-1
        return MyAltezza, MyCoor
        


def rePaintPic(image, imageLen, DictOfRighe, CoorY, c, c1, c2):
    #Dato il dizionario creato con checkRiga in input, ricolora il perimetro
    #e l'area di interesse in base al colore c1(area) o c2(perimetro) in input
    #Ritorna la lunghezza del perimetro e l'area della zona colorata
    LatoSuperiore=min(DictOfRighe)
    LatoInferiore=max(DictOfRighe)
    Perimetro=0
    Area=0
    for riga in DictOfRighe:
        if riga==LatoSuperiore or riga==LatoInferiore:
            lunghezza=range(CoorY, imageLen)
            for col in lunghezza:
                if image[riga][col]==c:
                    image[riga][col]=c2
                    Perimetro+=1
                else:
                    break
        else:
            lunghezza=range(CoorY, imageLen)
            for col in lunghezza:
                if col==CoorY or col==imageLen-1:
                    image[riga][col]=c2
                    Perimetro+=1
                else:
                    if image[riga][col]==c:
                        image[riga][col]=c1
                        Area+=1
                    else:
                        image[riga][col-1]=c2
                        Area-=1
                        Perimetro+=1
                        break
    if Area<0:
        Area=0
    if Perimetro<0:
        Perimetro=0
    return Area, Perimetro
            

        
        
    
def ricolora(fname, lista, fnameout):
    image=load(fname)
    
    imageHeight=len(image)
    imageLen=len(image[0])
    PairList=[]
    for data in lista:
        c=image[data[0]][data[1]]
        MyHeightData= checkColonna(image, data[0], data[1], imageHeight, c)
        DataDict= checkRiga(image, MyHeightData[1][0], MyHeightData[1][1], imageLen, imageHeight, c)
        AreaPerimeter=rePaintPic(image, imageLen, DataDict[0], DataDict[1],c, data[2], data[3])
        PairList.append(AreaPerimeter)
    save(image, fnameout)
    return PairList
