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
from immagini import load,save
def matrice(f,s):
    i=[[]for x in range(s)]
    r=0
    while r in range(0,len(f)):
        for x, c in enumerate(range(0,len(f[0]),40)):
            i[x]+=[int((f[c][r]==(255,255,255))or(f[c][r]==(0,0,0)))]
        r+=40
        if r>len(f):
            break
    i[0][0]=0
    return i
def color(f,pat,posi):
    for a,r in enumerate(pat):
        for b,v in enumerate(r):
            if v == 2:
                cposi = (a * 40, b * 40)
                for imga in range(0, 40):
                    for imgb in range(0, 40):
                        if (a, b) == posi:
                            f[cposi[0] + imgb][cposi[1] + imga] = (0,0,255)
                        elif (a, b)!= posi:
                            f[cposi[0] + imgb][cposi[1] + imga] = (0,255,0)
                        else:
                            break
    return f
def cammino(fname,  fname1):
    f=load(fname)
    m=matrice(f, 15)
    pat=matrice(f, 15)
    posi=(0, 0) 
    dire=(0, 1)
    p= ""
    pat[0][0] = 2
    c=int(pat[posi[0]][max(0,min(posi[1]-1,14))]==1)+\
            int(pat[max(0,min(posi[0]-1,14))][posi[1]]==1)+\
            int(pat[max(0,min(posi[0]+1,14))][posi[1]]==1)+\
            int(pat[posi[0]][max(0,min(posi[1]+1,14))]==1)
    while c>0:
        newposi = (max(0,min(posi[0] + dire[0], 14)),max(0,min(posi[1] + dire[1], 14)))
        nextc = m[newposi[0]][newposi[1]]
        patc = pat[newposi[0]][newposi[1]]
        if nextc*patc == 1:
            pat[newposi[0]][newposi[1]] = 2
            posi = (posi[0] + dire[0], posi[1] + dire[1])
            if dire==(1,0):
                p += '1'
            elif dire==(0,1):
                p += '0'
            elif dire==(-1,0):
                p += '3'
            else:
                p += '2'
        else:
            if dire==(1,0):
                dire = (0,-1)
            elif dire==(0,1):
                dire = (1,0)
            elif dire==(0,-1):
                dire = (-1,0)
            else:
                dire = (0,1)
        if int(pat[posi[0]][max(0,min(posi[1]-1,14))]==1)+\
            int(pat[max(0,min(posi[0]-1,14))][posi[1]]==1)+\
            int(pat[max(0,min(posi[0]+1,14))][posi[1]]==1)+\
            int(pat[posi[0]][max(0,min(posi[1]+1,14))]==1)<=0:
                break
    f=color(f,pat,posi)
    save(f,fname1)
    return p 

    
         
                        
            
    
    



    
   
    
    
    
    
