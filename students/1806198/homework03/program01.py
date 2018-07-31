from immagini import *

#campra 2 tuple di colori
def cmpcol(tupla1,tupla2=(256,256,256)):
    if tupla1[0]!=tupla2[0]:return False
    if tupla1[1]!=tupla2[1]:return False
    if tupla1[2]!=tupla2[2]:return False
    return True

#converte i colori dell img in valori binari 0/1
def img_to_01(img,c):
    img_01=[]
    for iriga in range(0,len(img)):
        riga=[]
        for ipixel in range(0,len(img[0])):
            if cmpcol(img[iriga][ipixel],c):riga+=[0]
            else: riga+=[1]
        img_01+=[riga]
    return img_01

#data una colonna, trova il max quadrato ottenibile restituendone lato, riga e flags aggiornati
def getmax_bottomdx(himg,img,col,colonna_flag,lmax):
    
    q=0; max_q=0; y=0
    
    for riga in range(himg-1,-1,-1):
        
        if img[riga][col] > 0:colonna_flag[riga] = 0
        else:colonna_flag[riga] += 1
        
        if colonna_flag[riga] > lmax:
            q += 1
            if q > max_q:
                max_q = q;  y=riga
        else: q = 0
        
    return max_q,y,colonna_flag

#data una colonna, trova il max quadrato ottenibile restituendone lato, riga e flags aggiornati
def getmax_topsx(himg,img,col,colonna_flag,lmax):
    
    q=0; max_q=0; y=0
    
    for riga in range(0,himg):
        
        if img[riga][col] > 0:colonna_flag[riga] = 0
        else:colonna_flag[riga] += 1
        
        if colonna_flag[riga] > lmax:
            q += 1
            if q > max_q:
                max_q = q;  y=riga
        else: q = 0
        
    return max_q,y,colonna_flag

#trova il quadrato piu grande scannerizzando dall angolo in basso a sx
def bottomdx(img,himg,m):
    
    colonna_flag = [0 for i in range(himg)]
    lmax=0; pixels=[]
  
    for col in range(m-1,-1,-1): 
        max_q,y,colonna_flag= getmax_bottomdx (himg,img,col,colonna_flag,lmax)
        if max_q > lmax:
            lmax += 1;  pixels+=[[col,y]]

    coord=min(pixels)    
    return lmax,coord[0],coord[1]


#trova il quadrato piu grande scannerizzando dall angolo in alto a dx
def topsx(img,himg,m):
    
    colonna_flag = [0 for i in range(himg)]
    lmax=0; pixels=[]
  
    for col in range(0,m):
        max_q,y,colonna_flag= getmax_topsx (himg,img,col,colonna_flag,lmax)
        if max_q > lmax:
            lmax+=1;  pixels+=[[col,y]]

    coord=max(pixels) 
    return lmax,coord[0]-(lmax-1),coord[1]-(lmax-1)

#funzione del programma
def quadrato(filename,c):

    #dati
    img=load(filename)
    wimg=len(img[0])
    himg=len(img)
    n_img=img_to_01(img,c)

    #trovo 2 quadrati
    lmax,y,x=bottomdx(n_img,himg,wimg)
    lmax2,y2,x2=topsx(n_img,himg,wimg)

    #restituisco il quadrato piu appropiato
    if y2<y: return (lmax,(y2,x2))
    if y2==y and x2<x: return (lmax,(y2,x2))
    return (lmax,(y,x))
