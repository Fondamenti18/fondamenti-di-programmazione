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
import numpy as np

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    lsImmagine,x,y=CaricaImm(fname)
    Lato=40
    arScacchiera=Scacchiera(lsImmagine,x,y,Lato)
    
    x=len(arScacchiera[0])
    y=len(arScacchiera)
    arScacchiera[0][0]='verde'
    
    i,j,strCammino=Muovi(arScacchiera,x,y)               
    arScacchiera[j][i]='blu'
    
    ColoraImmagine(arScacchiera,lsImmagine,Lato)
    
    save(lsImmagine,fname1)
    
    return strCammino

def Colora(Colore):
    dzColori={}
    dzColori['nero']=(0, 0, 0)
    dzColori['bianco']=(255,255,255)
    dzColori['rosso']=(255,0,0)
    dzColori['blu']=(0,0,255)
    dzColori['verde']=(0,255,0)
    return dzColori[Colore]

def deColora(tpColore):
    dzColori={}
    dzColori[(0, 0, 0)]='nero'
    dzColori[(255,255,255)]='bianco'
    dzColori[(255,0,0)]='rosso'
    dzColori[(0,0,255)]='blu'
    dzColori[(0,255,0)]='verde'
    return dzColori[tpColore]

def CaricaImm(filename):
    lsImmagine=load(filename)
    x=len(lsImmagine[0])
    y=len(lsImmagine)
    return lsImmagine,x,y

def Scacchiera(lsImmagine,x,y,Lato):
    lsScacchiera=[]
    for j in range(0,y,Lato):
        ls=[]
        for i in range(0,x,Lato):
            ls+=[deColora(lsImmagine[j][i])]
        lsScacchiera+=[ls]
    return np.asarray(lsScacchiera)

def Ostacolo(i,j,StepR,StepC,arScacchiera,x,y):
    if j+StepR==y or j+StepR<0 or i+StepC==x or i+StepC<0:
        return True
    elif arScacchiera[j+StepR][i+StepC]=='rosso' or arScacchiera[j+StepR][i+StepC]=='verde':
        return True
    else:
        return False

def CambiaDirezione(Direzione):
    if Direzione==3:
        return 0
    else:
        return Direzione+1

def Finish(j,i,arScacchiera,x,y):
    return Ostacolo(i,j,0,1,arScacchiera,x,y) and Ostacolo(i,j,1,0,arScacchiera,x,y) and Ostacolo(i,j,0,-1,arScacchiera,x,y) and Ostacolo(i,j,-1,0,arScacchiera,x,y)
    
def Muovi(arScacchiera,x,y):
    dzStep={}
    dzStep[0]=0,1#dx
    dzStep[1]=1,0#giu
    dzStep[2]=0,-1#sx
    dzStep[3]=-1,0#su
    
    j=0
    i=0
    
    strCammino=''
    
    Direzione=0
    NuovaDirezione=0
    
    Finito=Finish(j,i,arScacchiera,x,y)
    
    while Finito==False:        

        StepR,StepC=dzStep[Direzione]        

        NonPossoMuovere=Ostacolo(i,j,StepR,StepC,arScacchiera,x,y)
        
        while NonPossoMuovere==True:
            NuovaDirezione=CambiaDirezione(Direzione)
            Direzione=NuovaDirezione
            StepR,StepC=dzStep[Direzione]
            NonPossoMuovere=Ostacolo(i,j,StepR,StepC,arScacchiera,x,y)
            
        j+=StepR
        i+=StepC
        arScacchiera[j][i]='verde'
        strCammino+=str(Direzione)
        Finito=Finish(j,i,arScacchiera,x,y)
        
    return i,j,strCammino

def ColoraImmagine(arScacchiera,lsImmagine,Lato):
    for i in range(len(lsImmagine)):
        for j in range(len(lsImmagine[0])):
            lsImmagine[j][i]=Colora(arScacchiera[j//Lato][i//Lato])
    return