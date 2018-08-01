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

def accanna(x,y):
    return 0<=x<=600 and 0<=y<=600

def accanna_1(x):
    return 0<=x<560 

def accanna_2(y):
    return 0<=y<=520 

def accanna_3(x):
    return 40<=x<=600

def pitturala(x,y,f):
    for Z in range(x, x+40):
        for Jay in range(y, y+40):             
            f[Jay][Z] = (0,255,0)

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    f=load(fname)
    codifica=''
    x=0
    y=0
    arigirala=0
    r=(255,0,0)
    v=(0,255,0)
    
    while arigirala<4:
        
        while accanna_1(x) and f[y][x+40]!=r  and f[y][x+40]!=v:
            arigirala=0
            pitturala(x,y,f)
            x+=40
            codifica+='0'
        arigirala+=1
            
        while accanna_2(y) and f[y+40][x]!=r and f[y+40][x]!=v:
            arigirala=0
            pitturala(x,y,f)
            y+=40
            codifica+='1'
        arigirala+=1
          
        while accanna_3(x) and f[y][x-40]!=r and f[y][x-40]!=v:
            arigirala=0
            pitturala(x,y,f)
            x-=40
            codifica+='2'
        arigirala+=1
        
        while accanna(x,y) and f[y-40][x]!=r and f[y-40][x]!=v:
            arigirala=0
            pitturala(x,y,f)
            y-=40
            codifica+='3'
        arigirala+=1
        
    else:    
        arigirala=0
        for px in range(x, x+40):
            for py in range(y, y+40):                         
                f[py][px] = (0,0,255)
    
    
    save(f,fname1)
    return codifica