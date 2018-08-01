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
import numpy as np
#import math
#import datetime

def quadrato(filename,c):
    '''Implementare qui la funzione'''

#    ora=datetime.datetime.now()

    lsImmagine,x,y=CaricaImm(filename) 
    arImmagineFiltro,arCoordZeri=FiltroColore(lsImmagine,c,x,y)
    
    XCamp=0
    RangeXCamp=0
    YCamp=0
    RangeYCamp=0
    
    LatoMax=0
    LatoMaxCamp=0
    
    TuplaBellissima=(0,(0,0))
    TuplaBellissimaCamp=(0,(0,0))
    
    XCamp,RangeXCamp,YCamp,RangeYCamp=CampionamentoImm(arImmagineFiltro,x,y)
    
    LatoMaxCamp,TuplaBellissimaCamp=Analizza(arImmagineFiltro,XCamp,RangeXCamp,YCamp,RangeYCamp,0,TuplaBellissimaCamp,arCoordZeri)
    
    #RWow=dzQuadrati[LatoMax][1]
    #CWow=dzQuadrati[LatoMax][0]
    #if arImmagineFiltro[RWow:RWow+LatoMax+1,CWow:CWow+LatoMax+1].sum()!=(LatoMax+1)**2:
    #    LatoMax=max(dzQuadrati.keys())
    #    return (LatoMax,dzQuadrati[LatoMax])
    
    if LatoMaxCamp>0:
        LatoMaxCamp-=1
    else:
        LatoMaxCamp=0
    TuplaBellissima=(0,(0,0))

#    print(datetime.datetime.now()-ora)        
        
    LatoMax,TuplaBellissima=Analizza(arImmagineFiltro,0,x,0,y,LatoMaxCamp,TuplaBellissima,arCoordZeri)

#    print(datetime.datetime.now()-ora)

    return TuplaBellissima

def Analizza(arImmagineFiltro,OrigineX,RangeX,OrigineY,RangeY,LatoMax,TuplaBellissima,arCoordZeri):
    FineY=OrigineY+RangeY
    FineX=OrigineX+RangeX
    for j in range(OrigineY,FineY):
        if j+LatoMax>=FineY:
            break
        iMax=0
        for i in range(OrigineX,FineX):
            #if len(dzQuadrati)>0:
            #    LatoMax=max(dzQuadrati.keys())
            #else:
            #    LatoMax=0
            
            #if DistBordoY<LatoMax+1:
            #    j=FineY
            if i+LatoMax>=FineX:
                break
#            elif arImmagineFiltro[j:j+LatoMax,i:i+LatoMax].sum()==(LatoMax)**2 and len(dzQuadrati)==0:
#                dzQuadrati[LatoMax]=(i,j)
            elif i<iMax:
                pass
            elif arImmagineFiltro[j][i]==1 and arImmagineFiltro[j:j+LatoMax+1,i:i+LatoMax+1].sum()==(LatoMax+1)**2:
            #elif arImmagineFiltro[j][i]==1:
                Lato=CercaQuadrato(arImmagineFiltro,j,i,FineX,FineY,LatoMax)
                LatoMax=Lato
                TuplaBellissima=(Lato,(i,j))
                i=i+Lato-1
                #if Lato>LatoMax:
                #    dzQuadrati[Lato]=(i,j)
#                while Lato>LatoMax:
#                    LatoTest=CreaQuadrato(arImmagineFiltro,j,i,Lato)
#                   if LatoTest==True:
#                        if not Lato in dzQuadrati.keys():
#                            dzQuadrati[Lato]=(i,j)
#                            Lato=0
#                    else:
#                        Lato-=1
            elif arImmagineFiltro[j][i]==1:
                iMax=arCoordZeri[j:j+LatoMax+1,i:i+LatoMax+1].max()
        
#        print(j,i,FineY,j+LatoMax,LatoMax)
        
    LatoMax=TuplaBellissima[0]
    return LatoMax,TuplaBellissima

