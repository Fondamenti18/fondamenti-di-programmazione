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



    y=lista[1][0]
    x=lista[1][1]
    c= pixel[x][y]
    #print(lista[1][2])
    lu=up(pixel,x,y,c,lista[1][2],lista[1][3])
    ld=down(pixel,x,y,c,lista[1][2],lista[1][3])
    ll=left(pixel,x,y,c,lista[1][2],lista[1][3])
    print(pixel[0][99])
    #print(righe(pixel))
    lr=right(pixel,x,y,c,lista[1][2],lista[1][3])
    colora(pixel,y,x,1,1,lista[1][2])
    print(lista[1][0])
    for x in range(lu,int(ld/2)):
        if x != lista[1][1]:
            annie=right1(pixel,x,y,c,lista[1][2],lista[1][3])
        #if annie != lista[0][0]:
            #colora(pixel,annie-1,x,1,1,lista[0][3])
            #print(annie)
            yi=left1(pixel,x,y,c,lista[1][2],lista[1][3])
    for x in range(ld-1,int(ld/2)-1,-1):
        if x != lista[1][1]:
            annie=right2(pixel,x,y,c,lista[1][2],lista[1][3],ld)
        #if annie != lista[0][0]:
            #colora(pixel,annie-1,x,1,1,lista[0][3])
            #print(annie)
            yi=left2(pixel,x,y,c,lista[1][2],lista[1][3],ld)
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

def righe(img) :
    return len(img)
def colonne(img) :
    return len(img[0])
def colora(img, x, y, w, h, c):
    '''disegna sull'immagine img un rettangolo di colore c, ampiezza w e altezza h a partire dal pixel (y,x)'''
    for px in range(x, x+w):
        for py in range(y, y+h):
            #if inside(img,px,py):
            img[py][px] = c
            
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
def save(img, filename):
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)

  
def down(pixel,x,y,c,col,col2):
    x+=1
    #print(x)
    p=0
    p1=0
    while(x < righe(pixel) and pixel[x][y] == c):
        #print(pixel[x][y])
        p+=1
        colora(pixel,y,x,1,1,col)
        #print(pixel[x][y])
       
        x+=1
    p1+=1
    colora(pixel,y,x-1,1,1,col2) #se diversoda zero fare cosi
    return [x,p,p1]
    
def up(pixel,x,y,c,col,col2):
    #print('ciao')
    x=x-1
    #print(x)
    #print(x,y)
    p=0
    p1=0
    while(pixel[x][y] == c and x>= 0):
        #print(pixel[x][y])
        p+=1
        colora(pixel,y,x,1,1,col)
        #print(pixel[x][y])
        #print(x)
        x=x-1
    if x < 0:
        p1+=1
        colora(pixel,y,x+1,1,1,col2)
        return [x+1,p,p1]
    else:
        p1+=1
        colora(pixel,y,x+1,1,1,col2)
        return [x+1,p,p1]
def left(pixel,x,y,c,col,col2):
    y=y-1
    p=0
    p1=0
    while(y>=0 and pixel[x][y] == c):
        #print(pixel[x][y])
        if x == 0:
            #print(x)
            p1+=1
            colora(pixel,y,x,1,1,col2)
        else:
            p+=1
            colora(pixel,y,x,1,1,col)
        #print(pixel[x][y])
        y=y-1
    if y < 0:
        #print(y+1,x)
        #print(x)
        p1+=1
        colora(pixel,y+1,x,1,1,col2) #x-1
        #pass
        return [y+1,p,p1]
    p1+=1
    colora(pixel,y+1,x,1,1,col2)
    return [y,p,p1]

def left1(pixel,x,y,c,col,col2,lz,lr):
    y=y-1
    #print(y)
    p=0
    p1=0
    while(y >= 0 and pixel[x][y] == c):
        #print(pixel[x][y])
        if(y==0 or x == 0 or (pixel[x-1][y] != col2 and pixel[x-1][y] != col )):
            #print(pixel[x-1][y])
            #print(col2)
            #print('ciao')
            #print(x)
            p1+=1
            colora(pixel,y,x,1,1,col2)
        else:
            p+=1
            colora(pixel,y,x,1,1,col)
        #print(pixel[x][y])
        y=y-1
    p1+=1
    colora(pixel,y+1,x,1,1,col2)
    return [y,p,p1]

def left2(pixel,x,y,c,col,col2,ld,lr):
    y=y-1
    #print(y)
    p=0
    p1=1
    while(y >=0 and pixel[x][y] == c and x < colonne(pixel)):
        #print(pixel[x][y])
        if( y == 0 or x == ld-1 or ( pixel[x+1][y] != col2 and pixel[x+1][y] != col)): #c'era ==0
            #print(pixel[x-1][y])
            
            
            #print(y)
            p1+=1
            colora(pixel,y,x,1,1,col2)
        else:
            p+=1
            colora(pixel,y,x,1,1,col)
        #print(pixel[x][y])
        y=y-1
    #y=y+1
    if y < 0:
        #print(y+1,x)
        p1+=1
        colora(pixel,y+1,x-1,1,1,col2)
        #pass
        return [y+1,p,p1]
    elif y >0:
        p1+=1
        colora(pixel,y+1,x,1,1,col2)
        return [y,p,p1]
    elif y == 0 and pixel[x][y] != col2:
        p1+=1
        colora(pixel,y+1,x,1,1,col2)
        return [y,p,p1]
