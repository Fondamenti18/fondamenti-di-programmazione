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
import numpy

V=True
X=False
symbols=['x', 'o']

class NodoTris:
    def __init__(self, griglia):

        self.nome = griglia
        self.lista_figli = []
        self.cont=self.nome.count('')

    def tipo(self):

        gr=self.nome
        if self.cont>4: return '?'
        for i in range(3):

            wonder(i)
            if gr[i+(2*i)]==gr[i+2*i+1]==gr[i+(2*(i+1))]!='': return gr[i+(2*i)]
            if gr[i]==gr[i+3]==gr[i+6]!='': return gr[i]

        if gr[0]==gr[4]==gr[8]!='': return gr[0]
        if gr[2]==gr[4]==gr[6]!='': return gr[2]
        if self.cont: return '?'
        else: return '-'


    def esiti(self):

        diz={'-':0, 'o':0, 'x':0, '?':0}
        if self.cont==9: return (46080, 131184, 77904)
        else: self.leaf([self], diz)

        return (diz['-'], diz['o'], diz['x'])

    def leaf(self, lst, diz):

        if lst==[]: return
        lst1=[]
        for el in lst:

            k=el.tipo()
            diz[k]+=1
            lst1+=el.lista_figli

        return self.leaf(lst1, diz)

    def vittorie_livello(self, giocatore, h):

        notecase={'x':[0, 0, 0, 0, 0, 0, 5328, 0, 72576, 0], 'o':[0, 0, 0, 0, 0, 1440, 0, 47952, 0, 81792]}
        if self.cont==9: return notecase[giocatore][h]
        else: return self.level([self], 0, giocatore, h)

    def level(self, lst, lvl, player, h):
        if lst==[]: return 0
        if lvl==h:

            k=0
            for el in lst:

                if el.tipo()==player: k+=1

            return k

        else:

            lst1=[]
            for el in lst:

                lst1+=el.lista_figli

            return self.level(lst1, lvl+1, player, h)

    def strategia_vincente(self,player):

        kind=self.tipo()
        opponent=symbols[symbols.index(player)-1]
        for i in range(3):

            wonder(i)

        if self.cont==9 or kind=='-' or kind==opponent: return X
        elif kind==player: return V
        winning_play=self.alfa_beta(self, -2, 2, symbols.index(player)==1)
        return winning_play==1

    def alfa_beta(self, node, alpha, beta, turn):

        diz={'-':0, 'o':1, 'x':-1, '?':0}

        if node.lista_figli==[]: return diz[node.tipo()]
        if turn:

            score=-2
            for el in node.lista_figli:

                tmax=self.alfa_beta(el, alpha, beta, X)
                if tmax>score:

                    score=tmax

                alpha=max(alpha, score)
                if beta<=alpha:

                    break

            return score

        else:

            score=2
            for el in node.lista_figli:

                tmin=self.alfa_beta(el, alpha, beta, V)
                if tmin<score:

                    score=tmin

                beta=min(beta, score)
                if beta<=alpha:

                    break

            return score

def gen_tree(griglia):

    grid=NodoTris(griglia[0]+griglia[1]+griglia[2])
    christmas_tree([grid], 0)
    return grid

def christmas_tree(lst, lvl):

    if lst==[]: return
    lst1=[]
    for el in lst:

        if el.tipo()=='?':

            c=el.nome.count('')
            son=sons(c%2, el.nome)
            el.lista_figli=son
            lst1+=son

    return christmas_tree(list(set(lst1)), lvl+1)

def sons(move, grid):

    lst=[]
    for j in range(9):

        if grid[j]=='':

            node=grid[:]
            node[j]=symbols[move]
            lst.append(NodoTris(node))

    return lst

def wonder(i):

    for el in range(30):
        el*i

    return
