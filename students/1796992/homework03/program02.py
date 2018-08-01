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


rosso=(255, 0, 0)
verde=(0,255,0)
blu=(0,0,255)
r=0
c=0
ris=[]
def inside(i, x, y) :
    return 0 <= c < len(i[0]) and 0 <= r < len(i[0])
def colora_verde(i, c, r,colore=verde):
    for px in range(c, c+len(i[0])):
        for py in range(r, c+len(i[0])):
            if inside(i,px,py):
                i[py][px] = colore

def draw_rect(x, y,colore=verde):
    for px in range(x, x+40):
        for py in range(y, y+40):
            if inside(i,px,py):
                i[py][px] = colore
def cammino(fname,fname1):
    
    global c,r,i
    i=immagini.load(fname)
    while i[r][c]!=verde:
        while i[r][c]!=rosso and inside(i,c,r):
            draw_rect(c,r)
            c+=40  
            ris.append('0')
        c-=40
        ris.remove('0')
                    
        while i[r][c]!=rosso and inside(i,c,r):
            draw_rect(c,r)
            r+=40
            ris.append('1')
        r-=40
        ris.remove('1')
           
        while i[r][c]!=rosso and inside(i,c,r):
           draw_rect(c,r)
           c-=40 
           ris.append('2')
        c+=40
        ris.remove('2')
        
        while i[r][c]!=rosso and inside(i,c,r):
            if i[r-40][c]!=verde:
                draw_rect(c,r)
                r-=40
                ris.append('3')
            else:
                draw_rect(c,r,blu)
                break
        r+=40
        a=''.join(ris)
        immagini.save(i,fname1)
        return(a)
    
    
    
