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

from copy import deepcopy
 
def conta_elemento(griglia, el):
    count = 0
    for row in griglia:
        for elem in row:
            if elem == el:
                count += 1
    return count
 
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = gen_tree(griglia, False) #lista dei nodi figli
        self.turno = turno(griglia)
 
    def tipo(self):
        '''inserire qui il vostro codice'''
        return tipo(self.nome)
 
    def esiti(self):
        '''inserire qui il vostro codice'''
        r = [0, 0, 0]
        t = self.tipo()
        if t == '-':
            r[0] = 1
        elif t == 'o':
            r[1] = 1
        elif t == 'x':
            r[2] = 1
        for nodo in self.lista_figli:
            e = list(nodo.esiti())
            for i in range(3):
                r[i] += e[i]
        return tuple(r)
 
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        if h == 0:
            if self.tipo() == giocatore:
                return 1
            return 0
        count = 0
        for nodo in self.lista_figli:
            count += nodo.vittorie_livello(giocatore, h-1)
        return count
 
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        tipo = self.tipo()
        if tipo == giocatore:
            return True
        if tipo == '?':
            if self.turno == giocatore:
                for nodo in self.lista_figli:
                    if nodo.strategia_vincente(giocatore):
                        return True
                return False
            else:
                for nodo in self.lista_figli:
                    if not nodo.strategia_vincente(giocatore):
                        return False
                return True
        else:
            return False
 
def turno(griglia):
    if conta_elemento(griglia, 'x') == conta_elemento(griglia, 'o'):
        return 'o'
    return 'x'
 
def tipo(campo):
        for i in range(3):
            if campo[i][0] != '' and campo[i][0] == campo[i][1] and campo[i][1] == campo[i][2]:
                return campo[i][0]
        for i in range(3):
            if campo[0][i] != '' and campo[0][i] == campo[1][i] and campo[1][i] == campo[2][i]:
                return campo[0][i]
        if campo[0][0] != '' and campo[0][0] == campo[1][1] and campo[1][1] == campo[2][2]:
            return campo[0][0]
        if campo[0][2] != '' and campo[0][2] == campo[1][1] and campo[1][1] == campo[2][0]:
            return campo[0][2]
        if conta_elemento(campo, '') == 0:
            return '-'
        else:
            return '?'
 
def gen_tree(griglia, rad=True):
    '''inserire qui il vostro codice'''
    if rad:
        return NodoTris(griglia)
    if tipo(griglia) != '?':
        return []
    mossa = turno(griglia)
    comb = list()
    for i,x in enumerate(griglia):
        for k,y in enumerate(x):
            if y == '':
                copia = deepcopy(griglia)
                copia[i][k] = mossa
                comb.append(NodoTris(copia))
    return comb
