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

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

def cammino(fname,  fname1):
    coord=(0,0)
    hop=40
    percorso=""
    scacchiera=load(fname)
    coord, percorso = movimento(coord[0],coord[1],percorso, scacchiera,hop,fname1)
    colora_blu(coord[0],coord[1],hop, scacchiera)
    save(scacchiera, fname1)
    return percorso
    
    
def movimento (x,y,percorso,scacchiera,hop,fname1):
    cambi_direz=0
    direzione=0
    while(cambi_direz<4):
        #print(x," ",y," ", direzione," ", cambi_direz)
        #print(valuta_mov(direzione,x,y,scacchiera,hop))
        if (valuta_mov(direzione,x,y,scacchiera,hop)):
            x,y=esegui_mov(direzione,x,y,scacchiera,hop)
            cambi_direz=0
            percorso=percorso+str(direzione)
        else:
            cambi_direz+=1
            direzione+=1
        if direzione==4:
            direzione=0        
    return (x,y) , percorso

def valuta_mov(direz,x,y,scacchiera,hop):
    if direz==0:    return destra(x,y,scacchiera,hop)
    if direz==1:    return giu(x,y,scacchiera,hop)
    if direz==2:    return sinistra(x,y,scacchiera,hop)
    if direz==3:    return su(x,y,scacchiera,hop)
    return False
    
def destra(x,y,scacchiera,hop): 
    if (x+hop<len(scacchiera[0]) and (scacchiera[y][x+hop]!=red) and (scacchiera[y][x+hop]!=green)):    
        return True
    return False
def giu(x,y,scacchiera,hop): 
    if (y+hop<len(scacchiera)-1 and (scacchiera[y+hop][x]!=red) and (scacchiera[y+hop][x]!=green)):     
        return True
    return False
def sinistra(x,y,scacchiera,hop):   
    if (x-hop>=0 and (scacchiera[y][x-hop]!=red) and (scacchiera[y][x-hop]!=green)):
        return True
    return False
def su(x,y,scacchiera,hop):
    if (y-hop>=0 and (scacchiera[y-hop][x]!=red) and (scacchiera[y-hop][x]!=green)):    
        return True
    return False

def esegui_mov(direz, x,y, scacchiera,hop):
    colora_verde(x,y,hop, scacchiera)
    if direz==0:    x+=hop
    if direz==1:    y+=hop
    if direz==2:    x-=hop
    if direz==3:    y-=hop
    return x,y

def colora_verde(x,y, hop, scacchiera):
    for a in range(y,y+hop,1):
        for b in range (x, x+40,1):
            scacchiera[a][b]=green
def colora_blu(x,y, hop, scacchiera):
    #print (" coloro di blu da ",x," ",y)
    for a in range(y,y+40):
        for b in range (x, x+40):
            #print(a,b)
            scacchiera[a][b]=blue