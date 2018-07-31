# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 00:40:22 2017

@author: Original Bomber
"""

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

from immagini import load, save

MOSSE = {0:(40, 0), 1:(0, 40), 2:(-40, 0), 3:(0, -40)} # associo i comandi alle variazioni di punti (x, y)
VERDE=(0, 255, 0)
ROSSO=(255, 0, 0)
BLU=(0, 0, 255)


def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    passaggi = []
    
    img = load(fname)
    lato=40
    # effettuo la prima mossa verso destra!
    draw_cella(img, 0, 0, lato, lato, VERDE)
    muovi(img, 40, 0, 0, 0, lato, passaggi)
    
    # salvo l'immagine
    save(img, fname1)
    
    return "".join(passaggi)

'''
Questa funzione esegue lo spostamento di un quadratino nella posizione mossa
Verifica che non ci siano ostacoli e quindi calcola le nuove coordinate del quadratino 
Nel caso di ostacoli prova a rotare di 90 rispetto all'ultima rotazione passata e richiama se stessa
Se rotazione = 270 rimango fermo ed esco dalla funzione
La funzione memorizza gli spostamenti nella stringa "passaggi'
'''

def muovi(img, x, y, mossa, rotazione, lato, passaggi):
        
    while True:
    
        if rotazione==360:
            # se sto su me stesso esco
            x, y = posizione_precedente(x, y, mossa)
            draw_cella(img, x, y, lato, lato, BLU)
            #print("rotato tutto esco")            
            break
        
        # controllo se la coordinata corrispondente all'angolo superiore sinistro del quadretto sia interna all'immagine
        if not inside(img, x, y) or img[y][x]==ROSSO or img[y][x]==VERDE: # FUORI AREA o ROSSO o VERDE provo a muovermi
           
            #print("Fuori area sono finito nella cella:", x, y)
    
            # imposto coordinate della cella da cui sono venuto
            x, y = posizione_precedente(x, y, mossa)
    
            if mossa == 3: mossa=0
            else: mossa+=1
    
            # non mi muovo e devo ruotare!
            rotazione+=90
    
            # calcolo le nuove coordinate del robottino continuando nell stessa direzione
            x=x+int(MOSSE[mossa][0])
            y=y+int(MOSSE[mossa][1])   
            #print("Fuori area provo la cella-->", x, y, "mossa:", mossa, "passaggi:", passaggi, "rotazione:",rotazione)
            continue
       
        # se sono qui vuol dire che mi sono potuto muovere, quindi disegno cella verde e aggiorno passaggi
        # NON HO TROVATO IMPEDIMENTI
        passaggi.append(str(mossa))
        # riazzero la rotazione
        rotazione=0
        # scrivo cella verde
        draw_cella(img, x, y, lato, lato, VERDE)
        #print("campo libero: sto nella cella", x, y, "e la disegno")
        # calcolo le nuove coordinate del robottino continuando nell stessa direzione
        x=x+int(MOSSE[mossa][0])
        y=y+int(MOSSE[mossa][1])            
    
        #print("proverò la cella-->", x, y, "mossa:", mossa, "passaggi:", passaggi, "rotazione:",rotazione)
        

def posizione_precedente(x, y, mossa):
    ''' Questa funzione ritorna la posizione precedente sulla base di mossa'''
    return x-int(MOSSE[mossa][0]), y-int(MOSSE[mossa][1])
    
    
def draw_cella(img, x, y, w, h, c):
    ''' Disegna su img un rettangolo
    con lo spigolo in alto a sinistra in (x, y), 
    larghezza w, altezza h e di colore c. VA in errore se il rettangolo 
    fuoriesce dall'immagine 
    messo controllo inside (se pixel è dentro o no immagine
    '''
    # per ogni riga del rettabgolo,
    for j in range(y, y+h):
        # per ogni colonna i della riga j
        for i in range(x, x+w):
            # imposta il colore c solo se pixel è dentro immagine
            if inside(img, i, j):
                img[j][i] = c        
    
def inside(img, x, y):
    '''Verifica se il pixel di coordinate x,y è contenuto nella immagine'''
    return 0 <= x < width(img) and 0 <= y < height(img)

def width(img):
    return len(img[0]) # è la prima riga mi da le colonne e dunque la larghezza

def height(img):
    return len(img) # numero di righe quindi l'altezza della matrice
   
if __name__ == '__main__':
    args        = ('I1.png','t1.png')
    #args        = ('I2.png','t2.png')
    #args        = ('I3.png','t3.png')
    #args       = ('I4.png','t4.png')
    ret=cammino(*args)
    print(ret)
