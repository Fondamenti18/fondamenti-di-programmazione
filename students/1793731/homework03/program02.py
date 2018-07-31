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

import immagini

def cammino(fname,  fname1):
    
    file=immagini.load(fname)
    ris=''
    x=0; y=0
    xpros=0; ypros=0
    dire=0; count=0

    while count<4:
        xpros,ypros=movimento(dire,x,y)
        try:
            if (comptuple(file[ypros][xpros],(255,0,0)) or comptuple(file[ypros][xpros],(0,255,0))) and xpros>=0 and ypros>=0 :
                count+=1
                dire+=1
                if dire==4:dire=0
            elif xpros>=0 and ypros>=0:
                file=ricolora(x,y,file,(0,255,0))
                count=0
                x=xpros
                y=ypros
                ris+=str(dire)
            else:
                count+=1
                dire+=1
                if dire==4:dire=0
        except:
            count+=1
            dire+=1
            if dire==4:dire=0

    ricolora(x,y,file,(0,0,255))
    immagini.save(file,fname1)
    
    return ris
    
def comptuple(t1,t2):
    if t1[0]==t2[0] and t1[1]==t2[1] and t1[2]==t2[2]:
        return True         
    else:
        return False

def ricolora(x,y,file,colore): #per ricolorare i pixel 
    for line in range(y,y+40,1):
        for rig in range(x,x+40,1):
            file[line][rig] = colore
    return file
                

def movimento(dire,x,y): #per muoversi
    if dire==0:
        return x+40,y
    if dire==1:
        return x,y+40
    if dire==2:
        return x-40,y
    if dire==3:
        return x,y-40
    
                    
            