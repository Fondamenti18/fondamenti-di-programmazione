# Il tris è un popolarissimo gioco. Si gioca su una griglia quadrata di 3x3
# caselle. A turno, i due giocatori scelgono una cella vuota e vi disegnano il
# proprio simbolo (un giocatore ha come simbolo una 'o' e l'avversario una 'x').
# Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta
# orizzontale, verticale o diagonale. Se la griglia viene riempita senza che
# nessuno dei giocatori sia riuscito a completare una linea retta di tre
# simboli, il gioco finisce in parità. Nel caso in cui il gioco finisse in
# parità, la partita è detta "patta". Per convenzione a griglia vuota la prima
# mossa spetta sempre al giocatore 'o'.
#
# Una configurazione del gioco è dunque univocamente determinata dal contenuto
# della griglia.
#
# Nel seguito assumiamo che il contenuto della griglia sia rappresentato tramite
# lista di liste. La dimensione della lista di liste M è 3x3 ed M[i][j] contiene
# '', 'x', o 'o' a seconda che la cella della griglia appartenente all'iesima
# riga e j-ma colonna sia ancora libera, contenga il simbolo 'x' o contenga il
# simbolo 'o'.
#
# Data una configurazione C del gioco, l'albero di gioco per C è l'albero che
# si ottiene ricorsivamente partendo dalla configurazione C e assegnando come
# figli le configurazioni che è possibile ottenere da C con una mossa ulteriore
# del gioco. Ovviamente risulteranno foglie dell'albero i possibili esiti della
# partita vale a dire le diverse configurazioni cui è possibile arrivare
# partendo da C e che rappresentano patte, vittorie per 'o' o vittorie per 'x'.
# Se veda ad esempio l'immagine albero_di_gioco.png che mostra l'albero di
# gioco che si ottiene a partire dalla configurazione rappresentata da
# [['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']].
#
# Si consideri la seguente Classe di oggetti:
#
#   class NodoTris:
#       def __init__(self, griglia):
#           self.nome = griglia
#           self.lista_figli = []
#
# Bisogna progettare le seguente funzione gen_tree(griglia) che, data la
# configurazione di gioco griglia, costruisce l'albero di gioco che si ottiene a
# partire dalla configurazione griglia e ne restituisce la radice. I nodi
# dell'albero devono essere oggetti della classe NodoTris.
#
# Per testare la correttezza della vostra implementazione di gen_tree() il grade
# utilizzerà quattro metodi della classe NodoTris che dovete comunque
# implementare:
#
# 1) tipo(self)
#  che, dato un nodo NodoTris, restituisce:
#   - 'o' se la configurazione rappresentata dal nodo è una configurazione di
#      vittoria per il giocatore 'o';
#   - 'x' se la configurazione rappresentata dal nodo è una configurazione di
#     vittoria per il giocatore 'x';
#   - '-' se la configurazione rappresentata dal nodo è una configurazione di
#     patta;
#   - '?' se la configurazione rappresentata dal nodo è una configurazione di
#     gioco non ancora terminato.
#
# 2) esiti(self)
#  che, dato un nodo radice di un albero di gioco, restituisce una tripla con i
#  possibili esiti della partita che ha come configurazione iniziale quella
#  rappresentata dal nodo. Più precisamente: il primo elemento della tripla è il
#  numero di patte possibili, il secondo è il numero di possibili vittorie per
#  il giocatore 'o' mentre il terzo elemento è il numero di possibili vittorie
#  per il giocatore 'x'.
#
# 3) vittorie_livello(self, giocatore, h)
#  che, dato un nodo radice di un albero di gioco, uno dei due giocatori ed un
#  intero h, restituisce il numero di nodi che rappresentano una vittoria per il
#  giocatore e si trovano ad altezza h nell'albero. In altri termini restituisce
#  il numero di vittorie possibili per giocatore in esattamente h mosse, nella
#  partita che ha come configurazione iniziale quella rappresentata dalla radice
#  dell'albero.
#
# 4) strategia_vincente(self, giocatore)
#  che, dato un nodo radice di un albero di gioco ed uno dei due giocatori,
#  restituisce True o False. Restituisce True se giocatore ha una strategia
#  vincente nella partita che ha come configurazione iniziale quella
#  rappresentata dal nodo radice, False altrimenti.
#
#  Nota che un giocatore ha una strategia vincente rispetto ad una certa
#  configurazione se, qualunque siano le mosse dell'avversario ha sempre la
#  possibilità di rispondere in modo che la partita termini con la sua vittoria.
#
# Potete ovviamente definire ulteriori funzioni e altri metodi per la Classe
# NodiTris se li ritenete utili al fine della risoluzione del compito.
#
# Potete assumere che le configurazioni di gioco rappresentate da griglia siano
# sempre configurazioni lecite (vale a dire ottenute dopo un certo numero di
# mosse a parire dalla griglia vuota).
#
# AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
# importare moduli che non sono nella libreria standard.
#
# ATTENZIONE: i test vengono eseguiti con un timeout globale di 2*N secondi (se
# il grader esegue N test).

class NodoTris:
    def __init__(self, grid):
        self.nome = grid # La griglia con i valori.
        self.lista_figli = set() # Insieme dei sviluppi del nodo.
        self.status = '' # Lo stato del nodo ('o', 'x', '?', '-').
        self.turn = '' # 0 -> 'o'; 1 -> 'x'.

        self.score = []

    def tipo(self):
        return self.status # Viene calcolato durante la creazione dell'albero.

    def esiti(self):
        result = [0, 0, 0]

        perform_endings(self, result)

        return tuple(result)

    def vittorie_livello(self, player, dest_lvl, current_lvl = 0):
        if dest_lvl == current_lvl:
            return int(self.status == player) # Torna 1 o 0.

        else: # Ancora non si raggiunge 'dest_lvl'.
            wins = 0

            for sub_config in self.lista_figli:
                wins += sub_config.vittorie_livello(player,
                                                    dest_lvl,
                                                    current_lvl + 1)

        return wins

    def strategia_vincente(self,giocatore):
        if giocatore == 'o':
            opposite = 'x'
        else:
            opposite = 'o'

        result =  strategy(self, giocatore, opposite)

        if result == -1:
            return False
        else:
            return True

