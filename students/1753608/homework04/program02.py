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

1) DONE
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
        self.circle = 0
        self.cross = 0
        self.holes = []
        self.winner = None
        self.triad = [0,0,0]
        self.win = 0
        self.strategy = False
        self.lista_figli = [] #lista dei nodi figli

    def tipo(self):
        winner = self._tipo("col")
        if(not winner):
            winner = self._tipo("row")
            if(not winner):
                winner = self._diagonals()
                if(not winner):
                    if(len(self.holes) > 0):
                        winner = "?"
                    else:
                        winner = "-"
        return winner

    def _tipo(self,dir,x=0,y=0):
        best = None
        while(x < 3):
            comb = []
            elemA = self._direction(dir,x,y)
            comb.append(elemA)
            y+=1
            while(y < 3):
                elemB = self._direction(dir,x,y)
                if(elemA != elemB):
                    y+=1
                    continue
                else: comb.append(elemB)
                y += 1
            if(len(comb) == 3 and comb[0] != ""):
                best = comb
            y=0
            x+=1
        try:
            return best[0]
        except:
            return None

    def _direction(self, dir, y, x):
        col = dir == "col"
        if (col):
            elem = self.nome[y][x]
        else:
            elem = self.nome[x][y]
        if(not col and elem == ""): self.holes.append((x,y))
        elif(not col):
            if(elem == "o"):
                self.circle+=1
            elif(elem == "x"):
                self.cross+=1
        return elem

    def _diagonals(self,x=0,y=0):
        centro = self.nome[x+1][y+1]
        d1 = self.nome[x][y]
        d2 = self.nome[x][y+2]
        if (d1 == centro == self.nome[x+2][y+2]) and d1 != None:
            return d1
        if (d2 == centro == self.nome[x+2][y]) and d2 != None:
            return d2

    def esiti(self):
        if(self.winner != '?'):
            self._triad(self.winner)
        else:
            self._esiti(self.lista_figli)
        return tuple(self.triad)

    def _esiti(self,figli):
        for child in figli:
            if(child.winner != "?"):
                self._triad(child.winner)
                continue
            if(child.lista_figli != []):
                self._esiti(child.lista_figli)

    def _triad(self,winner):
        if(winner == "-"):
            self.triad[0] +=1
        if (winner == "o"):
            self.triad[1] += 1
        if (winner == "x"):
            self.triad[2] += 1

    def vittorie_livello(self, giocatore, h):
        self.win = 0
        lvl = 0
        if( h == 0):
            if(self.winner == giocatore):
                self.win+=1
        else:
            self._vittorie_livello(self.lista_figli,giocatore,lvl+1,h)
        return self.win

    def _vittorie_livello(self,figli,giocatore,lvl,h):
        if(lvl > h):
            return False
        for child in figli:
            if(h == lvl):
                if(child.winner == giocatore):
                    self.win+=1
            else:
                self._vittorie_livello(child.lista_figli,giocatore,lvl+1,h)

    def strategia_vincente(self,giocatore):
        avversario = self.get_avversario(giocatore)
        if(self.winner == "?"):
            strategy = self._strategia_vincente(self.lista_figli,giocatore,avversario,0,0,0)
        elif(self.winner == giocatore):
            strategy = True
        return strategy

    def _strategia_vincente(self,figli,giocatore,avversario,croce,patta,cerchio):
        for child in figli:
            if(child.lista_figli != []):
                return self._strategia_vincente(child.lista_figli, giocatore,avversario,croce,patta,cerchio)
            if(child.winner != "?"):
                if(child.winner == avversario):
                    croce+=1
                if(child.winner == "-"):
                    patta +=1
                if(child.winner == giocatore):
                    cerchio +=1
        return cerchio > patta+croce

    def get_avversario(self,giocatore):
        if (giocatore == "o"):
            return "x"
        elif (giocatore == "x"):
            return "o"

def _next(root):
    if(root.circle > root.cross):
        return "x"
    return "o"

def _copy(griglia):
    new = []
    for row in griglia:
        new.append(list(row))
    return new

def _get_triad(outcomes):
    triad = [0,0,0]
    for e in outcomes:
        if(e == "-"):
            triad[0] +=1
        if(e == "o"):
            triad[1] +=1
        if(e == "x"):
            triad[2] +=1
    return tuple(triad)

def genera(griglia):
    root = NodoTris(griglia)
    root.winner = root.tipo()
    next = _next(root)
    if(root.winner == "?"):
        for e in root.holes:
            new = _copy(griglia)
            x = e[0]
            y = e[1]
            new[x][y] = next
            root.lista_figli.append(new)
    for i,figlio in enumerate(root.lista_figli):
         root.lista_figli[i] = genera(figlio)
    return root

vuota = [['','',''],
         ['','',''],
         ['','','']]
main = None

def gen_tree(griglia):
    global main
    if(main == None): main = genera(vuota)
    if(griglia == main.nome):
        my_tree = main
    else:
        my_tree = _gen_tree(griglia,main.lista_figli,None)
    return my_tree

def _gen_tree(griglia,figli,value):
    for figlio in figli:
        if(figlio.nome == griglia):
            value = figlio
            return value
        else:
            value = _gen_tree(griglia, figlio.lista_figli,value)
    return value