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

import png
from immagini import *
from IPython.display import Image

def righe(img) : return len(img)

def colonne(img) : return len(img[0])

def create(w,h,c=(0,0,0)):
    img = []
    for _ in range(h):#scala il primo
        riga = []  #crea il cotenitore della prima riga
        for _ in range(w):#scorre tutta la riga fino alla larghezza indicata
            riga+=[c] #riempie i pixel della riga
        img+=[riga] #salva la riga nel contenitore finale che salverà ogni riga
    return img

def load(filename):
    with open(filename, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
    return img

def coso3(cane,c):
    xy=[]
    for x in range(len(cane)):
        boz=[]
        for y in range(len(cane[x])):
            if(cane[x][y] == c):
                boz+=[x,y]
        xy=[boz]
        print(boz)
    return xy


def coso(cane,c):
    xy=[]
    for x in range(len(cane)):
        for y in range(len(cane[x])):
            if(cane[x][y])==c :
                xy+=[x,y]
                return xy
def coso2(cane,c,xy):
    #print(xy[1])
   
    for y in range(xy[1],len(cane[xy[0]])):
        if(cane[xy[0]][y])!=c :
            return [xy[0],y-1]
        
def ppp(cane,c,qt):
    for x in range(len(cane)):
        for y in range(len(cane[x])):
            #print(qt)
            #print(cane[x][y])
            if cane[x][y] == c  and [x,y] not in qt :
                #print('ciao')
                return [x,y]
            #if cane[x][y] == cane[-1][-1]:
                #return 0
def ddd(cane,c,xy):
    for x in range(xy[0],len(cane)):
        #print(x)
        for y in range(xy[1],len(cane[x])):
            #print([cane[x][y]])
            #print(xy[1])
            #print('\n')
            if(cane[x][y]!=c):
                
                return [xy[0],y-1]
def dudu(cane,c,xy,sup):
    
    for x in range(xy[0],sup):
        #print(x)
        #print(sup)
        
            #print([cane[x][y]])
            #print(y)
        if(cane[x][xy[1]]!=c):
            return [x-1,xy[1]]
def dul(cane,c,xy,sup):
    
    for x in range(xy[0],xy[0]+sup):
        #print(x)
        #print(sup)
        #print('ciao')
            #print([cane[x][y]])
            #print(y)
        #print(x)
        #print(sup-1)
        if(cane[x][xy[1]]==c and x == xy[0]+sup-1):
            return [x,xy[1]]

def pull(cane,c,xy,sup):    
    #for x in range(xy[0],len(cane)):
    #print(xy)
    for y in range(xy[1],sup+xy[1]):
            #print([cane[x][y]])
        #print(xy[1]+sup)
        #print(cane[39][32])
           # print(sup+xy[1])
            #print('\n')# and x == xy[0]+sup-1
            #print(cane[x][50])
            
        if( y == xy[1]+sup-1 and cane[xy[0]][y] == c):
            #print('ciao')
            #print(xy[0])
            #print(xy)
            return [xy[0],y]
                

                   

def riempiDu(xySH,xyDH,xySL,xyDL):
    goku=[]
    goku=[[xySH]]
    #print(xyDL[1])
    #print(goku[0])
    for x in range(xySH[1]+1,xyDH[1]):
        #print(x)
        goku[0]+=[[xySH[0],x]]
    goku[0]+=[xyDH]

    for z in range(xySH[0]+1,xySL[0]+1):
        #print(z)
        goku[0]+=[[z,xySH[1]]]
        for y in range(xySH[1]+1,xyDH[1]):
            
            goku[0]+=[[z,y]]
        #print(xyDL[1])
        goku[0]+=[[z,xyDL[1]]]
        #gocool+=[goku]
        #goku=[]
        #print('ciao')
    #print(goku)
    #print(gocool)
    
    #print(len(goku[0]))
    return goku
def trovaq(cane,c,qt):
    xy=[]
    xy2=[]
    xy3=[]
    xy4=[]
    if ppp(cane,c,qt) is not None:
        xy=ppp(cane,c,qt)
        xy2=ddd(cane,c,xy)
        xy3=dudu(cane,c,xy,len(cane))
        xy4=ddd(cane,c,xy3)
    
    #print(xy4)
    #print(xy3)
    #print(xy2)
    #print(xy)
        return [[xy,xy2,xy3,xy4]]
        
def quadrato(filename,c):
    '''Implementare qui la funzione'''
    cane=load(filename)
#print(cane[118][187])
    d={}
    xy=[]
    box1=[]
    box=[]
    if trovaq(cane,c,box) is not None:
        
        xy+=trovaq(cane,c,box)
        #print(xy)
        sup=xy[0][1][1]-xy[0][0][1]+1
        left=xy[0][2][0]-xy[0][0][0]+1
        right=xy[0][3][0]-xy[0][1][0]+1
        if(sup <= right and sup <=left):
            xy[0][2]=dul(cane,c,xy[0][0],sup)
            xy[0][3]=ddd(cane,c,xy[0][2])
            if sup not in d:
                d[sup]=xy[0][0]
        box1=riempiDu(xy[0][0],xy[0][1],xy[0][2],xy[0][3])
        box=box1[0][:]
    else:
        xy=ppp(cane,c,[])
        d[1]=xy 
    x=1
    for x in range(1,15):
        if trovaq(cane,c,box) is not None:
            xy+=trovaq(cane,c,box)
            sup=xy[x][1][1]-xy[x][0][1]+1
            left=xy[x][2][0]-xy[x][0][0]+1
            right=xy[x][3][0]-xy[x][1][0]+1
            bot=xy[x][3][1]-xy[x][2][1]+1

            if(sup <= right and sup <=left and sup <= bot):
                xy[x][2]=dul(cane,c,xy[x][0],sup)
                xy[x][3]=ddd(cane,c,xy[x][2])
                if sup not in d:
                    d[sup]=xy[x][0]
            elif(bot <= right and bot <=left and bot <= sup):
                #print(xy[x][0])
                #xy[x][1]=dul(cane,c,xy[x][0],bot)
                #xy[x][3]=ddd(cane,c,xy[x][2])
                xy[x][1]=pull(cane,c,xy[x][0],bot)
                #print(xy[x][2])
                xy[x][2]=dul(cane,c,xy[x][0],bot)
                xy[x][3]=ddd(cane,c,xy[x][2])
                xy[x][3]=pull(cane,c,xy[x][2],bot)
                if bot not in d:
                    d[bot]=xy[x][0]
            elif right < sup and right <= left and right <= bot:

            #print(right)
            #print(sup)
                xy[x][1]=pull(cane,c,xy[x][0],right)
                #print(xy[x][2])
                xy[x][3]=pull(cane,c,xy[x][2],right)#devo creare un simile per i lati
            #print(xy[x][3])
                if right not in d:
                    d[right]=xy[x][0]
            box1=riempiDu(xy[x][0],xy[x][1],xy[x][2],xy[x][3])
            box+=box1[0][:] #non funziona
    #print(box)
    #print(d)
    #print(xy)
    #print(box)
        #d[sup]=xy[x][0]
        #box+=riempiDu(xy[x][0],xy[x][1],xy[x][2],xy[x][3])
        #print(box)
    #print(d)
    g=sorted(d,reverse=True)
    g=g[0]
    #print(g)
    #print(cane[50][99])
    return (g,(d[g][1],d[g][0]))
   
#quadrato('Ist3.png',(255,0,0))
