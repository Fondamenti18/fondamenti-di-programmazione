from immagini import *

def pixinim(x,y,hi,wi):
    return 0 <= y <hi and 0<= x < wi

def adiacent(x,y):
    ad1=(x+1,y)
    ad2=(x-1,y)
    ad3=(x,y+1)
    ad4=(x,y-1)
    return ad1,ad2,ad3,ad4

"""    
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)
"""
def ricolora(fname, lista, fnameout):
    img=load(fname)
    hi=len(img)
    wi=len(img[0])
    lista1=set()
    conta=0
    contp=0
    listaap=[]
    listafatt=set()
    for el in lista:
        x1,y1,c1,c2=el
        ccheck=img[y1][x1]
        
        lista1.add((x1,y1))
        while len(lista1)>0:
            x,y=lista1.pop()
            if not pixinim(x,y,hi,wi) or img[y][x]!=ccheck:
                continue
            ad1,ad2,ad3,ad4=adiacent(x,y)
            lili=[ad1,ad2,ad3,ad4]
            for ele in lili:
                if pixinim(ele[0],ele[1],hi,wi):
                    if img[ele[1]][ele[0]]!=ccheck:
                        if (ele[0],ele[1]) not in listafatt:
                            contp+=1
                            img[y][x]=c2
                            listafatt.add((x,y))
                            break
                else:
                    contp+=1
                    img[y][x]=c2
                    listafatt.add((x,y))
                    break
            else:
                img[y][x]=c1
                listafatt.add((x,y))
                conta+=1
            for le in lili:
                if le not in listafatt:
                    lista1.add(le)
            """
            lista1.add(ad1)
            lista1.add(ad2)        
            lista1.add(ad3)
            lista1.add(ad4)
            """
        else:
            listafatt=set()
            listaap.append((conta,contp))
            conta=0
            contp=0
        
            
            
            
            
            
            
    save(img,fnameout)
    return listaap

"""
cicia=ricolora('I1.png',[(25,25,(0,0,0),(0,5*i,5*i)) for i in range(1,25)],"DOPO.png")

print("LA MIA /n",cicia)
"""