'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco di una macchinetta che gira su una pista di formula 1.

Il gioco consiste in un percorso di gara, rappresentato da una griglia di caratteri
(' '=vuoto, '#' = ostacolo, 'A....Z' = auto, '|' = traguardo 'O' = buca tutti gli altri caratteri sono ostacoli)
nella quale si trova la macchina del giocatore (un carattere 'A..Z'), che deve:
    correre attorno alla pista per un intero giro senza sbattere contro ostacoli o altre macchine
    raggiungere il traguardo
    fermarsi senza sbattere (vx=vy=0)

Il punteggio di gioco e' il numero di step che sono stati necessari a percorrere la gara e fermarsi senza sbattere.

Ad ogni istante il simulatore della macchinetta conosce:
    x, y:   la posizione della macchina sulla griglia di gioco
    vx, vy: la velocita' corrente della macchina
Ad ogni step della simulazione il giocatore puo' solo:
    incrementare di 1, decrementare di 1 o lasciare come sono i valodi vx, vy della velocita' (-1,0,+1)
corrispondentemente il simulatore:
    somma gli incrementi/decrementi alle due variabili vx,vy
    somma le velocita' vx,vy alla posizione x,y ottenendo la prossima posizione della macchina
    controlla se la nuova posizione e' vuota
        se la nuova posizione e' occupata (da un ostacolo o da un'altra macchina) il gioco termina senza completare la corsa
        se la posizione contiene una buca si slitta di un carattere a caso fino a restare sulla strada o su un ostacolo
        altrimenti si sposta la macchina sulla nuova posizione
    se il traguardo e' stato raggiunto nella direzione giusta e la macchina e' ferma (vx=vy=0) la gara termina
    altrimenti si riesegue un nuovo step (chiedendo alla funzione 'ai' del giocatore cosa fare)

Il programma che dovete realizzare e' l'AI che guida la macchina, che riceve come input:
    la griglia di gioco del passo precedente (comprese le altre macchine)
    la griglia di gioco del passo corrente (comprese le altre macchine)
    la posizione x,y della propria macchina
    la velocita' vx,vy della propria macchina
    il carattere che individua la vostra macchina
    il verso di rotazione (-1= si parte verso sinistra rispetto al traguardo, +1= si parte verso destra rispetto al traguardo)
    la posizione startx,starty di partenza della macchina
e deve produrre in output la coppia:
    ax, ay  variazione della velocita (coppia di valori -1,0,+1)
La simulazione di tutti i 3 percorsi di gara per la qualificazione (senza visualizzazione) deve impiegare al piu' 1 minuto.

In questo esercizio la valutazione avverra' in tre fasi:
    giro di qualificazione: 
        la macchina gira sulla pista di gara da sola, senza altri concorrenti su 3 piste in cui non sono presenti barriere di buche
        superare questa prova da' il punteggio minimo di qualificazione (18)
    giro di premio:
        la macchina gira su una pista di gara simile (ma diversa) da quella "Roma" che contiene barriere di buche
        superare questa prova da' il punteggio di qualificazione 24

    La classifica ottenuta nella qualificazione viene usata per determinare i gironi e poi il torneo di gara della fase successiva
    chi non completa il giro di qualificazione non partecipa al successivo torneo e non e' sufficiente

    Gironi e torneo ad eliminazione:
        (per ogni scontro vengono eseguite due gare, con A a sinistra e B a destra e viceversa)
        viene organizzato un torneo in cui prima si eseguono dei gironi di 4-5 auto
            Le due auto che ottengono il miglior punteggio sul girone partecipano alle eliminatorie successive
            Per ogni gara del girone vengono assegnati:
                3 punti a chi vince la gara
                1 punto per pareggio o scontro
                0 punti a chi perde
                a parita' di punteggio vince la macchina che ha fatto meno incidenti
                a parita' di incidenti viene simulata un'altra gara con una pista con barriere di buche (tipo "roma" per intenderci)

        Le due auto qualificate di ciascun girone partecipano ad una fase eliminatoria a scontro diretto
            l'auto vincente passa il turno (in caso di patta su esegue una gara aggiuntiva con barriere di buche casuali)

    La classifica finale della fase a scontro diretto determina i voti:
        I livelli del torneo ad eliminazione individuano i voti ottenuti, a seconda del numero di partecipanti (per esempio 6 livelli -> 2.1 voti per livello circa)
        Per avere la sufficienza bisogna aver completato almeno il giro di qualificazione sulle diverse piste
        Se una macchina ha ottenuto il voto 24 nella fase di qualificazione, il voto finale dell'esercizio e' almeno 24

