from immagini import *

def quadrato(filename,c):
    img=load(filename)
    #larghezza (w)
    w= len(img[0])
    #altezza (h)
    h= len(img)
    
    global lista1
    lista1=[]
    
    def prova():
        global lista1
        for wi in range(w):
            for hi in range(h):
                if img[hi][wi]==c:
                    lista1=lista1+[[hi,wi]]
    prova()
    
    if len(lista1)==1:
        return (len(lista1),(lista1[0][1],lista1[0][0]))
    else:
        pass
    
    global lista3
    lista3=[]
    
    global lista2
    lista2=[]
    
    global d
    d=0
        
    for v in lista1:
        global a
        a=0
        global b
        b=[]
        def prova(v):
            global d
            global lista2
            if [v[0]+1,v[1]+1] in lista1:
                global c
                global lista3
                global b
                global a
                a=a+1
                v[0]=v[0]+1
                v[1]=v[1]+1
                b=[v[0],v[1],a]
                return prova(v)
            else:
                if b!=[]:
                    if b[2]>d:
                        d=b[2]
                        lista3=[b]
        prova(v)
    

    coord=(d+1,(lista3[0][1]-d,lista3[0][0]-d))
    return coord
