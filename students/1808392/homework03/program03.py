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
    '''Implementare qui la funzione'''
    lstImg = load(fname)
    import copy
    imgOri=[]
    imgOri=copy.deepcopy(lstImg)
    getEl=0
    imgPrec=[]
    imgPrec=copy.deepcopy(lstImg)
    lstDati=[]
    for i in range(0,len(lista)):
        lstImg,Perim,lstMov = Color(lstImg,lista[getEl][0],lista[getEl][1],lista[getEl][2],lista[getEl][3],lstDati,imgOri,imgPrec)
        
        lstDati = Area(lstImg,imgPrec,Perim,lstDati,lstMov)
        getEl+=1
        imgPrec=[x[:] for x in lstImg]
        
        
    save(lstImg,fnameout)
    
    return lstDati
def insideImg(img,y,x):
    return 0 <= y < rows(img) and 0<=x<columns(img)

def rows(img):
    return len(img)

def columns(img):
    return len(img[0])

def Color(img,x,y,col,col2,lstAP,imgOri,imgPrec):
    #trovo pixel collegati

    lstMov = []
    lbEnd = False
    lbEnd1 = False
    lbEnd2 = False
    lbEnd3 = False
    lbEnd4 = False
    countPerim=0
    countArea=0
    if insideImg(img,x,y):
        x1,y1,x2,y2,x3,y3,x4,y4 = x,y,x,y,x,y,x,y
        while (lbEnd==False):
            if lbEnd1 == False:
                if insideImg(img,y1+1,x1) and imgPrec[y][x] == imgPrec[y1+1][x1]:
                    countArea+=1
                    img[y1+1][x1] = col
                    lstMov.append((y1+1,x1))
                    
                    y1 += 1
                    tmp = x1
                    while(insideImg(img,y1,x1+1) and imgPrec[y][x] == imgPrec[y1][x1+1]):
                        countArea +=1
                        img[y1][x1+1] = col
                        lstMov.append((y1,x1+1))
                        x1+=1
                    
                    img[y1][x1] = col2
                    lstMov.append((y1,x1))
                    countPerim +=1
                    x1=tmp
                else:
                    img[y1][x1] = col2
                    lstMov.append((y1,x1))
                    lbEnd1 = True
            
            if  lbEnd2 == False:
                if insideImg(img,y2-1,x2) and imgPrec[y][x] == imgPrec[y2-1][x2]:
                   
                    countArea+=1
                    img[y2-1][x2]=col
                    lstMov.append((y2-1,x2))
                    y2 -= 1
                    tmp = x2
                    while(insideImg(img,y2,x2-1) and imgPrec[y][x] == imgPrec[y2][x2-1]):
                       
                        countArea+=1
                        img[y2][x2-1] = col
                        lstMov.append((y2,x2-1))
                        x2-=1
                    img[y2][x2] = col2
                    lstMov.append((y2,x2))
                    countPerim +=1
                    x2=tmp
                else:
                    img[y2][x2] = col2
                    lstMov.append((y2,x2))
                    lbEnd2 = True
                
            if  lbEnd3 == False:
                if insideImg(img,y3,x3+1) and imgPrec[y][x] == imgPrec[y3][x3+1]:
                    
                    countArea+=1
                    img[y3][x3+1]=col
                    lstMov.append((y3,x3+1))
                    x3 += 1
                    tmp =y3
                    while(insideImg(img,y3-1,x3) and imgPrec[y][x] == imgPrec[y3-1][x3]):
                     
                        img[y3-1][x3] = col
                        lstMov.append((y3-1,x3))
                        countArea+=1
                        y3-=1  
                    img[y3][x3] = col2
                    lstMov.append((y3,x3))
                    countPerim +=1
                    y3=tmp
                else:
                    img[y3][x3] = col2
                    lstMov.append((y3,x3))
                    lbEnd3 = True
                        
                
            if  lbEnd4 == False:
                if insideImg(img,y4,x4-1) and imgPrec[y][x] == imgPrec[y4][x4-1]:
                   
                    img[y4][x4-1]=col
                    lstMov.append((y4,x4-1))
                    countArea+=1
                    x4 -= 1
                    
                    tmp =y4
                    while(insideImg(img,y4+1,x4) and imgPrec[y][x] == imgPrec[y4+1][x4]):
                      
                        img[y4+1][x4] = col
                        lstMov.append((y4+1,x4))
                        countArea+=1
                        y4+=1
                    
                    img[y4][x4] =col2
                    lstMov.append((y4,x4))
                    countPerim +=1
                    y4=tmp
                else:
                    img[y4][x4] = col2
                    lstMov.append((y4,x4))
                    lbEnd4 = True
            
            
            if lbEnd1 == True and lbEnd2 == True and lbEnd3 == True and lbEnd4 == True:
                lbEnd = True
                
        
        countArea+=1
        lstMov.append((y,x))
        img[y][x] = col
        j,h,j1,h1,j2,h2,j3,h3,j4,h4 = x,y,x,y,x,y,x,y,x,y
        lbEnd=False
        lbEnd1 = False
        lbEnd2 = False
        lbEnd3 = False
        lbEnd4 = False
        while (lbEnd==False):
            if lbEnd1 == False:
                if insideImg(img,h1+1,j1) and imgPrec[h][j] == imgPrec[h1+1][j1] :
                    if img[h1+1][j1] == imgOri[h1+1][j1]:
                        img[h1+1][j1] =col
                        lstMov.append((h1+1,j1))
                        countArea+=1
                    h1 += 1
                    tmp = j1

                    while(insideImg(img,h1,j1-1) and imgPrec[h][j] == imgPrec[h1][j1-1]):
                        if img[h1][j1-1] == imgOri[h1][j1-1]:
                            img[h1][j1-1] = col
                            lstMov.append((h1,j1-1))
                            countArea+=1
                        j1-=1  
                        
                    img[h1][j1] = col2
                    lstMov.append((h1,j1))
                    countPerim +=1
                    j1=tmp
                    
                else:
                    img[h1][j1] =col2
                    lstMov.append((h1,j1))
                    lbEnd1 = True
   
            if  lbEnd2 == False:
                if insideImg(img,h2-1,j2) and imgPrec[h][j] == imgPrec[h2-1][j2]:
                    if img[h2-1][j2] == imgOri[h2-1][j2]:
                        img[h2-1][j2]=col
                        lstMov.append((h2-1,j2))
                        countArea+=1
                    h2 -= 1
                    tmp = j2
                    while(insideImg(img,h2,j2+1) and imgPrec[h][j] == imgPrec[h2][j2+1]):
                        if img[h2][j2+1] == imgOri[h2][j2+1]:
                            img[h2][j2+1] = col
                            lstMov.append((h2,j2+1))
                            countArea+=1
                        j2+=1
                    
                    img[h2][j2] = col2
                    lstMov.append((h2,j2))
                    countPerim +=1
                    j2=tmp
                else:
                    img[h2][j2] = col2
                    lstMov.append((h2,j2))
                    lbEnd2 = True
                
            if  lbEnd3 == False:
                if insideImg(img,h3,j3+1) and imgPrec[h][j] == imgPrec[h3][j3+1]:
                    if img[h3][j3+1] == imgOri[h3][j3+1]:
                        img[h3][j3+1]=col
                        lstMov.append((h3,j3+1))
                        countArea+=1
                    j3 += 1
                    tmp =h3
                    while(insideImg(img,h3+1,j3) and imgPrec[h][j] == imgPrec[h3+1][j3]):
                        if  img[h3+1][j3] == imgOri[h3+1][j3]:
                            img[h3+1][j3] =col
                            lstMov.append((h3+1,j3))
                            countArea+=1
                        h3+=1
                    
                    img[h3][j3] =col2
                    lstMov.append((h3,j3))
                    countPerim +=1
                    h3=tmp
                else:
                    img[h3][j3] = col2
                    lstMov.append((h3,j3))
                    lbEnd3 = True
                        
                
            if  lbEnd4 == False:
                if insideImg(img,h4,j4-1) and imgPrec[h][j] == imgPrec[h4][j4-1]:
                    if img[h4][j4-1] == imgOri[h4][j4-1]:
                        img[h4][j4-1]=col
                        lstMov.append((h4,j4-1))
                        countArea+=1
                    j4 -= 1
                    tmp =h4
                    while(insideImg(img,h4-1,j4) and imgPrec[h][j] == imgPrec[h4-1][j4]):
                        if img[h4-1][j4] == imgOri[h4-1][j4]:
                            img[h4-1][j4] = col
                            lstMov.append((h4-1,j4))
                            countArea+=1
                        h4-=1
                    img[h4][j4] =col2
                    lstMov.append((h4,j4))
                    countPerim +=1
                    h4=tmp
                else:
                     img[h4][j4] =col2
                     lstMov.append((h4,j4))
                     lbEnd4 = True
            
            
            if lbEnd1 == True and lbEnd2 == True and lbEnd3 == True and lbEnd4 == True:
                lbEnd = True
        
    else:
        return [0]
    
    

    return img,countPerim,lstMov

def Area (img,imgPrec,Perim,lstDati,lstMov):
    lstDati.append((len(set(lstMov))-Perim,Perim))
    return lstDati


