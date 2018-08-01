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

import copy

class NodoTris:

    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self._tipo = self._calcola_tipo()
        self.prossimo_giocatore = 'o'
        self.celle_libere = []

        if self._tipo in ('o', 'x'):
            return
        o_count = 0
        x_count = 0
        for i in range(3):
            for j in range(3):
                if griglia[i][j] == '':
                    self.celle_libere.append( (i,j) )
                elif griglia[i][j] == 'o':
                    o_count += 1
                elif griglia[i][j] == 'x':
                    x_count += 1
        #print(f"x_count ({x_count}) o_count ({o_count})")
        if x_count >= o_count:
            #print(f"x_count ({x_count}) > o_count ({o_count})")
            self.prossimo_giocatore = 'o'
        elif o_count > x_count:
            self.prossimo_giocatore = 'x'

    

    def _calcola_tipo(self):
        non_terminato = False

        for i in range(3):
            if (self.nome[i][0] == self.nome[i][1] == self.nome[i][2]) and self.nome[i][0] != '':
                return self.nome[i][0]
            if self.nome[i][0] == '' or self.nome[i][1] == '' or self.nome[i][2] == '':
                non_terminato = True
        for j in range(3):
            if (self.nome[0][j] == self.nome[1][j] == self.nome[2][j]) and self.nome[0][j] != '':
                return self.nome[0][j]
        if (self.nome[0][0] == self.nome[1][1] == self.nome[2][2]) and self.nome[1][1] != '':
            return self.nome[1][1]
        if (self.nome[0][2] == self.nome[1][1] == self.nome[2][0]) and self.nome[1][1] != '':
            return self.nome[1][1]
        if non_terminato:
            return '?'
        return '-'

    def tipo(self):
        return self._tipo
    
    def esiti(self):
        t = self.tipo()
        if t == '-': return (1,0,0)
        if t == 'o': return (0,1,0)
        if t == 'x': return (0,0,1) 
        p,o,x = 0,0,0
        for f in self.lista_figli:
            e = f.esiti()
            p += e[0]
            o += e[1]
            x += e[2]
        return p,o,x

    def _esito(self):
        e = {'-' : (1,0,0),
             'o' : (0,1,0),
             'x' : (0,0,1),
             '?' : (0,0,0)}
        return e.get( self.tipo() )

    
    def vittorie_livello(self, giocatore, h):
        #print(f"vittorie_livello of height {h}")
        if h == 0:
            #print(f"self._esito(): {self._esito()}")
            if giocatore == 'o':
                return self._esito()[1]
            else:
                return self._esito()[2]
        r = sum(f.vittorie_livello(giocatore, h-1) for f in self.lista_figli)
        #print(f"sum: {r}, height: {h}")
        return r


    def strategia_vincente(self,giocatore):
        """
        Dato un nodo radice di un albero di gioco ed uno dei due giocatori, 
        restituisce True o False. 
        Restituisce True se giocatore ha una strategia vincente nella partita
        che ha come configurazione iniziale quella rappresentata dal nodo 
        radice, False altrimenti.
        Nota che un giocatore ha una strategia vincente rispetto ad una certa 
        configurazione se, qualunque siano le mosse dell'avversario ha sempre 
        la possibilita' di rispondere in modo che la partita termini con la 
        sua vittoria.
        """
        print(self.nome)
        if self.tipo() == giocatore:
            print("True")
            return True
        if self.tipo() not in ('-', '?'):
            print("False")
            return False

        for f in self.lista_figli:
            if f.strategia_vincente(giocatore) is True:
                return True
        return False
        
def gen_tree(griglia):
    root = NodoTris(griglia)
    figli = []
    for i,j in root.celle_libere:
        griglia_copy = copy.deepcopy(griglia)
        griglia_copy[i][j] = root.prossimo_giocatore
        figli.append( gen_tree(griglia_copy) )
    root.lista_figli = figli
    return root