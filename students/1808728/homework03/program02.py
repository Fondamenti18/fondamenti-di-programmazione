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
    a = load(fname)
    b = load(fname)
    diz= {1:0,2:40,3:80,4:120,5:160,6:200,7:240,8:280,9:320,10:360,11:400,12:440,13:480,14:520,15:560}
    x = 1
    y = 1
    r = (255,0,0)
    g = (0,255,0)
    robot = ''
    i = 0
    a[0][0] = g
    for x1 in range(diz[x],diz[x]+40):
        for y1 in range(diz[y],diz[y]+40):
            b[y1][x1] = (0,255,0)
    while True:
        contatore = 0
        if i == 0:
            if x < 15:
                x+= 1
                if a[diz[y]][diz[x]] == r or a[diz[y]][diz[x]] == g:
                    i = 1
                    contatore +=1
                    x-=1
                else:
                    robot = robot + '0'
                    contatore = 0
                    for x1 in range(diz[x],diz[x]+40):
                        for y1 in range(diz[y],diz[y]+40):
                            b[y1][x1] = (0,255,0)
                    a[diz[y]][diz[x]] = g
            else:
                i = 1
                contatore +=1
        if i == 1:
            if y < 15:
                y+=1
                if a[diz[y]][diz[x]]  == r or a[diz[y]][diz[x]] == g:
                    i = 2
                    contatore +=1
                    y-=1
                else:
                    robot = robot + '1'
                    contatore = 0
                    a[diz[y]][diz[x]] = g
                    for x1 in range(diz[x],diz[x]+40):
                        for y1 in range(diz[y],diz[y]+40):
                            b[y1][x1] = (0,255,0)
            else:
                i = 2
        if i == 2:
             if x > 1:
                x-=1
                if a[diz[y]][diz[x]]  == r or a[diz[y]][diz[x]] == g:
                    i = 3
                    contatore +=1
                    x+=1
                else:
                    robot = robot + '2'
                    contatore = 0
                    a[diz[y]][diz[x]]  = g
                    for x1 in range(diz[x],diz[x]+40):
                        for y1 in range(diz[y],diz[y]+40):
                            b[y1][x1] = (0,255,0)
             else:
                  i = 3
                  contatore +=1
        if i == 3:
             if y > 1:
                y-=1
                if a[diz[y]][diz[x]] == r or a[diz[y]][diz[x]] == g:
                    contatore +=1
                    i = 0
                    y+=1
                else:
                    robot = robot + '3'
                    contatore = 0
                    a[diz[y]][diz[x]] = g
                    for x1 in range(diz[x],diz[x]+40):
                        for y1 in range(diz[y],diz[y]+40):
                            b[y1][x1] = (0,255,0)
             else:
                 i = 0
                 contatore +=1
        if contatore >= 4:
            for x1 in range(diz[x],diz[x]+40):
                for y1 in range(diz[y],diz[y]+40):
                    b[y1][x1] = (0,0,255)
            break
    
    save(b,fname1)
    return(robot)
            
