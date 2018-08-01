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
fname='I1.png'
def cammino(fname,fname1):
    im=load(fname)
    y,x,l,tl,bw,count=0,0,[],[],((0,0,0),(255,255,255)),''
    base=quindici(im,y,x,l,tl)
    y,x,my,mx,f,c,sy,sx=0,0,0,1,0,'',0,0
    while True:
        try:
            if base[y][x] in bw and x>=0 and y>=0 and x<=14 and y<=14:
                base[y][x]=(0,255,0)
                f=0
                if mx==1:count=count+'0'
                elif my==1:count=count+'1'
                elif mx==-1:count=count+'2'
                elif my==-1:count=count+'3'
            else:
                f+=1
                if f==5:
                    base[sy][sx]=(0,0,255)
                    break
                if mx==1:
                    x-=1
                    mx,my=0,1
                elif my==1:
                    y-=1
                    my,mx=0,-1
                elif mx==-1:
                    x+=1
                    mx,my=0,-1
                elif my==-1:
                    y+=1
                    my,mx=0,1
        except:
            f+=1
            if f==5:
                base[sy][sx]=(0,0,255)
                break
            if mx==1:
                x-=1
                mx,my=0,1
            elif my==1:
                y-=1
                my,mx=0,-1
            elif mx==-1:
                x+=1
                mx,my=0,-1
            elif my==-1:
                y+=1
                my,mx=0,1
        sy,sx=y,x
        y+=my
        x+=mx
    save(quaranta(base),fname1)
    return count[1:]




def quaranta(base):
    immagine,a=[],0
    for b in base:
        c,img=0,[]
        for d in b:
            a+=1
            d=[d]*40
            img.extend(d)
        while c<40:
            c+=1
            immagine.append(img)
    return immagine
def quindici(im,y,x,l,tl):
    for b in im:
        y+=1
        if y%40==0:
            for a in b:
                x+=1
                if x%40==0:
                    l.append(a)
            tl.append(l)
        l=[]
    return tl








