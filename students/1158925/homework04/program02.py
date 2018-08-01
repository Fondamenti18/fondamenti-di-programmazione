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

Una configurazione del gioco e' dunque univocamente determinata	 dal contenuto della griglia.

Nel seguito assumiamo che il contenuto della griglia sia  rappresentato tramite	 lista di liste.
La dimensione della lista di liste M e'	 3x3 ed	  M[i][j] contiene	'', 'x', o 'o'	a seconda 
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


Bisogna progettare le seguente	funzione 

gen_tree(griglia)
che, data la configurazione di gioco griglia,  costruisce l'albero di gioco che si ottiene a partire 
dalla configurazione griglia e ne restituisce la radice. I nodi dell'albero devono essere 
oggetti della classe NodoTris.

Per testare la correttezza della vostra implementazione di gen_tree() il grade utilizzera' quattro metodi 
della	classe NodoTris che dovete comunque implementare: 

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
import _pickle

class NodoTris:
    CACHE={}
    ROWS=[(0,0,1,1,2,2),
          (2,0,1,1,0,2),
          (0,0,0,1,0,2),
          (1,0,1,1,1,2),
          (2,0,2,1,2,2),
          (0,0,1,0,2,0),
          (0,1,1,1,2,1),
          (0,2,1,2,2,2)]

    def __init__(self, griglia,empties,padre):
        self.nome = griglia
        self.padre = padre
        self.empties = empties
        self.lista_figli = [] #lista dei nodi figli
        self._esiti = [0,0,0] #patte, o , x

        if self.padre:
            self.livello = padre.livello +1
            self.player = 'o' if padre.player == 'x' else 'x'
        else:
            self.livello = 0
            self.player = 'o' if sum([cell=='' for row in self.nome for cell in row]) %2 > 0 else 'x'

        self._tipo = self.check_victory()
        self._is_victory = self._tipo == 'o' or self._tipo == 'x'


    def check_victory(self):

        for row in NodoTris.ROWS:
            x1,y1,x2,y2,x3,y3= row
            res1 =self.nome[y1][x1]
            res2 =self.nome[y2][x2]
            res3 =self.nome[y3][x3]
            os=0
            xs=0


            os += 1 if res1 == 'o' else 0
            os += 1 if res2 == 'o' else 0
            os += 1 if res3 == 'o' else 0

            if os == 3:
                self._esiti[1] = 1
                return 'o'

            xs += 1 if res1 == 'x' else 0
            xs += 1 if res2 == 'x' else 0
            xs += 1 if res3 == 'x' else 0

            if xs == 3:
                self._esiti[2] = 1
                return 'x'

        if len(self.empties) > 0:
            return '?'
        else:
            self._esiti[0] = 1
            return '-'

    @property
    def is_victory(self):
        return self._is_victory

    def score(self,giocatore):
        if self._tipo == giocatore:
            return 10 - self.livello
        elif self._tipo == '?' or self._tipo == '-':
            return 0
        else:
            return self.livello -10

    def strategia_vincente(self, giocatore):
        if self._tipo!='?':
            return self.score(giocatore)

        scores = []

        for move in self.lista_figli:
            scores.append(move.strategia_vincente(giocatore))

        if self.player == giocatore:
            max_score_index = max(scores)
            return max_score_index >0
        else:
            min_score_index = min(scores)
            return min_score_index >0

    def tipo(self):
        '''inserire qui il vostro codice'''
        return self._tipo

    def esiti(self):
        '''inserire qui il vostro codice'''
        l_esiti=[0,0,0]
        self.get_esiti(l_esiti)
        return tuple(l_esiti)

    def get_esiti(self,esiti):
        esiti[0] += self._esiti[0]
        esiti[1] += self._esiti[1]
        esiti[2] += self._esiti[2]

        for child in self.lista_figli:
            child.get_esiti(esiti)


    def _vittorie_livello(self,giocatore,h,vittorie):
        if self.livello == h and self._tipo == giocatore:
            vittorie[0]+=1
        else:
            for child in self.lista_figli:
                child._vittorie_livello(giocatore,h,vittorie)

    def vittorie_livello(self, giocatore, h):
        vittorie = [0]
        self._vittorie_livello(giocatore,h,vittorie)
        return vittorie[0]

    def __repr__(self):
        return str(self.nome)


def allinea_livello(node):
    for child in node.lista_figli:
        child.livello = node.livello +1
        allinea_livello(child)

def step(grid, empties,padre):
    k = _pickle.dumps(grid,-1)

    try:
        node = NodoTris.CACHE[k]
        if padre:
            node.livello = padre.livello+1
            node.padre = padre
            allinea_livello(node)

        return node

    except:
        node = NodoTris(grid,empties,padre)
        NodoTris.CACHE[k] = node

        if node.is_victory:
            return node

        for slot in empties:

            next_grid = _pickle.loads(k)
            next_grid[slot[1]][slot[0]] = node.player
            new_empties = _pickle.loads(_pickle.dumps(empties,-1))
            new_empties.remove(slot)
            child = step(next_grid,new_empties,node)
            node.lista_figli.append(child)


        return node

def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    NodoTris.CACHE.clear()
    empties=[(i,j) for i in range(3) for j in range(3) if griglia[j][i] == '']
    # for i in range(3):
    #     for j in range(3):
    #         if griglia[j][i] == '':
    #             empties.append([i,j])
    root = step(griglia,empties,None)
    return root

if __name__ == "__main__":

    # a=gen_tree([['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']])
    # print("strategia vincente", a.strategia_vincente('x'))
    # print("vittorie_livello o", [a.vittorie_livello('o',h) for h in range(4)])
    # print("vittorie_livello x", [a.vittorie_livello('x',h) for h in range(4)])
    # b = gen_tree([['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']])
    # print(b.strategia_vincente('o'))
    # c = gen_tree([['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']])
    # print(c.strategia_vincente('x'))
    # d = gen_tree([['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']])
    # print(d.strategia_vincente('o'))
    g1=[['x', 'o', 'o'],
        ['x', 'x', 'o'],
        ['',  '',  '']]
    #
    # g5=[['', 'x', ''], ['', 'o', ''], ['', '', '']] #True
    # g6=[['', 'o', ''], ['', 'x', ''], ['', '', '']] #False
    # g7=[['', 'x', 'o'], ['', '', ''], ['', '', '']] #True
    # g8=[['', 'o', 'x'], ['', '', ''], ['', '', '']] #False
    # listab=[g5,g6,g7,g8]
    # listab=[g1]
    # lista1= [gen_tree(x) for x in listab]
    #
    # print(gen_tree(g1).strategia_vincente('x'))
    # print("########") #[False, True]
    # print(gen_tree(g1).strategia_vincente('o'))
    #lista3=[y.esiti() for y in lista1]
    #gen_tree([['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']])
    g5 = [['', 'x', ''], ['', 'o', ''], ['', '', '']]
    g6 = [['', 'o', ''], ['', 'x', ''], ['', '', '']]
    g7 = [['', 'x', 'o'], ['', '', ''], ['', '', '']]
    g8 = [['', 'o', 'x'], ['', '', ''], ['', '', '']]
    listab = [g1]

    lista1 = [gen_tree(x) for x in listab]

    lista2 = [y.strategia_vincente('x') for y in lista1]
    print(lista2)

    #[True, False, True, False]

    # print(gen_tree(g1).strategia_vincente('x'))
    # print("#####")
    # print(gen_tree(g1).strategia_vincente('o'))

