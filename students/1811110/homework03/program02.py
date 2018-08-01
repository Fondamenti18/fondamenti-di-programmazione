'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato lung. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  cambiocolorete di rosso).

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
legge l'immagine della scacchiera in fname, cambiocolore di verde le celle della scacchiera percorse dal robottino prima di fermarsi, 
cambiocolore di blu la cella in cui il robottino si ferma e registra l'immagine ricambiocoloreta nel file fname1. 
Inoltre restituisce una mess dove in sequanza sono codificati i passi effettuati dal robottino prima di fermarsi. 
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

def controllodx(immagine,x,lung,y,rosso,verde,guardia):
    if dentro(immagine,x,y+lung)==True and immagine[y+lung][x]!=rosso and immagine[y+lung][x]!=verde :
        guardia=1
    
    elif dentro(immagine,x,y-lung)==True and immagine[y-lung][x]!=rosso and immagine[y-lung][x]!=verde :
        guardia=3
    elif dentro(immagine,x+lung,y)==True and immagine[y][x+lung]!=rosso and immagine[y][x+lung]!=verde :
        guardia=0
    else:
        guardia=4
    return guardia
def versodx(immagine,x,y,rosso,verde,lung,mess):
    
    guardia=0
    while dentro(immagine,x,y)==True and immagine[y][x]!= rosso and immagine[y][x]!= verde:
        cambiocolore(x,y,verde,immagine,lung)
        mess+="0"
        x+=lung
    x-=lung
    guardia=controllodx(immagine,x,lung,y,rosso,verde,guardia)
    
    return x,guardia,mess

def controllogiu(immagine,x,lung,y,rosso,verde,guardia):
    if dentro(immagine,x-lung,y)==True and immagine[y][x-lung]!=rosso and immagine[y][x-lung]!=verde :
        guardia=2
    
    elif dentro(immagine,x+lung,y)==True and immagine[y][x+lung]!=rosso and immagine[y][x+lung]!=verde :
        guardia=0
    elif dentro(immagine,x,y+lung)==True and immagine[y+lung][x]!=rosso and immagine[y+lung][x]!=verde :
        guardia=1
    else:
        guardia=4
    return guardia

def versogiu(immagine,x,y,rosso,verde,lung,mess):
    guardia=0
    while dentro(immagine,x,y)==True and immagine[y][x]!= rosso and immagine[y][x]!= verde:
        cambiocolore(x,y,verde,immagine,lung)
        mess+="1"
        y+=lung
    y-=lung
    guardia=controllogiu(immagine,x,lung,y,rosso,verde,guardia)
    
    return y,guardia,mess

def controllosx(immagine,x,lung,y,rosso,verde,guardia):
    if dentro(immagine,x,y-lung)==True and immagine[y-lung][x]!=rosso and immagine[y-lung][x]!=verde :
        guardia=3
   
    elif dentro(immagine,x,y+lung)==True and immagine[y+lung][x]!=rosso and immagine[y+lung][x]!=verde :
        guardia=1
    elif dentro(immagine,x-lung,y)==True and immagine[y][x-lung]!=rosso and immagine[y][x-lung]!=verde :
        guardia=2
    else:
        guardia=4
    return guardia

def versosx(immagine,x,y,rosso,verde,lung,mess):
    guardia=0
    while dentro(immagine,x,y)==True and immagine[y][x]!= rosso and immagine[y][x]!= verde:
        cambiocolore(x,y,verde,immagine,lung)
        mess+="2"
        x-=lung
    x+=lung
    guardia=controllosx(immagine,x,lung,y,rosso,verde,guardia)
    return x,guardia,mess


def controllosu(immagine,x,lung,y,rosso,verde,guardia):
    if dentro(immagine,x+lung,y)==True and immagine[y][x+lung]!=rosso and immagine[y][x+lung]!=verde :
        guardia=0
    
    elif dentro(immagine,x-lung,y)==True and immagine[y][x-lung]!=rosso and immagine[y][x-lung]!=verde :
        guardia=2
    elif dentro(immagine,x,y-lung)==True and immagine[y-lung][x]!=rosso and immagine[y-lung][x]!=verde :
        guardia=3
    else:
        guardia=4
    return guardia
        
def versosu(immagine,x,y,rosso,verde,lung,mess):
    guardia=0
    while dentro(immagine,x,y)==True and immagine[y][x]!= rosso and immagine[y][x]!= verde:
        cambiocolore(x,y,verde,immagine,lung)
        mess+="3"
        y-=lung
    y+=lung
    guardia=controllosu(immagine,x,lung,y,rosso,verde,guardia)
    
    return y,guardia,mess

def dentro (immagine,i,j):
    iw=len(immagine[0])
    ih=len(immagine)
    if 0<=i<iw and 0<=j<ih:
        return True
    else:
        return False

def cambiocolore(x,y,c,immagine,lung):
    for j in range(y,y+lung):
        for i in range(x,x+lung):
            immagine[j][i]=c


def cammino(fname,  fname1):
    immagine=load(fname)
    blu=(0,0,255)
    verde=(0,255,0)
    rosso=(255,0,0)
    bianco=(255,255,255)
    nero=(0,0,0)    
    x=0
    y=0
    lung=40
    guardia=0
    cambiocolore(x,y,verde,immagine,lung)
    mess=''
    for i in range(0,9000):
            if guardia==0:
                    x,guardia,mess=versodx(immagine,x+lung,y,rosso,verde,lung,mess)
            elif guardia==1:
                    y,guardia,mess=versogiu(immagine,x,y+lung,rosso,verde,lung,mess)
            elif guardia==2:
                    x,guardia,mess=versosx(immagine,x-lung,y,rosso,verde,lung,mess)
            elif guardia==3:
                    y,guardia,mess=versosu(immagine,x,y-lung,rosso,verde,lung,mess)
            else:
                cambiocolore(x,y,blu,immagine,lung)
                break
    save(immagine,fname1)
    return mess

    

 


    
    
            
    
        
