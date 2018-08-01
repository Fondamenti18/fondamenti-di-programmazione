import sys

lastdist=9999

#ritorna il numero di passi del cammino minimo
def get_steps(precedente,partenza,dest):
    cnt=1
    attuale=dest
    while True:
        if attuale==partenza:break
        cnt+=1;attuale=precedente[attuale]
    return cnt

#ritorna gli adiacenti di un punto (raggiungibili)
def get_adiacenti(riga,colonna,altezza,larghezza,matrice_circuito):
    adiacenti={}
    for irig in range(-1,2):
        ind1=riga+irig;
        if inside(ind1,altezza):
            for icol in range(-1,2):
                ind2=colonna+icol
                if matrice_circuito[ind1][ind2]!= sys.maxsize and inside(ind2,larghezza):
                    adiacenti[(ind1,ind2)] = matrice_circuito[ind1][ind2]
    return adiacenti

#ritorna true se il punto e dentro il circuito
def inside(b,k):
    return 0<=b<k

def get_grafo(non_visitati,partenza):
    grafo={}
    for nodo in non_visitati:
        grafo[nodo] = sys.maxsize
    grafo[partenza]=0
    return grafo
    
#funzione globale per la ricerca del cammino minimo
def cammino_minimo(dizionario,dest,partenza):

    precedente={}
    non_visitati=dizionario.copy()
    grafo=get_grafo(non_visitati,partenza)

    while len(non_visitati)>0:
        prossimo=''
        
        for nodo in non_visitati:
            if prossimo == '': prossimo = nodo
            elif grafo[nodo] < grafo[prossimo]:prossimo = nodo

        for adiacente,peso in dizionario[prossimo].items():
            if grafo[adiacente] > grafo[prossimo]+peso:
                precedente[adiacente]= prossimo
                grafo[adiacente]= grafo[prossimo]+peso
                
        non_visitati.pop(prossimo)

    return get_steps(precedente,partenza,dest)

#ritorna una griglia che contiene 'numeri', ossia pesi per la ricerca con i nodi
def pesa_griglia(griglia,car):
    griglia_pesata=[]
    ins=set([' ','O',car])
    for riga in griglia:
        riga_pesata=[]
        for col in riga:
            if col in ins: riga_pesata+=[1]
            else: riga_pesata+=[sys.maxsize]
        griglia_pesata+=[riga_pesata]
    return griglia_pesata

#prepara una struttura dati utile per l algoritmo di ricerca del cammino minimo
def dizionario_pesi(matrice_circuito):
    
    dizionario = {}
    altezza=len(matrice_circuito)
    larghezza= len(matrice_circuito[0])

    for riga in range(altezza):
        for colonna in range(larghezza):
            if matrice_circuito[riga][colonna]!=sys.maxsize:
                dizionario[(riga, colonna)]=get_adiacenti(riga,colonna,altezza,larghezza,matrice_circuito)

    return dizionario

#ritorna l insieme dei punti adiacenti raggiungibili da un punto ad una data velocità
def get_punti(griglia_corrente,vx,vy,x,y):
    lim1=len(griglia_corrente);lim2=len(griglia_corrente[0])
    punti=set()
    for iy in range(-1,2):
        ky=vy+y+iy  
        if inside(ky,lim1):
            for ix in range(-1,2):           
                kx=vx+x+ix
                if inside(kx,lim2) and griglia_corrente[ky][kx]==' ':
                    punti.add((ky,kx,iy,ix,vy+iy,vx+ix))
    return punti


#riutorna i punti adiacenti in cui si avra almeno una possibilità di restare
#in strada per i prossimi 10 passaggi
def cerca_punti(griglia_corrente,car,strdest,pos):
    punti=get_punti(griglia_corrente,pos[5],pos[4],pos[1],pos[0])

    possibili=set()

    for punto in punti:
        x=punto[5];y=punto[4];
        if x<0: x=x*-1;
        if y<0: y=y*-1;
        massimo=max([x,y])
        cnt=insegui_punto(griglia_corrente,punto,0,0,massimo)
        if cnt>0: possibili.add(punto)

    return possibili

#funzione ricorsiva per cerca_punti() che analizza tutti i path 'figli'
def insegui_punto(griglia_corrente,pos,lim,cnt,k):
    if cnt>0 or lim==k :return 1
    
    punti=get_punti(griglia_corrente,pos[5],pos[4],pos[1],pos[0])
    
    if lim<k:
        for punto in punti:
            cnt+=insegui_punto(griglia_corrente,punto,lim+1,cnt,k)
          
    return cnt

def deve_frenare(laps,vx,vy):
    return (laps>0 or  lastdist<progressione(vx)) and (vx!=0 or vy!=0)

#ritorna il punto piu vicino all arrivo, data una lista
def get_migliore(possibili,dest,dizionario,vx,vy,laps):

    global lastdist
    tuplabest=(0,0,0,0,0,0);minlen=sys.maxsize;
    tuplaworst=(0,0,0,0,0,0);maxlen=-99;
    
    for punto in possibili:
        lung=cammino_minimo(dizionario,dest,(punto[0],punto[1]))
        if minlen>lung:minlen=lung;tuplabest=punto
        if maxlen<lung:maxlen=lung;tuplaworst=punto

    if deve_frenare(laps,vx,vy):
        if -2<vx<2 and -2<vy<2:return vx*-1,vy*-1
        lastdist=maxlen
        return tuplaworst[3],tuplaworst[2]

    lastdist=minlen;    
    return tuplabest[3],tuplabest[2]


#ritorna la destinazione
def get_dest(starty,startx,verso):
    dest=(starty,startx-2)
    if verso<0:dest=(starty,startx+2)
    return dest

#ritorna un fattore che determina quando incominciare a frenare prima del traguardo
def progressione(l):
    n=1;
    if l<0:l=l*-1
    while n<l: n=n*(n+1)//2; n+=1
    return(n-1)*l

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):

    #ritorna la destinazione puntata
    dest=get_dest(starty,startx,verso)

    #ritorna i punti raggiungibili flaggati come sicuri,
    #ossia punti in cui si avrà sempre almeno 1 possibilità di non andare fuoristrada per i prossimi 10 passaggi 
    possibili=cerca_punti(griglia_corrente,car,dest,(y,x,0,0,vy,vx))

    griglia_pesata=pesa_griglia(griglia_corrente,car)
    dizionario=dizionario_pesi(griglia_pesata)    

    #senno sceglie il punto tra i possibili piu vicino alla destinazione
    return get_migliore(possibili,dest,dizionario,vx,vy,laps)
