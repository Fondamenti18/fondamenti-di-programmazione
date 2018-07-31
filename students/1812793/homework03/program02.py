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
    img=load(fname)
    co=[0,0]
    passi=[]
    colora(img,co,(0,255,0))
    direzione=controlla(img,co,passi)
    while direzione!=4:
        if direzione==0:
            co[0]+=40
            passi+=[0]
        elif direzione==1:
            co[1]+=40
            passi+=[1]
        elif direzione==2:
            co[0]-=40
            passi+=[2]
        else:
            co[1]-=40
            passi+=[3]
        colora(img,co,(0,255,0))
        direzione=controlla(img,co,passi)
    colora(img,co,(0,0,255))
    save(img,fname1)
    passi=[str(x) for x in passi]
    return "".join(passi)
        
    
def colora(img,co,colore):
    for riga in range(co[1],co[1]+40):
        for colonna in range(co[0],co[0]+40):
            img[riga][colonna]=colore

def controlla(img,co,passi):
    if passi==[] and img[co[1]][co[0]+40]!=(255,0,0):
        return 0
    pos=trova(img,co,passi[-1])
    return pos
        

def trova(img,co,x):
    a=4
    f=[0,1,2,3]
    l=[]
    if len(img[co[1]])-co[0]>40 and img[co[1]][co[0]+40] not in {(255,0,0),(0,255,0)}:
        l+=[0]
    if len(img)-co[1]>40 and img[co[1]+40][co[0]] not in {(255,0,0),(0,255,0)}:
        l+=[1]
    if co[0]>=40 and img[co[1]][co[0]-40] not in {(255,0,0),(0,255,0)}:
        l+=[2]
    if co[1]>=40 and img[co[1]-40][co[0]] not in {(255,0,0),(0,255,0)}:
        l+=[3]
    
    if l!=[]:    
        if x in l:
             a=f[x]
        elif x!=3:
            if f[x+1] in l:
                a=f[x+1]
            else:
                a=f[x-1]
        elif 0 in l:
            a=0
        else:
            a=f[x-1]
    return a