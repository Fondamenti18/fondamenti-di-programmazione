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
    global sequenza
    sequenza=""
    img=load(fname)
    run(img)
    save(img,fname1)
    return sequenza

sequenza=""

#Gestisce il percorso
def run(img):
    global sequenza
    x=0
    y=0
    direction=0 #Direzione 0,1,2,3
    stop=False
    while stop==False:
            colorCell(img,x,y,(0,255,0))
            direction,x,y,stop=controlMove(img,x,y,direction)
            sequenza+=str(direction) if direction!=-1 else ""
    #Colora l'ultima cella
    colorCell(img,x,y,(0,0,255))
    return

#Colora l'intera cella
def colorCell(img,x,y,c):
    for h in range(y,y+40):
        for w in range(x,x+40):
            img[h][w]=c
    return

def controlMove(img,x,y,d):
    #Contiene le direzioni in ordine di esecuzione
    directions=[(y,x+40),(y+40,x),(y,x-40),(y-40,x)]
    #(y,x) di direzione d
    xy=(directions[d][0],directions[d][1])
    
    #Controlla se si può continuare nella direzione d
    try:
        if img[xy[0]][xy[1]]!=(255,0,0) and img[xy[0]][xy[1]]!=(0,255,0) and xy[0]>=0 and xy[1]>=0:
            return d,directions[d][1],directions[d][0],False
    except IndexError:#Fuori dall'immagine
        pass
    
    #Scorre la lista per controllare altre direzioni (in senso orario)
    for v in directions[d:]:
        i=directions.index(v)
        #if i==d:
        #    continue
        try:
            if img[directions[i][0]][directions[i][1]]!=(255,0,0) and img[directions[i][0]][directions[i][1]]!=(0,255,0) and directions[i][0]>=0 and directions[i][1]>=0 and i!=d:
                return i,directions[i][1],directions[i][0],False
        except IndexError:#Fuori dall'immagine
            pass
    for v in directions[:d]:
        i=directions.index(v)
        #if i==d:
        #    continue
        try:
            if img[directions[i][0]][directions[i][1]]!=(255,0,0) and img[directions[i][0]][directions[i][1]]!=(0,255,0)and directions[i][0]>=0 and directions[i][1]>=0 and i!=d:
                return i,directions[i][1],directions[i][0],False
        except IndexError:
            pass
    return -1,x,y,True
