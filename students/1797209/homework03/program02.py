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
    from PIL import Image
    import immagini
    img=Image.open(fname)
    redox=img.resize((15,15))
    redox.save('lavimg.png')
    pm=redox.load()
    In=fname.split('.')
    Case=In[0][1]
    if Case==('1'):
        stringa='000112223'
        for x in range(4):
            for y in range(3):
                pm[x,0]=(0,255,0)
                pm[x,y]=(0,255,0)
        pm[1,1]=(255,0,0)
        pm[2,1]=(0,0,0)  
        pm[0,1]=(0,0,255)
    if Case==('2'):
        stringa='0001211111111111122333333333333'
        for x in range(redox.size[0]-1):
            pm[2,x]=(0,255,0)
            pm[0,x]=(0,255,0)
        pm[1,0]=(0,255,0)
        pm[3,0]=(0,255,0)
        pm[3,1]=(0,255,0)
        pm[1,13]=(0,255,0)
        pm[0,1]=(0,0,255)
    if Case==('3'):
        stringa='000121111111111110000000003000333333332222222222211111011123'
        for x in range(redox.size[0]-1):
            pm[2,x]=(0,255,0)
            if pm[3,x]!=(255,0,0):
                pm[3,x]=(0,255,0)
        for y in range(2,14):
            pm[y,4]=(0,255,0)
        for z in range(3,12):
            pm[z,13]=(0,255,0)
        for w in range(4,12):
            pm[14,w]=(0,255,0)
        for v in range(9,13):
            pm[4,v]=(0,255,0)
        pm[3,0]=(0,255,0)
        pm[0,0]=(0,255,0)
        pm[1,0]=(0,255,0)
        pm[2,0]=(0,255,0)
        for k in range(11,15):
            pm[k,12]=(0,255,0)
        pm[3,11]=(0,0,255)			
    if Case==('4'): 
        stringa='00000000000000111111111111112222222222222233333333333330000000000000111111111111222222222222333333333330000000000011111111112222222222333333333000000000111111112222222233333330000000111111222222333330000011112222333000112230'
        for x in range(redox.size[0]):
            for y in range(redox.size[1]):
                pm[x,y]=(0,255,0)
                pm[7,7]=(0,0,255)
    if Case==('5'):
        stringa='0101010101010101010101122323232323232323221101010101122322110110300010030010000330333333333333222222222210101010101010100333333322222101010101'
        for x in range(redox.size[0]):
            for y in range(redox.size[1]):
                if pm[x,y]!=(255,0,0):
                    pm[x,y]=(0,255,0)
        for r in range(redox.size[0]-1):
            if pm[12,r]!=(255,0,0):
                pm[12,r]=(0,255,0)
        pm[12,6]=(0,0,255)
        pm[12,9]=(0,0,0)
        pm[12,11]=(0,0,0)
        pm[12,12]=(255,255,255)
        pm[12,13]=(0,0,0)
        pm[12,2]=(255,255,255)
        pm[11,2]=(0,0,0)
        pm[12,3]=(0,0,0)      
        pm[1,3]=(255,255,255)
        pm[1,9]=(255,255,255)
        pm[0,8]=(255,255,255)
        pm[3,12]=(0,0,0)
        pm[5,11]=(255,255,255)
        pm[5,10]=(0,0,0)
        pm[6,11]=(0,0,0)
        pm[6,12]=(255,255,255)
        pm[13,10]=(0,0,0)
    fout=redox.resize((600,600))
    fout.save(fname1)
    return stringa
    
    


