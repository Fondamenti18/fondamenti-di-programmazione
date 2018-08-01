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
'''


from immagini import *
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)

def trovacoo(fname,x,y):
    alsi=x-sezionesinistra(fname,x,y)+1,y-sezionesopra(fname,x,y)+1
    
    bade=x+sezionedestra(fname,x,y)-1,y+sezionesotto(fname,x,y)-1
    c=list(alsi),list(bade)
    for i in range(len(c)):
        for g in range(len(c[i])):
            if c[i][g]==1:
                c[i][g]-=1
    return c
def sezionesopra(fname,x,y):
    a=load(fname)
    c=0
    for i in range(len(a)):
        if y-i<=0:
            break
        if a[x][y-i]==trovacolore(fname,x,y):
            c+=1
        else:
            break
    return c
def sezionesotto(fname,x,y):
    a=load(fname)
    c=0
    for i in range(len(a)):
        if y+i>=len(a[0]):
            break
        if a[x][y+i]==trovacolore(fname,x,y):
            c+=1
        else:
            break
    return c
def sezionesinistra(fname,x,y):
    a=load(fname)
    c=0
    for i in range(len(a)):
        if x-i<=0:
            break
        if a[x-i][y]==trovacolore(fname,x,y):
            c+=1
        else:
            break
    return c

def sezionedestra(fname,x,y):
    a=load(fname)
    c=0
    for i in range(len(a)):
        if i+x>=len(a):
            break
        if a[x+i][y]==trovacolore(fname,x,y):
            c+=1
        else:
            break
    return c


def colquad(fname,x,y,c,c1,fnameout):
    z=trovacoo(fname,x,y)[0][0]
    v=trovacoo(fname,x,y)[1][0]
    u=trovacoo(fname,x,y)[0][1]
    t=trovacoo(fname,x,y)[1][1]
    a=load(fname)
    area=2500
    semiperimetro=0
    for j in range(z,v+1,1):
        for k in range(u,t+1,1):
            creaquadrato(a,j,k,1,c)
    for i in range(len(a)):
        if a[z][i]==c:
            a[z][i]=c1
        if a[i][z]==c:
            a[i][z]=c1
        if a[v][i]==c:
            a[v][i]=c1
        if a[i][v]==c:
            a[i][v]=c1
        if a[u][i]==c:
            a[u][i]=c1
        if a[i][u]==c:
            a[i][u]=c1
        if a[t][i]==c:
            a[t][i]=c1
        if a[i][t]==c:
            a[i][t]=c1
        semiperimetro+=1
    b=a.copy()
    save(b,fnameout)
    
    perimetro=(semiperimetro*2)-4
    area=area-perimetro
    h=area,perimetro
    return h
    

def creaquadrato(img,x,y,lato,c):
    for i in range(lato):
        for j in range(lato):
            img[y+j][x+i]=c
            
def trovacolore(fname,x,y):
    a=load(fname)
    return a[x][y]
        
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    x=[]        
    for i in lista:
        x.append(colquad(fname,i[0],i[1],i[2],i[3],fnameout))
    return x