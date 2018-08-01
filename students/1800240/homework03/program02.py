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

def controlla(img, x, y):
#Controlla se una casella il cui pixel in alto a sinistra ha coordinate (x, y) è libera.

    black = (  0,   0,   0)
    white = (255, 255, 255)  
     
    if 0 <= x < 600 and 0 <= y < 600:
        if img[x][y] == black or img[x][y] == white:
            return True
    else:
        return False

def colora(img,x,y,colore):
#Colora una casella il cui pixel in alto a sinistra ha coordinate (x, y). 
  
    for xi in range(x, x + 40):
        for yi in range(y, y + 40):
            img[xi][yi] = colore

def cammino(fname, fname1):
    
    img_og = load(fname)
    img_mod = img_og.copy()
    
    passi = ''
    
    green = (0, 255, 0)
    blue = (0, 0, 255)
    
    x = 0
    y = 0
    
    #Colora di verde la prima casella.
    colora(img_mod, 0, 0, green) 

    #Colora le caselle fin quando non ci sono piu caselle libere in nessuna direzione.
    while controlla(img_mod, x, y + 40) == True or controlla(img_mod, x + 40, y) == True or controlla(img_mod, x, y - 40) == True or controlla(img_mod, x - 40, y) == True:
        
        while controlla(img_mod, x, y + 40) == True:
            colora(img_mod, x, y + 40, green)
            passi += '0'
            y += 40
        while controlla(img_mod, x + 40, y) == True:
            colora(img_mod, x + 40, y, green)
            passi += '1'
            x += 40
        while controlla(img_mod, x, y - 40) == True:
            colora(img_mod, x, y - 40, green)
            passi += '2'
            y -= 40
        while controlla(img_mod, x - 40, y) == True:
            colora(img_mod, x - 40, y, green)
            passi += '3'
            x -= 40
            
    #Colora di blu la casella finale.    
    colora(img_mod, x, y, blue)
    
    save(img_mod, fname1)
    return passi