def right(pixel,x,y,c,col,col2,):
    #print('ciao')
    y=y+1
    #if pixel[x][y] == c:
        #y=y+1
    p=0
    p1=0
    while(y < colonne(pixel) and pixel[x][y] == c ):
        #print(pixel[x][y])
        if x ==0:
            p1+=1
            colora(pixel,y,x,1,1,col2)
        else:
            p+=0
            colora(pixel,y,x,1,1,col)
        #print(pixel[x][y])
        
        y=y+1
    #print(y)
    p1+=1
    colora(pixel,y-1,x,1,1,col2)
    return [y,p,p1]
    #else:
        #return y-1
def right1(pixel,x,y,c,col,col2,lz,ll):
    #print('ciao')
    y=y+1
    p=0
    p1=0
    #if pixel[x][y] == c:
        #y=y+1
    #print(col2)
    #print(x)
    while(y < colonne(pixel) and pixel[x][y] == c ):
        #print(pixel[x][y])
        #print(col2)
        if(x == lz or x == 0 or (pixel[x-1][y] != col2 and pixel[x-1][y] != col )):
            #print(pixel[x-1][y])
            #print(col2)
            #print(x)
            #print(y)
            p1+=1
            colora(pixel,y,x,1,1,col2)
        else:
            p+=1
            colora(pixel,y,x,1,1,col)
        #print(pixel[x][y])
        
        y=y+1
    #print(y)
    p1+=1
    colora(pixel,y-1,x,1,1,col2) #ll
    return [y,p,p1]

def right2(pixel,x,y,c,col,col2,ld,ll):
    #print('ciao')
    p=0
    p1=0
    y=y+1
    while(y < colonne(pixel) and pixel[x][y] == c ):
        #print(pixel[x][y])
        #print(col2)
        #print(x)
        #print(ld)
        #print(y)
        if( x == 0 or x == ld-1 or (pixel[x+1][y] != col2 and pixel[x+1][y] != col and pixel[x+1][y] != c) or (pixel[x-1][y] != col2 and pixel[x-1][y] != col and pixel[x-1][y] != c)):
            #print(pixel[x-1][y])
            #print(col2)
            #print(x,y)
            #print(x,y)
            #print(y)
            p1+=1
            colora(pixel,y,x,1,1,col2)
        else:
            p+=1
            colora(pixel,y,x,1,1,col)
        #print(pixel[x][y])
        
        y=y+1
    
    
    if y > 1:
        #print(y)
        #print(x)
        p1+=1
        colora(pixel,y-1,x,1,1,col2)
        return [y,p,p1]
    p1+=1
    colora(pixel,ll-1,x,1,1,col2)
    return [y,p,p1]
def right2i(pixel,x,y,c,col,col2,ld,ll):
    #print('ciao')
    y=y+1
    p=0
    p1=0
    while(y < colonne(pixel) and pixel[x][y] == c ):
        #print(pixel[x][y])
        #print(col2)
        #print(x)
        #print(ld)
        #print(y)
        if( y == ld-1 or x == ld-1 or (pixel[x+1][y] != col2 and pixel[x+1][y] != col and pixel[x+1][y] != c) or (pixel[x-1][y] != col2 and pixel[x-1][y] != col and pixel[x-1][y] != c)):
            #print(pixel[x-1][y])
            #print(col2)
            #print(x,y)
            #print(x,y)
            #print(y)
            p1+=1
            colora(pixel,y,x,1,1,col2)
        else:
            p+=0
            colora(pixel,y,x,1,1,col)
        #print(pixel[x][y])
        
        y=y+1
    
    #print(y)
    if y > 1:
        #colora(pixel,y-1,x,1,1,col2)
        return [y,p,p1]
    p1+=1
    colora(pixel,ll-1,x,1,1,col2)
    return [y,p,p1]

def left2i(pixel,x,y,c,col,col2,ld,lr):
    #y=y-1
    #print(y)
    p=0
    p1=0
    while(y >=0 and pixel[x][y] == c and x < colonne(pixel)):
        #print(pixel[x][y])
        if( y == ld-1 or x == ld-1 or (pixel[x][y-1] != col2 and pixel[x][y-1] != col and pixel[x][y-1] != c) or (pixel[x-1][y] != col2 and pixel[x-1][y] != col and pixel[x-1][y] != c)): #c'era ==0
            #print(pixel[x-1][y])
            
            
            #print(y)
            p1+=1
            colora(pixel,y,x,1,1,col2)
        else:
            p+=1
            colora(pixel,y,x,1,1,col)
        #print(pixel[x][y])
        y=y-1
    #y=y+1
    if y < 0:
        #print(y+1,x)
        p1+=1
        colora(pixel,y+1,x-1,1,1,col2)
        #pass
        return [y+1,p,p1]
    elif y >0:
        #colora(pixel,y+1,x,1,1,col2)
        return [y,p,p1]
    elif y == 0:
        p1+=1
        colora(pixel,y,x,1,1,col2)
        return [y,p,p1]


