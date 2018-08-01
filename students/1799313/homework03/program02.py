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
    pic=load(fname)
    bluda=(0,0,255)
    verdastro=(0,255,0)
    rossetto=(255,0,0)
    asc=0
    ordina=0
    ctralt=0
    colore(asc,ordina,verdastro,pic)
    risultatofinale=''
    for i in range(0,7000):
            if ctralt==0:
                if dentro(pic,asc+40,ordina) and pic[ordina][asc+40]!=rossetto and pic[ordina][asc+40]!=verdastro: 
                        ris=''
                        asc=asc+40
                        while dentro(pic,asc,ordina)==1 and pic[ordina][asc]!= rossetto and pic[ordina][asc]!= verdastro:
                            colore(asc,ordina,verdastro,pic)
                            ris+="0"
                            asc+=40
                        asc-=40
                        if dentro(pic,asc,ordina+40)==1 and pic[ordina+40][asc]!=rossetto and pic[ordina+40][asc]!=verdastro :
                            ctralt=1
                        elif dentro(pic,asc-40,ordina)==1 and pic[ordina][asc-40]!=rossetto and pic[ordina][asc-40]!=verdastro :
                            ctralt=2
                        elif dentro(pic,asc,ordina-40)==1 and pic[ordina-40][asc]!=rossetto and pic[ordina-40][asc]!=verdastro :
                            ctralt=3
                        elif dentro(pic,asc+40,ordina)==1 and pic[ordina][asc+40]!=rossetto and pic[ordina][asc+40]!=verdastro :
                            ctralt=0
                        else:
                            ctralt=4
                        risultatofinale+=ris
            elif ctralt==1:
                if dentro(pic,asc,ordina+40) and pic[ordina+40][asc]!=rossetto and pic[ordina+40][asc]!=verdastro:
                    ris=''
                    ordina+=40
                    while dentro(pic,asc,ordina)==1 and pic[ordina][asc]!= rossetto and pic[ordina][asc]!= verdastro:
                        colore(asc,ordina,verdastro,pic)
                        ris+="1"
                        ordina+=40
                    ordina-=40
                    if dentro(pic,asc-40,ordina)==1 and pic[ordina][asc-40]!=rossetto and pic[ordina][asc-40]!=verdastro :
                        ctralt=2
                    elif dentro(pic,asc,ordina-40)==1 and pic[ordina-40][asc]!=rossetto and pic[ordina-40][asc]!=verdastro :
                        ctralt=3
                    elif dentro(pic,asc+40,ordina)==1 and pic[ordina][asc+40]!=rossetto and pic[ordina][asc+40]!=verdastro :
                        ctralt=0
                    elif dentro(pic,asc,ordina+40)==1 and pic[ordina+40][asc]!=rossetto and pic[ordina+40][asc]!=verdastro :
                        ctralt=1
                    else:
                        ctralt=4
                    risultatofinale+=ris
            elif ctralt==2:
                if dentro(pic,asc-40,ordina) and pic[ordina][asc-40]!=rossetto and pic[ordina][asc-40]!=verdastro:
                    asc,ctralt,ris=sinistra3(pic,asc-40,ordina,rossetto,verdastro)
                    risultatofinale+=ris
            elif ctralt==3:
                if dentro(pic,asc,ordina-40) and pic[ordina-40][asc]!=rossetto and pic[ordina-40][asc]!=verdastro:
                    ordina,ctralt,ris=susu(pic,asc,ordina-40,rossetto,verdastro)
                    risultatofinale+=ris
            else:
                colore(asc,ordina,bluda,pic)
                break
    save(pic,fname1)
    return risultatofinale


def sinistra3(pic,asc,ordina,rossetto,verdastro):
    ris=''
    while dentro(pic,asc,ordina)==1 and pic[ordina][asc]!= rossetto and pic[ordina][asc]!= verdastro:
        colore(asc,ordina,verdastro,pic)
        ris+="2"
        asc-=40
    asc+=40
    if dentro(pic,asc,ordina-40)==1 and pic[ordina-40][asc]!=rossetto and pic[ordina-40][asc]!=verdastro :
        ctralt=3
    elif dentro(pic,asc+40,ordina)==1 and pic[ordina][asc+40]!=rossetto and pic[ordina][asc+40]!=verdastro :
        ctralt=0
    elif dentro(pic,asc,ordina+40)==1 and pic[ordina+40][asc]!=rossetto and pic[ordina+40][asc]!=verdastro :
        ctralt=1
    elif dentro(pic,asc-40,ordina)==1 and pic[ordina][asc-40]!=rossetto and pic[ordina][asc-40]!=verdastro :
        ctralt=2
    else:
        ctralt=4
    return asc,ctralt,ris


def susu(pic,asc,ordina,rossetto,verdastro):
    ris=''
    while dentro(pic,asc,ordina)==1 and pic[ordina][asc]!= rossetto and pic[ordina][asc]!= verdastro:
        colore(asc,ordina,verdastro,pic)
        ris+="3"
        ordina-=40
    ordina+=40
    if dentro(pic,asc+40,ordina)==1 and pic[ordina][asc+40]!=rossetto and pic[ordina][asc+40]!=verdastro :
        ctralt=0
    elif dentro(pic,asc,ordina+40)==1 and pic[ordina+40][asc]!=rossetto and pic[ordina+40][asc]!=verdastro :
        ctralt=1
    elif dentro(pic,asc-40,ordina)==1 and pic[ordina][asc-40]!=rossetto and pic[ordina][asc-40]!=verdastro :
        ctralt=2
    elif dentro(pic,asc,ordina-40)==1 and pic[ordina-40][asc]!=rossetto and pic[ordina-40][asc]!=verdastro :
        ctralt=3
    else:
        ctralt=4
    return ordina,ctralt,ris

def dentro (pic,i,j):
    iw,ih=len(pic[0]),len(pic)
    return 0<=i<iw and 0<=j<ih

def colore(xx,yy,c,pic):
    for u in range(yy,yy+40):
        for o in range(xx,xx+40):
            pic[u][o]=c
    



    
    
            
    
        
