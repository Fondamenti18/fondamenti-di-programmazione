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
    (NUOVO) il numero di attraversamenti del traguardo fatti dalla macchina (contromano se negativo)
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

import math

class _GraphNode:
    '''Rappresenta un nodo del grafo.
    Da usarsi solo all'interno di Graph.'''
    def __init__(self,name,adj,pos):
        self.name = name
        self.adj = set(adj)
        self.pos = pos
class Graph:
    '''Rappresenta un grafo.'''
    def __init__(self):
        '''Inizializza un grafo vuoto.'''
        self._nodes = {}
    
    def addNode(self, name, pos):
        '''Aggiunge un nodo name, se non esiste'''
        if name in self._nodes: return
        self._nodes[name]=_GraphNode(name,set(),pos)
    def addEdge(self, name1, name2):
        '''Aggiunge un arco che collega i nodi
        name1 e name2'''
        if name1 not in self._nodes: return
        if name2 not in self._nodes: return
        self._nodes[name1].adj.add(name2)
        self._nodes[name2].adj.add(name1)
    def adjacents(self, name):
        '''Ritorna una lista dei nomi dei nodi
        adiacenti al nodo name, se il nodo non
        esiste, ritorna None'''
        
        if name not in self._nodes: return None
        return list(self._nodes[name].adj)
    def nodes(self):
        '''Ritorna una lista dei nomi dei nodi'''
        return list(self._nodes.keys())
    def edges(self):
        '''Ritorna una lista degli archi'''
        edges = set()
        for name, node in self._nodes.items():
            for adj in node.adj:
                # salta archi ripetuti
                if (adj, name) in edges:
                    continue
                edges.add( (name,adj) )
        return list(edges)
    def pos(self, name):
        '''Ritorna la posizione del nodo name'''
        if name not in self._nodes: return None
        return self._nodes[name].pos

def parse_labyrinth(lines):
    '''Creare il grafo dei corridoi e il grafo dei
    muri a partire da un labirinto testulae.'''
   
    # Dimensioni del labirinto
    w, h = len(lines[0]), len(lines)
    # grafo di corridoi e muri
    corridors = Graph()
    walls = Graph()
    # aggiunta dei nodi
    for j in range(h):
        for i in range(w):
            # calcola la posizione
            pos = (i, j)
            # aggiungi il nodo ai corridoi o muri
            if lines[j][i] == ' ':
                corridors.addNode( (i,j), pos )
            else:
                walls.addNode( (i,j), pos )
    # aggiunta degli archi
    for j in range(h):
        for i in range(w):
            # itera sui possibili vicini
            adj = [(1,1),(1,-1),(-1,1),(-1,-1),(-1,0),(1,0),(0,-1),(0,1)]
            for di, dj in adj:
                # coordinate vicino
                ii, jj = i + di, j + dj
                if ii < 0 or jj < 0: continue
                if ii >= w or jj >= h: continue
                # verifica se entrambi sono corridoi
                if (lines[j][i] == ' ' and lines[jj][ii] == ' '):
                    corridors.addEdge((i,j),(ii,jj))
                # verifica se entrambi sono muri
                elif (lines[j][i] != ' ' and lines[jj][ii] != ' '):
                    walls.addEdge((i,j),(ii,jj))
    return corridors, walls
def distance(g, name):
    
    visited = set([name])
    active = set([name])
    # Dizionario delle distanze
    dist = {name:0}
    while active:
        newactive = set()
        while active:
            u = active.pop()
            
            for v in g.adjacents(u):
                if v not in visited:
                    visited.add(v)
                    newactive.add(v)
                    # Distanza del nodo visitato
                    dist[v] = dist[u] + 1
        active = newactive
    return dist


def h_score(coord,d_h):
    return d_h[coord]

