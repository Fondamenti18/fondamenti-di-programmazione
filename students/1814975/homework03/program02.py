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


from immagini import *

def cammino(fname,  fname1):
    Implementare qui la funzione'''
    
def disegna_quad(quad,x,y,lato,colore):
    for i in range(lato):
        for j in range(lato):
                quad[y+j][x+i]=colore    
            
from immagini import *
def cammino(fname,fname1):
    img=load(fname)    
    xiniz=0
    yiniz=0
    dx=40
    dy=0
    stringa=''
    if img[yiniz][xiniz]==(0,0,0) or img[yiniz][xiniz]==(255,255,255):
            disegna_quad(img,xiniz,yiniz,40,(0,255,0))
    while ((0<=xiniz<600 and 0<=yiniz+40<600) and (img[yiniz+40][xiniz]==(0,0,0) or img[yiniz+40][xiniz]==(255,255,255))) or \
          ((0<=xiniz-40<600 and 0<=yiniz<600) and (img[yiniz][xiniz-40]==(0,0,0) or img[yiniz][xiniz-40]==(255,255,255))) or \
          ((0<=xiniz<600 and 0<=yiniz-40<600) and (img[yiniz-40][xiniz]==(0,0,0) or img[yiniz-40][xiniz]==(255,255,255))) or \
          ((0<=xiniz+40<600 and 0<=yiniz<600) and (img[yiniz][xiniz+40]==(0,0,0) or img[yiniz][xiniz+40]==(255,255,255))):
        xiniz += dx
        yiniz += dy
        if 0<=xiniz<600 and 0<=yiniz<600 and (img[yiniz][xiniz]==(0,0,0) or img[yiniz][xiniz]==(255,255,255)):
            disegna_quad(img,xiniz,yiniz,40,(0,255,0))
            if dx==40 and dy==0:
                stringa+='0'
            if dx==0 and dy==40:
                stringa+='1'
            if dx==-40 and dy==0:
                stringa+='2'
            if dx==0 and dy==-40:
                stringa+='3'    
        else:
            dpx=dx
            dpy=dy
            xiniz -=dx
            yiniz -=dy
            if dpx==40 and dpy==0:
                dx=0
                dy=40
            if dpx==0 and dpy==40:
                dx=-40
                dy=0
            if dpx==-40 and dpy==0:
                dx=0
                dy=-40
            if dpx==0 and dpy==-40:
                dx=40
                dy=0
    disegna_quad(img,xiniz,yiniz,40,(0,0,255))
    save(img,fname1)
    return stringa
#print(cammino('I5.png','mia.png')) 
    
    
    
    
    
    