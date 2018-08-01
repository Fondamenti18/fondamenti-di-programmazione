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

def matrixCopy(matrix):
    cop = []
    for line in matrix:
        cop.append(line.copy())
    return cop

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli

    def buildTree(self):
        if self.tipo() != '?':
            return None
        s = self.turn()
        for i in range(3):
            for j in range(3):
                if self.nome[i][j] == '':
                    newgriglia = matrixCopy(self.nome)
                    newgriglia[i][j] = s
                    figlio = NodoTris(newgriglia)
                    figlio.buildTree()
                    self.lista_figli.append(figlio)

    def turn(self):
        no, nx = 0, 0
        for i in range(3):
            for j in range(3):
                if self.nome[i][j] == 'o':
                    no+=1
                if self.nome[i][j] == 'x':
                    nx+=1
        return 'o' if no == nx else 'x'

    def checkLine(self, line):
        if self.nome[line][0] == self.nome[line][1] == self.nome[line][2] != '':
            return self.nome[line][0]
        return '-'

    def checkCol(self, col):
        if self.nome[0][col] == self.nome[1][col] == self.nome[2][col] != '':
            return self.nome[0][col]
        return '-'

    def checkDiag(self):
        if self.nome[0][0] == self.nome[1][1] == self.nome[2][2] != '':
            return self.nome[0][0]
        if self.nome[0][2] == self.nome[1][1] == self.nome[2][0] != '':
            return self.nome[0][2]
        return '-'

    def complete(self):
        for i in range(3):
            for j in range(3):
                if self.nome[i][j] == '':
                    return False
        return True

    def debugPrint(self):
        print(self.nome, self.tipo())
        for i in self.lista_figli:
            i.debugPrint()

    def tipo(self):
        for i in range(3):
            r = self.checkLine(i)
            if r != '-':
                return r
            c = self.checkCol(i)
            if c != '-':
                return c
        d = self.checkDiag()
        if d != '-':
            return d
        return '-' if self.complete() else '?'

    def getName(self):
        s = ''
        for i in range(3):
            for j in range(3):
                s += (self.nome[i][j] if self.nome[i][j] != '' else ' ')
        return s

    def getEsiti(self, memo):
        s = self.getName()
        if s in memo:
            return memo[s]
        p, vo, vx = 0, 0, 0
        tp = self.tipo()
        if tp == '-': p+=1
        if tp == 'o': vo+=1
        if tp == 'x': vx+=1
        for v in self.lista_figli:
            res = v.getEsiti(memo)
            p += res[0]
            vo += res[1]
            vx += res[2]
        memo[s] = (p, vo, vx)
        return (p, vo, vx)

    def esiti(self):
        memo = {}
        return self.getEsiti(memo)

    def getWinInLevel(self, giocatore, h, memo):
        s = self.getName()+' '+str(h)
        if s in memo:
            return memo[s]
        if h == 0:
            return 1 if self.tipo() == giocatore else 0
        tot = 0
        for f in self.lista_figli:
            tot += f.getWinInLevel(giocatore, h-1, memo)
        memo[s] = tot
        return tot

    def vittorie_livello(self, giocatore, h):
        memo = {}
        return self.getWinInLevel(giocatore, h, memo)

    def bestPossible(self, memo): #miglior risultato possibile per il giocatore corrente
        s = self.getName()
        if s in memo:
            return memo[s]
        if self.tipo() != '?':
            if self.tipo() == '-':
                return 0
            return 1 if self.tipo() == self.turn() else -1
        best = -1
        for v in self.lista_figli:
            best = max(best, -v.bestPossible(memo))
        memo[s] = best
        return best

    def strategia_vincente(self,giocatore):
        memo = {}
        best = self.bestPossible(memo)
        if self.turn() == giocatore:
            return best == 1
        return best == -1

def gen_tree(griglia):
    root = NodoTris(griglia)
    root.buildTree()
    return root

if __name__ == '__main__':
    #r = gen_tree([['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']])
    r = gen_tree([['', '', ''], ['', '', ''], ['', '', '']])
    print(r.strategia_vincente('x'), r.strategia_vincente('o'))
