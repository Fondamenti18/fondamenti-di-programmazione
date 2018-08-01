'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3x3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo 
(un giocatore ha come simbolo una "o" e l'avversario una 'x'). 
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta 
orizzontale, verticale o diagonale. Se la griglia viene riempita 
senza che nessuno dei giocatori sia riuscito a completare una linea 
retta di tre simboli, il gioco finisce in parit . Nel caso in cui il gioco 
finisse in parit, la partita detta "patta". 
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
che, dato un nodo NodoTris, restituisce:
 'o' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'o'
 'x' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'x'
 '-' se la configurazione rappresentata dal nodo e' una configurazione di patta
 '?' se la configurazione rappresentata dal nodo e' una configurazione di gioco non ancora terminato

2)
esiti(self)
che, dato un nodo radice di un albero di gioco, restituisce una tripla con i possibili 
esiti della partita che ha come configurazione iniziale quella rappresentata dal nodo. 
Piu' precisamente: il primo elemento della tripla il numero di  patte possibili, 
il secondo e' il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento
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
lecite (vale a dire ottenute dopo un certo numero di mosse a parire dalla griglia vuota).


AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.

ATTENZIONE: i test vengono eseguiti con un timeout globale di 2*N secondi (se il grader esegue N test).
'''

class NodoTris(object):
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        
    def tipo(self):
        esito = '?'
        # Il primo elemento non deve essere stringa vuota, quindi la sua lunghezza deve essere > 0
        t = (len(self.nome[0][0])>0) and (self.nome[0][0] == self.nome[0][1] == self.nome[0][2])        # 1 - Tris in riga 0
        if t:
            esito = self.nome[0][1]   # prendo uno dei 3 simboli tanto sono tutti e 3 uguali
        
        if not t:
            t = (len(self.nome[1][0])>0) and (self.nome[1][0] == self.nome[1][1] == self.nome[1][2])    # 2 - Tris in riga 1
            if t:
                esito = self.nome[1][0]
        
        if not t:
            t = (len(self.nome[2][0])>0) and (self.nome[2][0] == self.nome[2][1] == self.nome[2][2])    # 3 - Tris in riga 2
            if t:
                esito = self.nome[2][0]
        
        if not t:
            t = (len(self.nome[0][0])>0) and (self.nome[0][0] == self.nome[1][0] == self.nome[2][0])    # 4 - Tris in colonna 0
            if t:
                esito = self.nome[0][0]
        
        if not t:
            t = (len(self.nome[0][1])>0) and (self.nome[0][1] == self.nome[1][1] == self.nome[2][1])    # 5 - Tris in colonna 1
            if t:
                esito = self.nome[0][1]
        
        if not t:
            t = (len(self.nome[0][2])>0) and (self.nome[0][2] == self.nome[1][2] == self.nome[2][2])    # 6 - Tris in colonna 2
            if t:
                esito = self.nome[0][2]
        
        if not t:
            t = (len(self.nome[0][0])>0) and (self.nome[0][0] == self.nome[1][1] == self.nome[2][2])    # 7 - Tris in diagonale alto sinistra - basso destra
            if t:
                esito = self.nome[0][0]
        
        if not t:
            t = (len(self.nome[0][2])>0) and (self.nome[0][2] == self.nome[1][1] == self.nome[2][0])    # 8 - Tris in diagonale alto destra - basso sinistra
            if t:
                esito = self.nome[0][2]
        
        if not t:
            x = self.nome[0].count('') + self.nome[1].count('') + self.nome[2].count('')
            if x == 0:   # non ci sono altre caselle 
                esito = '-'   # patta
        return esito
        
    def esiti(self):
        p = vo = vx = 0
        p, vo, vx = self.esiti2(p, vo, vx)
        return p, vo, vx
        
    def esiti2(self, p, vo, vx):
        if len(self.lista_figli)>0:
            for x in self.lista_figli:
                p, vo, vx = x.esiti2(p, vo, vx)
        else:
            esito = self.tipo()
            if esito=='-':
                p = p + 1
            elif esito == 'o':
                vo = vo + 1
            elif esito == 'x':
                vx = vx + 1
        return p, vo, vx
     
    def vittorie_livello(self, giocatore, h):
        liv = 0
        n = self.vittorie(giocatore, h , liv)
        return n
        
    def vittorie(self, giocatore, h, liv):
        n = 0   # contatore delle vittorie
        if self.tipo()==giocatore and h == liv:
            n = 1
        elif liv<h:
            for x in self.lista_figli:
                n = n + x.vittorie(giocatore, h, liv+1)
        return n
    
    def strategia_vincente(self,giocatore):
        if self.tipo() == giocatore:
                t = True
        elif self.tipo() == '?':
                for x in self.lista_figli:
                    t = x.strategia_vincente(giocatore)
        else:
                t = False
               
        return t
        

     
def gen_tree(griglia):
    x = griglia[0].count('x') + griglia[1].count('x') + griglia[2].count('x') 
    y = griglia[0].count('o') + griglia[1].count('o') + griglia[2].count('o')
    if x<y:
        d = 'x'
    else:
        d = 'o'
    T = pippo(griglia, d)
    return T

def pippo(g, d):
    T = NodoTris(g)
    if T.tipo() == '?': 
        for i in range(3):
            for j in range(3):
                if T.nome[i][j] == '':
                    h = copia(g)   
                    x = g[0].count('x') + g[1].count('x') + g[2].count('x') 
                    y = g[0].count('o') + g[1].count('o') + g[2].count('o')
                    if x<y:
                        d = 'x'
                    else:
                        d = 'o'
                    
                    h[i][j] = d
                    R = pippo(h, d)
                    T.lista_figli.append(R)
    
    return T          

def stampa(T):
    print(str(T.nome[0]))
    print(str(T.nome[1]))
    print(str(T.nome[2]))
    
def copia(M):
    
    N = []
    for r in M:
        R = []
        R[:] = r
        N.append(R)
    return N

def prove():
    g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
    g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
    g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
    g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]
    lista=[g1, g2, g3, g4]
    lista1=[gen_tree(x) for x in lista]
    return lista1
    