def alto(lu,ld,diff,pixel,lista,lr,ll,x,y,c,z):

    area=0
    for x in range(lu,ld-diff):
        annie=right1(pixel,x,y,c,lista[z][2],lista[z][3],lu,lr)               
        yi=left1(pixel,x,y,c,lista[z][2],lista[z][3],lu,ll)    
        if annie is not None and yi is not None:
            area+=annie[0]+yi[0]
def conta(pixel,c):
    count=0
    for x in range(len(pixel)):
        for y in range(len(pixel[0])):
            if pixel[x][y] == c:
                count+=1
    return count
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    pixel=load(fname)
    x=lista[0][1]
    y=lista[0][0]
    c=pixel[x][y]
    #z=0len(lista)
    #print(lista[4][3])
    ris=[]
    originaleA=0
    originaleB=0
    contatoreA=0
    contatoreB=0
    cloneA=0
    cloneB=0
    bella=conta(pixel,lista[0][2])
    #print(bella)
    #print(originaleB)
    #for i in range(1,25):
        #print((50-i*2)**2,(50-i*2+1)*4)
    #print(((50-i*2)**2,(50-i*2+1)*4) for i in range(1,25) )
    #print(lista[0][3])
    #print(conta(pixel,(0,5,5)))
    #cloneA=conta(pixel,lista[0][2])
    #cloneB=conta(pixel,lista[0][3])
    #print(cloneA,cloneB)
    for z in range(len(lista)):
        y=lista[z][0]
        x=lista[z][1]
        c= pixel[x][y]
        originaleA=conta(pixel,lista[z][2])
        originaleB=conta(pixel,lista[z][3])
        lu1=up(pixel,x,y,c,lista[z][2],lista[z][3])
        ld1=down(pixel,x,y,c,lista[z][2],lista[z][3])

        ll1=left(pixel,x,y,c,lista[z][2],lista[z][3])
        lr1=right(pixel,x,y,c,lista[z][2],lista[z][3])
        lu=lu1[0]
        ld=ld1[0]
        ll=ll1[0]
        lr=lr1[0]
        area=lu1[1]+ld1[0]+ll1[0]+lr1[0]
        colora(pixel,y,x,1,1,lista[z][2])
        #print(x,y)
        #print(lu1[2])
        #print(ld1[2])
        #print(ll1[2])
        #print(lr1[2])
        #print(lista[z][2],lista[z][3])
        #print(originaleA,originaleB)        
        diff= int((ld - lista[z][1]))  # c'era un //2
        

        alto(lu,ld,diff,pixel,lista,lr,ll,x,y,c,z)
            #print(colore2)                
        for x in range(ld-1,ld-diff,-1):
            #print(x)
            #if x != lista[z][1]:
            annie=right2(pixel,x,y,c,lista[z][2],lista[z][3],ld,lr)
            yi=left2(pixel,x,y,c,lista[z][2],lista[z][3],ld,ll)
            if annie is not None and yi is not None:
                area+=annie[0]+yi[0]
        if x-1 == y:
        #print(x,y)
            for x in range(ld-1,ld-diff,-1):
        
                annie=right2i(pixel,x,ld-1,c,lista[z][2],lista[z][3],ld,lr) #(righe(pixel)-1)-y
                yi=left2i(pixel,x,ld-1,c,lista[z][2],lista[z][3],ld,ll)
        contatoreA=conta(pixel,lista[z][2])
        contatoreB=conta(pixel,lista[z][3])
        #print(contatoreA,contatoreB, originaleA, originaleB)
        #print(originaleA,originaleB)
        #print(contatoreA,originaleA)
        #print('ciao',originaleA,contatoreA)
        if  (originaleB==0 and bella != 0) or originaleB != 0  :
            contatoreB= contatoreB-originaleB
            contatoreA= contatoreA - originaleA
        elif originaleA == contatoreA :
            contatoreB= contatoreB-originaleB
            contatoreA= contatoreA - originaleA  
        cloneB=contatoreB
        #if originaleB != 0:
            
        cloneA=contatoreA
        #
        
            #pass
         
        
        
        #if originaleB != contatoreB:
            
        ris+=[(contatoreA,contatoreB)]
    #print(ris)
    #print(conta(pixel,(255,0,0)))
    save(pixel,fnameout)
    return ris
    

#lista=[(0,0,(0,0,0),(0,5*i,5*i)) for i in range(1,25)]
#ricolora('I1.png',lista,'test7.png')