def CaricaImm(filename):
    lsImmagine=load(filename) 
    y=len(lsImmagine) #y=altezza, cioè la lunghezza della lista
    x=len(lsImmagine[0]) #x=lunghezza, cioè la lunghezza di una riga della lista    
    return lsImmagine,x,y

def CercaQuadrato(arImmagineFiltro,j,i,x,y,LatoMax):
#    if arImmagineFiltro[j:j+LatoMax,i:i+LatoMax].sum()!=(LatoMax)**2:
#        return 0
    
#    TotUni=arImmagineFiltro[j:j+min(x-i,y-j),i:i+min(x-i,y-j)].sum()
#    LatoPiccolo=LatoMax
    
#    if TotUni==min(x-i,y-j)**2:
#    if arImmagineFiltro[j:j+min(x-i,y-j),i:i+min(x-i,y-j)].sum()==min(x-i,y-j)**2:
#        return min(x-i,y-j)

#    LatoGrande=int(math.sqrt(TotUni))+1

    #for l in range(LatoMax+1,LatoGrande+1):
    for l in range(LatoMax+1,min(x-i,y-j)+1):
        if arImmagineFiltro[j:j+l,i:i+l].min()==0:
            return l-1
    
#    Lato=(LatoPiccolo+LatoGrande)//2
#    
#    while LatoGrande>(LatoMax+1):
#        if arImmagineFiltro[j:j+Lato,i:i+Lato].min()==1:
#            if arImmagineFiltro[j:j+1+Lato,i:i+1+Lato].min()==0:
#                return Lato
#            elif arImmagineFiltro[j:j+1+Lato,i:i+1+Lato].min()==1:
#                LatoPiccolo=Lato+1
#                Lato=(LatoPiccolo+LatoGrande)//2
#        elif arImmagineFiltro[j:j+Lato,i:i+Lato].min()==0:
#            if arImmagineFiltro[j:j-1+Lato,i:i-1+Lato].min()==1:
#                return Lato-1
#            elif arImmagineFiltro[j:j-1+Lato,i:i-1+Lato].min()==0:
#                LatoGrande=Lato-1
#                Lato=(LatoPiccolo+LatoGrande)//2
            
#    for l in range(LatoMax+1,min(x-i,y-j)):
#        if arImmagineFiltro[j:j+l,i:i+l].min()==1:
#            pass
#        else:
#            return l-1

#    for l in range(LatoMax+1,min(x-i,y-j)):
#        if arImmagineFiltro[j+l][i+l]==0 or arImmagineFiltro[j+l][i]==0 or arImmagineFiltro[j][i+l]==0:
#            return l
    return min(x-i,y-j)    

def FiltroColore(lsImmagine,c,x,y):
    lsFiltroColore=[]
    lsCoordZeri=[]
    for j in range(y):
        ls=[]
        lsZ=[]
        for i in range(x):
            if lsImmagine[j][i]==c:
                ls+=[1]
                lsZ+=[0]
            else:
                ls+=[0]
                lsZ+=[i]
        lsFiltroColore+=[ls]
        lsCoordZeri+=[lsZ]
    return np.asarray(lsFiltroColore),np.asarray(lsCoordZeri)

def CampionamentoImm(arImmagineFiltro,x,y):
    TotUni=0
    MaxUni=0
    PixelImg=x*y
    PixelCamp=250*1000
    if x*y>=PixelCamp:
        UnitaCampionamento=PixelImg//PixelCamp
        Lato=min(x,y)//UnitaCampionamento
    else:
        Lato=0
    R=0
    C=0
    if Lato>1:
        for j in range(0,min(x,y),Lato):
            for i in range(0,min(x,y),Lato):
                TotUni=arImmagineFiltro[j:j+Lato,i:i+Lato].sum()
                if TotUni>MaxUni:
                    MaxUni=TotUni
                    C=i
                    R=j
    if MaxUni==0:
        return 0,x,0,y
    else:
        return C,Lato,R,Lato