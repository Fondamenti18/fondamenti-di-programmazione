'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3×3 caselle.
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


class NodoTris:
    def __init__(self, griglia):

        self.nome = [['', '', ''], ['', '', ''], ['', '', '']]

        for i in range(3):
            for j in range(3):
                self.nome[i][j] = griglia[i][j]

        self.lista_figli = []  # lista dei nodi figli

        self.draw = 0
        self.o_wins = 0
        self.x_wins = 0

    def tipo(self):
        '''inserire qui il vostro codice'''
        if (self.nome[0][0] == self.nome[0][1] == self.nome[0][2] == 'o'
                or self.nome[1][0] == self.nome[1][1] == self.nome[1][2] == 'o'
                or self.nome[2][0] == self.nome[2][1] == self.nome[2][2] == 'o'):
            return 'o'

        if (self.nome[0][0] == self.nome[1][0] == self.nome[2][0] == 'o'
                or self.nome[0][1] == self.nome[1][1] == self.nome[2][1] == 'o'
                or self.nome[0][2] == self.nome[1][2] == self.nome[2][2] == 'o'):
            return 'o'

        if self.nome[0][0] == self.nome[1][1] == self.nome[2][2] == 'o':
            return 'o'

        if (self.nome[0][0] == self.nome[0][1] == self.nome[0][2] == 'x'
                or self.nome[1][0] == self.nome[1][1] == self.nome[1][2] == 'x'
                or self.nome[2][0] == self.nome[2][1] == self.nome[2][2] == 'x'):
            return 'x'
        if (self.nome[0][0] == self.nome[1][0] == self.nome[2][0] == 'x'
                or self.nome[0][1] == self.nome[1][1] == self.nome[2][1] == 'x'
                or self.nome[0][2] == self.nome[1][2] == self.nome[2][2] == 'x'):
            return 'x'

        if self.nome[0][0] == self.nome[1][1] == self.nome[2][2] == 'x':
            return 'x'

        if '' in self.nome[0] or '' in self.nome[1] or '' in self.nome[2]:
            return '?'

        return '-'

    def esiti(self, node=None):
        '''inserire qui il vostro codice'''

        if node is None:
            node = self

        status = node.tipo()
        if status == '-':
            self.draw += 1
        elif status == 'x':
            self.x_wins += 1
        elif status == 'o':
            self.o_wins += 1

        nodes_list = []
        nodes_list += node.lista_figli

        for i in range(len(nodes_list)):
            self.esiti(nodes_list[i])

        return (self.draw, self.o_wins, self.x_wins)

    def vittorie_livello(self, giocatore, h, lvl=0, nodes_list=None):
        '''inserire qui il vostro codice'''
        if lvl > h:
            return 0
        else:
            if nodes_list is None:
                nodes_list = [self]

            counter = 0

            children_list = []

            for i in range(len(nodes_list)):
                children_list += nodes_list[i].lista_figli
                if h == lvl:
                    if nodes_list[i].tipo() == giocatore:
                        counter += 1

            return counter + self.vittorie_livello(giocatore, h, lvl + 1, children_list)

        '''
        lvl_node = [self]
        children_nodes = [self]

        lvl_number = 0

        while lvl_number < h:
            lvl_node = []
            lvl_node += children_nodes
            children_nodes = []

            for i in range(len(lvl_node)):
                children_nodes += lvl_node[i].lista_figli
            lvl_number += 1

        winning_counter = 0
        for i in range(len(children_nodes)):
            if children_nodes[i].tipo() == giocatore:
                winning_counter += 1

        return winning_counter
        '''

    def max_height(self):
        lvl_node = [self]
        children_nodes = [self]

        lvl_number = -1

        while children_nodes:
            lvl_node = []
            lvl_node += children_nodes
            children_nodes = []

            for i in range(len(lvl_node)):
                children_nodes += lvl_node[i].lista_figli
            lvl_number += 1

        return lvl_number

    def strategia_vincente(self, giocatore):
        '''inserire qui il vostro codice'''
        max_h = self.max_height()

        if giocatore == 'o':
            win_max_h_opponent = self.vittorie_livello('x', max_h)
            if win_max_h_opponent > 0:
                return False
            else:
                return True
        elif giocatore == 'x':
            win_max_h_opponent = self.vittorie_livello('o', max_h)
            if win_max_h_opponent > 0:
                return False
            else:
                return True


def gen_tree(griglia, turn='o'):
    '''inserire qui il vostro codice'''

    tree_node = NodoTris(griglia)

    children_list = []

    if tree_node.tipo() == '?':
        for i in range(3):
            for j in range(3):
                if griglia[i][j] == '':
                    griglia[i][j] = turn
                    children_list += [gen_tree(griglia, 'x' if turn == 'o' else 'o')]
                    griglia[i][j] = ''

    tree_node.lista_figli.extend(children_list)

    return tree_node
