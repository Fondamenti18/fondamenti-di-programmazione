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

from random     import randint

global percorso
global indice
global fine
global prossima_acc
fine=(0,0)
percorso=[]
indice=0
prossima_acc=(0,0)

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty,laps):
    global fine
    fine=(startx+(-2*verso),starty)
    if x==startx and y==starty:
        return 1*verso,0*verso
    return valuta_mossa(x,y,griglia_corrente, vx,vy,verso,laps)
    
def valuta_mossa(x,y,griglia_corrente,vx,vy,verso, laps=0,rec=0):
    diz={}
    if laps>0:
        if vx>0:
            if vy==0:
                accelerazioni={(-1,0),(0,0)}
            elif vy>0:
                accelerazioni={(-1,-1),(-1,0),(0,0)}
            elif vy<0:
                accelerazioni={(-1,1),(-1,0),(0,0)}
        elif vx<0:
            if vy==0:
               accelerazioni={(1,0),(0,0)}
            elif vy>0:
                accelerazioni={(1,-1),(1,0),(0,0)}
            elif vy<0:
                accelerazioni={(1,1),(1,0),(0,0)}
        elif vx==0:
            if vy==0:
               accelerazioni={(0,0)}
            elif vy>0:
                accelerazioni={(0,-1),(0,0)}
            elif vy<0:
                accelerazioni={(0,1),(0,0)}
    else:
        if vx>4:
            if vy>4:
                accelerazioni={(0,0),(-1,0),(0,-1),(-1,-1)}
            elif vy<-4:
                accelerazioni={(0,1),(0,0),(-1,0),(0,-1),(-1,-1),(-1,1)}
            else:
                if vy<0:
                    accelerazioni={(0,1),(0,0),(-1,0),(-1,1)}
                if vy>0:
                    accelerazioni={(0,0),(-1,0),(0,-1),(-1,-1)}
                else:
                    accelerazioni={(0,1),(0,0),(-1,0),(0,-1),(-1,-1),(-1,1)}
        elif vx<-4:
            if vy>4:
                accelerazioni={(1,0),(0,0),(0,-1),(1,-1)}
            elif vy<-4:
                accelerazioni={(1,0),(0,1),(0,0), (1,1),(1,-1)}
            else:
                if vy<0:
                    accelerazioni={(1,0),(0,1),(0,0),(0,-1), (1,1),(1,-1)}
                if vy>0:
                    accelerazioni={(1,0),(0,1),(0,0),(0,-1), (1,1),(1,-1)}
                else:
                    accelerazioni={(1,0),(0,1),(0,0),(0,-1), (1,1),(1,-1)}
        else:
            if vy>4:
                if vx<0:    
                    accelerazioni={(0,0),(-1,0),(0,-1),(-1,-1)}
                if vx<0:    
                    accelerazioni={(1,0),(0,0),(0,-1),(1,-1)}
                else:
                    accelerazioni={(1,0),(0,0),(-1,0),(0,-1),(-1,-1),(1,-1)}
                    
            elif vy<-4:
                if vx<0:    
                    accelerazioni={(1,0),(0,1),(0,0), (1,1),(-1,1)}
                if vx<0:    
                    accelerazioni={(0,1),(0,0),(-1,0), (1,1),(-1,1)}
                else:
                    accelerazioni={(1,0),(0,1),(0,0),(-1,0), (1,1),(-1,1)}
            else:
                accelerazioni={(1,0),(0,1),(0,0),(-1,0),(0,-1),(-1,-1), (1,1),(-1,1),(1,-1)}
    
    
    for ax, ay in accelerazioni:
        ny, nx =y+vy+ay, x+vx+ax
        if nx<0 or nx>=len(griglia_corrente[0]) or ny<0 or ny>=len(griglia_corrente):    continue
        if griglia_corrente[ny][nx]==' ':
            if rec<min(3,max(abs(vx),abs(vy))-1):
                try:
                    prossima=valuta_mossa(nx,ny,griglia_corrente, vx+ax,vy+ay, verso,laps, rec+1)
                except:
                    continue
            per=pathfinder(griglia_corrente, fine, (nx,ny))   
            if len(per) not in diz.keys() and len(per)!=0:
                diz[len(per)]=[]
            diz[len(per)].append((ax,ay))

    if laps>0 and rec==0:
        try:
            a=min(diz.keys())
            ax,ay=diz[a].pop()
            return ax,ay
        except:
            ax,ay=0,0
            if vx!=0:
                ax=int((-vx)/vx*verso)
            if vy!=0:
                ay=int((-vy)/vy*verso)
            return ax,ay
    
    a=min(diz.keys())
    ax,ay=diz[a].pop()
    return ax,ay
    
def pathfinder(img, start,end):
    w, h = len(img[0]),len(img)
    sx , sy = start
    color =img[sy][sx]
    visited= set([start])
    active=set([start])
    tree={start:None}
    while active and end not in visited:
        newactive = set()
        while active:
            x, y = active.pop()
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1),(1,1)]:
                ax,ay = x+dx, y+dy
                if ax<0 or ax>=w or ay<0 or ay>=h:  continue
                if img[ay][ax] not in {' ','O'}:    continue
                a=(ax,ay)
                if a in visited:    continue
                visited.add(a)
                newactive.add(a)
                tree[a]=(x,y)
        active=newactive
    if end not in visited:  return None
    p=path(tree, end)
    return p

def printPath(graph, n1, n2):
    tree= visitTree(graph, n1)
    p = path(tree, n2)
    return p
        
def path(tree, name):
    root=None
    for n, gen in tree.items():
        if gen == None:
            root = n
            break
    if name in tree:
        path=[name]
        while name!=root:
            name=tree[name]
            path.insert(0,name)
        return path
    else:
        return []