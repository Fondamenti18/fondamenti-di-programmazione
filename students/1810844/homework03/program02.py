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

def controlla(matrice,posx,posy,dirO,dirV):
    
    libera = False
    seq = ""
    #se è rivolto verso destra
    if dirO == 1 and posx != 14:
        a = matrice[posy*40][(posx+dirO)*40]
        #print(a)
        if a == (0,0,0) or a == (255,255,255):
            libera = True
            seq += "0"
            #print("libero a destra")
    #se è rivolto verso sinistra
    elif dirO == -1 and posx != 0:
        a = matrice[posy*40][(posx+dirO)*40]
        if a == (0,0,0) or a == (255,255,255):
            libera = True
            seq += "2"
    #se è rivolto verso giu
    elif dirV == 1 and posy != 14:
        a = matrice[(posy+dirV)*40][posx*40]
        if a == (0,0,0) or a == (255,255,255):
            libera = True
            seq += "1"
    #se è rivolto verso su
    elif dirV == -1 and posy != 0:
        a = matrice[(posy+dirV)*40][posx*40]
        if a == (0,0,0) or a == (255,255,255):
            libera = True
            seq += "3"
    return libera,seq

def colora_verde(matrice,x,y):
    for i in range(0,40):
        for j in range(0,40):
            matrice[i+(y*40)][j+(x*40)] = (0,255,0)
    return matrice
            
def colora_blu(matrice,x,y):
    for i in range(0,40):
        for j in range(0,40):
            matrice[i+(y*40)][j+(x*40)] = (0,0,255)
    return matrice

def vai(posx,posy,dirO,dirV):
    posx += dirO
    posy += dirV
    return posx,posy

def gira(dirO,dirV):
    #print("gira")
    if dirO != 0:
        dirV = dirO
        dirO = 0
    else:
        dirO = dirV*(-1)
        dirV = 0
    return dirO,dirV

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    posx = 0
    posy = 0
    gradi = 0
    dirO = 1
    dirV = 0
    sequenza = ""
    matrice = load(fname)
    fermo = False
    
    while fermo == False:
        if gradi != 360:
            var = controlla(matrice,posx,posy,dirO,dirV)
            if var[0] == False:
                dirO,dirV = gira(dirO,dirV)
                gradi += 90
            else:
                matrice = colora_verde(matrice,posx,posy)
                posx,posy = vai(posx,posy,dirO,dirV)
                gradi = 0
                sequenza += var[1]
        else:
            matrice = colora_blu(matrice,posx,posy)
            fermo = True
    
    save(matrice,fname1)
    
    
    return sequenza