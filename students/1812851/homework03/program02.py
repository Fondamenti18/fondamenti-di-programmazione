'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra (x crescente). 
Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o verticale. 
Le regole di movimento del robottino sono le seguenti: 
- al generico step, si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci e' gia transitato in passato. 
- se invece la cella risulta occupata o e' una cella su cui ha gia transitato, ruota di 90 gradi in senso orario ed aspetta lo step successivo. 
- dopo aver ruotato  di 360 gradi senza essere riuscito a spostarsi si ferma. 

Progettare la funzione  percorso(fname, fname1) che presi in input:
- il percorso di un file (fname) contenente l'immagine in formato .png di una scacchiera con ostacoli
- il percorso di un file di tipo .png (fname1) da creare
legge l'immagine della scacchiera in fname, colora di verde le celle della scacchiera percorse dal robottino prima di fermarsi, 
colora di blu la cella in cui il robottino si ferma e registra l'immagine ricolorata nel file fname1. 
Inoltre restituisce una stringa dove in sequanza sono codificati i passi effettuati dal robottino prima di fermarsi. 
La codifica e' a seguente: 
    '0' per un passo verso destra (x crescenti)
    '1' per un passo verso il basso (y crescenti)
    '2' per un passo verso sinistra (x decrescenti)
    '3' per un passo verso l'alto (y decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt 

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)

Image()
'''

from IPython.display import Image
from immagini import *



global blue
global red
global green
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)

def cammino(fname,  fname1):
    percorso=''
    percmod=[]
    img=[]
    imgris=[]
    img=load(fname)
    
    dir=0
    x=0
    y=0
    flag=0
    #while flag==0:
    while flag==0:
        (dir,y,x)=checkdirsucc(dir,y,x,img,percmod)
        print(dir,y,x)
        if dir!='s':
            
            #imgris=coloracasella(y,x,(0,255,0),percmod)
            percorso+=str(dir) 
            percmod=convertitore(percorso)
        else:
            flag=1
    #save(imgris,'prova2.png')
    percorso=percorso[0:-1]
    return percorso#,percmod

'''
def checkdirsucc(x,y,dir,img):
    blue=(0,0,255)
    red=(255,0,0)
    green=(0,255,0)
    lenquad=40
    lentot=len(img)
    for i in range(3):
        if dir==0:  #0 1,3    
            xmod=x+lenquad    #x+40  y
            ymod=y
        
        if dir==1:  #1 2,0  
            xmod=x            #x     y+40
            ymod=y+lenquad    
    
        if dir==2:  #2 3,1  
            xmod=x-lenquad    #x-40  y    
            ymod=y
        if dir==3:  #3 0,2
            xmod=x            #x     y-40
            ymod=y-lenquad 
        print(x,y)
        if xmod<(lentot-1) and ymod<(lentot-1):
            if img[xmod][ymod]!=(red) or img[xmod][ymod]!=(green):
                return dir
        if i==1:
            dir=dir+1
        if i==2:
            dir=dir+2
        if dir==4:
            dir=0
        if dir==5:
            dir=1
    return 0
'''    

def checkdirsucc(dir,y,x,img,percmod):
    #lenquad=40
    #lentot=len(img)
    if dir == 0:
        risdx,y,x=checkdx(y,x,img,percmod)
        if risdx == 1:
            return 0,y,x
        rissx,y,x=checkdown(y,x,img,percmod)
        if rissx == 1:
            return 1,y,x
        risup,y,x=checkup(y,x,img,percmod)
        if risup == 1:
            return 3,y,x
    if dir==1:
        risdown,y,x=checkdown(y,x,img,percmod)
        if risdown==1:
            return 1,y,x
        rissx,y,x=checksx(y,x,img,percmod)
        if rissx==1:
            return 2,y,x
        risdx,y,x=checkdx(y,x,img,percmod)
        if risdx==1:
            return 0,y,x
    if dir==2:
        rissx,y,x=checksx(y,x,img,percmod)
        if rissx==1:
            return 2,y,x
        risup,y,x=checkup(y,x,img,percmod)
        if risup==1:
            return 3,y,x
        risdown,y,x=checkdown(y,x,img,percmod)
        if risdown==1:
            return 1,y,x
    if dir==3:
        risup,y,x=checkup(y,x,img,percmod)
        if risup==1:
            return 3,y,x
        risdx,y,x=checkdx(y,x,img,percmod)
        if risdx==1:
            return 0,y,x
        rissx,y,x=checksx(y,x,img,percmod)
        if rissx==1:
            return 2,y,x
    print('arrivato allo stop')
    return 's',y,x

def checkdx(y,x,img,percmod):                    #return 0 not ok; 1 ok
    xmod=x+40 
    ymod=y
    #print(x,y)
    if xmod<0 or xmod>599 or ymod<0 or xmod>599:   #punti fuori dall'immagine
        return 0,y,x
    if img[ymod][xmod]==red or (ymod,xmod)in percmod:
        #print(x,img[y][x])
        return 0,y,x
    return 1,ymod,xmod
    
def checkdown(y,x,img,percmod):
    ymod=y+40
    xmod=x
    if xmod<0 or xmod>599 or ymod<0 or xmod>599:   #punti fuori dall'immagine
        return 0,y,x
    if img[ymod][xmod]==red or (ymod,xmod)in percmod:
        #print(x,img[y][x])
        return 0,y,x
    return 1,ymod,xmod

def checksx(y,x,img,percmod):
    xmod=x-40
    ymod=y
    #print(x,y)
    #print(xmod,ymod)
    if xmod<0 or xmod>599 or (ymod,xmod)in percmod:   #punti fuori dall'immagine
        return 0,y,x
    if img[ymod][xmod]==red or img[ymod][xmod]==green:
        #print(x,y,x,img[y][x])
        return 0,y,x
    return 1,ymod,xmod

def checkup(y,x,img,percmod):
    ymod=y-40
    xmod=x
    if xmod<0 or xmod>599 or (ymod,xmod)in percmod:   #punti fuori dall'immagine
        return 0,y,x
    if img[ymod][xmod]==red or img[ymod][xmod]==green:
        #print(imgris[ymod][xmod])
        return 0,y,x
    return 1,ymod,xmod

def coloracasella(y,x,c,img):
    for i in range(40):
        for l in range(40):
            #print(y+i,x+i)
            img[y+i][x+l]=c
    return img
            
def convertitore(st):
    st=str(st)
    x=0
    y=0
    ris=[]
    for i in range(len(st)):
        if st[i]=='0':
            x+=40
        if st[i]=='1':
            y+=40
        if st[i]=='2':
            x-=40
        if st[i]=='3':
            y-=40
        ris.append((y,x))
    return ris

'''def creaminitab(fname):
    img=load(fname)
    ris=crealistaliste(15,15)
    for i in range(l):
        for l in range(h):
            ris[i][l]=img[i*40][l*40]
    return ris

def crealistaliste(l,h):
    mod=[]
    ris=[]
    for i in range(l):
        for l in range(h):
            mod.append('0')
        ris.append(mod)
        mod=[]
    return print(ris)

'''
'''
ris=[]
for i in range(3):
    ris.append(mod)
    mod=[]
    for l in range(3):
        mod.append(0)
        '''