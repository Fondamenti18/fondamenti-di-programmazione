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
        w= len(img[0])
        h= len(img)
        
        global lista
        lista=''
        
        nero=(0,0,0)
        bianco=(255,255,255)
        verde=(0,255,0)
        blu=(0,0,255)
        rosso=(255,0,0)
        
        global inizio_w
        inizio_w=0
        global fine_w
        fine_w=40
        global inizio_h
        inizio_h=0
        global fine_h
        fine_h=40
        
        global coord_fin
        coord_fin=[]
        
        for x in range(inizio_w,fine_w):
                for y in range(inizio_h,fine_h):
                        img[x][y]=verde
        
        def cam_dx(inizio_w,fine_w,inizio_h,fine_h):
            global coord_fin
            coord_fin=[inizio_w,fine_w,inizio_h,fine_h]
            s=0
            if fine_h>560:
                s=2
            if s==0:
                for x in range(inizio_w,fine_w):
                    for y in range(inizio_h+40,fine_h+40):
                        if img[x][y]==bianco:
                            img[x][y]=verde
                        elif img[x][y]==nero:
                            img[x][y]=verde
                        elif img[x][y]==verde:
                            s=2
                        elif img[x][y]==rosso:
                            s=2
            if s==0:
                try:
                    global lista
                    lista=lista+'0'
                    return cam_dx(inizio_w,fine_w,inizio_h+40,fine_h+40)
                except:
                    pass
            else:
                def cam_basso(inizio_w,fine_w,inizio_h,fine_h):
                    global coord_fin
                    coord_fin=[inizio_w,fine_w,inizio_h,fine_h]
                    s=0
                    if fine_w>560:
                        s=2
                    if s==0:
                        for x in range(inizio_w+40,fine_w+40):
                            for y in range(inizio_h,fine_h):
                                if img[x][y]==bianco:
                                    img[x][y]=verde
                                elif img[x][y]==nero:
                                    img[x][y]=verde
                                elif img[x][y]==verde:
                                    s=2
                                elif img[x][y]==rosso:
                                    s=2
                    if s==0:
                        try:
                            global lista
                            lista=lista+'1'
                            return cam_basso(inizio_w+40,fine_w+40,inizio_h,fine_h)
                        except:
                            pass
                    else:
                        def cam_sx(inizio_w,fine_w,inizio_h,fine_h):
                            global coord_fin
                            coord_fin=[inizio_w,fine_w,inizio_h,fine_h]
                            s=0
                            if inizio_h<=1:
                               s=2
                            if s==0:
                                for x in range(inizio_w,fine_w):
                                    for y in range(inizio_h-40,fine_h-40):
                                        if img[x][y]==bianco:
                                            img[x][y]=verde
                                        elif img[x][y]==nero:
                                            img[x][y]=verde
                                        elif img[x][y]==verde:
                                                    s=2
                                        elif img[x][y]==rosso:
                                            s=2
                            if s==0:
                                global lista
                                lista=lista+'2'
                                return cam_sx(inizio_w,fine_w,inizio_h-40,fine_h-40)
                            else:
                                def cam_su(inizio_w,fine_w,inizio_h,fine_h):
                                    global coord_fin
                                    coord_fin=[inizio_w,fine_w,inizio_h,fine_h]
                                    s=0
                                    if inizio_w<=1:
                                        s=2
                                    if s==0:
                                        for x in range(inizio_w-40,fine_w-40):
                                            for y in range(inizio_h,fine_h):
                                                if img[x][y]==bianco:
                                                    img[x][y]=verde
                                                elif img[x][y]==nero:
                                                    img[x][y]=verde
                                                elif img[x][y]==verde:
                                                    s=2
                                                elif img[x][y]==rosso:
                                                    s=2
                                    if s==0:
                                        global lista
                                        lista=lista+'3'
                                        listafin=lista
                                        return cam_su(inizio_w-40,fine_w-40,inizio_h,fine_h)
                                    else:
                                        return cam_dx(inizio_w,fine_w,inizio_h,fine_h)
                                    
                                cam_su(inizio_w,fine_w,inizio_h,fine_h)
                        cam_sx(inizio_w,fine_w,inizio_h,fine_h)
                cam_basso(inizio_w,fine_w,inizio_h,fine_h)
        cam_dx(inizio_w,fine_w,inizio_h,fine_h)
        
        for x in range(coord_fin[0],coord_fin[1]):
            for y in range(coord_fin[2],coord_fin[3]):
                img[x][y]=blu
        img=save(img,fname1)
        
        return lista









