from immagini import *
colori=[(255,255,255),(0,0,0),(0,255,0),(255,0,0),(0,0,255)]

#campra 2 tuple di colori
def cmpcol(tupla1,tupla2=(256,256,256)):
    if tupla1[0]!=tupla2[0]:return False
    if tupla1[1]!=tupla2[1]:return False
    if tupla1[2]!=tupla2[2]:return False
    return True

#porta l imagine in array di 013
def img_to_field(img):
    campo=[]
    for iriga in range(0,len(img),40):
        riga=[]
        for ipixel in range(0,len(img[0]),40):
            if cmpcol(img[iriga][ipixel],(255,0,0)): riga+=[3]
            elif cmpcol(img[iriga][ipixel],(255,255,255)): riga+=[0]
            else: riga+=[1]
        campo+=[riga]
    return campo

#porta l array 0123 in immagine
def field_to_img(campo):
    img=[]
    for riga in campo:
        rigo=[colori[casella] for casella in riga for i in range(0,40)]
        righe=[rigo for i in range(0,40)]
        img+=righe
    return img

#restituisce la prossima casella
def find_next(direzione,x,y):
    if direzione==0: return y,x+1
    elif direzione ==1: return y+1,x
    elif direzione ==2: return y,x-1
    else: return y-1,x

#cambia direzione
def change_dir(direzione,cnt):
    direzione+=1;cnt+=1
    if direzione >3: direzione=0
    return direzione,cnt

#sposta ogni volta il robot
def mov(campo,direzione,nx,ny,oy,ox,cnt,codifica):
    try:
        if campo[ny][nx] < 2 and ny>=0 and nx>=0:
            campo[oy][ox]=2; campo[ny][nx]=4
            cnt=0; ox=nx; oy=ny
            codifica+=str(direzione)
        else: direzione,cnt=change_dir(direzione,cnt)
    except: direzione,cnt=change_dir(direzione,cnt)
    return campo,direzione,cnt,codifica,nx,ny,oy,ox

#si occupa di trovare il percorso e far spostare il robot
def find_path(campo):
    nx=0; ny=0; ox=0; oy=0; cnt=0; direzione=0; codifica=''
    while True:
        ny,nx=find_next(direzione,ox,oy)
        campo,direzione,cnt,codifica,nx,ny,oy,ox= mov (campo,direzione,nx,ny,oy,ox,cnt,codifica)
        if cnt>3: break
    return codifica,campo

#funzione del programma
def cammino(fname,  fname1):
    codifica,campo=find_path(img_to_field(load(fname)))
    save(field_to_img(campo) ,fname1)
    return codifica
