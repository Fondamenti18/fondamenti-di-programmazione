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
elif (perc[x+40][y] != (255,0,0)):
            colora(perc,y,x,40,40,(0,255,0))
            if(x+40 < 600):
                x=x+40
                ù
            while(perc[x][y] != (0,0,255)):
        
        if(perc[x][y] != (255,0,0)):
            if(perc[x][y+40] == (0,255,0)):
                #print('ciaao')
                colora(perc,y,x,40,40,(0,0,255))
                return [x,y]
            else:
                colora(perc,y,x,40,40,(0,255,0))
        else:
            print('ciao')
            colora(perc,y-40,x,40,40,(0,0,255))#guardare qua tolto il -40
            print(x,y)
            #print(perc[0][160])
            return [x,y-40] #tolto 40 per dare la pos prima 
            break
        if(y+40 < 600 -40 ):
            y=y+40
        else:
            #colora(perc,y+40,x,40,40,(0,0,255))
            print(x,y)
            #print(x,y)
            return [x,y+40]
            break
    print('ciaosss')
'''

from immagini import *
def righe(img) :
    return len(img)
def colonne(img) :
    return len(img[0])
def inside(img, x, y):
    return 0 <= y < righe(img) and 0 <= x < colonne(img)
def load(filename):
    with open(filename, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
    return img
def save(img, filename):
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)
    
def create(w,h,c=(0,0,0)):
    img = []
    for _ in range(h):
        riga = [] 
        for _ in range(w):
            riga+=[c]
        img+=[riga]
    return img

def colora(img, x, y, w, h, c):
    '''disegna sull'immagine img un rettangolo di colore c, ampiezza w e altezza h a partire dal pixel (y,x)'''
    for px in range(x, x+w):
        for py in range(y, y+h):
            #if inside(img,px,py):
            img[py][px] = c
def passo(perc,zx,zy):
    x=0+zx
    y=0+zy
    #print('ciao')
    
        #print('===?')
    #for x in range(x, len(perc),40):
    c=0
    if(0<=y <= 560):
        for y in range(y, len(perc),40):
        #print('ciao')
            if perc[x][y] != (255,0,0) and perc[x][y] != (0,255,0):
         #   print('ciao')
                colora(perc,y,x,40,40,(0,255,0))
                c+=1
            else:
                if c>0:
                    if zy == 0:
                        return [x+40,y-40,'0'*(c-1)]
                    else:
                        return [x+40,y-40,'0'*(c)]
                else:
                    return [x+40,y-40]
            if y == 560:
                #print('eeCOOO')
                if c>0:
                    if zy == 0:
                        c=c-1
                    return [x+40,y,'0'*c]
                else:
                    return [x+40,y]
                    break
        #print('ciaozzzz')
        return [x,y]
    else:
        #print('hooo0')
        return [x+40,y-40]
def giu(perc,zx,zy):
    x=0+zx
    y=0+zy
    c=0
    if(0<= x <= 560):
        for x in range(zx,len(perc),40):
        #print('===?')
        
        #for yy in range(y,-1,-40):
        #print('ciao')
        #print(x)
            if perc[x][y] != (255,0,0) and perc[x][y] != (0,255,0):
                #print('ciao')
                colora(perc,y,x,40,40,(0,255,0))
                c+=1
            else:
                #print(x)
                #print(perc[40][520])
                if c>0:
                    return [x-40,y-40,'1'*c]
                else:
                    return [x-40,y-40]
            if x == 560:
                #print(x)
                #print('ola')
                if c>0:
                    return [x,y-40,'1'*c]
                else:
                    return [x,y-40]
                    break
        #print(x)
        #print('ahahaha')
        return [x,y]
    else:
        #print(x)
        #print('oafe')
        return [x-40,y-40]
def sinistra(perc,zx,zy):
    x=0+zx
    y=0+zy
    #print('ciao')
    #print(x,y)
        #print('===?')
    #for x in range(x, len(perc),40):
    c=0
    if(560 >= x >= 0):
        for y in range(y,-1,-40):
        #print('ciao')
            if perc[x][y] != (255,0,0) and perc[x][y] != (0,255,0):
            #print('ciao')
                colora(perc,y,x,40,40,(0,255,0))
                c+=1
            else:
                #print(x,y)
                if c>0:
                    return [x-40,y+40,'2'*c]
                else:
                    return [x-40,y+40]
            if y == 0:
                if c>0:
                    return [x-40,y,'2'*(c)]
                else:
                    return [x-40,y]
                break

        return [x-40,y+40]
    else:
        print('ciao0')
        return [x,y]
