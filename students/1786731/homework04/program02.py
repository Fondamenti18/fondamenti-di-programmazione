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
'''

from testlib import check, runtests

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.type = 'n' # type not set
        self.results = None

    def tipo(self):
        if self.type == 'n':
            self.type = self.getTipo()

        return self.type
        
    def esiti(self):
        self.results = self.compute_esiti()
        
        return (self.results[0], self.results[1], self.results[2])
    
    def vittorie_livello(self, giocatore, h):
        return self.count_wins_at_level(giocatore, h, 0)

    def win_strat(self):
        count = 0
        for r in range(9):
            i = r // 3
            j = r % 3
            count += 1 if (self.nome[i][j] == 'x') | (self.nome[i][j] == 'o') else 0
    
        if count == 2:
            # if 'o' in the center and x in a middle corner
            if (self.nome[1][1] == 'o') & (self.nome[0][0] == '') & (self.nome[0][2] == '') & (self.nome[2][0] == '') & (self.nome[2][2] == ''):
                return 'o'
            # if 'o' in one corner and x in a middle corner            
            if ((self.nome[0][0] == 'o') | (self.nome[0][2] == 'o') | (self.nome[2][0] == 'o') | (self.nome[2][2] == 'o')) & ((self.nome[0][1] == 'x') | (self.nome[1][0] == 'x') | (self.nome[1][2] == 'x') | (self.nome[2][1] == 'x')):
                return 'o'

        return ''

    def wsr(self, giocatore):
        TargetPlayerPlays = who_plays(self.nome)
        if giocatore == 'x':
            TargetPlayerPlays = not TargetPlayerPlays



        result = self.tipo()
        if (result != '?' and result != '-') or len(self.lista_figli) == 0:
            # leaf node
            if result == giocatore:
                return True
            else:
                return False




        if TargetPlayerPlays:
            # check for at least one child winning over every move of his opponent
            for child in self.lista_figli:
                if child.wsr(giocatore):
                    return True

            return False
        else:
            # has to win over every move from his opponent
            for child in self.lista_figli:
                if not child.wsr(giocatore):
                    return False

            return True
            




    def strategia_vincente(self,giocatore):

        return self.wsr(giocatore)


    def find_first_winner(self, depth):
        # check if we have a winning config
        if (self.tipo() == 'x') | (self.tipo() == 'o'):
            return (self.tipo(), depth)


        smallestdepth = 999
        fres = None

        # if we don't, check all of our children      
        for child in self.lista_figli:
            result = child.find_first_winner(depth + 1)
            
            if result != None and (result[0] == 'x' or result[0] == 'o'):
                # which depth gave us a result?
                resultdepth = result[1]

                # override previous only if smaller
                if resultdepth < smallestdepth:
                    smallestdepth = result[1] 
                    fres = result


                if resultdepth - depth < 2:
                    return fres    
                else:
                    continue   # one of the other children may yield a better result

        return fres

    def find_first_winner_single_move(self, giocatore):      
        for child in self.lista_figli:
            if child.tipo() == giocatore:
                return True

        return False
  
        

    def getTipo(self):
        '''inserire qui il vostro codice'''
        griglia = self.nome

        toprow = ''.join(griglia[0]) 
        midrow = ''.join(griglia[1]) 
        botrow = ''.join(griglia[2])
        topcol = griglia[0][0] + griglia[1][0] + griglia[2][0]
        midcol = griglia[0][1] + griglia[1][1] + griglia[2][1]
        botcol = griglia[0][2] + griglia[1][2] + griglia[2][2]
        lxdiag = griglia[0][0] + griglia[1][1] + griglia[2][2] 
        rxdiag = griglia[0][2] + griglia[1][1] + griglia[2][0]

        if (toprow == "xxx") | (midrow == "xxx") | (botrow == "xxx") | (topcol == "xxx") | (midcol == "xxx") | (botcol == "xxx") | (lxdiag == "xxx") | (rxdiag == "xxx"):
           return 'x'

        if (toprow == "ooo") | (midrow == "ooo") | (botrow == "ooo") | (topcol == "ooo") | (midcol == "ooo") | (botcol == "ooo") | (lxdiag == "ooo") | (rxdiag == "ooo"):
           return 'o'

        for r in range(9):
            i = r // 3
            j = r % 3

            if griglia[i][j] == '':
                return '?'

        return '-'

    def compute_esiti(self):
        # update results for this node, and eventually return it
        tipo = self.tipo()
        newresults = [0, 0, 0]
        
        if tipo == '-':
            newresults[0] = 1
            return newresults

        if tipo == 'o':
            newresults[1] = 1
            return newresults

        if tipo == 'x':
            newresults[2] = 1
            return newresults

        for child in self.lista_figli:
            res = child.compute_esiti()
            newresults[0] += res[0]
            newresults[1] += res[1]
            newresults[2] += res[2]

        return newresults

    def count_wins_at_level(self, player, targetDepth, depth):
        count = 0

        if depth == targetDepth and self.tipo() == player:
            return count + 1

        # don't check children below target depth
        if depth == targetDepth:
            return count

        for child in self.lista_figli:
            childcount = child.count_wins_at_level(player, targetDepth, depth + 1)
            count += childcount

        return count

def who_plays(griglia):
    Oplays = False

    counter = 0 
    for r in range(9):
        i = r // 3
        j = r % 3

        if griglia[i][j] != '':
            counter += 1

    if counter % 2 == 0:
        Oplays = True
    
    return Oplays

def new_grid(griglia, i, j, mark):
    newgrid = [ [] for r in range(3) ]

    for x in range(3):
        for y in range(3):
            newgrid[x].append(griglia[x][y])


    newgrid[i][j] = 'o' if mark == True else 'x'

    return newgrid

def compute_tree(Oplays, griglia):
    # crea nodo
    node = NodoTris(griglia)

    # if this node is a winning node, skip further computations
    tipo = node.tipo()
    if ((tipo == 'o') | (tipo == 'x')):
        return node

    # computes children
    for r in range(9):
        i = r // 3
        j = r % 3

        if griglia[i][j] == '':
            child = compute_tree(not Oplays, new_grid(griglia, i, j, Oplays))
            node.lista_figli.append(child)

    # returns the node
    return node

def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    Oplays = who_plays(griglia)

    root = compute_tree(Oplays, griglia)

    return root

    # debug = 0
    

dsfdsf = gen_tree([['o', 'x', 'o'], ['o', 'o', 'x'], ['x', '', '']])
dsfdsf.strategia_vincente('o')