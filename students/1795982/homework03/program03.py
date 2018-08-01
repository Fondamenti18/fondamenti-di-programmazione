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
    immagine=load(fname)
    w=len(immagine[0])
    h=len(immagine)
    listaRisultati=[]
    for tupla in lista:
        bordo=[]
        area=0
        coloreRiempimento=tupla[2]
        coloreBordo=tupla[3]
        coloreOriginale=immagine[tupla[1]][tupla[0]]
        x0=tupla[0]
        y0=tupla[1]

        r,g,b=coloreOriginale
        coloreCornice=(255-r,255-g,255-b)
        tmpimg=[]
        riga=[]

        for c in range(w+2):
            riga+=[coloreCornice]
        tmpimg+=[riga]  
        for r in range(1,h+1):
            riga=[]
            riga+=[coloreCornice]
            for c in range(1,w+1):
                riga.append(immagine[r-1][c-1])
            riga+=[coloreCornice]
            tmpimg+=[riga]
        riga=[]
        for c in range(w+2):
            riga+=[coloreCornice]
        tmpimg+=[riga]
        
        immagine[y0][x0] = coloreRiempimento
        area+=1
        
        x0=x0+1         
        y0=y0+1         
        
        if isbordo(x0,y0,coloreOriginale,tmpimg)==True:
            bordo.append((y0-1,x0-1))
        for x in range(x0-1, 0, -1):    
            if isconnesso(x,y0,coloreOriginale, tmpimg)==True:
                immagine[y0-1][x-1] = coloreRiempimento
                area+=1
                if isbordo(x,y0,coloreOriginale,tmpimg)==True:
                    bordo.append((y0-1,x-1))
            else:
                break
        for x in range(x0+1, w+1):      
            if isconnesso(x,y0,coloreOriginale, tmpimg)==True:
                immagine[y0-1][x-1] = coloreRiempimento
                area+=1
                if isbordo(x,y0,coloreOriginale,tmpimg)==True:
                    bordo.append((y0-1,x-1))
            else:
                break
          
        for y in range(y0-1, 0, -1):
            iscolorato, areapiu = coloraRiga(y,coloreOriginale,coloreRiempimento,immagine,tmpimg,bordo)
            area+=areapiu        
        for y in range(y0+1, h+1):
            iscolorato, areapiu =coloraRiga(y,coloreOriginale,coloreRiempimento,immagine,tmpimg,bordo)
            area+=areapiu
            
        iscolorato=True
        while iscolorato==True:
            iscolorato=False
            for y in range(1,h+1):
                if coloraRiga(y,coloreOriginale,coloreRiempimento,immagine,tmpimg,bordo)[0]==True:
                    iscolorato=True
                    area+=areapiu 
            if iscolorato==False:
                break
            for y in range(h+1,1,-1):
                if coloraRiga(y,coloreOriginale,coloreRiempimento,immagine,tmpimg,bordo)[0]==True:
                    iscolorato=True
                    area+=areapiu 
        perimetro=len(bordo)
        
        for punto in bordo:
            immagine[punto[0]][punto[1]]=coloreBordo
        area-=perimetro
        risultato=(area, perimetro)

        listaRisultati.append(risultato)
       
    save(immagine, fnameout)
    return (listaRisultati)


def isbordo(x,y,colore,img):
   
    if img[y][x-1] != colore or img[y][x+1] != colore or img[y-1][x] != colore or img[y+1][x] != colore:
        return True
    else:
        return False

def isconnesso(x,y,colore,img):
    
    if img[y][x] == colore and (img[y][x-1] == colore or img[y][x+1] == colore or img[y-1][x] == colore or img[y+1][x] == colore):
        return True
    else:
        return False
            
def coloraRiga(riga,coloreOriginale,coloreRiempimento,imgori,tmpimg,bordo):
    w=len(tmpimg[0])-2
    h=len(tmpimg)-2
    ritorno=False
    areapiu=0
    for x in range(1, w+1):
        if (tmpimg[riga][x] == coloreOriginale) and ((tmpimg[riga][x-1]==coloreOriginale and imgori[riga-1][x-2] == coloreRiempimento) or
                                                   (tmpimg[riga][x+1]==coloreOriginale and imgori[riga-1][x] == coloreRiempimento) or
                                                   (tmpimg[riga-1][x]==coloreOriginale and imgori[riga-2][x-1] == coloreRiempimento) or
                                                   (tmpimg[riga+1][x]==coloreOriginale and imgori[riga][x-1] == coloreRiempimento)):
            if imgori[riga-1][x-1] != coloreRiempimento:    
                
                imgori[riga-1][x-1] = coloreRiempimento
                areapiu+=1
                if isbordo(x,riga,coloreOriginale,tmpimg)==True:
                    bordo.append((riga-1,x-1))
                ritorno=True
    return (ritorno,areapiu)
      
           
        
            
        
        
    

