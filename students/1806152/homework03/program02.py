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
    '''Implementare qui la funzione'''
    latotassella=40
    passi=""
    img=load(fname)
    x=0
    y=0
    pquadrato=img[y][x]
    boolean=True
    bianco=(255,255,255)
    nero=(0,0,0)
    rosso=(255,0,0)
    verde=(0,255,0)
    blu=(0,0,255)
    while boolean == True:
        flag=1
        giro=0
        print("start while")
        if flag < 5:
            print(pquadrato)
            if giro==0:
                print(giro)
                j=x
                pdestro=img[y][x+40]
                if pdestro != rosso or pdestro != verde:
                    draw(img,x,y,latotassella,latotassella,verde)
                    j=j+40
                    x=j
                    pquadrato=img[y][j]
                    passi=passi+"0"
                    flag=1 
                else:
                    print(flag)
                    giro+=1
                    flag+=1
                    print(flag)
            else:
                pass

            if giro==1:
                print(giro)
                j=y
                pbasso=img[y+40][x]
                if pbasso != rosso or pbasso != verde:
                    draw(img,x,y,latotassella,latotassella,verde)
                    j=j+40
                    y=j
                    pquadrato=img[j][x]
                    passi=passi+"1"
                    flag=1
                else:
                    giro+=1
                    flag+=1
            else:
                pass
            
            if giro==2:
                print(giro)
                j=x
                psinistra=img [y][x-40]
                if psinistra != rosso or psinistra != verde:
                    draw(img,x,y,latotassella,latotassella,verde)
                    j=j-40
                    x=j
                    pquadrato=img [y][j]
                    passi=passi+"2"
                    flag=1
                else:
                    giro+=1
                    flag+=1
            else:
                pass
			
            if giro==3:
                print(giro)
                j=y
                palto= img [y-40][x]
                if palto != rosso or palto != verde:
                    draw(img,x,y,latotassella,latotassella,verde)
                    j=j-40
                    y=j
                    pquadrato=img [j][x]
                    passi=passi+"3"
                    flag=1
                else:
                    giro+=1
                    flag+=1
            else:
                pass

            if 3<giro:
                giro=0
        else:
            boolean = False
			

    draw(img,x,y,latotassella,latotassella,blu) 
    save(img,fname1)
    return passi,fname1

def draw(img,x,y,w,h,c):
    for j in range(y,y+h):
        for i in range(x,x+w):
            img[j][i] = c
		
