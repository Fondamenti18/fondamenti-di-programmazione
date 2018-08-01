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
import immagini

def change_color(im,loc_now,color):
    row=loc_now[0]-39
    col=loc_now[1]-39
    for i in range(row,row+40):
        for j in range(col,col+40):
            im[i][j]=color
            
    return im

def change_arrow(im,arrow,loc_now,x):

    row=len(im)
    col=len(im[0])
    all_move=[-1, -1, -1 ,-1]
    
    if((loc_now[1]+x<=col)):
        if( (im[loc_now[0]][loc_now[1]+x] != (255,0,0)) & (im[loc_now[0]][loc_now[1]+x] != (0,255,0)) ):
            all_move[0]=0
    if(loc_now[0]+x<=row):
         if((im[loc_now[0]+x][loc_now[1]]!=(255,0,0))& (im[loc_now[0]+x][loc_now[1]]!=(0,255,0)) ):
             all_move[1]=1
    if (loc_now[1]-x>0) :
        if((im[loc_now[0]][loc_now[1]-x] != (255,0,0))& (im[loc_now[0]][loc_now[1]-x] != (0,255,0)) ):
            all_move[2]=2
    if (loc_now[0]-x>0):
        if((im[loc_now[0]-x][loc_now[1]] != (255,0,0)) & (im[loc_now[0]-x][loc_now[1]] != (0,255,0)) ):
            all_move[3]=3

    result=all_move[arrow:]+all_move[:arrow]
    existing=[value for value in result if value !=-1]
    
    if(existing == []):
        return -1
    else:
        return existing[0]

    


def cammino(fname,  fname1):
    im=immagini.load(fname)
    row=len(im)
    col=len(im[0])
    str_result=''
    loc_now=[39,39]
    x=40
    arrow=0   
    im=change_color(im,loc_now,(0,255,0))
    while(arrow>=0):
            
        #check Right
        if(arrow==0):
            loc_now[1]=loc_now[1]+x
            str_result+='0'
        elif( (arrow==1)):
            loc_now[0]=loc_now[0]+x
            str_result+='1'
        elif((arrow==2)):
            loc_now[1]=loc_now[1]-x
            str_result+='2'
        elif((arrow==3)):
            loc_now[0]=loc_now[0]-x
            str_result+='3'
        else:    
            break
        im=change_color(im,loc_now,(0,255,0))
        arrow=change_arrow(im,arrow,loc_now,x)


    im=change_color(im,loc_now,(0,0,255))        
    immagini.save(im,fname1)
    return str_result




            
        
