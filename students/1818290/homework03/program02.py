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

from immagini import png

def cammino(fname,  fname1):
    imglist=load(fname)
    return controllo(imglist,fname1)



def controllo(imglist,fname1):
    lis=[]
    x=0
    y=0
    while dentro(imglist,x+40,y)==True and (imglist[y][x+40]==(0,0,0)or imglist[y][x+40]==(255,255,255))\
      or  dentro(imglist,x-40,y)==True and (imglist[y][x-40]==(0,0,0)or imglist[y][x-40]==(255,255,255))\
      or  dentro(imglist,x,y+40)==True and (imglist[y+40][x]==(0,0,0)or imglist[y+40][x]==(255,255,255))\
      or  dentro(imglist,x,y-40)==True and (imglist[y-40][x]==(0,0,0)or imglist[y-40][x]==(255,255,255)):
          while dentro(imglist,x+40,y)==True and (imglist[y][x+40]==(0,0,0)or imglist[y][x+40]==(255,255,255)):
              x=risxp(imglist,x,y,lis)
              lis.append('0')
          disegna(imglist,x,y,40,40,(0,255,0))
          while dentro(imglist,x,y+40)==True and (imglist[y+40][x]==(0,0,0)or imglist[y+40][x]==(255,255,255)):
              y=risyp(imglist,x,y,lis)
              lis.append('1')
          disegna(imglist,x,y,40,40,(0,255,0))        
          while dentro(imglist,x-40,y)==True and (imglist[y][x-40]==(0,0,0)or imglist[y][x-40]==(255,255,255)):
              x=risxn(imglist,x,y,lis)
              lis.append('2')
          disegna(imglist,x,y,40,40,(0,255,0))
          while dentro(imglist,x,y-40)==True and (imglist[y-40][x]==(0,0,0)or imglist[y-40][x]==(255,255,255)):
              y=risyn(imglist,x,y,lis)
              lis.append('3')
          disegna(imglist,x,y,40,40,(0,255,0))
          
    disegna(imglist,x,y,40,40,(0,0,255))
    save(imglist,fname1)
    return ''.join(lis)
    

def risxp(imglist,x,y,lis):
    disegna(imglist,x,y,40,40,(0,255,0))
    x+=40
    return x
    
def risxn(imglist,x,y,lis):
    disegna(imglist,x,y,40,40,(0,255,0))
    x-=40
    return x
    
def risyp(imglist,x,y,lis):
    disegna(imglist,x,y,40,40,(0,255,0))
    y+=40
    return y

def risyn(imglist,x,y,lis):
    disegna(imglist,x,y,40,40,(0,255,0))
    y-=40
    return y



    
def dentro(imglist,x,y):
    alt=len(imglist)
    lun=len(imglist[0])
    return 0 <= y < alt and 0 <=x <lun


def disegna(imglist,a,b,w,h,c):
    for coorx in range (a,a+w ):
        for coory in range(b, b+h):
            if dentro(imglist,coorx,coory):
                imglist[coory][coorx]=c
        
    
def load(fname):
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return img

def save(img, filename):
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)