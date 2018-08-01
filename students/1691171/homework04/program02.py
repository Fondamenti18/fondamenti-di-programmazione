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

1) NON DEVE ESSERE RICORSIVO
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
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli

    def tipo_nodo(self):
        ris = '-'
        i = 0
        while i < len(self.nome):
            if self.nome[i][0] == 'o' and self.nome[i][1] == 'o' and self.nome[i][2] == 'o':
                ris = 'o'
            elif self.nome[i][0] == 'x' and self.nome[i][1] == 'x' and self.nome[i][2] == 'x':
                ris = 'x'
            i += 1

        i = 0
        while i < len(self.nome[0]):
            if self.nome[0][i] == 'o' and self.nome[1][i] == 'o' and self.nome[2][i] == 'o':
                ris = 'o'
            elif self.nome[0][i] == 'x' and self.nome[1][i] == 'x' and self.nome[2][i] == 'x':
                ris = 'x'
            i += 1

        if self.nome[0][0] == 'o' and self.nome[1][1] == 'o' and self.nome[2][2] == 'o':
            ris = 'o'
        elif self.nome[0][0] == 'x' and self.nome[1][1] == 'x' and self.nome[2][2] == 'x':
            ris = 'x'

        if self.nome[0][2] == 'o' and self.nome[1][1] == 'o' and self.nome[2][0] == 'o':
            ris = 'o'
        elif self.nome[0][2] == 'x' and self.nome[1][1] == 'x' and self.nome[2][0] == 'x':
            ris = 'x'

        if ris == '-':  # controllo se e' una patta
            i = 0
            while i < len(self.nome):
                j = 0
                while j < len(self.nome[0]):
                    if self.nome[i][j] == '':
                        ris = '?'
                    j += 1
                i += 1

        return ris

    def tipo(self):
        return self.tipo_nodo()

    def calcola_esiti(self, ris):
        tipo = self.tipo()
        if tipo == '-':
            ris[0] += 1
        elif tipo == 'o':
            ris[1] += 1
        elif tipo == 'x':
            ris[2] += 1
        else:
            for f in self.lista_figli:
                f.calcola_esiti(ris)

    def __str__(self):
        return str(self.nome)

    '''
    2)
    esiti(self)
    che, dato un nodo radice di un albero di gioco, restituisce una tripla con i possibili
    esiti della partita che ha come configurazione iniziale quella rappresentata dal nodo.
    Piu' precisamente: il primo elemento della tripla  e' il numero di  patte possibili,
    il secondo e' il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento
    e' il numero di possibili vittorie per il giocatore 'x'.
    '''
    def esiti(self):
        ris = [0,0,0]
        self.calcola_esiti(ris)
        return (ris[0], ris[1], ris[2])

    '''
    3)
    vittorie_livello(self, giocatore, h)
    che, dato un nodo radice di un albero di gioco, uno dei due giocatori ed un intero h,
    restituisce il numero di nodi che rappresentano una vittoria per il giocatore e si
    trovano ad altezza h nell'albero. In altri termini restituisce il numero di vittorie possibili
    per giocatore in esattamente h mosse, nella partita che ha come configurazione iniziale
    quella rappresentata dalla radice dell'albero.
    '''

    def vittorie(self, giocatore, h, corrente):
        if h == corrente and self.tipo() == giocatore:
            return 1
        else:
            v = 0
            for n in self.lista_figli:
                v += n.vittorie(giocatore, h, corrente+1)
            return v

    def vittorie_livello(self, giocatore, h):
        if self.tipo() == giocatore and h == 0:
            return 1
        corrente = 0
        v = 0
        for n in self.lista_figli:
            v += n.vittorie(giocatore, h, corrente+1)
        return v

    '''
    4)
    strategia_vincente(self,giocatore)
    che, dato un nodo radice di un albero di gioco ed uno dei due giocatori, restituisce True o False.
    Restituisce True  se  giocatore ha una strategia vincente  nella partita
    che ha come configurazione iniziale quella rappresentata dal nodo radice, False altrimenti.

    Nota che un giocatore ha una strategia vincente rispetto ad una certa configurazione se,
    qualunque siano le mosse dell'avversario ha sempre la possibilita' di rispondere in modo
    che la partita termini con la sua vittoria.
    '''

    def strategia_vincente(self,giocatore):
        if self.tipo() == giocatore:
            return True
        elif self.tipo() == '?':
            # vince = True
            for f in self.lista_figli:
                return f.strategia_vincente(giocatore)
            # return vince
        else:
            return False

    def prossimo_turno(self):
        counto, countx = 0, 0
        for i in self.nome:
            for j in i:
                if j == 'o':
                    counto += 1
                elif j == 'x':
                    countx += 1
        if counto == countx:
            return 'o'
        return 'x'

def gen_tree(griglia):
    r = NodoTris(griglia)
    if r.tipo() == '?':
        prox = r.prossimo_turno()
        righe = len(griglia)
        colonne = len(griglia[0])
        i = 0
        while i < righe:
            j = 0
            while j < colonne:
                if griglia[i][j] == '':
                    griglia2 = [griglia[0][:], griglia[1][:], griglia[2][:]]
                    griglia2[i][j] = prox
                    a = gen_tree(griglia2)
                    r.lista_figli.append(a)
                j += 1
            i += 1
    return r