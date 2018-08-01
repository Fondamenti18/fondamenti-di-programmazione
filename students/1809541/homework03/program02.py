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
def movimento(scacchiera,x,y,step=''):
    contacicli=0
    #prima casella
    for i in range(x,x+40):
        for n in range(y,y+40):
            scacchiera[i][n]=(0,255,0)
    #destra
    try:
        while scacchiera[x][y+40]!=(255,0,0) and scacchiera[x][y+40]!=(0,255,0):
            if y+40>len(scacchiera[0]):
                break
            for i in range(x,x+40):
                for n in range(y+40,y+80):
                    scacchiera[i][n]=(0,255,0)
            step+='0'
            y+=40
            contacicli+=1
    except IndexError:
        pass
    #giu
    try:
        while scacchiera[x+40][y]!=(255,0,0) and scacchiera[x+40][y]!=(0,255,0):
            for i in range(x+40,x+80):
                for n in range(y,y+40):
                    scacchiera[i][n]=(0,255,0)
            step+='1'
            x+=40
            contacicli+=1
    except IndexError:
        pass
    #sinistra
    while scacchiera[x][y-40]!=(255,0,0) and scacchiera[x][y-40]!=(0,255,0):
        if y-40<0:
            break
        for i in range(x,x+40):
            for n in range(y-40,y):
                scacchiera[i][n]=(0,255,0)
        step+='2'
        y-=40
        contacicli+=1
    #su
    while scacchiera[x-40][y]!=(255,0,0) and scacchiera[x-40][y]!=(0,255,0):
        if x-40<0:
            break
        for i in range(x-40,x):
            for n in range(y,y+40):
                scacchiera[i][n]=(0,255,0)
        step+='3'
        x-=40
        contacicli+=1
    return step,contacicli,x,y

import immagini
def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    step=''
    scacchiera=immagini.load(fname)
    x=0
    y=0
    var=movimento(scacchiera,x,y,step)
    step+=var[0]
    while 1:
        if var[1]==0:
            for i in range(var[2],var[2]+40):
               for n in range(var[3],var[3]+40):
                    scacchiera[i][n]=(0,0,255)
            break
        else:
            var=movimento(scacchiera,var[2],var[3])
            step+=var[0]
    immagini.save(scacchiera,fname1)
    return step
