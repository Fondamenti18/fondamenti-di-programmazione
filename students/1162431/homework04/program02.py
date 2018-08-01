'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3x3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo 
(un giocatore ha come simbolo una "o" e l'avversario una 'x'). 
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta 
orizzontale, verticale o diagonale. Se la griglia viene riempita 
senza che nessuno dei giocatori sia riuscito a completare una linea 
retta di tre simboli, il gioco finisce in parita'. Nel caso in cui il gioco 
finisse in parita', la partita e' detta "patta". 
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
Piu' precisamente: il primo elemento della tripla  e' il numero di  patte possibili, 
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

PLAYER = 'o'
OPPONENT = 'x'
FREE_CELL = ''

WIN_CONDITIONS = (
    ((0, 0), (1, 1), (2, 2)),
    ((2, 2), (1, 1), (0, 0)),

    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),

    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
)

TYPE_WIN = 'o'
TYPE_LOSE = 'x'
TYPE_DRAW = '-'
TYPE_UNKNOW = '?'

from copy import deepcopy

def get_turn(grid):
    player = 0
    opponent = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == PLAYER:
                player = player + 1
            elif grid[y][x] == OPPONENT:
                opponent = opponent + 1

    return PLAYER if player <= opponent else OPPONENT

def make_move(node, position, player):
    x, y = position
    new_grid = deepcopy(node.nome)
    new_grid[y][x] = player
    return NodoTris(
        new_grid,
        next_turn=PLAYER if player == OPPONENT else OPPONENT
    )

def check_conditions(m):
    draw = True
    for i in range(len(WIN_CONDITIONS)):
        win = True
        lose = True
        for x, y in WIN_CONDITIONS[i]:
            cell = m[y][x]

            win = win and (cell == PLAYER)
            lose = lose and (cell == OPPONENT)
            draw = draw and (cell != FREE_CELL)

        if win or lose:
            return TYPE_WIN if win else TYPE_LOSE

    return TYPE_DRAW if draw else TYPE_UNKNOW

class NodoTris:
    def __init__(self, griglia, next_turn = None):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self._tipo = None
        self.next_turn = next_turn if next_turn is not None else get_turn(griglia)
        self.init_childs()

    def init_childs(self):
        if self.tipo() != TYPE_UNKNOW:
            return 

        grid = self.nome
        player = 0
        opponent = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):

                if grid[y][x] == PLAYER:
                    player = player + 1
                elif grid[y][x] == OPPONENT:
                    opponent = opponent + 1 
                else:
                    new_grid = deepcopy(self.nome)
                    new_grid[y][x] = self.next_turn
                    self.lista_figli.append(
                        make_move(self, (x, y), self.next_turn)
                    )

    
    def tipo(self):
        '''inserire qui il vostro codice'''

        if self._tipo is None:
            m = self.nome

            self._tipo = check_conditions(m)

        return self._tipo
        
    def esiti(self):
        '''inserire qui il vostro codice'''
        tipo = self.tipo()
        esito = (
            1 if tipo == TYPE_DRAW else 0,
            1 if tipo == TYPE_WIN else 0,
            1 if tipo == TYPE_LOSE else 0
        )

        for child in self.lista_figli:
            esito = tuple(map(sum, zip(esito, child.esiti())))

        return esito
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''

        tipo = self.tipo()
        if h == 0:
            return 1 if tipo == (TYPE_WIN if giocatore == PLAYER else TYPE_LOSE) else 0

        wins = 0
        for child in self.lista_figli:
            wins += child.vittorie_livello(giocatore, h - 1)

        return wins
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''

        tipo = self.tipo()
        type_needed = TYPE_WIN if giocatore == PLAYER else TYPE_LOSE

        if tipo != TYPE_UNKNOW:
            return tipo == type_needed

        win_strategy = True
        for child in self.lista_figli:
            if child.tipo() == TYPE_UNKNOW:
                win_strategy =  child.strategia_vincente(giocatore) and win_strategy
            else:
                return child.tipo() == type_needed
            

        return win_strategy
        
def gen_tree(griglia):
    '''inserire qui il vostro codice'''

    return NodoTris(griglia)