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

def inside(img,x,y):
    return 0<=x<len(img[0]) and 0<=y<len(img)

def disegna_quadrato(img,x,y,s,c):
    for px in range(x,x+s):
        for py in range(y,y+s):
            if inside(img,px,py):
                img[py][px]=c
def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    l=[]
    imgc=load(fname)
    stringa=''
    lar=len(imgc[0])
    lun=len(imgc)
    riga=0
    colonna=0
    rotazione=0
    a='0'
  
    while(rotazione<4):
        if(a=='0' and colonna+40<lar and imgc[riga][colonna+40]!=(255,0,0) and imgc[riga][colonna+40]!=(0,255,0)):
            l+='0'
            disegna_quadrato(imgc,colonna,riga,40,(0,255,0))
            colonna+=40
            rotazione=0
           
                
        elif(a=='1' and riga+40<lun and imgc[riga+40][colonna]!=(255,0,0)and imgc[riga+40][colonna]!=(0,255,0)):
            l+='1'
            disegna_quadrato(imgc,colonna,riga,40,(0,255,0))
            riga+=40
            rotazione=0
            
                
        elif( a=='2' and colonna-40>=0 and imgc[riga][colonna-40]!=(255,0,0) and imgc[riga][colonna-40]!=(0,255,0)):
            l+='2'
            disegna_quadrato(imgc,colonna,riga,40,(0,255,0))
            colonna-=40
            rotazione=0
            
                
        elif(a=='3' and riga-1>=0 and imgc[riga-1][colonna]!=(255,0,0)and imgc[riga-1][colonna]!=(0,255,0)):
            l+='3'
            disegna_quadrato(imgc,colonna,riga,40,(0,255,0))          
            riga-=40
            rotazione=0
            
                
        else:
           
            if (a=='0' and riga+40<lun and imgc[riga+40][colonna]!=(255,0,0)and imgc[riga+40][colonna]!=(0,255,0)):
                a='1'
                l+='1'
                disegna_quadrato(imgc,colonna,riga,40,(0,255,0))     
                riga+=40
               
                
            elif (a=='1'and colonna-40>=0 and imgc[riga][colonna-40]!=(255,0,0) and imgc[riga][colonna-40]!=(0,255,0)):
                a='2'
                l+='2'
                disegna_quadrato(imgc,colonna,riga,40,(0,255,0))        
                colonna-=40
               
                
            elif (a=='2' and riga-40>=0 and imgc[riga-40][colonna]!=(255,0,0)and imgc[riga-40][colonna]!=(0,255,0)) :
                a='3'
                l+='3'
                disegna_quadrato(imgc,colonna,riga,40,(0,255,0))        
                riga-=40
               
                
            elif (a=='3'and colonna+40<lar and imgc[riga][colonna+40]!=(255,0,0) and imgc[riga][colonna+40]!=(0,255,0)):
                a='0'
                l+='0'
                disegna_quadrato(imgc,colonna,riga,40,(0,255,0))        
                colonna+=40
               
            
            else:
                if a=='0' :
                    a='1'
                    rotazione+=1
                elif a=='1' :
                    a='2'
                    rotazione+=1
                elif a=='2':
                    a='3'
                    rotazione+=1
                elif a=='3':  
                    a='0'
                    rotazione+=1
    print(len(l))               
    for i in range(0,len(l)):
        stringa+=l[i]
    disegna_quadrato(imgc,colonna,riga,40,(0,0,255))                 
    save(imgc,fname1)
    return stringa
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
