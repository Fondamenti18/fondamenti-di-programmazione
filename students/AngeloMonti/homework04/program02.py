'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3×3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo 
(un giocatore ha come simbolo una "o" e l'avversario una 'x'). 
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta 
orizzontale, verticale o diagonale. Se la griglia viene riempita 
senza che nessuno dei giocatori sia riuscito a completare una linea 
retta di tre simboli, il gioco finisce in parità. Nel caso in cui il gioco 
finisse in parità, la partita è detta "patta". 
Per convenzione a griglia vuota la prima mossa spetta sempre al giocatore 'o'

Una configurazione del gioco e' dunque univocamente determinata  dal contenuto della griglia.

Nel seguito assumiamo che il contenuto della griglia sia  rappresentato tramite  lista di liste.
La dimensione della lista di liste M e'  3x3 ed   M[i][j] contiene  '', 'x', o 'o'  a seconda 
che la cella della griglia appartenente all'iesima riga e j-ma colonna sia ancora libera, 
contenga il simbolo 'x' o contenga il simbolo 'o'. 

Data una configurazione C del gioco, l'albero di gioco per C e' l'albero che 
si ottiene ricorsivamente partendo dalla configurazione C e assegnando come figli le configurazioni 
che e' possibile ottenere da C con una mossa ulteriore del gioco. Ovviamente  risulteranno 
foglie dell'albero i possibili esiti della partita vale a dire le diverse configurazioni cui e' 
possibile arrivare partendo da C e che rappresentano patte, vittorie per 'o' o vittorie per 'x'.
Se veda ad esempio l'immagine albero_di_gioco.png che mostra l' albero di gioco che si ottiene a partire 
dalla configurazione rappresentata da [['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
 

Si consideri la seguente Classe di oggetti:


class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] 


Bisogna progettare le seguente  funzione 

gen_tree(griglia)
che, data la configurazione di gioco griglia,  costruisce l'albero di gioco che si ottiene a partire 
dalla configurazione griglia e ne restituisce la radice. I nodi dell'albero devono essere 
oggetti della classe NodoTris.

Per testare la correttezza della vostra implementazione di gen_tree() il grade utilizzera' quattro metodi 
della   classe NodoTris che dovete comunque implementare: 

1)
tipo(self)
che, dato un nodo radice di un albero di gioco, restituisce:
 'o' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore '0'
 'x' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'x'
 '-' se la configurazione rappresentata dal nodo e' una configurazione di patta
 '?' se la configurazione rappresentata dal nodo e' una configurazione di gioco non ancora terminato

2)
esiti(self)
che, dato un nodo radice di un albero di gioco, restituisce una tripla con i possibili 
esiti della partita che ha come configurazione iniziale quella rappresentata dal nodo. 
Piu' precisamente: il primo elemento della tripla  è il numero di  patte possibili, 
il secondo è il numero di possibili vittorie  per il giocatore 'o' mentre  il tezo elemento 
e' il numero di possibili vittorie per il giocatore 'x'.

3)
vittorie_livello(self, giocatore, h)
che, dato un nodo radice di un albero di gioco, uno dei due giocatori ed un intero h,
restituisce il numero di nodi che rappresentano una vittoria per il giocatore e si 
trovano ad altezza h nell'albero. In altri termini restituisce il numero di vittorie possibili 
per giocatore in esattamente h mosse, nella partita che ha come configurazione iniziale 
quella rappresentata dalla radice dell'albero.

4)
strategia_vincente(self,giocatore)
che, dato un nodo radice di un albero di gioco ed uno dei due giocatori, restituisce True o False. 
Restituisce True  se  giocatore ha una strategia vincente  nella partita 
che ha come configurazione iniziale quella rappresentata dal nodo radice, False altrimenti.

Nota che un giocatore ha una strategia vincente rispetto ad una certa configurazione se, 
qualunque siano le mosse dell'avversario ha sempre la possibilita' di rispondere in modo 
che la partita termini con la sua vittoria.

Potete ovviamente definire ulteriori  funzioni e altri metodi per la   Classe NodiTris 
se li  ritenete utili al fine della risoluzione del compito.

Potete assumere che le configurazioni di gioco rappresentate da griglia siano sempre configurazioni 
lecite (vale a dire ottenute dopo un certo numero di mosse a parire dall griglia vuota).


 AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.
