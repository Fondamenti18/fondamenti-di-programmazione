'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre paralleli agli assi dell'immagine.

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
    img=load(filename)
    quadrati=searchColor(img, c)
    
    return max(quadrati),quadrati[max(quadrati)]

#Cerca colore c nell'immagine
def searchColor(img, c):
    lstPoints=[]
    w=len(img[0]) #x
    h=len(img) #y
    
    quadrati={}
    for y in range(h): #righe
        lSquare,xSquare,ySquare=0,0,0
        for x in range(w): #colonne
            px=img[y][x]
            #Individua il colore
            if(img[y][x]==c):
                lSquare,xSquare,ySquare,points=preSquareBuilding(img,x,y,c,lSquare,xSquare,ySquare,lstPoints)
                if(points!=()):
                    lstPoints.append(points)
                quadrati = buildDict(quadrati,lSquare,xSquare,ySquare)
            else:
                lSquare,xSquare,ySquare=0,0,0
    return quadrati

#Gestisce i quadrati principali e semplifica le operazioni per i sotto-quadrati 
def preSquareBuilding(img,x,y,c,lSquare,xSquare,ySquare,lstPoints):
    #Entra nel ciclo ogni volta che trova un colore c non consecutivo agli altri pixel
    #oppure quando un pixel non rientra nel lato del quadrato più vicino
    if lSquare==0:
        lSquare,xSquare,ySquare=buildSquare(img,x,y,c,0)
        points=(lSquare,xSquare,ySquare)
        return lSquare,xSquare,ySquare,points
    else:
         lSquare,xSquare,ySquare=controlPoints(img,c,x,y,lstPoints)
         return lSquare,xSquare,ySquare,()
    return

#Controlla se è un punto di un quadrato già analizzato
def controlPoints(img,c,x,y,lstPoints):
    for i,point in enumerate(lstPoints):
        lLstSquare=lstPoints[i][0]
        xLstSquare=lstPoints[i][1]
        yLstSquare=lstPoints[i][2]
        #Controlla se è un punto di un quadrato già analizzato
        if (x in range(xLstSquare+lLstSquare)) and (y in range(yLstSquare+lLstSquare)):
            #Calcola il lato l da cui iniziare a prova a creare dei quadrati
            lStart=((xLstSquare+lLstSquare))-x if((xLstSquare+lLstSquare)-x)<=((yLstSquare+lLstSquare)-y) else ((yLstSquare+lLstSquare)-y)
            return buildSquare(img,x,y,c,lStart)
        else:
            return 0,0,0
            #Può capitare che un pixel si trova ad l+(1..2..3) di un quadrato di lato l
            #return buildSquare(img,x,y,c,0)
    return

#Controlla la forma date le coordinate di partenza
def buildSquare(img,x,y,c,lStart):
    hSquare=0
    lOk=lStart #Indica fino a quale l*l esiste un quadrato di colore c
    for w in range(0,len(img[0])-x): #scorre dal punto x fino alla fine della riga
        hSquare+=1
        if trySquares(y,x,lOk,hSquare,img,c)==False: #hSquare=w+1
            break #Se ritorna 'False', non si può costruire un quadrato con quel lato
        lOk=hSquare
        
    return lOk,x,y

#Prova a costruire un quadrato di colore c
def trySquares(y,x,lOk,l,img,c):
            #row col
    #riga=img[y+l-1][x:x+l] #Lista di colori della riga
    #Controlla se si può aggiungere una nuova colonna al quadrato
    for hSquare in range(l):
        a=y+hSquare
        b=x+lOk
        if(img[y+hSquare][x+lOk]!=c):
            return False
    
    #Controlla se si può aggiungere una nuova riga al quadrato
    for wSquare in range(l):
        a=y+lOk
        b=x+wSquare
        if(img[y+lOk][x+wSquare]!=c):
            return False
    
    return True #Il quadrato si può allargare di una riga e una colonna

#Costruisce un dizionario con tutti i dati dei quadrati con lato diverso
def buildDict(quadrati,lQuadr,xQuadr,yQuadr):
    #Non considero i quadrati con lato uguale poichè si deve prendere in considerazione soltanto il primo
    if lQuadr not in quadrati.keys():
        quadrati[lQuadr]=xQuadr,yQuadr
    return quadrati
