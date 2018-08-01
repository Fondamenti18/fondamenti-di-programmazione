'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco di una macchinetta che gira su una pista di formula 1.

Il gioco consiste in un percorso di gara, rappresentato da una griglia di caratteri (' '=vuoto, '#' = ostacolo,
 'A....Z' = auto, '|' = traguardo)
nella quale si trova la macchina del giocatore (un carattere 'A..Z'), che deve:
    correre attorno alla pista per un intero giro senza sbattere contro ostacoli o altre macchine
    superare il traguardo
    fermarsi senza sbattere

Il punteggio di gioco e' il numero di step che sono stati necessari a percorrere la gara e fermarsi senza sbattere.

Ad ogni istante il simulatore della macchinetta conosce:
    x, y:   la posizione della macchina sulla griglia di gioco
    dx, dy: la velocita' corrente della macchina
Ad ogni step della simulazione il giocatore puo' solo:
    incrementare di 1, decrementare di 1 o lasciare come sono i valodi dx, dy della velocita' (-1,0,+1)
corrispondentemente il simulatore:
    somma gli incrementi/decrementi alle due variabili dx,dy
    somma le velocita' dx,dy alla posizione x,y ottenendo la prossima posizione della macchina
    controlla se la nuova posizione e' vuota
        se la nuova posizione e' occupata (da un ostacolo o da un'altra macchina) il gioco termina senza completare la corsa
        altrimenti si sposta la macchina sulla nuova posizione
    se il traguardo e' stato superato e la macchina e' ferma (dx=dy=0) la gara termina
    altrimenti si riesegue un nuovo step (chiedendo al giocatore cosa fare)

Il programma che dovete realizzare e' l'AI che guida la macchina, che riceve come input:
    la griglia di gioco del passo precedente (comprese le altre macchine)
    la griglia di gioco del passo corrente (comprese le altre macchine)
    la posizione x,y della propria macchina
    la velocita' dx,dy della propria macchina
e deve produrre in output la coppia:
    ax, ay  variazione della velocita (coppia di valori -1,0,+1)
Il vostro programma DEVE terminare la propri esecuzione entro 1 secondo, pena la squalifica.

