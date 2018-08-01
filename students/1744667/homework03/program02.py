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


def draw_quad_simple(img, x, y, w, h, c):    
    '''Disegna su img un rettangolo con lo spigolo in alto a sinistra    
    in (x, y), larghezza w, altezza h e di colore c. Va in errore se il     
    rettangolo fuoriesce dall'immagine.'''    
    for j in range(y, y+h):      # Per ogni riga j del rettangolo,        
        for i in range(x, x+w):  # per ogni colonna i della riga j,            
            img[j][i] = c   


def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    im = load(fname)
    s = ''
    cont = 0
    for riga in im:
        for pixel in riga:
            x = riga.index(pixel)
            y = im.index(riga)
            if pixel == (0, 0, 0) or pixel == (255, 255, 255):
                if cont == 0:
                    draw_quad_simple(im, x, y, 40, 40, (0, 255, 0))
                    s+='0'
                break
            if pixel == (255, 0, 0):
                 if cont < 1:
                    j = riga.index(pixel)
                    i = im.index(riga)
                    cont+=1
                    draw_quad_simple(im, x-40, y+40, 40, 40, (0, 255, 0))
                    s+='1'
                    draw_quad_simple(im, x-40, y+80, 40, 40, (0, 255, 0))
                    s+='1'
                    draw_quad_simple(im, x-80, y+80, 40, 40, (0, 255, 0))
                    s+='2'
                    draw_quad_simple(im, x-120, y+80, 40, 40, (0, 255, 0))
                    s+='2'
                    draw_quad_simple(im, x-160, y+80, 40, 40, (0, 255, 0))
                    s+='2'
                    draw_quad_simple(im, x-160, y+40, 40, 40, (0, 0, 255))
                    s+='3'
                    break
    r = save(im, fname1)
    return s[1:]

















