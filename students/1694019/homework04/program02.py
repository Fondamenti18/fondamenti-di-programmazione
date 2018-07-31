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
Si veda ad esempio l'immagine albero_di_gioco.png che mostra l' albero di gioco che si ottiene a partire
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

from itertools import chain, permutations

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.last_move = self.find_last_move()

    def tipo(self):
        '''inserire qui il vostro codice'''
        #pos = permutations((0,1,2))
        diagonale = self.dgnl(self.nome)
        diagonale_inv = self.dgnl_inv(self.nome)
        colonna0,colonna1,colonna2 = self.clmn(self.nome,0), self.clmn(self.nome,1), self.clmn(self.nome,2)
        riga0,riga1,riga2 = self.nome[0], self.nome[1], self.nome[2]
        #case game end
        if (len(set(diagonale)) == 1) or (len(set(diagonale_inv)) == 1):
            if diagonale[0] == 'o': return 'o' #if the diagonal has equal elements
            elif diagonale_inv[0] == 'o': return 'o'
            else: return 'x'
        #case game not end
        if ("" in colonna0) or ("" in colonna1) or ("" in colonna2) or ("" in riga0) or ("" in riga1) or ("" in riga2): return "?"
        elif (len(set(colonna0)) == 1) or (len(set(colonna1)) == 1) or (len(set(colonna2)) == 1):
            if (colonna0.count('o') == 3) or (colonna1.count('o') == 3) or (colonna2.count('o') == 3): return 'o'
            elif (colonna0.count('x') == 3) or (colonna1.count('x') == 3) or (colonna2.count('x') == 3): return 'x'
        elif (len(set(riga0)) == 1) or (len(set(riga1)) == 1) or (len(set(riga2)) == 1):
            if (riga0.count('o') == 3) or (riga1.count('o') == 3) or (riga2.count('o') == 3): return 'o'
            elif (riga0.count('x') == 3) or (riga1.count('x') == 3) or (riga2.count('x') == 3): return 'x'
        #case flap and reaming
        else: return "-"

    def clmn(self,matrix,n_colonna):
        colonna = []
        for i in range(len(matrix)):
            colonna.append(matrix[i][n_colonna])
        return colonna

    def dgnl(self,matrix):
        diagonale = []
        for i in range(len(matrix)):
            diagonale.append(matrix[i][i])  # These are the diagonal elements
        return diagonale

    def dgnl_inv(self,matrix):
        diagonale_inv = []
        for i in reversed(range(len(matrix))):
            diagonale_inv.append(matrix[i][i])  # These are the diagonal elements
        return diagonale_inv

    def find_last_move(self):
        #t = True
        nodo = self.nome
        lst = []
        for x in nodo:
            for c in x:
                lst.append(c)
        if len(lst) > 0:
            if len(lst)%2 == 0: return 'o'
            else: return 'x'
        else: return '-'

    def esiti(self):
        '''inserire qui il vostro codice'''


    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''

    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''


def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    g = NodoTris(griglia)
    if g.tipo() != 'x' or g.tipo() != 'o' or g.tipo() != '-':
        for riga in g.nome:
            if '' in riga:
                if g.last_move == 'x':
                    for elm in permutations(riga): #le permutazioni sono tuple
                        g1 = g.nome
                        g1 = del g1.nome[riga]
                        for i in elm:
                            g1.nome.append
                for child in g.lista_figli:
                    gen_tree(child)
    return g