In questo esercizio la valutazione avverra' in due fasi (su almeno 3 piste di gara):
    giro di qualificazione: 
        la macchina gira sulla pista di gara da sola, senza altri concorrenti
        la classifica ottenuta determina la pole-position (ordine di partenza) per la fase successiva
        chi non completa il giro di qualificazione non partecipa al successivo torneo
    torneo ad eliminazione: 
        viene organizzato un torneo ad eliminazione in cui su tutte le piste di gara:
            le macchine partono a coppie A,B in ordine di pole-position crescente (tempi crescenti)
            vengono eseguite due gare, con A a sinistra e B a destra e viceversa
            l'auto vincente passa il turno (in caso di patta si continua la gara per altri N giri finche' uno dei due vince)
    La classifica finale determina i voti:
        per avere la sufficienza bisogna aver completato almeno il giro di qualificazione sulle diverse piste
        La classifica viene suddivisa in 14 fasce che corrispondono ai voti da 18 a 31 ed a ciascun programma viene assegnato il voto corrispondente
        Se il numero di valori diversi dei tempi ottenuti e' minore di 14 il voto sara' proporzionale alla posizione della macchina 
        nella graduatoria (con il primo che prende 31 e l'ultimo 18)

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti
'''

from random     import randint
fine=False
listaP=[]

def ai(griglia_corrente, griglia_precedente, x, y, dx, dy, car, verso, startx, starty):
    '''inserite qui il vostro codice'''
    global fine
    if griglia_corrente[y][x]== griglia_precedente[y][x] and startx==x and starty==y:
        fine=False
        listaP=[]
    if griglia_corrente[starty][startx+1]=='|':
        i=starty
        while griglia_corrente[i][startx+1]=='|':
            griglia_precedente[i][startx+2]='|'
            griglia_precedente[i][startx+3]='|'
            griglia_precedente[i][startx+4]='|'
            griglia_precedente[i][startx+5]='|'
            i+=1
        i=starty
        while griglia_corrente[i][startx+1]=='|':
            griglia_precedente[i][startx+2]='|'
            griglia_precedente[i][startx+3]='|'
            griglia_precedente[i][startx+4]='|'
            griglia_precedente[i][startx+5]='|'
            i-=1
        if (x,y)==(startx+6,starty):
            print('ARRIVATO!')
            fine=True
            ax=ay=0
            if dy>=1:ay=-1
            elif dy<=-1:ay=+1
            #if dx<-1:ax=+1
            #elif dx>=0:ax=-1
            ax=-1
            return ax,ay
        if fine and griglia_precedente[y][x]=='|':
            ax=ay=0
            if dy>=1:ay=-1
            elif dy<=-1:ay=+1
            if dx>1:ax=-1
            elif dx<=0:ax=+1
            return ax,ay
        if fine and x<=startx:
            ax=0
            if dx>0:ax=-1
            elif dx<0:ax=+1
            ay=0
            if dy>0:ay=-1
            elif dy<0:ay=+1
            return ax,ay
        #x1,y1=visit_tree(x,y,dx,dy,griglia_precedente,startx+6,starty)
        x1,y1=visit_tree(x,y,dx,dy,griglia_precedente,startx+6,starty,griglia_corrente,startx,starty)
        ax=x1-(x+dx)
        ay=y1-(y+dy)
        return ax, ay
    else:
        i=starty
        while griglia_corrente[i][startx-1]=='|':
            griglia_precedente[i][startx-2]='|'
            griglia_precedente[i][startx-3]='|'
            griglia_precedente[i][startx-4]='|'
            griglia_precedente[i][startx-5]='|'
            i+=1
        i=starty
        while griglia_corrente[i][startx-1]=='|':
            griglia_precedente[i][startx-2]='|'
            griglia_precedente[i][startx-3]='|'
            griglia_precedente[i][startx-4]='|'
            griglia_precedente[i][startx-5]='|'
            i-=1
        if (x,y)==(startx-6,starty):
            fine=True
            ax=ay=0
            if dy>=1:ay=-1
            elif dy<=-1:ay=+1
            ax-=1
            return ax,ay
        if (x,y)==(startx-5,starty):
            fine=True
            ax=ay=0
            if dy>=1:ay=-1
            elif dy<=-1:ay=+1
            ax+=0
            return ax,ay
        if (x,y)==(startx-4,starty):
            fine=True
            ax=ay=0
            if dy>=1:ay=-1
            elif dy<=-1:ay=+1
            ax+=1
            return ax,ay
        if fine and griglia_precedente[y][x]=='|':
            ax=ay=0
            if dy>=1:ay=-1
            elif dy<=-1:ay=+1
            if dx>1:ax=-1
            elif dx<=0:ax=+1
            return ax,ay
        if fine and x>=startx:
            ax=0
            if dx>0:ax=-1
            elif dx<0:ax=+1
            ay=0
            if dy>0:ay=-1
            elif dy<0:ay=+1
            return ax,ay
        #x1,y1=visit_tree(x,y,dx,dy,griglia_precedente,startx-6,starty)
        x1,y1=visit_tree(x,y,dx,dy,griglia_precedente,startx-6,starty,griglia_corrente,startx,starty)
        ax=x1-(x+dx)
        ay=y1-(y+dy)
        return ax, ay
    

    
def visit_tree(x,y,dx,dy,griglia,destx,desty,griglia_corrente,startx,starty):
    '''Ritorna l'albero di visita tramite un 
    dizionario che ad ogni nodo visitato, a partire
    dal nodo name, associa il nome del nodo che lo
    ha scoperto, cioè il nodo genitore.'''
    global listaP
    if griglia_corrente[y][x]== griglia[y][x] and startx==x and starty==y:
        visited=set([((x,y),(dx,dy))])
        active= set([((x,y),(dx,dy))])
        tree = {((x,y),(dx,dy)):((x,y),(dx,dy))}         
        while active:
            newactive = set() 
            while active:
                u, vel = active.pop()  
                for a in [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]:
                    v=u[0]+vel[0]+a[0],u[1]+vel[1]+a[1]
                    if  -5<=vel[0]+a[0]<=5 and -5<=vel[1]+a[1]<=5 and 0<v[1]<len(griglia) and 0<v[0]<len(griglia[0]) and\
                    griglia[v[1]][v[0]] in ' ' and (v,(vel[0]+a[0],vel[1]+a[1])) not in visited:
                        visited.add((v,(vel[0]+a[0],vel[1]+a[1])))
                        newactive.add((v,(vel[0]+a[0],vel[1]+a[1])))
                        # Associa al nodo v al genitore
                        tree[(v,(vel[0]+a[0],vel[1]+a[1]))] = (u,vel)
                        if v==(destx,desty):
                            v=(v,(vel[0]+a[0],vel[1]+a[1]))
                            while tree[v]!=((x,y),(dx,dy)):
                                listaP+=[v[0]] 
                                v=tree[v]
                            listaP.reverse()
                            return v[0]
            active=newactive
    else:
       x=listaP[0]
       del listaP[0] 
       return x
        
def visit_tree1(x,y,dx,dy,griglia,destx,desty):
    '''Ritorna l'albero di visita tramite un 
    dizionario che ad ogni nodo visitato, a partire
    dal nodo name, associa il nome del nodo che lo
    ha scoperto, cioè il nodo genitore.'''
    visited=set([((x,y),(dx,dy))])
    active= set([((x,y),(dx,dy))])
    tree = {((x,y),(dx,dy)):((x,y),(dx,dy))}         
    while active:
        newactive = set() 
        while active:
            u, vel = active.pop()  
            for a in [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]:
                v=u[0]+vel[0]+a[0],u[1]+vel[1]+a[1]
                if  -4<=vel[0]+a[0]<=4 and -4<=vel[1]+a[1]<=4 and 0<v[1]<len(griglia) and 0<v[0]<len(griglia[0]) and\
                griglia[v[1]][v[0]] in ' ' and (v,(vel[0]+a[0],vel[1]+a[1])) not in visited:
                    visited.add((v,(vel[0]+a[0],vel[1]+a[1])))
                    newactive.add((v,(vel[0]+a[0],vel[1]+a[1])))
                    # Associa al nodo v al genitore
                    tree[(v,(vel[0]+a[0],vel[1]+a[1]))] = (u,vel)
                    if v==(destx,desty):
                        v=(v,(vel[0]+a[0],vel[1]+a[1]))
                        while tree[v]!=((x,y),(dx,dy)): 
                            v=tree[v]
                        return v[0]
        active=newactive
 

        
