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

def colorare_cella(img, w, h, c = (0, 255, 0)):
    '''ciclo per colorare una cella.'''
    for h1 in range(h, h+40):
        for w1 in range(w, w+40):
            img[h1][w1] = c

def camminare_avanti(img, w, h, sequenza):
    '''camminare in avanti.'''
    if w <= 560:
        if img[h][w] != (255, 0, 0) and img[h][w] != (0, 255, 0):
            colorare_cella(img, w, h)
            sequenza += '0'
            return camminare_avanti(img, w+40, h, sequenza)
        else:
            return w, h, sequenza
    else:
        return w, h, sequenza
    
def camminare_giu(img, w, h, sequenza):
    '''camminare verso il basso.'''
    if h <= 560:
        if img[h][w] != (255, 0, 0) and img[h][w] != (0, 255, 0):
            colorare_cella(img, w, h)
            sequenza += '1'
            return camminare_giu(img, w, h+40, sequenza)
        else:
            return w, h, sequenza
    else:
        return w, h, sequenza
    
def camminare_indietro(img, w, h, sequenza):
    '''camminare indietro.'''
    if w >= 0:
        if img[h][w] != (255, 0, 0) and img[h][w] != (0, 255, 0):
            colorare_cella(img, w, h)
            sequenza += '2'
            return camminare_indietro(img, w-40, h, sequenza)
        else:
            return w, h, sequenza
    else:
        return w, h, sequenza

def camminare_su(img, w, h, sequenza):
    '''camminare verso su.'''
    if h >= 0:
        if img[h][w] != (255, 0, 0) and img[h][w] != (0, 255, 0):
            colorare_cella(img, w, h)
            sequenza += '3'
            return camminare_su(img, w, h-40, sequenza)
        else:
            return w, h, sequenza
    else:
        return w, h, sequenza


def cammino(fname,  fname1):
    '''simulazione di un robot che cammina sulla scacchiera.'''
    sequenza = ''
    img = load(fname)
    
    w = -40
    h = -40
    lista_check_360 = []
    while (True):
        w, h, sequenza = camminare_avanti(img, w+40, h+40, sequenza)
        w, h, sequenza = camminare_giu(img, w-40, h+40, sequenza)
        w, h, sequenza = camminare_indietro(img, w-40, h-40, sequenza)
        w, h, sequenza = camminare_su(img, w+40, h-40, sequenza)
        
        lista_check_360.append([(w+40), (h+40), (w-40), (h-40)])
        if len(lista_check_360) > 1:
            if lista_check_360[0] != lista_check_360[1]:
                del lista_check_360[0]
            else:
                break
    
    h += 40
    colorare_cella(img, w, h, (0, 0, 255))
    
    save(img, fname1)
    return sequenza[1:]