def su(perc,zx,zy):
    x=0+zx
    y=0+zy
    c=0
    if(560 >= x >= 0):
        for x in range(zx,-1,-40):
        #print('===?')
        
        #for yy in range(y,-1,-40):
        #print('ciao')
        #print(x)
            if perc[x][y] != (255,0,0) and perc[x][y] != (0,255,0):
            #print('ciao')
                colora(perc,y,x,40,40,(0,255,0))
                #print('ciao')
                c+=1
            else:
                #print(x,y)
                #print(c)
                if c>0:
                    return [x+40,y+40,'3'*c]
                    #print(c)
                    #print(x+40,y+40)
                else:
                    return [x+40,y+40]
                #else:
                    #print('boh')
                    #print(x,y)
                    #return [x+40,y+40]
            if x == 0:
                #print('babe')
                if c>0:
                    return [x,y+40,'3'*c]
                else:
                    return [x,y+40]
                break
        return [x+40,y+40]
    else:
        #print('goku')
        if x > 560:
            if c>0:
                return [x-40,y,'3'*c]
            else:
                return [x-40,y]
        elif x < 0:
            if c>0:
                return [x+40,y+40,'3'*c]
            else:
                
                return [x+40,y+40] 

                    
                    
                    
def finito(lx,perc):
    if(  (perc[lx[0]][lx[1]+40] == (0,255,0) or perc[lx[0]][lx[1]+40] == (255,0,0)
              or lx[0] == 0 or lx[0] == 560 or lx[1] == 0 or lx[1]== 560) and
             (perc[lx[0]+40][lx[1]] == (0,255,0) or perc[lx[0]+40][lx[1]] == (255,0,0)
              or lx[0] == 0 or lx[0] == 560 or lx[1] == 0 or lx[1]== 560) and
             (perc[lx[0]][lx[1]-40] == (0,255,0) or perc[lx[0]][lx[1]-40] == (255,0,0)
              or lx[0] == 0 or lx[0] == 560 or lx[1] == 0 or lx[1]== 560) and
             (perc[lx[0]-40][lx[1]] == (0,255,0) or perc[lx[0]-40][lx[1]] == (255,0,0)
              or lx[0] == 0 or lx[0] == 560 or lx[1] == 0 or lx[1]== 560) ):
            #print('hey')
            colora(perc,lx[1],lx[0],40,40,(0,0,255))                    
def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    perc=load(fname)

    cod=''
    #save(perc,fname1)

    #for x in range(0,len(perc)):
        #for y in range(0,len(perc[x])):
            #if(perc[x][y] == (255,0,0)):
    #percorso(perc,0,0)
    #print(perc[0][120])


    ls=[]
    #lo stop per bordo funziona bene, bisogna ora fondere lo stop per colore
    ls=(passo(perc,0,0))
    
    if len(ls) == 3:
        cod+=ls[2]
    
    ld=giu(perc,ls[0],ls[1])
    if len(ld) == 3:
        #print('ciao')
        cod+=ld[2]
    
    #print(perc[40][80])
    
       
        #print('ciao')
    #print(ld)
    sin=sinistra(perc,ld[0],ld[1])
    if len(sin) == 3:
        cod+=sin[2]
    #print(sin)
    lsu=su(perc,sin[0],sin[1])#test2 il primo lsu non va su e quindi è giusto non dia il numero poiché non ha operato
    if len(lsu) == 3:
        cod+=lsu[2]
    #print(lsu)
    #print(cod)  #ultimo lavoro è aggiungere a tutti nel for i controlli
    #print(cod)
    for x in range(50):
    #print(ld)
    #print(sin)
    #print(lsu)
        ls=(passo(perc,lsu[0],lsu[1]))
        if len(ls) == 3:
            cod+=ls[2]
#destra
#giu
#sinistra
#su
        #print(ls)
        ld=giu(perc,ls[0],ls[1])
        if len(ld) == 3:
            cod+=ld[2]
        #print(ld)
        sin=sinistra(perc,ld[0],ld[1])
        if len(sin) == 3:
            cod+=sin[2]
        #print(sin)
        
        lsu=su(perc,sin[0],sin[1])
        if len(lsu) == 3:
            cod+=lsu[2]
        #print(lsu)
        #finito(lsu,perc)
    #print(lsu)
    colora(perc,lsu[1]-40,lsu[0],40,40,(0,0,255))
    #print(cod)
        #if(0,0,255) == perc[lsu[0]][lsu[1]]:
            #break
    #print(ls) #-40 +40
    #print(ld)
    #print(sin)
    #print(lsu)
    #[520, 560]
    #[480, 520]
    #[440, 560]
    #[0, 560]
    #
    #ls=(passo(perc,lsu[0],lsu[1]))
    #print(perc[560][160])
#destra
#giu
#sinistra
#su

    save(perc,fname1)
    return cod

    #save(verde,'prova.png')
    #print(perc)
    
#cammino('I3.png','t3.png')
