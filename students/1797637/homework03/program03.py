'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possibile e' necessario 
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
    img = load(fname)
    couples=[]

    for item in lista:  #For every item in the list of quadruples

        x= item[0]
        y= item[1]
        c1= item[2]
        c2= item[3]
        

        prev_col=img[y][x]

        to_color_c1=[(x,y)]
        discards=[]
        to_color_c2=[]

        pix_map=[]

        for i in range(len(img)):
            pix_map.append([])

        for y,row in enumerate(img):
            for item in row:
                pix_map[y].append(0)
        
        for pixel in to_color_c1:

            #if pixel not in discards:
            #if pix_map[y][x]==0:

            x=pixel[0]
            y=pixel[1]

            
            #discards.append((x,y))

            #print(item,x,y)

            pix_map[y][x]=1
            
            if x<len(img[0])-1:
                if pix_map[y][x+1]==0 and (x+1,y) not in to_color_c1:
                    if img[y][x+1]==prev_col :
                        to_color_c1.append((x+1,y))
                    else:
                        #to_color_c1.remove((x,y))
                        discards.append((x,y))
                        if (x,y) not in to_color_c2:
                            to_color_c2.append((x,y))
            else:
                if (x,y) not in to_color_c2:
                    to_color_c2.append((x,y))
                discards.append((x,y))

            if y<len(img)-1:
                if pix_map[y+1][x]==0 and (x,y+1) not in to_color_c1:
                    if img[y+1][x]==prev_col :
                        to_color_c1.append((x,y+1))
                    else:
                        #to_color_c1.remove((x,y))
                        discards.append((x,y))
                        if (x,y) not in to_color_c2:
                            to_color_c2.append((x,y))
            else:
                if (x,y) not in to_color_c2:
                    to_color_c2.append((x,y))
                discards.append((x,y))

            if x>0:
                if pix_map[y][x-1]==0  and (x-1,y) not in to_color_c1:
                    if img[y][x-1]==prev_col:
                        to_color_c1.append((x-1,y))
                    else:
                        #to_color_c1.remove((x,y))
                        discards.append((x,y))
                        if (x,y) not in to_color_c2:
                            to_color_c2.append((x,y))
            else: 
                if (x,y) not in to_color_c2:
                    to_color_c2.append((x,y))
                discards.append((x,y))

            if y>0:  
                if pix_map[y-1][x]==0 and (x,y-1) not in to_color_c1:
                    if img[y-1][x]==prev_col :
                        to_color_c1.append((x,y-1))
                    else:
                        #to_color_c1.remove((x,y))
                        discards.append(pixel)
                        if (x,y) not in to_color_c2:
                            to_color_c2.append((x,y))
            else:
                if (x,y) not in to_color_c2:
                    to_color_c2.append((x,y))
                discards.append((x,y))

            
        for pixel in discards:
            try:
                to_color_c1.remove(pixel)
            except Exception: pass
    
        
        for pixel in to_color_c1:
            
            x=pixel[0]
            y=pixel[1]

            img[y][x]=c1

        for pixel in to_color_c2:
            
            x=pixel[0]
            y=pixel[1]

            img[y][x]=c2
        
        couples.append((len(to_color_c1),len(to_color_c2)))
        
    #print(couples)
    save(img,fnameout)
    return couples

'''
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)
ricolora('I1.png',[(10,10,rosso,blu)],'test1.png')'''