COMPORTAMENTO: le auto che usano comportamenti scorrette non superano la qualificazione. Es.
    - precalcolare offline la strategia e inserirla nel programma
    - andare apposta contro l'auto dell'avversario
    - ...

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti

'''

from random import randint

inizioo=0
distSu=0
distGiu=0
distGiu=0
inversoX=False
traguardo=False

def prospettivaX(v1,griglia,x,y,verso):
    ''' funzione che mi dice se posso aumentare la velocita x '''
    global inversoX
    ris=0
    v=v1 + 1
    while v!=0:
        ris+=v
        v-=1
    for a in range(ris + 1):
            if griglia[y][x+a+1]=='#':
                if a==1: 
                    if verso==1:inversoX=True
                    else:inversoX=False
                ris2=0
                while v1!=0:
                    ris2+=v1
                    v1-=1
                for b in range(ris2 + 1):
                    if griglia[y][x+b+1]=='#': 
                        if verso==1:return 'de' # decelera
                        return 'ac'
                return 'ma' # mantieni
    if verso==1:return 'ac' # accelera
    return 'de'

def ctraguardo(griglia,y,x,vx):
    global traguardo
    for a in range(vx+1):
        if griglia[y][x+a]=='|': 
            traguardo=True
            return
        
def prospettivaXcontrario(v1,griglia,x,y,verso):
    ''' funzione che mi dice se posso aumentare la velocita x nel verso contrario'''
    global inversoX
    ris=0
    v=v1 + 1
    while v!=0:
        ris+=v
        v-=1
    for a in range(ris + 1):
        if griglia[y][x-a-1]=='#':
            if a==1:
                if verso==1:inversoX=False
                else:inversoX=True
            ris2=0
            while v1!=0:
                ris2+=v1
                v1-=1
            for b in range(ris2 + 1):
                if griglia[y][x-b-1]=='#': return 'de' # decelera
            return 'ma' # mantieni
    return 'ac' # accelera

def distanzaSu(griglia,x,y):
    d=0
    while griglia[y-d - 1][x]!='#':
        d+=1
    return d

def distanzaGiu(griglia,x,y):
    d=0
    while griglia[y+d + 1][x]!='#':
        d+=1
    return d

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty):
    '''inserite qui il vostro codice'''
    global inizioo,distSu,inversoX,distGiu,fgiu,traguardo
    risX,risY=0,0
    if vx==vy==0==inizioo:
        inizioo=1
        distSu=distanzaSu(griglia_corrente,x,y)
        return verso,0
    if vx==0: risX=0
    if not inversoX:
        if verso==1:
            rprosX=prospettivaX(abs(vx),griglia_corrente,x,y,verso)
        else: rprosX=prospettivaXcontrario(abs(vx),griglia_corrente,x,y,verso)
    else:
        if verso==1:
            rprosX=prospettivaXcontrario(abs(vx),griglia_corrente,x,y,verso)
        else: rprosX=prospettivaX(abs(vx),griglia_corrente,x,y,verso)   
    if rprosX=='ac':
        if vx>0 or (vx==0 and not inversoX): risX=1
        else: risX=-1
    elif rprosX=='ma': risX=0
    elif vx>0: risX=-1
    else: risX=1
    if not inversoX:
            ds=distanzaSu(griglia_corrente,x+risX-1,y)
            dg=distanzaGiu(griglia_corrente,x+risX-1,y)
    else:
        if verso==1:
            ds=distanzaSu(griglia_corrente,x-risX-1,y)
            dg=distanzaGiu(griglia_corrente,x-risX-1,y)
        else:
            ds=distanzaSu(griglia_corrente,x-risX+1,y)
            dg=distanzaGiu(griglia_corrente,x-risX+1,y)
    ri=abs(vy)+1
    vy2=abs(vy)
    while vy2!=0:
        ri+=vy2
        vy2-=1
    if ds>distSu: risY=-1
    elif ds<distSu: risY=1
    if griglia_corrente[y][x-1]=='#' or griglia_corrente[y][x+1]=='#':
        risY=0
    if ds==0:
        if dg>distGiu: risY=1
        elif dg<distGiu: risY=-1
        if griglia_corrente[y][x-1]=='#' or griglia_corrente[y][x+1]=='#':
            risY=0
    if vy>0:
        risY=0
        if griglia_corrente[y+1][x] =='#': risY=-1       
    distSu=ds
    distGiu=dg
    ctraguardo(griglia_corrente,y,x,vx)
    if traguardo: risX=-verso
    return risX,risY