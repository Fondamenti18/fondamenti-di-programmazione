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
'''

from immagini import *

def quad(img,x, y, PV, c):
    for k in range(x, x+PV):
        for z in range(y, y+PV):
            img[k][z] = c
    


'''def matrice(fname):
    img=load(fname)
    PO=0
    col=img[0][0]
    img1=[]
    for y in range(len(img)): 
        if img[0][y]==col:
            PO+=1
        else: break
    for y1 in range(len(img)//PO):
        appo=[]
        for x1 in range(len(img[0])//PO): 
            appo+=[img[PO*y1][PO*x1]]
        img1.append(appo)
    save(img1,'matrice.png')
    return img1, PO'''
    
def matrice(fname):
    img=load(fname)
    img1=[]
    for y1 in range(15):
        appo=[]
        for x1 in range(15): 
            appo+=[img[40*y1][40*x1]]
        img1.append(appo)
    save(img1,'matrice.png')
    return img1
            

def cammino(fname,fname1):
    img=matrice(fname)
    l=40
    s=''
    x=0
    y=0
    img[x][y]=(0, 255, 0)
    imgfin=load(fname)
    quad(imgfin,x,y,l,(0, 255, 0))
    
    while img[x][y]!=(0,0,255):
        a=0
        while y<len(img)-1:
            if img[x][y+1]==(255, 0, 0) or img[x][y+1]==(0, 255, 0):

                break
            y+=1
            s+='0'
            img[x][y]=(0,255,0)
            quad(imgfin,x*l,y*l,l,(0,255,0))
            a+=1
            
        while x<len(img[0])-1:
            if img[x+1][y]==(255, 0, 0) or img[x+1][y]==(0, 255, 0):
                break
            s+='1'
            x+=1
            img[x][y]=(0,255,0)
            quad(imgfin,x*l,y*l,l,(0,255,0))
            a+=1
            
        while y>0:
            if img[x][y-1]==(255, 0, 0) or img[x][y-1]==(0, 255, 0):
                break
            a+=1
            s+='2'
            y-=1
            img[x][y]=(0,255,0)
            quad(imgfin,x*l,y*l,l,(0,255,0))
            
        while x>0:
            if img[x-1][y]==(255, 0, 0) or img[x-1][y]==(0, 255, 0):
                break
            a+=1
            x-=1
            s+='3'
            img[x][y]=(0,255,0)
            quad(imgfin,x*l,y*l,l,(0,255,0))
            
        if a==0:
            img[x][y]=(0,0,255)
            quad(imgfin,x*l,y*l,l,(0,0,255))
    save(imgfin,fname1)
    
    return s
