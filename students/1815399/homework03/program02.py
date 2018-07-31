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
verde=(0,255,0)
rosso= (255,0,0)
blu=(0,0,255)


def cammino(fname,  fname1):
    direzione= 0
    img=load(fname)
    movimenti=''
    passo=''
    draw_rect(img,0,0,40,40,verde)
    x=0
    y=0
    while direzione< 360:
        
        
        if passo == '' or passo[-1] == '3' and direzione<360:
           
           
           movimenti,passo,x,img,direzione=destra(img,x,y,movimenti,passo)
          
           
        elif passo[-1] == '0' and direzione<360:
           
           
           movimenti,passo,y,img,direzione=basso(img,x,y,movimenti,passo)
           
        elif passo[-1] == '1' and direzione<360:
           
           
           movimenti,passo,x,img,direzione=sinistra(img,x,y,movimenti,passo)
          
        elif passo[-1]== '2' and direzione<360:
            
            
            movimenti,passo,y,img,direzione=alto(img,x,y,movimenti,passo)
            
    else:
       
        img=draw_rect(img,y,x,40,40,blu)
            
          
        
    
        
    
    save(img,fname1)
    return movimenti

def draw_rect(img,x,y,w,h,c):
    for px in range(x,x+w):
        for py in range(y,y+h):
            if inside (img,px,py):
                img[px][py] = c
    return img            
def inside(img,x,y,):
    return 0<=y<len(img) and 0<=x< len(img[0])                 

def destra(img,x,y,movimenti,passo):
    global direzione
    if x+40 == len(img[0]):
        passo+='0' 
        direzione+=90
    elif img[y][x+40] == rosso or img[y][x+40] == verde:
        passo+='0' 
        direzione+=90 
    else:
        direzione=0
        while (img[y][x] != rosso or img[y][x] != verde):
            
            x+=40
            passo+='0'
            img=draw_rect(img,y,x,40,40,verde)
            movimenti+='0'
            if x+40 == len(img[0]):
                break
            elif img[y][x+40] == rosso or img[y][x+40] == verde :
                break
                
            
    return movimenti,passo,x,img,direzione 
def basso(img,x,y,movimenti,passo):
    global direzione
    if y+40 == len(img):
        passo+='1'
        direzione+=90
    elif img[y+40][x] == rosso or img[y+40][x] == verde:
        passo+='1'
        direzione+=90
    else:
        direzione=0
        while img[y][x] != rosso or img[y][x] != verde:
            
            y+=40
            passo+='1'
            img=draw_rect(img,y,x,40,40,verde)
            movimenti+='1'
            if y+40 == len(img):
                break
            elif img[y+40][x] == rosso or img[y+40][x] == verde:
                break
            
    return movimenti,passo,y,img,direzione
def sinistra(img,x,y,movimenti,passo):
    global direzione
    if x==0:
       passo+='2'
       direzione+=90
    elif img[y][x-40] == rosso or img[y][x-40] == verde:
        passo+='2'
        direzione+=90
    else:
        direzione=0
        while (img[y][x] != rosso or img[y][x] != verde):
            
            x-=40
            passo+='2'
            direzione=0
            img=draw_rect(img,y,x,40,40,verde)
            movimenti+='2'
            if x == 0:
                break
            elif img[y][x-40] == rosso or img[y][x-40] == verde:
                break
            
    return movimenti,passo,x,img,direzione
def alto(img,x,y,movimenti,passo):
    global direzione
    if y-40 == 0:
        passo+='3'
        direzione+=90
    elif img[y-40][x] == rosso or img[y-40][x] == verde:
        passo+='3'
        direzione+=90
    else:
        direzione=0    
        while (img[y][x] != rosso or img[y][x] != verde):
            y-=40
            
            passo+='3'
            img=draw_rect(img,y,x,40,40,verde)
            movimenti+='3'
            if y==0:
                break
            elif img[y-40][x] == rosso or img[y-40][x] == verde:
                break
            
    return movimenti,passo,y,img,direzione