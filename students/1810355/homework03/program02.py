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

stringa=""
def cammino(fname,  fname1):
    global stringa
    
    img=load(fname)
    altezza=len(img)
    larghezza=len(img[0])
    stringa=""
    rosso=(255,000,000)
    verde=(000,255,000)
    
    
    def dis(img,x,y,c):
        for j in range (y,y+40):
                
                for h in range(x,x+40):
                    img[j][h]=c
        
        
 
    
    
    
    
    
  
    def disegna(img,x,y,c,r):
        global stringa
        if r > 4:
            dis(img,x-40,y,(000,000,255))
            #print(x,y)
            
            return 0   
        
         
        if x==600:
            disegna2(img,x-40,y+40,c,r+1)
            return 0
            
            
            
        if   img[y][x]==rosso or img[y][x]==verde  :
            disegna2(img,x-40,y+40,c,r+1) 
                
            return 0 
        
        else:
                   
            for j in range (y,y+40):
                
                for h in range(x,x+40):
                    img[j][h]=c
            stringa+="0"           
            disegna(img,x+40,y,c,0,)
        
    def disegna2(img,x,y,c,r):
        global stringa
        
        if y==600:
            disegna3(img,x-40,y-40 ,c,r+1)
            return 0
        
        if img[y][x]==rosso or img[y][x]==verde  :
           disegna3(img,x-40,y-40,c,r+1) 
           
           return 0
       
        
            
        else:
            
            for j in range (y,y+40):
                
                for h in range(x,x+40):
                    img[j][h]=c
            stringa+="1"
            disegna2(img,x,y+40,c,0)
 
    def disegna3(img,x,y,c,r):
        global stringa
        
        if img[y][x]==rosso or   img[y][x]==verde or x<0: 
            disegna4(img,x+40,y-40,c,r+1)
            
            return 0
        
        if x==0:
            dis(img,x,y,verde)
            stringa+="2"                             
            disegna4(img,x,y-40,c,r+1)
               
            return 0
        else:
            
            for j in range (y,y+40):
                
                for h in range(x,x+40):
                    img[j][h]=c
            stringa+="2"
            disegna3(img,x-40,y,c,0)
   
    def disegna4 (img,x,y,c,r):
        global stringa
        if img[y][x]==rosso or img[y][x]==verde or y<0 :
            disegna(img,x+40,y+40,c,r+1)
            
            return 0
        if y==0:
            dis(img,x,y,verde)
            stringa+="3"
            disegna(img,x+40,y,c,r+1)
           
            return 0
        else:
            
            for j in range (y,y+40):
                
                for h in range(x,x+40):
                    img[j][h]=c
            stringa+="3"
            disegna4(img,x,y-40,c,0)
            
    
    disegna(img,0,0,(0,255,000),0)
    save(img,fname1)
    n=stringa[1:]
    return (n)



