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

rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)

def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    lsImmagine=load(fname)
    x=len(lsImmagine[0])
    y=len(lsImmagine)
    
    lsRisultato=[]
    
    for i in range(len(lista)):
        CoordIniz=(lista[i][0],lista[i][1])
        #strProvenienzaIniz='o'
        
        ColoreIniz=(lsImmagine[CoordIniz[1]][CoordIniz[0]])
        Colore=lista[i][2]
        ColorePerimetro=lista[i][3]
        
        #print(CoordIniz,ColoreIniz,Colore,ColorePerimetro)
        
        lsArea=[]
        lsPerimetro=[]
        lsRicoloraArea=[]
        lsRicoloraPerimetro=[]

        lsPixel=[(CoordIniz)]#,strProvenienzaIniz)]
        
        #print(lsPixel)
        
        while len(lsPixel)>0:
            lsPixel=AnalisiIntorno(lsImmagine,x,y,lsPixel,lsArea,lsPerimetro,ColoreIniz,Colore,ColorePerimetro)
            
        lsRisultato+=[(len(lsArea),len(lsPerimetro))]
        lsRicoloraArea+=lsArea
        lsRicoloraPerimetro+=lsPerimetro
        
        for pixel in range(len(lsRicoloraArea)):
            j=lsRicoloraArea[pixel][1]
            i=lsRicoloraArea[pixel][0]
            lsImmagine[j][i]=Colore
        
        for pixel in range(len(lsRicoloraPerimetro)):
            j=lsRicoloraPerimetro[pixel][1]
            i=lsRicoloraPerimetro[pixel][0]
            lsImmagine[j][i]=ColorePerimetro

    save(lsImmagine,fnameout)
        
    return lsRisultato#, lsImmagine[1][0:10],(0,0) in lsPerimetro,ColorePerimetro

#def Colora(Colore):
#    dzColori={}
#    dzColori['rosso'] = (255,   0,   0)
#    dzColori['blu']   = (  0,   0, 255)
#    dzColori['verde'] = (  0, 255,   0)
#    dzColori['nero']  = (  0,   0,   0)
#    dzColori['bianco']= (255, 255, 255)
#    dzColori['giallo']= (255, 255,   0)
#    dzColori['cyan']  = (  0, 255, 255)
#    dzColori['magenta']= (255,  0, 255)
#    return dzColori[str(Colore)]

#def Step(strProvenienza):
#    dzProvenienza={}
#    dzProvenienza['o']=[((1,0),'dx'),((0,1),'giu'),((-1,0),'sx'),((0,-1),'su')]#provengo dall'origine, controllo tutte le direzioni
#    dzProvenienza['dx']=[((1,0),'dx'),((0,1),'giu'),((0,-1),'su')]#provengo da destra, controllo le direzioni tranne sx
#    dzProvenienza['giu']=[((1,0),'dx'),((-1,0),'sx'),((0,-1),'su')]#provengo da giu, controllo le direzioni tranne giu
#    dzProvenienza['sx']=[((0,1),'giu'),((-1,0),'sx'),((0,-1),'su')]#provengo da sx, controllo le direzioni tranne sx
#    dzProvenienza['su']=[((1,0),'dx'),((0,1),'giu'),((-1,0),'sx')]#provengo da su, controllo le direzioni tranne su
#    return dzProvenienza[strProvenienza]

def StessoColore(lsImmagine,x,y,Coordinate,lsNuoviPixel,ColoreIniz,Colore):
#    lsStep=Step(strProvenienza)
#    lsStep=[((1,0),'dx'),((0,1),'giu'),((-1,0),'sx'),((0,-1),'su')]
    lsStep=[(1,0),(0,1),(-1,0),(0,-1)] #(step c, step r)
    #lsStessoColore=[]
    TotStessoColore=0
    i,j=Coordinate
    for step in range(len(lsStep)):
        #print(lsStep[pixel][1])
        c,r=lsStep[step]
        if j+r==y or j+r<0 or i+c==x or i+c<0:
            pass
        elif lsImmagine[j+r][i+c]==ColoreIniz:
            TotStessoColore+=1
            lsNuoviPixel+=[(i+c,j+r)] #,lsStep[step][1])]
        #elif lsImmagine[j+r][i+c]==Colore:
        #    TotStessoColore+=1
#    if TotStessoColore==len(lsStep):
#        #lsNuoviPixel+=lsStessoColore
#        return True
#    else:
#        return False
    return TotStessoColore==len(lsStep)

def Bordo(lsImmagine,x,y,Coordinate):
    i,j=Coordinate    
    return i==x-1 or i==0 or j==y-1 or j==0

def AnalisiIntorno(lsImmagine,x,y,lsPixel,lsArea,lsPerimetro,ColoreIniz,Colore,ColorePerimetro):
    lsNuoviPixel=[]
    for pixel in range(len(lsPixel)):
        i,j=lsPixel[pixel]
#        strProvenienza=lsPixel[pixel][1]
        if (not (i,j) in lsArea) and (not (i,j) in lsPerimetro) and lsImmagine[j][i]==ColoreIniz:
            #if Bordo(lsImmagine,x,y,(i,j)):
                #coloro il pixel con il colore perimetro
                #lsImmagine[j][j]=ColorePerimetro
                #aggiungo le coordinate a lista perimetro
                #lsPerimetro+=[(i,j)]
                #lsNuoviPixel+=[(lsPixel[pixel])]
            if StessoColore(lsImmagine,x,y,(i,j),lsNuoviPixel,ColoreIniz,Colore):
                #coloro il pixel con il colore area
                #lsImmagine[j][j]=Colore
                #aggiungo le coordinate a lista area
                lsArea+=[(i,j)]
            else:
                #coloro il pixel con il colore perimetro
                #lsImmagine[j][j]=ColorePerimetro
                #aggiungo le coordinate a lista perimetro
                lsPerimetro+=[(i,j)]
    lsPixel=lsNuoviPixel
    return lsPixel