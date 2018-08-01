
from immagini import *

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

DESTRA=0
SINISTRA=2
SOTTO=1
SOPRA=3

def coloraCella(img,x,y,colore):
    for riga in range(y,y+40):
        for colonna in range(x,x+40):
            img[riga][colonna]=colore
    return img

def possoAndare(img, riga, colonna, senso,altezza,larghezza):
        if(senso==DESTRA):
            if colonna + 40 < larghezza and img[riga][colonna+40]!=RED and img[riga][colonna+40]!=GREEN:
                return True
        elif(senso==SOTTO):
            if riga+40<altezza and img[riga+40][colonna]!=RED and img[riga+40][colonna]!=GREEN:
                return True

        elif(senso==SINISTRA):
            if colonna-40>= 0 and img[riga][colonna-40]!=RED and img[riga][colonna-40]!=GREEN:
                return True
               
        elif(senso==SOPRA):
            if riga-40>=0 and img[riga-40][colonna]!=RED and img[riga-40][colonna]!=GREEN:
                return True
            
def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    img=load(fname)
    img=coloraCella(img,0,0,GREEN)
    
    senso = DESTRA
    mosse=[]
    riga=0
    colonna=0
    contatore = 0
    altezza=len(img)
    larghezza=len(img[0])
    while contatore<4:
        if(possoAndare(img,riga,colonna,senso,altezza,larghezza)):
           contatore=0
           mosse.append(senso)
           if(senso==DESTRA):
               img=coloraCella(img,colonna+40,riga,GREEN)
               colonna+=40
           elif(senso==SOTTO):
               img=coloraCella(img,colonna,riga+40,GREEN)
               riga+=40
           elif(senso==SINISTRA):
               img=coloraCella(img,colonna-40,riga,GREEN)
               colonna-=40
           elif(senso==SOPRA):
               img=coloraCella(img,colonna,riga-40,GREEN)
               riga-=40
        else:
           senso=(senso+1)%4
           contatore+=1
           
    coloraCella(img,colonna,riga,BLUE)
    save(img,fname1)
    return "".join(str(n) for n in mosse)

