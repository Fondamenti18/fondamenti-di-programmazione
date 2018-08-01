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
        self.lista_figli = []  # lista dei nodi figli

    def tipo(self):
        vincenti = [[(0, 0), (0, 1), (0, 2)],  # PRIMA RIGA
                    [(1, 0), (1, 1), (1, 2)],  # SECONDA RIGA
                    [(2, 0), (2, 1), (2, 2)],  # TERZA RIGA
                    [(0, 0), (1, 0), (2, 0)],  # PRIMA COLONNA
                    [(0, 1), (1, 1), (2, 1)],  # SECONDA COLONNA
                    [(0, 2), (1, 2), (2, 2)],  # TERZA COLONNA
                    [(0, 0), (1, 1), (2, 2)],  # DIAGONALE ALTO-SX -> BASSO-DX
                    [(0, 2), (1, 1), (2, 0)]]  # L'ALTRA DIAGONALE

        conta_vuoti = 0
        for x in range(len(self.nome)):
            for y in range(len(self.nome[0])):
                if self.nome[x][y] == '':
                    conta_vuoti += 1

        for check in vincenti:
            uno, due, tre = check
            a, b = uno
            c, d = due
            e, f = tre
            if self.nome[a][b] == self.nome[c][d] == self.nome[e][f]:
                if self.nome[a][b] != '':
                    return self.nome[a][b]

        if conta_vuoti == 0:
            return '-'
        else:
            return '?'

    def esiti(self):
        patta, vince_o, vince_x = 0, 0, 0
        tipo = self.tipo()
        if tipo == 'x':
            vince_x += 1
        elif tipo == 'o':
            vince_o += 1
        elif tipo == '-':
            patta += 1
        else:
            for x in self.lista_figli:
                patta1, vinceo1, vincex1 = x.esiti()
                patta += patta1
                vince_o += vinceo1
                vince_x += vincex1
        return patta, vince_o, vince_x

    def vittorie_livello(self, giocatore, h, altezza=0):
        contatore = 0
        if altezza == h:
            if self.tipo() == giocatore:
                return 1
        else:
            for x in self.lista_figli:
                contatore += x.vittorie_livello(giocatore, h, altezza + 1)
        return contatore

    def strategia_vincente(self, giocatore):
        if len(self.lista_figli) == 0:
            return self.tipo() == giocatore

        else:
            casi = [figlio.strategia_vincente(giocatore) for figlio in self.lista_figli]
            x, o = 0, 0
            for a in range(len(self.nome)):
                for b in range(len(self.nome[0])):
                    if self.nome[a][b] == 'x':
                        x += 1
                    if self.nome[a][b] == 'o':
                        o += 1
            mossa = 'o'
            if x < o:
                mossa = 'x'

            if mossa == giocatore:
                return True in casi
            else:
                return False not in casi


def gen_tree(griglia, configurazione=None):
    nodo = NodoTris(griglia)
    if not configurazione:                      # ricavo la configurazione (solo se sono la radice)
        num_o, num_x = 0, 0
        spazi = []
        for y, riga in enumerate(griglia):
            for x, quadrato in enumerate(riga):
                if quadrato == 'o':
                    num_o += 1
                elif quadrato == 'x':
                    num_x += 1
                else:
                    spazi.append((x, y))

        configurazione = (num_o, num_x, spazi)

    tipo = nodo.tipo()
    num_o, num_x, spazi = configurazione    # altrimenti la configurazione me la passa mio padre
    new_o, new_x = num_o, num_x
    if tipo == '?':                         # ricorsione: solo se la partita non è conclusa, altrimenti ritorno
        mossa = 'o'
        if num_o > num_x:                   # determino la mossa
            new_x += 1
            mossa = 'x'
        else:
            new_o += 1
        for spazio in spazi:                # riempio ricorsivamente gli spazi
            x, y = spazio
            new_griglia = [riga[:] for riga in griglia]
            new_spazi = spazi[:]

            new_griglia[y][x] = mossa
            new_spazi.remove(spazio)

            new_configurazione = (new_o, new_x, new_spazi)

            nodo.lista_figli.append(gen_tree(new_griglia, new_configurazione))

    return nodo