# ------------------------------------------------------------------------------

def perform_endings(node, result):
    exit = { '-' : 0, 'o' : 1, 'x' : 2 }

    if node.status != '?':
        result[exit[node.status]] += 1
        return

    for sub_config in node.lista_figli:
        perform_endings(sub_config, result)

def score(node, player, opponent):
    '''Ritorna il punteggio del giocatore sul nodo 'node'.'''
    if node.status == player:
        return 1
    else: # Se vince il nemico o pareggia è sempre una cosa negativa.
        return -1

def get_single_score(scores, value):
    '''Ritorna il punteggio in base a 'value'.'''
    if value in scores:
        return value
    else:
        return -value # Opposto.

def evalutate_strategy(node, opponent, scores):
    '''Valuta se è presente o meno una strategia vincente su 'node'.'''
    if node.turn == opponent:
        return get_single_score(scores, -1)
    else:
        return get_single_score(scores, 1)

def strategy(node, player, opponent):
    '''Ritorna la presenza di una strategia vincente per il giocatore.'''
    if not node.lista_figli:
        return score(node, player, opponent)

    scores = set()

    # Micro-ottimizzazione: la risoluzione dei nomi in Python è molto lenta,
    # sopratutto in casi di cicli come il for.
    add = scores.add
    for sub_config in node.lista_figli:
        add(strategy(sub_config, player, opponent))

    return evalutate_strategy(node, opponent, scores)

# ------------------------------------------------------------------------------

GRID_X = 1
GRID_O = 0
GRID_EMPTY = 10

def get_translated_cell(cell):
    '''Converte la cella dal formato della griglia di partenza a quello con
    la codifica numerica. Restituisce la cella convertita.
    '''
    if not cell:
        return GRID_EMPTY

    return int(cell != 'o') # 0 -> 'o', 1 -> 'x'.

def convert_grid(grid):
    '''Converte la griglia dal formato originale ad uno con le celle codificate
    in numeri.
    '''
    for row in range(3):
        for column in range(3):
            grid[row][column] = get_translated_cell(grid[row][column])

def calculate_sums(grid, sums):
    '''Calcola i risultati delle somme delle righe, colonne e diagonali e salva
    tutto sulla lista 'sums'.
    '''
    first_row = 0
    second_row = 1
    third_row = 2

    first_column = 3
    second_column = 4
    third_column = 5

    diag = 6
    rdiag = 7

    for step in range(0, 3):
        sums[first_row] += grid[0][step]
        sums[second_row] += grid[1][step]
        sums[third_row] += grid[2][step]

        sums[first_column] += grid[step][0]
        sums[second_column] += grid[step][1]
        sums[third_column] += grid[step][2]

    sums[diag] = grid[0][0] + grid[1][1] + grid[2][2]
    sums[rdiag] = grid[0][2] + grid[1][1] + grid[2][0]

def get_default_status(sums):
    '''Ritorna il simbolo di patta oppure partita non terminata, in base ai
    valori di 'sums'.
    '''
    if max(sums) >= GRID_EMPTY:
        return '?'
    else:
        return '-'

def get_status(grid):
    '''Ritorna lo stato delle griglia, che può essere '-', '?', 'x', 'o'.'''
    sums = [0, 0, 0, 0, 0, 0, 0, 0]

    calculate_sums(grid, sums)

    if 3 in sums: # tre 'x' (ossia 1) in fila.
        return 'x'
    elif 0 in sums: # tre 'o' (ossa 0) in fila.
        return 'o'

    return get_default_status(sums)

def get_copy_of(grid):
    '''Restituisce una copia della griglia.'''
    new_grid = []

    for row in range(3):
        new_grid += [[grid[row][0], grid[row][1], grid[row][2]]]

    return new_grid

def get_player(player):
    if player:
        return 'o'
    else:
        return 'x'

def next_move(tree, grid, row, column, player):
    if grid[row][column] == GRID_EMPTY:
        child_grid = get_copy_of(grid)
        child_grid[row][column] = player
        tree.lista_figli.add(get_tree(child_grid, player))

def get_tree(griglia, player):
    tree = NodoTris(griglia)

    tree.status = get_status(griglia)

    tree.turn = get_player(player)

    if tree.status != '?':
        return tree

    player = (player + 1) % 2

    for row in range(3):
        next_move(tree, griglia, row, 0, player)
        next_move(tree, griglia, row, 1, player)
        next_move(tree, griglia, row, 2, player)

    return tree

def get_start_player(grid):
    '''Ritorna il giocatore (codificato in numero) che deve effettuare la mossa
    al turno successivo rispetto alla griglia 'grid' convertita in numeri.
    '''
    first_row = 0
    second_row = 0
    third_row = 0

    for column in range(3):
        first_row += grid[0][column]
        second_row += grid[1][column]
        third_row += grid[2][column]

    # La somma di tutti i valori indica chi inizierà per primo.
    total = first_row + second_row + third_row

    if total == 90: # Griglia vuota.
        return 1
    else:
        return total % 2

def gen_tree(griglia):
    griglia = get_copy_of(griglia)
    convert_grid(griglia)

    start_player = get_start_player(griglia)

    return get_tree(griglia, start_player)
