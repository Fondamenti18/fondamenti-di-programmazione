from immagini import *
def cammino(fname,fname1):
    immag=load(fname)
    fermo=0
    x=0
    y=40
    risultato=''
    xx=0
    yy=0
    st=0
    while fermo!=6:
        immag,ap,fermo,x,y,st=trova(xx,yy,x,y,fermo,st,immag)
        if ap==True:
            risultato,xx,yy,fermo=sposta(risultato,xx,yy,x,y,st,immag)
    colora(xx,yy,immag,color='blue')
    save(immag,fname1)
    return risultato
    
def trova(xx,yy,x,y,fermo,st,immag):
    ap=True
    fine=''
    try:
        if (condizione(xx,yy,x,y,immag)==True):
            st,x,y,error=ruota_verso(st,x,y)
            if error=='ERRORE':
                fine='ERRORE'
            ap=False
    except IndexError:
        st,x,y,error=ruota_verso(st,x,y)
        if error=='ERRORE':
            fine='ERRORE'
        ap=False
    fermo+=1
    return immag,ap,fermo,x,y,st



def condizione(xx,yy,x,y,immagine):
    mod_y=somma(yy,y)
    mod_x=somma(xx,x)
    if immagine[mod_x][mod_y]==(0,255,0) or immagine[mod_x][mod_y]==(255,0,0) or mod_x<0 or mod_y<0:
        return True
    else:
        return False


def somma(x,y):
    cont=0
    cont=x+y
    return cont
    
def ruota_verso(verso,x,y):
    q=40
    neg_q=-40
    z=0
    error=''
    if verso==3:
        verso=0
        x=z
        y=q
        return verso,x,y,error
    elif verso==1:
        verso=2
        x=z
        y=neg_q
        return verso,x,y,error
    elif verso==0:
        verso=1
        x=q
        y=z
        return verso,x,y,error
    elif verso==2:
        verso=3
        x=neg_q
        y=z
        return verso,x,y,error
    else:
        error='ERRORE'
        return verso,x,y,error



def colora(x,y,immag,color):
    q=40
    som_x=somma(x,q)
    som_y=somma(y,q)
    c=y
    while(x<som_x):
        y=c
        while(y<som_y):
            if color=='verde':
                immag[x][y]=(0,255,0)
                y+=1
            elif color=='blue':
                immag[x][y]=(0,0,255)
                y+=1
            else:
                break
        x+=1
        
def sposta(risultato,xx,yy,x,y,st,immag):
    fermo=0
    cont=''
    cont=str(st)
    risultato+=cont
    colora(xx,yy,immag,color='verde')
    som_x=somma(xx,x)
    som_y=somma(yy,y)
    return risultato,som_x,som_y,fermo
   
    

