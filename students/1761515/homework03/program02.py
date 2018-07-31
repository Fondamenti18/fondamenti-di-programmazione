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

from immagini import png

def cammino(fname,fname1):
    img=load(fname)
    direzione=0
    x=20
    y=20
    img=coloraQuadrato(x,y,(0,255,0),img)#quadrato iniziale
    stringa=''
    stato = True
    while(stato):
        stato,x,y,direzione=controllaPos(x,y,direzione,img)
        if(stato):
            img=coloraQuadrato(x,y,(0,255,0),img)
            stringa+=str(direzione)
            
    img=coloraQuadrato(x,y,(0,0,255),img) #finale
    save(img,fname1)
    return stringa

def controllaPos(x,y,direzione,img):
    check=False
    conteggio=0
    while(check==False):
        if(y+40<=len(img[0])):
            if(direzione==0 and img[x][y+40]!=(255,0,0) and img[x][y+40]!=(0,255,0)):#se esce fuori a destra non eseguire
                y+=40
                check=True
                break
        if(x+40<=len(img)):
            if(direzione==1 and img[x+40][y]!=(255,0,0) and img[x+40][y]!=(0,255,0)):
                x+=40
                check=True
                break
        if(y-40>=0):
            if(direzione==2 and img[x][y-40]!=(255,0,0) and img[x][y-40]!=(0,255,0)):#vai a sinistra e controlla che non sia maggiore di 0
                y-=40
                check=True
                break
        if(x-40>=0):
            if(direzione==3 and img[x-40][y]!=(255,0,0) and img[x-40][y]!=(0,255,0)):#vai in alto e controlla che l altezza non sia minore di 0
                x-=40
                check=True
                break
        if(direzione >3):
            direzione=0
            conteggio+=1
        else:
            direzione+=1
            conteggio+=1
        if(conteggio>4):
            check=False
            break
            
    return check,x,y,direzione
   
def coloraQuadrato(x,y,colore,img):
    for riga in range(len(img[0])):#larghezza scacchiera
        for colonna in range(len(img)):#altezza scacchiera
            if(riga>=x-20 and riga<x+20 and colonna>= y-20 and colonna <y+20):
                img[riga][colonna]=colore
                
    return img

def load(fname):   
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

def save(img, filename):
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)