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

from immagini import load
from immagini import save

def create(w,h, c = (0,0,0)):
    img = []
    for _ in range(h):
        riga = []
        for _ in range(w):
            riga += [c]
        img += [riga]
    return img




def quadra(fname, x, y, c):
    for px in range(x, x + 40):
        for py in range(y, y + 40):
            try:
                fname[py][px] = c        
            except IndexError:
                pass


bianco = (255,255,255)
nero = (0,0,0)
verde = (0,255,0)
rosso = (255,0,0)
blu = (0,0,255)
def cor(img, s, c):
    w,h = len(img[0]), len(img)
    img1 = create(w+s*2, h+s*2, c)
    for y in range(h):
        for x in range(w):
            img1[y+s][x+s] = img[y][x]
    return img1

def senza(img):
    w,h = len(img[0]), len(img)
    img1 = create(w-80,h-80)
    for y in range(40,h-40):
        for x in range(40,w-40):
            
            img1[y-40][x-40] = img[y][x]
            
                
    return img1

def cammino(fname, fname1):
    prova = load(fname)
    prova = cor(prova, 40, (255,0,0))
    
    quad = '0'
    x = 40
    y = 40
    quadra(prova, x,y,verde)
    
    while set(quad[-4:]) != set('bsad'):
        
        while (quad[-1] == '0' or quad[-1] == 'd' )  and prova[y][x + 40] == bianco or prova[y][x + 40] == nero:
            x += 40
            quadra(prova, x, y , verde)
                
            quad += '0'
        else:
            quad += 'b'
        
       
        while (quad[-1] == '1' or quad[-1] == 'b') and prova[y + 40][x] == bianco or prova[y + 40][x] == nero:
            y += 40
            quadra(prova, x, y , verde)
            
            quad += '1'
        else:
            quad += 's'
        
        
        while (quad[-1] == '2' or quad[-1] == 's') and prova[y][x - 40] == bianco or prova[y][x - 40] == nero:
            x -= 40
            quadra(prova, x, y , verde)
                
            quad += '2'
        else:
            quad += 'a' 
           
        
        
        while (quad[-1] == '3' or quad[-1] == 'a') and prova[y - 40][x] == bianco or prova[y - 40][x] == nero:
            y -= 40
            quadra(prova, x, y , verde)
                
            quad += '3'
        else:
            quad += 'd'
    else:
        quadra(prova, x, y, blu)
    
    quad = quad.replace('d','')
    quad = quad.replace('a','')
    quad = quad.replace('b','')
    quad = quad.replace('s','')
    prova = senza(prova)
    save(prova, fname1)
    return quad[1:]      
