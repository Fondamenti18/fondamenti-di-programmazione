from immagini import load, save


def verif_dimensioni(x,y):
    return 0<=x<w and 0<=y<h
    

def p_visitabile(x,y):
    if verif_dimensioni(x,y):   #comprese in img
        if (x,y) not in ins_area and (x,y) not in ins_perimetro and img[y][x]==colore and (x,y) not in bufferino:
            return True
    return False

    
def p_vicini(x,y):
    cntt=0  #contatore
    for x1,y1 in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        if 0<=x1<w and 0<=y1<h and img[y1][x1]==colore:
            cntt+=1
    return cntt
    
    
def p_connessi(x,y):
    dora_esploratrice(x,y)
    while bufferino:
        (x,y)=bufferino.pop()
        if p_vicini(x,y)<4:
            ins_perimetro.add((x,y))
        else:
            ins_area.add((x,y))
        dora_esploratrice(x,y)
    

def dora_esploratrice(x0,y0):
    for direzione in ((0,1),(0,-1),(1,0),(-1,0)):
        x,y= x0+direzione[0],y0+direzione[1]
        while p_visitabile(x,y):
            bufferino.add((x,y))
            x += direzione[0]
            y += direzione[1] 
            

def colora_p(c1,c2):
    for x in range(w):
        for y in range(h):
            if (x,y) in ins_area:
                img[y][x]=c1
            elif (x,y) in ins_perimetro:
                img[y][x]=c2
       
    
def ricolora(fname, lista, fnameout):
    global h,w,img,bufferino,ins_area,ins_perimetro, colore
    img=load(fname)
    h=len(img)
    w=len(img[0])
    risultato=[]
    for task in lista:
        x,y,c1,c2=task[0],task[1],task[2],task[3]
        ins_area=set()
        ins_perimetro=set()
        colore=img[y][x] 
        bufferino={(x,y)}
        p_connessi(x,y)   #senza = perche non ritorna niente
        colora_p(c1,c2)
        risultato.append((len(ins_area),len(ins_perimetro)))
    save(img,fnameout)
    return risultato
