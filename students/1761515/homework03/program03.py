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
    img=load(fname)
    li=[]
    for elemento in lista:
        x=elemento[0]
        y=elemento[1]
        c1=elemento[2]
        c2=elemento[3]
        
        c=img[y][x]
        
        
        
        
        contadx=0
        contasx=0
        contasu=0
        contagiu=0
        tx=x
        while(tx<len(img[0])):
            if(img[y][tx]==c):
                contadx+=1
            else:
                break
            
            tx+=1
            #print(tx)
        
        tx=x-1
        while(tx>=0):
            if(img[y][tx]==c):
                contasx+=1
            else:
                break
            tx-=1   
            
        ty=y-1
        while(ty>=0):
            if(img[ty][x]==c):
                contasu+=1
            else:
                break
            ty-=1   
        
        ty=y
        while(ty<len(img)):
            if(img[ty][x]==c):
                contagiu+=1
            else:
                break
            #print(ty)
            ty+=1   
        
            
        #print(contadx,contasx,contasu,contagiu)
        
        xmax=x+contadx-1
        xmin=x-contasx
        #print(xmax,xmin)
        
        #print(contasu,contagiu)
        ymax=y+contagiu-1
        ymin=y-contasu
        #print(ymax,ymin)
        perimetro=0
        area=0
        for colonna in range(len(img)):
            for riga in range(len(img[0])):
                if(riga>=xmin and riga<=xmax and colonna>=ymin and colonna<=ymax):
                    if(riga==xmin or colonna==ymin or riga==xmax or colonna==ymax):
                        img[colonna][riga]=c2
                        perimetro+=1
                    elif(x!=0 and y!=0):
                        area+=1
                        img[colonna][riga]=c1
                    elif(x==0 and y==0 and img[colonna][riga]!=c1):
                        area+=1
                        img[colonna][riga]=c1
                    else:
                        img[colonna][riga]=c1
                
        
        
        
        
        #print(area,perimetro)
        
        li.append(tuple([area,perimetro]))
        save(img,fnameout)
        
        
        
        
    return li


def colora(x,y,coloreI,c1,c2,img):
    return 0
    
    
    

def load(fname):
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return img

def save(img, filename):
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)    
        
        
#print(ricolora('I1.png', [(10, 10, (255, 0, 0), (0, 0, 255))], 'test1.png'))  