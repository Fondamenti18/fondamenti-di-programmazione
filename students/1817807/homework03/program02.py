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

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    ac = ''
    em = 0
    y =0
    x= 0
    so = load(fname)
    
    def its2(x):
        return 0 <= x <= 559
    
    def its3(y):
        return 0 <= y <= 520
    
    def its4(x):
        return 40 <= x <= 600
    
    def its(x, y):
        return 0 <= x <= 600 and 0 <= y <= 600
    
    while em<4:
        
        while its2(x) and so [y][x+40] != (255,0,0) and so [y][x+40] != (0,255,0):
            
            for va in range(x, x+40):
                for da in range(y, y+40):
                    so[da][va] = (0,255,0)
            x+=40
            ac+= '0'
        em +=1
        
        while its3(y) and so [y+40][x] != (255,0,0) and so [y+40][x] != (0,255,0):
            
            for va in range(x, x+40):
                for da in range(y, y+40):
                    so[da][va] = (0,255,0)
            y+=40
            ac+= '1'
        em +=1
        
        while its4(x) and so [y][x-40] != (255,0,0) and so [y][x-40] != (0,255,0):
            em=0
            
            for va in range(x, x+40):
                for da in range(y, y+40):
                    so[da][va] = (0,255,0)
            x-=40
            ac+= '2'
        em +=1
        
        while its(x,y) and so [y-40][x] != (255,0,0) and so [y-40][x] != (0,255,0):
            em=0
            
            for va in range(x, x+40):
                for da in range(y, y+40):
                    so[da][va] = (0,255,0)
                y -=40
            ac+= '3'
        em +=1
    
    else:
        
        em = 0
        for va in range(x,x+40):
            for da in range (y, y+40):
                so[da][va] = (0,0,255)
    
    save(so, fname1)
    return ac