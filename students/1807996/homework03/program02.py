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
from immagini import*

def direzione(img,i,x):
    blue=(0,0,255)
    verde=(0,255,0)
    bianco=(255, 255, 255) 
    nero=(0,0,0)
    direzione=''
    verso=''
    while direzione!='stop':    
        m=0
        while x>39 and (img[i][x-40]==bianco or img[i][x-40]==nero):
            x-=40
            m+=1
            verso+='2'
            draw_quad_simple(img,i,x,verde)
        while i >39 and (img[i-40][x]==bianco or img[i-40][x]==nero):
            i-=40
            m+=1
            verso+='3'
            draw_quad_simple(img,i,x,verde)
        while x<551 and (img[i][x+40]==bianco or img[i][x+40]==nero): 
            x+=40
            m+=1
            verso+='0'
            draw_quad_simple(img,i,x,verde)
        while i<551 and (img[i+40][x]==bianco or img[i+40][x]==nero):
            i+=40
            m+=1
            verso+='1'
            draw_quad_simple(img,i,x,verde)
        if m==0:
            draw_quad_simple(img,i,x,blue)
            direzione='stop'
    return verso

def cammino(fname,fname1):
    img=load(fname)
    x=0
    i=0
    verde=(0,255,0)
    draw_quad_simple(img,i,x,verde)
    verso=direzione(img,i,x)
    draw_quad_simple(img,0,0,verde)
    save(img,fname1)
    return verso

def draw_quad_simple( img,i, x,c):
    for j in range( i, i + 40):
        for i in range( x, x + 40): 
            img[j][ i] = c  
               
