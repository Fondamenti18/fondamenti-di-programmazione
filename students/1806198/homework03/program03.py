from immagini import *
import copy

#controlla se un pixel è dentro il perimetro
def is_area(pixel,i,img):
    try:
        if img[pixel[0]+1][pixel[1]]==i and pixel[0]+1>=0 and pixel[1]>=0:
            if img[pixel[0]][pixel[1]+1]==i and pixel[0]>=0 and pixel[1]+1>=0:
                if img[pixel[0]-1][pixel[1]]==i  and pixel[0]-1>=0 and pixel[1]>=0:
                    if img[pixel[0]][pixel[1]-1]==i and pixel[0]>=0 and pixel[1]-1>=0:
                        if img[pixel[0]][pixel[1]]==i and pixel[0]>=0 and pixel[1]>=0:
                            return True
    except:pass
    return False

#controlla se un pixel, precedentemente salvato, è dentro il nuovo perimetro 
def is_areacnt(pixel,i,img):
    cnt=0
    try:
        if img[pixel[0]][pixel[1]]==i and pixel[0]>=0 and pixel[1]>=0:
            try:
                if img[pixel[0]+1][pixel[1]]==i and pixel[0]+1>=0 and pixel[1]>=0:
                    cnt+=1
            except:pass
            try:
                if img[pixel[0]][pixel[1]+1]==i and pixel[0]>=0 and pixel[1]+1>=0:
                    cnt+=1
            except:pass
            try:
                if img[pixel[0]-1][pixel[1]]==i  and pixel[0]-1>=0 and pixel[1]>=0:
                    cnt+=1
            except:pass
            try:
                if img[pixel[0]][pixel[1]-1]==i and pixel[0]>=0 and pixel[1]-1>=0:
                    cnt+=1
            except:pass
    except:pass
    return cnt

#dato un pixel restituisce una lista di pixel adiacenti di stesso colore
def get_adiacenti(pixel,check,img,i):
    ls=[]
    try:
        x=[pixel[0]+1,pixel[1]]
        if img[pixel[0]+1][pixel[1]]==i and x[0]>=0 and x[1]>=0:
            if x not in check:
                ls+=[x]
    except: pass
    try:
        x=[pixel[0],pixel[1]+1]
        if img[pixel[0]][pixel[1]+1]==i and x[0]>=0 and x[1]>=0:
            if x not in check:
                ls+=[x]
    except: pass
    try:
        x=[pixel[0]-1,pixel[1]]
        if img[pixel[0]-1][pixel[1]]==i and x[0]>=0 and x[1]>=0:
            if x not in check:
                ls+=[x]
    except: pass
    try:
        x=[pixel[0],pixel[1]-1]
        if img[pixel[0]][pixel[1]-1]==i and x[0]>=0 and x[1]>=0:
            if x not in check:
                ls+=[x]
    except: pass
    
    return ls

#data una tupla di input ritorna la lista delle posizioni dei pixel perimetro e area
def get_lss(check,img,i):
    tocol=[];toper=[];
    dacontrollare=copy.deepcopy(check)
    
    while(len(dacontrollare)>0):
        c=dacontrollare.pop()
        adiacenti=get_adiacenti(c,check,img,i)
        check+=adiacenti
        dacontrollare+=adiacenti
    
    for el in check:
        if is_area(el,i,img):tocol+=[el]
        else: toper+=[el]

    return tocol,toper

#data una matrice di indici di colori, ritorna l immagine contente i colori
def bin_to_img(img,coloripar):
    for riga in range(len(img)):
        for px in range(len(img[0])):
            colore=coloripar[img[riga][px]]
            img[riga][px]=colore
    return img

#data l immagine ritorna un matrice di indici, ove gli indici sono riferiti all array coloripar, anche esso restituito
def img_to_bin(img,lista):
    
    coloripar=[]
    for tupla in lista:
        if tupla[2] not in coloripar:
            coloripar+=[tupla[2]]
        if tupla[3] not in coloripar:
            coloripar+=[tupla[3]]

    for riga in range(len(img)):
        for px in range(len(img[0])):
            if img[riga][px] in coloripar:
                i=coloripar.index(img[riga][px])
                img[riga][px]=i
            else:
                coloripar+=[img[riga][px]]
                i=coloripar.index(img[riga][px])
                img[riga][px]=i
    return coloripar,img

#funzione del programma
def ricolora(fname, lista, fnameout):
    
    img=load(fname)
    ris=[]
    diz={}
    
    coloripar,img=img_to_bin(img,lista)
                    
    for tupla in lista:
        
        i=img[tupla[1]][tupla[0]];
        check=[[tupla[1],tupla[0]]];
        tocol=[];toper=[]
        
        c1i=coloripar.index(tupla[2])
        c2i=coloripar.index(tupla[3])
        
        if (tupla[0],tupla[1]) not in diz.keys():

            tocol,toper=get_lss(check,img,i)
            
        else:

            check2=diz.get((tupla[0],tupla[1]))
            check=check2[0]+check2[1]
            dacontrollare=check2[1]
    
            while(len(dacontrollare)>0):
                c=dacontrollare.pop()
                adiacenti=get_adiacenti(c,check,img,i)
                check+=adiacenti
                dacontrollare+=adiacenti
                
            for el in check:
                cnt=is_areacnt(el,i,img)
                if cnt==4:tocol+=[el]
                elif cnt>0: toper+=[el]

        ls=[tocol]+[toper]
        diz[(tupla[0],tupla[1])]=ls
        for pixel in tocol:img[pixel[0]][pixel[1]]=c1i
        for pixel in toper:img[pixel[0]][pixel[1]]=c2i
        ris+=[(len(tocol),len(toper))]


    img=bin_to_img(img,coloripar)
    save(img,fnameout)
    return ris


