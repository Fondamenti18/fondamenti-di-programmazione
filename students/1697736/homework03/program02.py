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
import png

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
    """ Salva la immagine img  nel file filename in formato PNG8.
        Img e' una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)

def inside(img, i, j):
    '''Ritorna True se il pixel (i, j) e' dentro l'immagine img, False
    altrimenti'''
    w, h = len(img[0]), len(img)
    return 0 <= i < w and 0 <= j < h

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    scacchiera = load(fname)
    stringa_dir = '' 
    direzione = 0
    startX = 0
    startY = 0
    giri = 0
    while giri<4:
        giri2=giri
    
        startX2 = startX
        startY2 = startY
        if(direzione == 0):
            startX += 40
        elif(direzione == 1):
            startY += 40
        elif(direzione == 2):
            startX -= 40
        elif(direzione == 3):
            startY -= 40
        
        if inside(scacchiera, startX, startY) == False:
            giri += 1
            direzione += 1
            
            if(direzione == 4):
                direzione = 0
            
            
            startX = startX2
            startY = startY2
                
            if(giri == 4):
                for y in range(startY,startY+40):
                    for x in range(startX,startX+40):
                        scacchiera[y][x] = (0,0,255)
            
        else:
            if(scacchiera[startY][startX] == (255,0,0) or scacchiera[startY][startX] == (0,255,0)):
                startX = startX2
                startY = startY2
                direzione += 1
                giri += 1
                if direzione == 4:
                    direzione = 0
                if(giri == 4):
                    for y in range(startY,startY+40):
                        for x in range(startX,startX+40):
                            scacchiera[y][x] = (0,0,255)
            else:
                for y in range(startY2,startY2+40):
                    for x in range(startX2,startX2+40):
                        scacchiera[y][x] = (0,255,0)
                giri = 0
                stringa_dir += str(direzione)
                        
        
               
    save(scacchiera, fname1)
    
    return stringa_dir