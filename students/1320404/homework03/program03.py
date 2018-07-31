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


import immagini
from IPython.display import Image
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)


    
def ricolora(fname, lista, fnameout):
    f=immagini.load(fname)
    out = f
    ris=[]
    for i in range(0,len(lista)):
        per=0
        are=0
        lunghezza=0
        lunghezza1=0
        lunghezza2=0
        altezza1=0
        altezza2=0
        altezza=0
        tupla=lista[i]
        x,y,c1,c2 = tupla
        colore_analiz = out[x][y]
        
        for colonne in range(x,len(out)):
            if out[y][colonne] == colore_analiz:
                lunghezza1 += 1
            else:    
                break
            
        for colonne in range(x-1,-1,-1):
            if out[y][colonne] == colore_analiz:
                lunghezza2 += 1
            else:    
                break
        lunghezza = lunghezza1+lunghezza2
        
        
        
        
        for righe in range(y,len(out[0])):
            if out[righe][x] == colore_analiz:
                altezza1 += 1
            else:        
                break
        for righe in range(y-1,-1,-1):
            if (out[righe][x] == colore_analiz):
                altezza2 += 1
            else:
                break
        
        altezza=altezza1+altezza2
        
        
        if lunghezza == altezza:
            lato = lunghezza-1
            
        verticeX = x - lunghezza2
        verticeY = y - altezza2
        
        
        for i in range(verticeX,lato):
            if out[i][verticeY] != c2:
                out[i][verticeY] = c2
                per+=1
        
        for i in range(verticeX,lato+1)  :
            if out[i][verticeY+lato] != c2:
                out[i][verticeY+lato] = c2
                per+=1
            
        for i in range(verticeY,lato):
            if out[verticeX][i]!= c2:
                out[verticeX][i] = c2
                per+=1
            
        for i in range(verticeY,lato):
            if out[verticeX+lato][i] != c2:
                out[verticeX+lato][i] = c2
                per+=1
        
        are = draw_rect(out,verticeX+1,verticeY+1,lato-1,lato-1,c1)
        test1=out
        immagini.save(test1,'test1.png')
        
            
        ris+=[(are,per)]
        
    return ris

def draw_rect(img, x, y, w, h, color):
    area=0
    for px in range(x, x+w):
        for py in range(y, y+h):
            try:
                area += 1
                img[py][px] = color
            except IndexError:
                return area
                pass
    return area