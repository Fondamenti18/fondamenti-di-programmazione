'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine.

Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e
registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista (nell'ordine),
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1,
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.

Per altri  esempi vedere il file grade03.txt

lunedi 14 funziona con grade03
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

def colora(x,y,cold,lpc,img,lpb,c,c1):
    t=(x,y)
    #global c, c1
    #print('primo',c,'secondo',c1)

    if cold==c: #(255,0,0):    #dest uguale a c
        lpc.append(t)
        img[y][x]=cold
    else:
        if img[y][x]!=c1: #(0,0,255): #dest o source diverso da c1
            lpb.append(t)
            img[y][x]=cold
    #img[y][x]=c

    return lpc,img,lpb


def check_adia(x,y,c,c0,lpc,img,img1,lpb,c1):
    #print('tipolista',type(lpc),'val:',lpc)
    #print('x,y-->',x,'--',y)
    #print(lpc)
    if not (x,y) in lpc:
        #print('qua')
        if inside(y,x,img):
            if img[y][x]==c0:
                #print('tipoprima colora',type(lpc),'val:',lpc)
                cold=c
                lpc,img1,lpb=colora(x,y,cold,lpc,img1,lpb,c,c1)
                #print('tipodopo  colora',type(lpc),'val:',lpc)
                cc1=False
                return cc1,lpc,img1,lpb
            else:
                cc1=True
                return cc1,lpc,img1,lpb
        else:
            cc1=True
            return cc1,lpc,img1,lpb
    cc1=False
    return cc1,lpc,img1,lpb


def incr(x,y,_,c,c1,c0,lpc,img,img1,lpb):    #scelta di estinazione destinazione
    #print('tipo',type(lpc))
    #print(_)
    if _==0:
        x=x+1
        cc1,lpc,img1,lpb=check_adia(x,y,c,c0,lpc,img,img1,lpb,c1)
        if cc1==True:
            cold=c1
            lpc,img1,lpb=colora(x-1,y,cold,lpc,img1,lpb,c,c1)
    elif _==1:
        y=y+1
        cc1,lpc,img1,lpb=check_adia(x,y,c,c0,lpc,img,img1,lpb,c1)
        if cc1==True:
            cold=c1
            lpc,img1,lpb=colora(x,y-1,cold,lpc,img1,lpb,c,c1)
    elif _==2:
        x=x-1
        #print('pass1')
        cc1,lpc,img1,lpb=check_adia(x,y,c,c0,lpc,img,img1,lpb,c1)
        #print('pass2')
        if cc1==True:
            cold=c1
            lpc,img1,lpb=colora(x+1,y,cold,lpc,img1,lpb,c,c1)
    elif _==3:
        y=y-1
        cc1,lpc,img1,lpb=check_adia(x,y,c,c0,lpc,img,img1,lpb,c1)
        if cc1==True:
            cold=c1
            lpc,img1,lpb=colora(x,y+1,cold,lpc,img1,lpb,c,c1)
    return lpc,img1,lpb

def save(name,fds): #salva img1 su disco
    pyfds=png.from_array(fds,'RGB')
    pyfds.save(name)

def connect(x,y,c,c1,img):

    img1=img
    #print('tipo',type(y),type(x))
    c0=img[y][x]
    lpc=list()
    lpb=list()
    lpc.append((x,y))
    #lpb.append((x,y))
    i=0
    img1[y][x]=c
    #for _1 in lpb:
    while (i<len(lpc)):

        #x,y=_1
        x,y=lpc[i]
        #---if i==0:
        #---    print('x,y entrata',x,'-',y)

        for _ in range (0,4):
            lpc,img1,lpb=incr(x,y,_,c,c1,c0,lpc,img,img1,lpb) #chiamata

        i+=1
    #save('prova.png',img1)
    #---print('lunghezza lpc',len(lpc))
    #---print('lunghezza lpb',len(lpb))
    print('-----')
    return img1, len(lpc), len(lpb)



#c=(255,0,0)
#c1=(0,0,255)
#connect(10,10,c,c1)


def ricolora(fname, lista, fnameout):
    ldati=list()
    i=0
    img=load(fname)
    img1=img
    while i<len(lista):
        #print('volta',lista)
        x,y,c,c1=lista[i]
    #x,y=lista[0][:-2]
    #c,c1=lista[0][2:]
    #global c,c1
    #print('x',x,'-y',y,'-c',c,'-c1',c1)
    #return
        #img=load(fname)
        img1,area,per=connect(x,y,c,c1,img)
        #ldati=[(area-per,per)]
        ldati.append((area-per,per))
        i+=1
    save(fnameout,img1)
    #area=area-per

    #ldati.append((area-per,per))
    return ldati   #ritorna lista
    #print('ppppppp',x,y,c,c1)

#ricolora('I1.png',[(10,10,(255,0,0),(0,0,255)),(90,10,(0,0,0),(0,255,0))],'test2.png')
#ricolora('I1.png',[(90,10,(0,0,0),(0,255,0)),(10,10,(255,0,0),(0,0,255))],'test2.png')
