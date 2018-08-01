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
        
def prossimacaselladestra(a,b,im):
    x1 = a + 40
    y1 = b
    casella = ()
    if (x1 < len(im) and x1 >= 0):
        casella = (im[y1][x1])
    return casella

def prossimacasellasinistra(a,b,im):
    x1 = a - 40
    y1 = b
    casella = ()
    if (x1 < len(im) and x1 >= 0):
        casella = (im[y1][x1])
    return casella

def prossimacasellasotto(a,b,im):
    x1 = a
    y1 =b + 40
    casella = ()
    if (y1 < len(im) and y1 >= 0):
        casella = (im[y1][x1])
    return casella

def prossimacasellasopra(a,b,im):
    x1 = a
    y1 =b - 40
    casella = ()
    if (y1 < len(im) and y1 >= 0):
        casella = (im[y1][x1])
    return casella

def checkprosscasella(x0,y0,rot,im):
    prosscas = ()
    col = ''
    if rot == 0:
        prosscas = prossimacaselladestra(x0,y0,im)
        if len(prosscas) != 0:
            col = colori(prosscas)
    if rot == 90:
        prosscas = prossimacasellasotto(x0,y0,im)
        if len(prosscas) != 0:
            col = colori(prosscas)
    if rot == 180:
        prosscas = prossimacasellasinistra(x0,y0,im)
        if len(prosscas) != 0:
            col = colori(prosscas)
    if rot == 270:
        prosscas = prossimacasellasopra(x0,y0,im)
        if len(prosscas) != 0:
            col = colori(prosscas)
    return col
        
    
    

def movimento(x0,y0,rotazione,movimenti):
    x1 = 0
    y1 = 0
    if rotazione == 0:
        x1 += x0 + 40
        y1 = y0
        movimenti.append('0')
    if rotazione == 90:
        x1 = x0
        y1 += y0 + 40
        movimenti.append('1')
    if rotazione == 180:
        x1 = x0 - 40
        y1 = y0
        movimenti.append('2')
    if rotazione == 270:
        x1 = x0
        y1 = y0 - 40
        movimenti.append('3')
    return x1,y1,movimenti
        
def rotazione(rot,fermo):
    if rot < 270:
        rot += 90
    else:
        rot = 0
    fermo +=1
    return rot,fermo
    
def colori(col):
    colore = ''
    if col == (255,0,0):
        colore = 'rosso'
    elif col == (0,255,0):
        colore = 'verde'
    else:
        colore = 'colore'
    return colore

def riempimento(posizione,colore,im):
    if colore == 'verde':
        for y in range(posizione[1]-1, posizione[1]-1 + 40):
            for x in range(posizione[0]-1, posizione[0]-1 + 40):
                im[y][x] = (0,255,0)
    if colore == 'blu':
        for y in range(posizione[1]-1, posizione[1]-1 + 40):
            for x in range(posizione[0]-1, posizione[0]-1 + 40):
                im[y][x] = (0,0,255)
    return im
    
def percorso(immagine):
    mov = True
    movimenti = []
    x0 = 1
    y0 = 1
    rot = 0
    fermo = 0
    col = ''
    while mov == True:
        col = checkprosscasella(x0,y0,rot,immagine)
        if col != 'rosso' and col != 'verde':
            if col != '':
                immagine = riempimento((x0,y0),'verde',immagine)
                x0,y0,movimenti = movimento(x0,y0,rot,movimenti)
                fermo = 0
            else:
                if fermo < 4:
                    rot,fermo = rotazione(rot,fermo)
                else:
                    mov = False
        else:
            if fermo < 4:
                rot,fermo = rotazione(rot,fermo)
            else:
                mov = False
    immagine = riempimento((x0,y0),'blu',immagine)
    return movimenti,immagine
        
        

def cammino(fname,  fname1):
    f = load(fname)
    movimenti = []
    movimenti,immagine = percorso(f)
    save(immagine,fname1)
    return ''.join(movimenti)
    

