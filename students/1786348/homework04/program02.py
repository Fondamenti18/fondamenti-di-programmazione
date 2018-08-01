"""
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
che, dato un nodo NodoTris, restituisce:
 'o' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'o'
 'x' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'x'
 '-' se la configurazione rappresentata dal nodo e' una configurazione di patta
 '?' se la configurazione rappresentata dal nodo e' una configurazione di gioco non ancora terminato

2)
esiti(self)
che, dato un nodo radice di un albero di gioco, restituisce una tripla con i possibili
esiti della partita che ha come configurazione iniziale quella rappresentata dal nodo.
Piu' precisamente: il primo elemento della tripla  è il numero di  patte possibili,
il secondo è il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento
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
"""

from copy import deepcopy
# from random import shuffle


class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []  # lista dei nodi figli

        self.possible_endings = False

    # def __getitem__(self, key):
    #     return self.lista_figli[key - 1] if key != 0 else self
    #
    # @property
    # def show(self):
    #     print("\n".join(str([r if len(r) else " " for r in l]) for l in self.nome))
    #     return

    def tipo(self):
        if len(self.lista_figli):
            return "?"

        winner = get_winner(self.nome)
        if not winner:
            return "-"

        return winner

    def esiti(self):
        if not self.possible_endings:
            self.possible_endings = collect_possible_ending(self, {})

        x = o = p = 0
        for moves in self.possible_endings.values():
            for e in moves:
                if e == "x":
                    x += 1

                elif e == "o":
                    o += 1

                else:
                    p += 1

        return p, o, x
    
    def vittorie_livello(self, giocatore, h):
        if not self.possible_endings:
            self.possible_endings = collect_possible_ending(self, {})

        winner = 0
        if h in self.possible_endings:
            for ending in self.possible_endings[h]:
                if ending == giocatore:
                    winner += 1

        return winner
    
    def strategia_vincente(self, giocatore):
        if not self.possible_endings:
            self.possible_endings = collect_possible_ending(self, {})

        last = [x for x in self.possible_endings.values()][-1]
        xes = last.count("x")
        oes = last.count("o")
        return True if giocatore == ("x" if max(xes, oes) == xes else "o") else False


def get_winner(grid):
    len00 = len(grid[0][0])
    len02 = len(grid[0][2])

    if len00 and grid[0][0] == grid[1][0] == grid[2][0]:
        return grid[0][0]

    elif len(grid[0][1]) and grid[0][1] == grid[1][1] == grid[2][1]:
        return grid[0][1]

    elif len02 and grid[0][2] == grid[1][2] == grid[2][2]:
        return grid[0][2]

    elif len00 and grid[0][0] == grid[0][1] == grid[0][2]:
        return grid[0][0]

    elif len(grid[1][0]) and grid[1][0] == grid[1][1] == grid[1][2]:
        return grid[1][0]

    elif len(grid[2][0]) and grid[2][0] == grid[2][1] == grid[2][2]:
        return grid[2][0]

    elif len00 and grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]

    elif len02 and grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]

    return False


def collect_possible_ending(node, ending, h=0):
    if h not in ending:
        ending.update({h: []})

    winner = node.tipo()
    if winner in "xo-":
        ending[h].append(winner)

    for subnode in node.lista_figli:
        ending = collect_possible_ending(subnode, ending, h+1)

    return ending


def next_round(grid):
    oes = xes = 0
    for y in grid:
        for x in y:
            if x == "o":
                oes += 1

            elif x == "x":
                xes += 1

    return "x" if oes > xes else "o"


def free_space(grid):
    free = []
    for y in range(3):
        for x in range(3):
            if not len(grid[y][x]):
                free.append((y, x))

    return free


def generate_next_move(grid):
    free = free_space(grid)
    result = []
    if not len(free):
        return result

    # shuffle(free)
    next_player = next_round(grid)
    for c in free:
        temp_grid = deepcopy(grid)
        y, x = c
        temp_grid[y][x] = next_player
        result.append(temp_grid)

    return result


def gen_tree(griglia):
    node = NodoTris(griglia)
    node.lista_figli = [gen_tree(grid) for grid in generate_next_move(node.nome)] \
        if not get_winner(griglia) else []
    return node