'''
from copy import deepcopy


class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        '''restituisce:
        'o' se  nodo.nome rappresenta una configurazione di vittoria per il giocatore '0'
        'x' se  nodo.nome rappresenta una configurazione di vittoria per il giocatore 'x'
        '-' se  nodo.nome rappresenta una configurazione di patta
        '?' se  nodo.nome rappresenta una configurazione di gioco non ancora terminato
        '''
        pos=self.nome
        for r in range(3):
            if pos[r][0]!='' and pos[r][0]==pos[r][1] and pos[r][1]==pos[r][2]: return pos[r][0]
        for c in range(3):
            if pos[0][c]!='' and pos[0][c]==pos[1][c] and pos[1][c]==pos[2][c]: return pos[0][c]
        if pos[0][0]!='' and pos[0][0]==pos[1][1] and pos[1][1]==pos[2][2]: return pos[0][0]
        if pos[0][2]!='' and pos[0][2]==pos[1][1] and pos[1][1]==pos[2][0]: return pos[0][2]
        for r in range(3):
            for c in range(3):
                if pos[r][c]=='':return '?'
        return '-'
    
    def esiti(self):
        '''restituisce una tripla con i possibili esiti della partita che ha come configurazione 
        iniziale quella rappresentata dal nodo. Piu' precisamente: il primo elemento della tripla  
        è il numero di  patte possibili, il secondo è il numero di possibili vittorie  per 'o' ed 
        il tezo il numero di possibili vittorie per 'x'.'''
        lista=[0,0,0]
        if self.lista_figli==[]:
            x=self.tipo()
            if  x=='-' : lista[0]=1
            elif x=='o': lista[1]=1
            else: lista[2]=1
            return tuple(lista)
        for figlio in self.lista_figli:
            tri=figlio.esiti()
            for i in range(3): lista[i]+=tri[i]
        return tuple(lista) 
        
    def vittorie_livello(self, giocatore, h):
        '''restituisce il numero di vittorie possibili per giocatore in esattamente h mosse, 
        nella partita che ha come configurazione iniziale self.nome'''
        if (ultimo(self.nome)==giocatore and h %2==0) or (ultimo(self.nome)!=giocatore and h %2==1): 
            return self.conta(h)
        return 0
        
    def conta(self,h):
        '''retituisce il numero di nodi di vittoria che sono a livello h nell'albero radicato nel nodo'''
        if h==0:
            if self.lista_figli==[] and self.tipo()!='-': 
                return 1
            return 0
        c=0
        for figlio in self.lista_figli:
            c+= figlio.conta(h-1)
        return c   
    
    def strategia_vincente(self,giocatore):
        ''' Restituisce True  se  giocatore ha una configurazione vincente, nella partita 
        che ha come configurazione iniziale quella rappresentata dal nodo.
        False altrimenti.
        '''
        if ultimo(self.nome)==giocatore: liv=0
        else: liv=1
        return self.strategia_vincente1(0,liv)
        
    def strategia_vincente1(self,h,liv):
        if h%2!=liv:
            if self.lista_figli==[]:return False
            for figlio in self.lista_figli:
                if figlio.strategia_vincente1(h+1,liv):return True
            return False
        else:
            if self.lista_figli==[]:
                if self.tipo()!='-': return True
                return False   
            for figlio in self.lista_figli:
                if not figlio.strategia_vincente1(h+1,liv):return False
            return True
    
def ultimo(griglia):
    '''restituisce l'ultimo giocatore che ha effettuato una mossa nella configurazione di gioco
    rappresentata dalla griglia. Nel caso la griglia sia vuota restituisce 'x' 
    '''
    d={'o':0,'x':0}
    for r in range(3):
        for c in range(3):
            if griglia[r][c]!='':d[griglia[r][c]]+=1
    if d['x']== d['o']: g='x'
    else: g='o'
    return g
   
                
def gen_tree(griglia):
    ''' restituisce la radice all'albero di gioco che si ottiene a partire dalla configurazione
    indicata da griglia'''
    return gen_tree1(griglia, ultimo(griglia))
    
def gen_tree1(griglia, g):
    nodo=NodoTris(griglia)
    if nodo.tipo()=='?':
        if g=='o':g='x'
        else: g='o'
        for r in range(3):
            for c in range(3):
               if griglia[r][c]=='':
                   griglia1=deepcopy(griglia)
                   griglia1[r][c]= g
                   nodo.lista_figli+=[gen_tree1(griglia1,g)]
    return nodo
    

