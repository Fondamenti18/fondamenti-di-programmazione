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
    pic = load(fname)
    for z in range(len(lista)):
        x = lista[z][0]
        y = lista[z][1]
        c = pic[y][x]
        c1 = lista[z][2]
        c2 = lista[z][3]
        c3 = (0,255,255)
        pxc1 = 0
        pxc2 = 0
    #--------------------------------
        oy = y
        while pic[oy][x] == c and oy-1 > -2:
            pic[oy][x] = c1
            oy -= 1
            pxc1 += 1
        else:
            pic[oy+1][x] = c2
            pxc2 += 1
            
        ox = x
        while pic[y][ox-1] == c and ox-1 > -1:
            pic[y][ox] = c1
            ox -= 1
            pxc1 += 1
        else:
            pic[y][ox] = c2
            pxc2 += 1
           
        for n in range(x-1,ox-1,-1):
            for i in range(y-1,oy,-1):
                if pic[i][n-1] == c:
                    pic[i][n] = c1
                    pxc1 += 1
                else:
                    pic[i][n] = c2
                    pxc2 += 1
                
        for n in range(x-1,ox-1,-1):
            for i in range(y-1,oy,-1):
                if i-1 < 0 or pic[i][n+1] != c1:
                    pic[i][n+1] = c2
                    pxc2 += 1
        #---------------------------------------------
        kx = x+1
        while kx+1 < len(pic) and pic[y][kx+1] == c:
            pic[y][kx] = c1
            kx += 1
            pxc1 += 1
        else:
            pic[y][kx] = c2
            pxc2 += 1
          
        for n in range(x+1,kx):
            for i in range(y-1,oy,-1):
                if pic[i-1][n+1] == c:
                    pic[i][n] = c1
                    pxc1 += 1
                else:
                    pic[i][n] = c2
                    pic[i][n+1] = c2
                    pxc2 += 2
        for n in range(x+1,kx):
            for i in range(y-1,oy,-1):
                if pic[i][n+1] != c1 or i-1 < 0:
                    pic[i][n+1] = c2 
                    pxc2 += 1
        #----------------------------------------------
        ky = y+1
        while ky+1 < len(pic) and pic[ky+1][x] == c:
            pic[ky][x] = c1
            ky += 1
            pxc1 += 1
        else:
            pic[ky][x] = c2
            pxc2 += 1
            
        for n in range(x,kx+1):
            for i in range(y,ky+1):
                if pic[i][n] == c or pic[i][n] == c1:
                    pic[i][n] = c1
                    pxc1 += 1
                else:
                    pic[i][n] = c2
                    pxc2 += 1
                   
        for n in range(x+1,kx+1):
            for i in range(y+1,ky+1):
                if n+1 > kx or pic[i][n+1] != c1:
                    pic[i][n] = c2
                    pxc2 += 1
                    
        for n in range(x+1,kx+1):
            for i in range(y+1,ky+1):
                if i+1 > ky or pic[i+1][n] != c1:
                    pic[i][n] = c2
                    pxc2 += 1
        #-----------------------------------------------
        for n in range(x-1,ox-1,-1):
            for i in range(y+1,ky+1):
                if pic[i][n] == c:
                    pic[i][n] = c1
                    pxc1 += 1
                else:
                    pic[i][n] = c2
                    pxc2 += 1
        for n in range(x-1,ox-1,-1):
            for i in range(y+1,ky+1):
                if i-1 < 0 or pic[i-1][n] != c1:
                    pic[i][n] = c2
                    pxc2 += 1
                   
        for n in range(x-1,ox-1,-1):
            for i in range(y+1,ky+1):
                if i+1 > ky or pic[i+1][n] != c1:
                    pic[i][n] = c2
                    pxc2 += 1
        return (pxc1,pxc2)

    save(pic,fnameout)


