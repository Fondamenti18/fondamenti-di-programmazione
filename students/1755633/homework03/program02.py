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

Si puo' assumere che la cella in alto a sinisprint('xdec')tra sia priva di ostacoli.

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
'''

from immagini import *

def altezza(img):   #ritorna altezza (pixel) img ->inside()
    return len(img)

def larghezza(img):    #ritorna larghezza(pixel) img  ->inside
    return len(img[0])

def inside(a,l,img):    #ritorna vero se il pixel è dentro l immagine altrimento falso
    a_img=altezza(img)
    l_img=larghezza(img)
    return 0 <=  a  < a_img and 0 <=  l  < l_img

def colora(x,y,c,img1):   #colora il quadrato 40x40 pixel nell img1 di colore blu='b' o verde='v'!='b'
    if c=='b':
        colore=(0,0,255)
    else:
        colore=(0,255,0)

    for _ in range(y,y+40):
        for _1 in range (x,x+40):
            img1[_][_1]=colore


#funzioni movimento________________________________________________________________________________________
def xcre(y,n,c,s,img1,img):
    #print('xcre')
    #s=''
    cod=1
    #print(cod)
    n+=40
    while True:
        if inside(y,n,img):    # se il pixel è dentro l immagine
            if img[y][n]!=(255,0,0) and img[y][n]!=(0,255,0):  #se il pixel non è rosso e non è verde
                colora(n,y,'v',img1)
                c=0
                #print(cod)
                s+=str(cod-1)
                #print('colorato il pixel x',n)
            else:  #se il pixel è rosso o verde
                #cod=1
                c+=1
                return cod, y, n-40,c,s,img1
                #controllo(cod,y,n-40)
        else:         #se il pixel è fuori l immagine
            #cod=1
            c+=1
            return cod, y, n-40,c,s,img1
            #controllo(cod, y,n-40)
        n+=40

def ycre(n,x,c,s,img1,img):
    #print('ycre')
    cod=2
    #s=''
    n+=40
    while True:
        if inside(n,x,img): #se il pixel sta dentro l immagine
            if img[n][x]!=(255,0,0) and img[n][x]!=(0,255,0):  #se il pixel non è rosso e non è verde
                colora(x,n,'v',img1)
                c=0
                s+=str(cod-1)
                #print('colorato il pixel y',n)
            else:    #se il pixel è rosso o verde
                #cod=2
                c+=1
                return cod, n-40, x,c,s,img1
                #controllo(cod,n-40,x)
        else:    #se il pixel è fuori l immagine
            #cod=2
            c+=1
            return cod, n-40, x,c,s,img1
            #controllo(cod,n-40,x)

        n+=40

def xdec(y,n,c,s,img1,img):
    #print('xdec')
    cod=3
    #s=''
    n-=40
    while True:
        if inside(y,n,img):
            if img[y][n]!=(255,0,0) and img[y][n]!=(0,255,0):
                colora(n,y,'v',img1)
                c=0
                s+=str(cod-1)
                #print('colorato il pixel x',n)
            else:
                #cod=3
                c+=1
                return cod, y, n+40,c,s,img1
                #controllo(cod,y,n+40)
        else:
            #cod=3
            c+=1
            return cod, y, n+40,c,s,img1
            #controllo(cod,y,n+40)
        n-=40

def ydec(n,x,c,s,img1,img):
    #print('ydec', s)
    cod=0
    #s=''
    n-=40
    while True:
        if inside(n,x,img):
            if img[n][x]!=(255,0,0) and img[n][x]!=(0,255,0):
                colora(x,n,'v',img1)
                c=0
                s+=str(cod+3)
                #print('colorato il pixel y',n)
            else:
                #cod=0
                c+=1
                return cod, n+40, x,c,s,img1
                #controllo(cod,n+40,x)
        else:

            #cod=0
            c+=1
            return cod, n+40, x,c,s,img1
            #controllo(cod,n+40,x)
        n-=40

def save(name,fds): #salva img1 su disco
    pyfds=png.from_array(fds,'RGB')
    pyfds.save(name)



def controllo(cod,y,x,c,s,fout,img1,img):

    #s+=s
    #print(s)
    #if s.find('0123')==-1: #se non trova la sottostringa '0123'
    while c!=4:
    #if checkl(y,x):
        if cod==0: #controllo(xcre(y,x))
            cod,y,x,c,s,img1=xcre(y,x,c,s,img1,img)
            controllo(cod,y,x,c,s,fout,img1,img)
            break

        elif cod==1: #controllo(ycre(y,x))
            cod,y,x,c,s,img1=ycre(y,x,c,s,img1,img)
            controllo(cod,y,x,c,s,fout,img1,img)
            break
        elif cod==2: #controllo(xdec(y,x))
            cod,y,x,c,s,img1=xdec(y,x,c,s,img1,img)
            controllo(cod,y,x,c,s,fout,img1,img)
            break
        elif cod==3: #controllo(ydec(y,x))
            cod,y,x,c,s,img1=ydec(y,x,c,s,img1,img)
            controllo(cod,y,x,c,s,fout,img1,img)
            break
    else:
        colora(x,y,'b',img1)
        save(fout,img1)
        #print('codi',s)
        #print(len(s))
        #return

    global a,i
    #print('codiprimaretu',s)
    i+=1
    if i==1:
        #print('sinif',s)
        a=s


    return a



def cammino(fname, fname1):
    global i
    codifica=''
    img=load(fname)
    img1=img
    colora(0,0,'v',img1)
    codifica=controllo(0,0,0,0,'',fname1,img1,img)
    i=0
    #print(codifica)
    #print(type(codifica), 'codifica', codifica)
    return codifica

a=str()
i=0
#fname='I1.png'
#fname1='prova1.png'
#cammino(fname,fname1)