def moveset(x,y,vx,vy,verso):
    if verso==1:
        return {(x+verso*vx,y+vy):(0,0), (x+verso*vx,y+vy+1):(0,1), (x+verso*(vx+1),y+vy):(1,0), (x+verso*vx,y+vy-1):(0,-1), (x+verso*(vx+1),y+vy+1):(1,1), (x+verso*(vx-1),y+vy-1):(-1,-1), (x+verso*(vx+1),y+vy-1):(1,-1), (x+verso*(vx-1),y+vy+1):(-1,1), (x+verso*(vx-1),y+vy):(-1,0)}      
    else:
        if vy>0:
            return { (x+vx,y+vy-1):(0,-1), (x+(vx-1),y+vy-1):(-1,-1),  (x+(vx+1),y+vy-1):(1,-1), (x+vx,y+vy):(0,0), (x+(vx-1),y+vy):(-1,0), (x+(vx+1),y+vy):(1,0), (x+(vx-1),y+vy+1):(-1,1), (x+vx,y+vy+1):(0,1), (x+(vx+1),y+vy+1):(1,1)}
        elif vy<0:
            return { (x+vx,y+vy+1):(0,1), (x+(vx+1),y+vy+1):(1,1), (x+(vx-1),y+vy+1):(-1,1), (x+vx,y+vy):(0,0), (x+(vx-1),y+vy):(-1,0), (x+(vx+1),y+vy):(1,0), (x+(vx-1),y+vy-1):(-1,-1),  (x+(vx+1),y+vy-1):(1,-1), (x+vx,y+vy-1):(0,-1)}
        else:
            return {(x+vx,y+vy):(0,0), (x+vx,y+vy+1):(0,1), (x+(vx+1),y+vy):(1,0), (x+vx,y+vy-1):(0,-1), (x+(vx+1),y+vy+1):(1,1), (x+(vx-1),y+vy-1):(-1,-1), (x+(vx+1),y+vy-1):(1,-1), (x+(vx-1),y+vy+1):(-1,1), (x+(vx-1),y+vy):(-1,0)}

def vel_min(mset,x,y,vx,vy):
    ris={}
    for j in mset.keys():
        vel=math.fabs(vx+mset[j][0])+math.fabs(vy+mset[j][1])
        ris[j]=vel
    return [k for k in ris.keys() if ris[k]==min([w for w in ris.values()])][0]
        


passati=[]
corridors=None

d_h=None
def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty,laps):
    
    
    global d_h
    global corridors
    global passati
    if len(passati)!=0 and (x,y) not in passati:
        passati.append((x,y))
    if laps>0:
        if vx>0:
            ax=-1
        elif vx<0:
            ax=1
        elif vx==0:
            ax=0
        if vy>0:
            ay=-1
        elif vy<0:
            ay=1
        elif vy==0:
            ay=0
        return ax,ay
    
    
    
    if x==startx and y==starty:
        passati=[(x,y)]
        
        corridors,walls=parse_labyrinth(griglia_corrente)
        
        
        
        if verso==1:
            d_h=distance(corridors,(startx-2,starty))
           
            
        else:
            d_h=distance(corridors,(startx+2,starty))
            
            
        return 1*verso, 0
    
    if verso==1 and startx-x<=5 and startx-x>=0 and math.fabs(starty-y)<10:
        if vx==0 and vy==0:
            return 1,0
        else:
            return 0,0
    if verso==-1 and x-startx<=2 and x-startx>=0 and math.fabs(starty-y)<10:
        if vx==0 and vy==0:
            return -1,0
        else:
            return 0,0
    
    else:
        
        mset=moveset(x,y,vx,vy,verso)
        
        l=list(mset.keys())
        for j in l:
            if j not in corridors._nodes.keys() or h_score(j,d_h)>=h_score((x,y),d_h) or j in passati:
                del mset[j]
        if vx==0 and vy==0:
            for j in l:
                if j in mset.keys() and mset[j]==(0,0):
                    del mset[j]
        prox=vel_min(mset,x,y,vx,vy)
        
        
        ris=(mset[prox][0], mset[prox][1])
        
        newcoord=(x+verso*(vx+ris[0]),y+vy+ris[1])
        
        
        new_mset=moveset(newcoord[0],newcoord[1],vx+ris[0],vy+ris[1],verso)
        for x in new_mset.keys():
            if x in corridors._nodes.keys():
                
                return mset[prox][0], mset[prox][1]
        
        

    
        
        
        
