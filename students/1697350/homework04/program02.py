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
from collections import defaultdict


class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []  # lista dei nodi figli
        self.padre = None
        self.pathsDone = False
        self.level = 0
        self.esitoDone = []
        self.vittorie_livelloDone = []
        self.strategia_vincenteDone = []
        self.esito = '?'
        self.root = self
        self.levelNodes = defaultdict(set)
        self.lista_mosse = []
        self.levelDictX = defaultdict(int)
        self.levelDictO = defaultdict(int)

    def checkRows(self, griglia):
        return self.checkGrid(griglia)

    def checkGrid(self, griglia):
        for i, lista in enumerate(griglia):
            if len(set(lista)) == 1 and lista[0] != '':
                return lista[0]
        return False

    def checkColumn(self, griglia):
        griglia = [col for col in zip(*griglia)]
        return self.checkGrid(griglia)

    def checkDiagonals(self, griglia):
        diagonal1 = [griglia[0][0], griglia[1][1], griglia[2][2]]
        diagonal2 = [griglia[0][2], griglia[1][1], griglia[2][0]]
        griglia = [diagonal1, diagonal2]
        return self.checkGrid(griglia)

    def checkPatta(self, griglia):
        for i, elem1 in enumerate(griglia):
            for j, elem2 in enumerate(elem1):
                if elem2 == '':
                    return False
        return True

    def printTree(self):
        self.printGriglia()
        for child in self.lista_figli:
            child.printTree()

    def printGriglia(self):
        print("------------------------")
        for row in self.nome:
            print(row)
        print("########################")

    def tipo(self):
        griglia = self.nome
        diagonal = self.checkDiagonals(griglia)
        rows = self.checkRows(griglia)
        columns = self.checkColumn(griglia)

        if rows: return rows

        if columns: return columns
        if diagonal: return diagonal

        if self.checkPatta(griglia):
            return '-'
        else:
            return '?'

    def init_method(self, type, giocatore = None, h = None):
        if type == 'esiti':
            self.esitoDone.append(1)
            if len(self.esitoDone) == 1:
                self.esiti()
        if type == 'vittorie_livello':
            self.vittorie_livelloDone.append(1)
            if len(self.vittorie_livelloDone) == 1:
                self.vittorie_livello(giocatore, h)
        if type == 'strategia_vincente':
            self.strategia_vincenteDone.append(1)
            if len(self.strategia_vincenteDone) == 1:
                self.strategia_vincente(giocatore)



    def esiti(self):
        self.init_method('esiti')
        num_p = 0
        num_o = 0
        num_x = 0
        head = makeMosse(self)

        for elem in head.lista_mosse:
            if elem == '-':
                num_p += 1
            elif elem == 'o':
                num_o += 1
            elif elem == 'x':
                num_x += 1
        return (num_p, num_o, num_x)

    def vittorie_livello(self, giocatore, h):
        self.init_method('vittorie_livello', giocatore, h)
        levelDict = None
        if giocatore == 'x':
            levelDict = self.levelDictX
        else:
            levelDict = self.levelDictO
        return levelDict[h]

    def strategia_vincente(self, giocatore):
        self.init_method('strategia_vincente', giocatore)
        for level, listNodes in self.levelNodes.items():

            countLevel = 0
            for node in listNodes:
                if node.esito == giocatore:
                    countLevel += 1
            if level > 0:
                countLevel2 = 0
                for node2 in self.levelNodes[level - 1]:
                    if node2.esito == '?':
                        countLevel2 += 1
                if countLevel > 0 and countLevel == countLevel2:
                    return True

        return False


def whoStart(griglia):
    numO = 0
    numX = 0
    for i, elem1 in enumerate(griglia):
        for j, elem2 in enumerate(elem1):
            if elem2 == 'o':
                numO += 1
            elif elem2 == 'x':
                numX += 1
    if numO > numX:
        return 'x'
    else:
        return 'o'


def copyGrid(griglia):
    griglia2 = []
    for i, elem1 in enumerate(griglia):
        innerGrid = []
        for j, elem2 in enumerate(elem1):
            innerGrid.append(elem2)
        griglia2.append(innerGrid)
    return griglia2


def makeMossa(node, casellaTurno):
    griglia = node.nome
    for i, elem1 in enumerate(griglia):
        for j, elem2 in enumerate(elem1):
            if elem2 == '':
                griglia2 = copyGrid(griglia)
                griglia2[i][j] = casellaTurno
                newNode = NodoTris(griglia2)
                node.lista_figli.append(newNode)


def makeMosse(head):
    if head.pathsDone:
        return head
    casellaTurno = whoStart(head.nome)

    if not head.checkPatta(head.nome):
        makeMossa(head, casellaTurno)
    tipo = head.tipo()
    head.root.levelNodes[head.level].add(head)
    if tipo == 'x':
        head.root.levelDictX[head.level] += 1
        head.root.lista_mosse.append("x")
        head.esito = 'x'
        return head.root

    elif tipo == 'o':
        head.root.lista_mosse.append("o")
        head.root.levelDictO[head.level] += 1
        head.esito = 'o'
        return head.root
    elif tipo == '-':
        head.esito = '-'
        head.root.lista_mosse.append("-")
        return head.root

    for child in head.lista_figli:
        child.level = head.level + 1
        child.padre = head
        child.root = head.root
        makeMosse(child)

    return head.root


def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    head = NodoTris(griglia)
    f = open("out.json", 'w')
    makeMosse(head)
    head.pathsDone = True

    # print(head.level)
    # print(head.lista_figli[0].level)
    # print(head.lista_figli[0].lista_figli[0].level)
    # casellaTurno = whoStart(head.nome)
    # makeMossa(head, casellaTurno)
    return head


