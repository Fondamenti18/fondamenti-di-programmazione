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

import immagini

def cammino(fname,  fname1):
    '''Colora di verde le celle della scacchiera dove passa il robottino,
    colora di blu la cella dove si ferma'''
    rosso = (255,0,0)
    verde = (0,255,0)
    blu = (0,0,255)
    scacchiera = immagini.load(fname)
    x = 0
    y = 0
    passi = 0
    codPassi = ''
    lenColonne = len(scacchiera[0])
    lenRighe = len(scacchiera)
    
    
    while True:
        #Vai a destra
        while y + 40  < lenColonne and scacchiera[x][y + 40] != rosso and scacchiera[x][y + 40] != verde:
            passi += 1
            colora(scacchiera, x, y, verde)
            y += 40
            codPassi += '0'
        
        #Vai verso il basso
        while x + 40  < lenRighe and scacchiera[x + 40][y] != rosso and scacchiera[x + 40][y] != verde:
            passi += 1
            colora(scacchiera, x, y, verde)
            x += 40
            codPassi += '1'
        
        #Vai a sinistra
        while y - 40  >= 0 and scacchiera[x][y - 40] != rosso and scacchiera[x][y - 40] != verde:
            passi += 1
            colora(scacchiera, x, y, verde)
            y -= 40
            codPassi += '2'
        
        #Vai verso l'alto
        while x - 40  >= 0 and scacchiera[x - 40][y] != rosso and scacchiera[x - 40][y] != verde:
            passi += 1
            colora(scacchiera, x, y, verde)
            x -= 40  
            codPassi += '3'
            
        if passi == 0:
            break
        passi = 0
        
    colora(scacchiera, x, y, blu)
    
    immagini.save(scacchiera, fname1)
    return codPassi
            
        
                


def colora(scacchiera, x, y, colore):
    '''Colora il cubo del colore impostato'''
    scac = scacchiera
    for riga in range(x, x + 40):
        for colonna in range(y, y + 40):
            scac[riga][colonna] = colore
    return scac



            
    
