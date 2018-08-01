'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3x3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo 
(un giocatore ha come simbolo una "o" e l'avversario una 'x'). 
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta 
orizzontale, verticale o diagonale. Se la griglia viene riempita 
senza che nessuno dei giocatori sia riuscito a completare una linea 
retta di tre simboli, il gioco finisce in paritĂ . Nel caso in cui il gioco 
finisse in paritĂ , la partita Ă¨ detta "patta". 
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
Piu' precisamente: il primo elemento della tripla  Ă¨ il numero di  patte possibili, 
il secondo Ă¨ il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento 
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
from copy import deepcopy

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.height = 0
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        if is_win(self.nome, 'o'):
            return 'o'
        if is_win(self.nome, 'x'):
            return 'x'
        if self.lista_figli:
            return '?'
        return '-'
        
    def esiti(self):
        patte = vic_o = vic_x = 0
        if self.tipo() == 'o':
            vic_o += 1
        if self.tipo() == 'x':
            vic_x += 1
        if self.tipo() == '-':
            patte += 1
        
        for ch in self.lista_figli:
            c1, c2, c3 = ch.esiti()
            patte += c1
            vic_o += c2
            vic_x += c3
        return patte, vic_o, vic_x
        
    
    def vittorie_livello(self, giocatore, h):
        cnt = 0
        if self.height == h:
                if is_win(self.nome, giocatore):
                    cnt += 1
        for n in self.lista_figli:
            cnt += n.vittorie_livello(giocatore, h)
        return cnt        
    
    def strategia_vincente(self,giocatore, level = 0):
        p = 'x' if giocatore == 'o' else 'o'
        for n in self.lista_figli:
            if is_win(n.nome, p):
                return False
            n.strategia_vincente(p)
        return True
        
def walk_board(griglia):
    empty = []
    for i in range(3):
        for j in range(3):
            if griglia[i][j] == "":
                empty.append((i, j))
    return empty   

def check_win(griglia, x, y, player):

    if (griglia[0][y] == player) and griglia[0][y] == griglia[1][y] ==  griglia[2][y]:
        return True

    if (griglia[x][0] == player) and griglia[x][0] == griglia[x][1] == griglia [x][2]:
        return True

    if (griglia[0][0] == player) and griglia[0][0] == griglia[1][1] == griglia [2][2]:
        return True

    if (griglia[0][2] == player) and griglia[0][2] == griglia[1][1] == griglia [2][0]:
        return True

    return False  
    
def is_win(griglia, player):
    for i in range(3):
        for j in range(3):
            if griglia[i][j] == player:
                if check_win(griglia, i, j, player):
                    return True
    return False
      
def gen_tree(griglia, player = 'o', level = 0):
    root = NodoTris(griglia) 
    root.height = level
    disp = walk_board(root.nome)
    p = 'o' if level % 2 == 0 else 'x'
    if is_win(root.nome, 'o' if p == 'x' else 'x') or not disp:
        return root
    for coord in disp:
        g = deepcopy(root.nome)
        g[coord[0]][coord[1]] = p
        n = NodoTris(g)
        if not check_win(g, coord[0], coord[1], p):
            root.lista_figli += [gen_tree(n.nome, p, level + 1)]
        else:
            n.height = level+1
            root.lista_figli += [n]
    return root
