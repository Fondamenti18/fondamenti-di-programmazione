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

import png
def draw_quad(img,x,y,w,h,c):
    for j in range(y,y+h):
        for i in range(x,x+w):
            if  inside(img,i,j):
                img[j][i] = c
def inside(img,i,j):
    iw ,ih = len(img[0]),len(img)
    return 0 <= i < iw and 0 <= j < ih

#def cammino(fname,  fname1):
'''Implementare qui la funzione'''


def save(filename,img):
        '''salva un'immagine in formato png'''
        pyimg=png.from_array(img,'RGB')
        pyimg.save(filename)
        return

# inizio programma >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def cammino(fname,fname1):
    import time

    with open(fname, mode='rb') as f:
            reader = png.Reader(file=f)
            w, h, png_img, _ = reader.asRGB8()
            img = []
            for line in png_img:
                l = []
                for i in range(0, len(line), 3):
                    l+=[(line[i], line[i+1], line[i+2])]
                img+=[l]
    E=[0,40]
    W=[0,-40]
    N=[-40,0]
    S=[40,0]
    px=20
    py=20
    i=0
    vecchie_pos=()
    passi=''
    passo='0'
    fine='True'
    rosso=(255,0,0)
    direzione=E
    draw_quad(img,0,0,40,40,(255,0,0))
    while fine:
        p1=px
        p2=py
        px=px+direzione[0]
        py=py+direzione[1]
        vecchie_pos=vecchie_pos+(p1,p2)
        time.sleep(0.1)
        if i >2 :
            fine='False'
            break
        if img[px][py]==rosso or py < 20 or py > 580 :
            i=i+1
            px=px-direzione[0]
            py=py-direzione[1]
            px=p1
            py=p2
            if i == 2 :
                fine='False'
                numero_passi=len(passi)
                for k in range (numero_passi+1):
                    i=k*2
                    draw_quad(img,vecchie_pos[i+1]-20,vecchie_pos[i]-20,40,40,(0,255,0))
                draw_quad(img,vecchie_pos[i+1]-20,vecchie_pos[i]-20,40,40,(0,0,255))
                break
            if direzione==E: 
                  direzione =S
                  passo='1'
                  px=px + direzione[0]
                  py=py + direzione[1]
            elif direzione==S:
                 direzione =W
                 passo='2'
                 px=px + direzione[0]
                 py=py + direzione[1]
            elif direzione==W:
                 direzione=N
                 passo='3'
                 px=px + direzione[0]
                 py=py + direzione[1]
            else:
                 direzione==N
                 direzione=E
                 passo='0'
                 
        else:
            i=0
        passi=passi+passo
    save(fname1,img)
    return passi
