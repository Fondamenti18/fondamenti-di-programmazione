'''

Definiamo adiacenti di un pixel w di un immagine i pixel adiacenti a w in  orizzontale ora in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(asc,ordina) ha dunque come adiacenti i pixel   
con coordinate (asc-1,ordina),(asc+1,ordina),(asc,ordina-1),(asc,ordina+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere listone'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

peri caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (asc,ordina,c1,c2) dove  asc e ordina sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge listone'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra listone'immagine ricolorata nel file fnameout.

listone'operazione di ricolorazione e' la seguente. peri ciascuna delle quadruple (asc,ordina,c1,c2) della lista (nell'ordine), 
- tutti i pixel connessi al pixel  di coordinate (asc,ordina) nell'immagine vanno ricolorati col colore c1, 
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è listone'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio listone'immagine 'I1.png', listone'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' listone'immagine 'OUT1.png' identica all'immagine di partenza se non peri il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

peri ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- listone'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
peri altri  esempi vedere il file grade03.txt 
'''

from immagini import *
import sys
sys.setrecursionlimit(2000000000)
col= (155,  6, 255)

def ricolora(fname, lista, fnameout):
    pic=load(fname)        
    riss=[]
    for element  in lista:
        peri=element[3]
        cont=element[2]
        listone=[]
        c=pic[element[1]][element[0]]
        listaperi=[]
        
        def colorarearea(pic,asc,ordina,c,area):                   
            try:                                                                 
                if pic[ordina][asc+1]==c:
                    pic[ordina][asc+1]=col 
                    listone.append([ordina,asc+1])
                    colorarearea(pic,asc+1,ordina,c,area)
                    
                if pic[ordina][asc-1]==c:
                    pic[ordina][asc-1]=col
                    listone.append([ordina,asc-1])
                    colorarearea(pic,asc-1,ordina,c,area)
                    
                if pic[ordina+1][asc]==c:
                    pic[ordina+1][asc]=col
                    listone.append([ordina+1,asc])
                    colorarearea(pic,asc,ordina+1,c,area)
                    
                if pic[ordina-1][asc]==c:
                    pic[ordina-1][asc]=col
                    h=[]
                    listone.append([ordina-1,asc])
                    colorarearea(pic,asc,ordina-1,c,area)                                                                        
                else:
                    return 0   
            except: 
                IndexError
            
        colorarearea(pic,element[0],element[1],c,element[2])
        listaperi=[]
        listaarea=[]
        for i in listone:
            ora=i[1]
            w=i[0]
            
            try:
                if pic[w][ora+1]!=col or pic[w][ora-1]!=col or pic[w+1][ora]!=col or pic[w-1][ora]!=col:
                   listaperi.append(i)
                else:
                    listaarea.append(i)
            except IndexError:
                listaperi.append([w,ora])
                                                                                                                  
        for element in listaperi:   
            pic[element[0]][element[1]]=peri
            
        for o  in listaarea:
            pic[o[0]][o[1]]=cont
        
        save(pic,fnameout)
        riss.append((len(listaarea),len(listaperi)))                 
    
    return(riss)

                
                
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
