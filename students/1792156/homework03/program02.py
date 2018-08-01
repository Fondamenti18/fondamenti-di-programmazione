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
    x=0
    y=0
    comm=''
    n=(0,0,0)
    b=(255,255,255)
    g=(0,255,0)
    count=0
    img=load(fname)
    while count in range(0,2,1):
        while  0<=x<560 and (img[y][x+40]==b or img[y][x+40]==n):
            for index in range(y,y+40):
                for index_a in range(x,x+40):
                        img[index][index_a]=g
            comm+='0'
            x+=40
        count=count+1  
        while 0<=y<=520 and (img[y+40][x]==b or img[y+40][x]==n):
            count=0
            for index in range(y,y+40):
                for index_a in range(x,x+40):
                    img[index][index_a]=g
            comm+='1'
            y+=40
        while 40<=x<=600 and (img[y][x-40]==b or img[y][x-40]==n):
            count=0
            for index in range(y,y+40):
                for index_a in range(x,x+40):
                    img[index][index_a]=g
            comm+='2'
            x-=40
        while (0<=y<=600 and 0<=x<=600) and (img[y-40][x]==b or img[y-40][x]==n) :
            count=0
            for index in range(y,y+40):
                for index_a in range(x,x+40):
                    img[index][index_a]=g
            comm+='3'
            y-=40
    else:    
        for index in range(y,y+40):
            for index_a in range(x,x+40):
                img[index][index_a]=g
                return comm            
                save(img,fname1)
    