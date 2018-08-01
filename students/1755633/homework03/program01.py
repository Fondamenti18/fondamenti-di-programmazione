'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contine un immagine in formato png della  tipologia appena descritta.
- una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0 e 255 compresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e colore C interamente visibile nell'immagine.
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione
all'interno dell'immagine del punto in alto a sinistra del quadrato.

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine.

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''

from immagini import *


def altezza(img):   #ritorna altezza (pixel) img ->inside()
    #print(img)
    return len(img)

def larghezza(img):    #ritorna larghezza(pixel) img  ->inside
    return len(img[0])

def inside(a,l,img):    #ritorna vero se il pixel è dentro l immagine altrimento falpb
    #print(img)
    a_img=altezza(img)
    l_img=larghezza(img)
    return 0 <=  a  < a_img and 0 <=  l  < l_img


def check_lati(xv,yv,i,c,img,img1):
    #print('qua1')
    #if xv==100 and yv==40:
    #----colora(xv,yv,1,(0,100,100),img1)
    for _ in range(xv,xv+i):
        #print('qua2')
        if img[yv+i][_]!=c:  #yfissa e x varia
            stop=True
            return stop
    for _1 in range(yv,yv+i):
        #print('qua3')
        #print(xv,'-',_)
        if img[_1][xv+i]!=c:
            stop=True
            return stop
    stop=False
    return stop

def save(name,fds): #salva img1 su disco
    pyfds=png.from_array(fds,'RGB')
    pyfds.save(name)

def colora(x,y,lun,c,img1):   #colora il quadrato 40x40 pixel nell img1 di colore blu='b' o verde='v'!='b'

    for _ in range(y,y+lun):
        for _1 in range (x,x+lun):
            img1[_][_1]=c


def quadrato(filename,c):
    img=load(filename)
    alt=altezza(img)
    larg=larghezza(img)
    img1=img

    print('altezza-',alt,'larghezza',larg)
    lato=0
    conty=0
    i=0
    while(conty<alt):#for _ in range (0,alt):
        contx=0
        #--------print('ciao')
        #x=contx

        while(contx<larg):#for _1 in range(0,larg):
            #--print('pro')
            #print(_1,'0')
            #print(_,'righe')
            if img[conty][contx]==c: #se è un vertice, inizio di un quadrato
                x=contx
                y=conty
                #print('entra con',y,'-',x)
                #-------print('primacontrollo',y+1,'-',x+1)

                #if inside(y+1,x+1,img): #----------
                if 0 <=  y+1  < alt and 0 <=  x+1  < larg:   #------------bbbuona-----
                #if inside(y+i,x+i,img) and img[conty+i][contx+i]==c:   #------------inside del pizel diagonale successivo
                #if inside(y+lato,x+lato,img) and img[conty+lato][contx+lato]==c:
                    i=0

                    while True:
                        stop=False
                        #print('p')
                        #print(img[1][40])
                        #print('dopo',img[0][39])
                        #--------print(y,'-',x,'con i>',i)
                        #print(i)
                        if 0 <=  y+i  < alt and 0 <=  x+i  < larg: #inside del pizel diagonale successivo
                            if img[y+i][x+i]==c:   #pizel diagonale successivo è C
                                #------print('primo if')

                                stop=check_lati(x,y,i,c,img,img1)
                                #------print('stop',stop)
                                if stop!=True: #se i lati sono tutti di colore c
                                #print('secondo if')
                                    if i+1>lato:
                                        lato=i+1
                                        #print('coordi',x,'-',y)
                                        co=(x,y)
                                        rt=(lato,co)
                                else:
                                    #------print('terzo if')

                                    break
                                colora(x,y,1,(0,100,100),img1)
                                i+=1
                            else:

                                contx+=x+i+1  #opzione aggiunta
                                #conty+=y+i+1
                                break

                        else:
                            break
            contx+=1
        #conty+=i+1
        conty+=1


    #colora(100,50,60,(150,150,150),img1)
    l1,co=rt
    x1,y1=co
    colora(x1,y1,l1,(0,240,160),img1)
    img1[y1][x1]=(200,250,50)
    #img1[50][100]=(0,0,0)
    save('provaout.png',img1)
    print(rt)
    return rt



#c=(0,0,255)
#c=(255,0,0)
#c=(255,255,255)


#quadrato('Ist3.png',c)
