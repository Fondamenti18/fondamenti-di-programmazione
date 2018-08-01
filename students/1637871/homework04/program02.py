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

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        empty = ''
        wins = [[(1, 0), (1, 1), (1, 2)], [(0, 0), (0, 1), (0, 2)], [(0, 1), (1, 1), (2, 1)],
                [(0, 0), (1, 0), (2, 0)], [(0, 2), (1, 2), (2, 2)], [(2, 0), (2, 1), (2, 2)],
                [(0, 2), (1, 1), (2, 0)], [(0, 0), (1, 1), (2, 2)]]
        for x in wins:
            qw, er, ty = x
            q, w = qw;
            e, r = er;
            t, y = ty
            if self.nome[e][r] == self.nome[t][y] == self.nome[q][w]:
                if self.nome[q][w] != empty:
                    ritorno = self.nome[e][r]
                    return ritorno
        empties = 0
        h = len(self.nome)
        k = len(self.nome[0])
        for x in range(h):
            for y in range(k):
                if self.nome[x][y] == empty: empties += 1
        if empties != 0:
            return '?'
        else:
            return '-'


    def esiti(self):
        vo = 0; vx = 0; p = 0
        t = self.tipo()
        if t == 'x': vx += 1
        elif t == '-': p += 1
        elif t == 'o': vo += 1
        else:
            for el in self.lista_figli:
                ris = el.esiti()
                vx += ris[2]; vo += ris[1]; p += ris[0]
        return p, vo, vx


    def my_vittorie_livello(self, giocatore, h, height):
        count = 0
        if height == h:
            if self.tipo() == giocatore: return 1
        else:
            for el in self.lista_figli: count += el.my_vittorie_livello(giocatore, h, height + 1)
        return count

    def vittorie_livello(self, giocatore, h):
        ris = self.my_vittorie_livello(giocatore, h, 0)
        return ris


    def strategia_vincente(self,giocatore):
        lista = []  # creo una lista vuota
        cnx = 0  # contatore x
        cno = 0  # contantore o
        mossa = 'o'  # la mia mossa è sempre o
        if self.lista_figli == []:  # se lista figli è vuota
            if self.tipo() == giocatore:  # se la vittoria corrisponde al giocatore
                return True  # ritorna vero
            else:
                return False  # sennò falso
        else:  # altrimenti se la vittoria è del giocatore avversario
            for x in self.nome:  # per x in matrice
                for y in x:  # per y in lista nella matrice
                    if y == 'x':  # se y uguale ad x
                        cnx += 1  # incremento conta x
                    elif y == 'o':  # se y uguale ad o
                        cno += 1  # incremento conta o
            if cnx < cno:  # se conta x è minore di conta o
                mossa = 'x'  # allora la mossa tocca ad x
            for x in self.lista_figli:  # per x in lista dei figli
                lista.append(x.strategia_vincente(
                    giocatore))  # metto nella mia lista la funzione ricorsiva di x per strategia vincente
            if mossa == giocatore:  # se mossa corrisponde al giocatore
                for x in lista:  # ciclo in lista creata
                    if x == True:  # se corrisponde a True
                        return True  # ritorno True
                return False  # altrimenti False
            if mossa != giocatore:  # se mossa non corrisponde al giocatore
                for x in lista:  # ciclo in lista e vedo se c'è almeno un False il giocatore in quella parte non vince
                    if x == False:
                        return False  # ritorno false
                return True  # sennò vero


def my_gen_tree(griglia, cnf):
    node = NodoTris(griglia);no = cnf[0];nx = cnf[1];spaces = cnf[2];nex = nx;neo = no
    if node.tipo() != '-' and node.tipo() != 'o' and node.tipo() != 'x':
        move = 'o'
        if nx < no: nex += 1; move = 'x'
        else:neo += 1
        for space in spaces:
            a, b = space
            ngriglia = []
            for row in griglia: ngriglia.append(row[:])
            nspaces = []
            for x in spaces: nspaces.append(x)
            ngriglia[b][a] = move
            nspaces.remove(space)
            node.lista_figli.append(my_gen_tree(ngriglia, (neo, nex, nspaces)))
    return node

def gen_tree(griglia):
    no = 0; nx = 0; spaces = []; b = 0
    for row in griglia:
        a = 0
        for s in row:
            if s == 'x': nx += 1
            elif s == 'o': no += 1
            else: spaces.append((a, b))
            a+=1
        b+=1
    node = my_gen_tree(griglia, (no, nx, spaces))
    return node
