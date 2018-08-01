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
def cammino(fname,fname1):
    img = load(fname)
    i = 0
    j = 0
    t = ""
    l = []
    test1 = 0
    test2 = 0
    test3 = 0
    test4 = 0
    a = 1
    b = 1
    x = 1
    d = 1
    total = a+b+x+d
    z = 0
    while total!=0:

        f = destra(img,i,j,t,test1,a,l)
        i = f[1]
        j = f[2]
        t = f[3]
        a = f[0]
        


        s = giu(img,i,j,t ,test2,b,l)
        i = s[1]
        j = s[2]
        t = s[3]
        b = s[0]

        
        r = sinistra(img,i,j, t ,test3,x,l)
        i = r[1]
        j = r[2]
        t = r[3]
        x = r[0]
        
        
        u = su(img,i,j,t ,test4,d,l)
        i = u[1]
        j = u[2]
        t = u[3]
        d = u[0]
        total = a + b+ x + d
    h = j - 40
    for i in range(i,i+40):
        for h in range(h,h + 40):
            img[i][h] = (0,0,255)
            h = h - 39
    save(img,fname1)
    t = t[1:-1]
    t = t + str(bip(l))
    return t

def destra(img,i,j,t,test1,a,l):
    while j < 600 :
        if img[i][j] != (255,0,0) and img[i][j]!= (0,255,0) :
            t = t + "0"
            img = colorami(img,i,j)
            j = j + 40
            test1 = 1
        else:
            break
    a = test(test1)
    l.append((a,0))
    test1 = 0
    j = j - 40
    i = i + 40
    return a , i , j , t  , l
def giu(img,i,j,t,test2,b,l):
    while i < 600 :
        if img[i][j] != (255,0,0) and img[i][j] != (0,255,0):
            t = t + "1"
            img = colorami(img,i,j)
            i = i + 40
            test2 = 1
        else :
            break
    b = test(test2)
    l.append((b,1))
    test2 = 0
    i = i - 40
    j = j - 40
    return b , i , j , t  , l


def sinistra(img,i,j,t,test3,x,l):
    while img[i][j] != (255,0,0)  and j >= 0 and img[i][j] != (0,255,0): 
        t = t + "2"
        img = colorami(img,i,j)
        j = j - 40
        test3 = 1
    x = test(test3)
    l.append((x,2))
    test3= 0
    i = i - 40
    j = j + 40
    return x , i , j , t , l
    
    
def su(img,i,j,t,test4,d,l):
    while img[i][j] != (255,0,0) and i >= 0 and img[i][j] != (0,255,0):
        t = t + "3"
        img = colorami(img,i,j)
        i = i - 40
        test4 = 1 
    d = test(test4)
    l.append((d,3))
    test4 = 0
    i = i + 40
    j = j + 40
    return d , i , j , t , l


def test(a):
    c = 1
    if a == 0 :
        c = 0
    return c


def colorami(img,i,j):
    for i in range(i,i+40):
        for j in range(j,j+40):
            img[i][j] = (0,255,0)
        j = j - 39
    return img
def bip(l):
    i = 0
    for i in range(len(l)-1,-1,-1):
        if l[i][0] == 1 :
            return l[i][1]
    
    

    
        
    
    
            

                   
                       

    
