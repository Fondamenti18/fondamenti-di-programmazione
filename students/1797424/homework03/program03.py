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
from collections import deque
    
def ricolora(fname, lista, fnameout):
    image=immagini.load(fname)
    returnValue = []
    

    def fill(y,x):
        queue=deque([(y,x)])
        visited=set()
        border=set()
        image_len_y=len(image)
        image_len_x=len(image[0])

        
        def valid(t,q):
            if t in visited:
                return False
            elif t in queue:
                return False
            elif t[0]<0 or t[1]<0:
                border.add(q)
                return False
            elif t[1]>=image_len_x or t[0]>=image_len_y:
                border.add(q)
                return False
            elif image[t[0]][t[1]]!=image[q[0]][q[1]]:
                border.add(q)
                return False
            else:
                return True


        while queue:
            q=queue[0]
            visited.add(q)


            if valid((q[0],q[1]+1),q): 
                queue.append((q[0],q[1]+1))
            if valid((q[0]+1,q[1]),q): 
                queue.append((q[0]+1,q[1]))
            if valid((q[0],q[1]-1),q):
                queue.append((q[0],q[1]-1))
            if valid((q[0]-1,q[1]),q): 
                queue.append((q[0]-1,q[1]))
            
            image[q[0]][q[1]]=color1
            queue.popleft()
    
        
        area=len(visited)-len(border)
        for p in border:
            image[p[0]][p[1]]=color2
        return area,len(border)
    
    
    

    
    for i in lista:
        x=i[0]
        y=i[1]
        color1=i[2]
        color2=i[3]

        counter=fill(y,x)
        returnValue.append(counter)
        
        
    immagini.save(image, fnameout)
    return returnValue





