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

scacchiera = []

coordinate = []

direzionecorrente = 0

def colora(cx, cy, colore = (0, 255, 0)):
    
    global scacchiera
    
    for x in range(cx, cx + 40):
        
        for y in range(cy, cy + 40):
            
            scacchiera[y][x] = colore

def prossimacella(cx, cy, direzionecorrente, numerocambidirezione):
    
    global scacchiera
    
    if numerocambidirezione == 4:
        
        return -1, -1, -1, False
    
    ix, iy = calcolaipotetichecoordinate(cx, cy, direzionecorrente)   
    
    if ix >= 0 and iy >= 0 and ix <= 599 and iy <= 599:
        
        #print("ix", ix , " iy", iy)
        
        #print("Colore cella:", scacchiera[iy][ix])
        
        if scacchiera[iy][ix] == (0, 0, 0) or scacchiera[iy][ix] == (255, 255, 255):
        
            return ix, iy, direzionecorrente, True
        
        else:
            
            return prossimacella(cx, cy, cambiadirezione(direzionecorrente), numerocambidirezione = numerocambidirezione + 1)

    else:
    
        return prossimacella(cx, cy, cambiadirezione(direzionecorrente), numerocambidirezione = numerocambidirezione + 1)
    
        
def cambiadirezione(direzionecorrente):
    
    if direzionecorrente == 3:
        
        return 0
    
    else:
        
        return direzionecorrente + 1
    

def calcolaipotetichecoordinate(cx, cy, direzionecorrente):

    if direzionecorrente == 0:
        
        cx += 40
        
    if direzionecorrente == 1:
        
        cy += 40
        
    if direzionecorrente == 2:
        
        cx -= 40
        
    if direzionecorrente == 3:
        
        cy -= 40
        
    return cx, cy
            
            
def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    
    global scacchiera
    
    global direzionecorrente
    
    percorso = ""
    
    global coordinate
    
    scacchiera = load(fname)
    
    colora(0, 0)
    
    lx, ly = (0, 0)
    
    coordinate.append((0, 0))
    
    cx, cy, direzionecorrente, possomuovermi = prossimacella(0, 0, direzionecorrente, 0)
    
    while possomuovermi == True:
        
        percorso = percorso[:] + str(direzionecorrente)
        
        colora(cx, cy)
        
        lx, ly = cx, cy
        
        coordinate.append((cx, cy))
        
        #print(coordinate)
        
        cx, cy, direzionecorrente, possomuovermi = prossimacella(cx, cy, direzionecorrente, 0)
        
        
        
    colora(lx, ly, (0, 0, 255))    
        
        
    save(scacchiera, fname1)
    
    
        
    return(percorso)
        