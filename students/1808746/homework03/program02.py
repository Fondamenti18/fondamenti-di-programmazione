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

import png

def cammino(fname, fname1):
    #carico l'immagine e la rendo lista di liste di pixel
    img=load(fname)
    
    y=0
    x=0
    #si dichiara la lista che conterrà tutte le lettere che identificano i passi effettuato dal robot
    percorso=[]
    
    tentativi(img, x, y, percorso)
    
    #si salva l'immagine modificata nel percorso richiesto
    save(img, fname1)
    
    percorso=''.join(percorso)
    return percorso

def tentativi(img,x,y, percorso):
    '''effettua i tentativi su tutte le caselle adiacenti a quella il cui primo pixel ha coordinate (x,y).
    Ciascun ciclo while controlla se la casella adiacente esiste; si ripete il ciclo 1 fintanto la casella a destra esiste e, come verifica la funzione chiamata, è bianca o nera; quando non esiste o diventa verde o rossa, si esce dal ciclo while e si ripete la stessa cosa con un secondo ciclo che controlla la casella sotto. '''

    while inside(img,x+40,y):
        x+=40
        provaDx=versoDx(img, x, y, percorso)
        #quando provaDx diventa falsa, significa che la casella a destra è rossa o verde, quindi bisogna ruotare il robottino (uscendo dal ciclo while) e si decrementa la variabile x per tornare alla casella del penultimo tentativo.
        if provaDx==False:
            x-=40
            break        
    
    while inside(img,x,y+40):
        y+=40
        provaSt=versoSt(img, x, y, percorso)
        #quando provaSt diventa falsa, significa che la casella sotto è rossa o verde, quindi bisogna ruotare il robottino (uscendo dal ciclo while) e si decrementa la variabile y per tornare alla casella del penultimo tentativo.
        if provaSt==False:
            y-=40
            break
    
    while inside(img,x-40,y):
        x-=40
        provaSx=versoSx(img, x, y, percorso)
        #quando provaSx diventa falsa, significa che la casella a sinistra è rossa o verde, quindi bisogna ruotare il robottino (uscendo dal ciclo while) e si incrementa la variabile x per tornare alla casella del penultimo tentativo.
        if provaSx==False:
            x+=40
            break
    
    while inside(img,x,y-40):
        y-=40
        provaSp=versoSp(img, x, y, percorso)
        #quando provaSp diventa falsa, significa che la casella sopra è rossa o verde, quindi bisogna ruotare il robottino (uscendo dal ciclo while) e si incrementa la variabile x per tornare alla casella del penultimo tentativo.
        if provaSp==False:
            y+=40
            break
    
    #si utilizza la funzione ricorsiva per provare a vedere se il robottino può fare altri passi (dopo che si è girato di 360gradi)
    try:
        tentativi(img, x, y, percorso)
    #quando la chiamata alla funzione ricorsiva avvia un loop, significa che il robottino non può più muoversi in nessuna delle caselle adiacenti, perciò si procede con la colorazione in blu della casella dove si trova e si conclude l'immagine
    except:
        disegnaBlu(img, x, y)
    
    
def versoDx(img, x, y, percorso):
    '''Controlla il colore della casella adiacente (a destra) a quella il cui primo punto ha coordinate (x,y). Se non è bianca o nera, ma verde o rossa, ritorna False per uscire dal ciclo while di tentativi.'''
    if img[y][x]==(0,0,0) or img[y][x]==(255,255,255): #se la casella di fronte è NERA o BIANCA
        disegnaVerde(img,x-40,y)
        #si effettua un passo verso DESTRA, quindi si aggiunge '0' al percorso effettuato
        percorso+='0'
        return True
    elif img[y][x]==(255,0,0) or img[y][x]==(0,255,0): #se la casella di fronte è ROSSA o VERDE
        return False


def versoSt(img,x,y,percorso):
    '''Controlla il colore della casella adiacente (in basso) a quella il cui primo punto ha coordinate (x,y). Se non è bianca o nera, ma verde o rossa, ritorna False per uscire dal ciclo while di tentativi.'''
    if img[y][x]==(0,0,0) or img[y][x]==(255,255,255): #se la casella di fronte è NERA o BIANCA
        disegnaVerde(img,x,y-40)
        #si effettua un passo verso SOTTO, quindi si aggiunge '1' al percorso effettuato
        percorso+='1'
        return True
    elif img[y][x]==(255,0,0) or img[y][x]==(0,255,0): #se la casella di fronte è ROSSA o VERDE
        return False


def versoSx(img,x,y,percorso):
    '''Controlla il colore della casella adiacente (a sinistra) a quella il cui primo punto ha coordinate (x,y). Se non è bianca o nera, ma verde o rossa, ritorna False per uscire dal ciclo while di tentativi.'''
    if img[y][x]==(0,0,0) or img[y][x]==(255,255,255): #se la casella di fronte è NERA o BIANCA
        disegnaVerde(img,x+40,y)
        #si effettua un passo verso SINISTRA, quindi si aggiunge '2' al percorso effettuato
        percorso+='2'
        return True
    elif img[y][x]==(255,0,0) or img[y][x]==(0,255,0): #se la casella di fronte è ROSSA o VERDE
        return False
    
        
 
def versoSp(img,x,y,percorso):
    '''Controlla il colore della casella adiacente (in alto) a quella il cui primo punto ha coordinate (x,y). Se non è bianca o nera, ma verde o rossa, ritorna False per uscire dal ciclo while di tentativi.'''
    if img[y][x]==(0,0,0) or img[y][x]==(255,255,255): #se la casella di fronte è NERA o BIANCA
        disegnaVerde(img,x,y+40)
        #si effettua un passo verso SOPRA, quindi si aggiunge '3' al percorso effettuato
        percorso+='3'
        return True
    elif img[y][x]==(255,0,0) or img[y][x]==(0,255,0): #se la casella di fronte è ROSSA o VERDE
        return False

     
def disegnaVerde(img, x, y, c=(0,255,0)):
    '''disegna sull'immagine img un quadrato di colore VERDE, ampiezza 40 e altezza 40 a partire dal pixel (x,y)'''
    for px in range(x, x+40):
        for py in range(y, y+40):
            if inside(img,px,py):
                img[py][px] = c

def disegnaBlu(img, x, y, c=(0,0,255)):
    '''disegna sull'immagine img un quadrato di colore BLU, ampiezza 40 e altezza 40 a partire dal pixel (x,y)'''
    for px in range(x, x+40):
        for py in range(y, y+40):
            if inside(img,px,py):
                img[py][px] = c  
        
def inside(img, x, y):
    '''verifica per ciascun pixel dato in input se si trova all'interno dell'immagine)'''
    return 0 <= y < len(img) and 0 <= x < len(img[0])

def load(fname):
    """ Carica la immagine PNG dal file fname.
        Torna una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return img

def save(img, fname1):
    """ Salva la immagine img  nel file filename in formato PNG8.
        Img e' una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    pngimg = png.from_array(img,'RGB')
    pngimg.save(fname1)

if __name__=='__main__':
    cammino('I4.png','t4.png')

