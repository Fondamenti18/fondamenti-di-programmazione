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

from immagini import load,save
    
def ricolora(fname, lista, fnameout):
    img=load(fname)
    risult=[]
    for x in lista:
        ap=singolo(img,x[0],x[1],x[2],x[3])
        risult.append(ap)
    save(img,fnameout)
    return risult
    
    
def singolo(img,x,y,c1,c2):
    perimetro=1
    listadacol=[]
    listadacol.append([x,y])
    colore=img[y][x]
    perimetro+=pixelconnessi(img,x,y,colore,listadacol)
    
    for pix in listadacol:
        perimetro+=pixelconnessi(img,pix[0],pix[1],colore,listadacol)
    bordo=contorno(img,x,y,listadacol)
    for pix in listadacol:   
        img[pix[1]][pix[0]]=c1
    for c in bordo:
        img[c[1]][c[0]]=c2
    perimetrocontorno=len(bordo)-4
    area=perimetro-perimetrocontorno
    ap=(area,perimetrocontorno)
    return ap
    
def pixelconnessi(img,x,y,colore,listadacol):
    ysin=y#10   
    ydes=y#10
    xsin=x#90
    xdes=x#90
    cont=0
    try:
        while img[ysin][x]==colore and inside(img,x,ysin):
            if [x,ysin] not in listadacol:
                listadacol.append([x,ysin])
                cont+=1
            ysin-=1
            while img[ydes][x]==colore and inside(img,x,ydes):
                if [x,ydes] not in listadacol: 
                    listadacol.append([x,ydes])
                    cont+=1
                ydes+=1
            while img[y][xsin]==colore and inside(img,xsin,y):
                if [xsin,y] not in listadacol:
                    listadacol.append([xsin,y])
                    cont+=1
                xsin-=1
            while img[y][xdes]==colore and inside(img,xdes,y):
                if [xdes,y] not in listadacol:
                    listadacol.append([xdes,y]) 
                    cont+=1
                xdes+=1
    except IndexError:
        pass
    return cont
def contorno(img,x,y,listadacol):
    bordo=[]
    insx=set()
    insy=set()
    for x in listadacol:
        insx.add(x[0])
    for x in listadacol:
        insy.add(x[1])
    masx=max(insx)#49
    minx=min(insx)#0
    masy=max(insy)#49
    miny=min(insy)#0
    for x in range(len(insx)):
        bordo.append([miny,x])
    for x in range(len(insy)):
        bordo.append([x,masx])
    for x in range(len(insy)):
        bordo.append([x,minx])
    for x in range(len(insx)):
        bordo.append([masy,x])
    return bordo
    
        
    


def inside(img, x, y):
    return 0 <= y < len(img[1]) and 0 <= x < len(img[0])
    

