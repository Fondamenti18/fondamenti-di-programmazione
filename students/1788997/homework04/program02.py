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

from copy import copy

def win(gr):
    if gr[0] == gr[3] == gr[6] != '': return gr[0]
    if gr[1] == gr[4] == gr[7] != '': return gr[1]
    if gr[2] == gr[5] == gr[8] != '': return gr[2]
    
    if gr[0] == gr[1] == gr[2] != '': return gr[0]
    if gr[3] == gr[4] == gr[5] != '': return gr[3]
    if gr[6] == gr[7] == gr[8] != '': return gr[6]
    
    if gr[0] == gr[4] == gr[8] != '': return gr[0]
    if gr[2] == gr[4] == gr[6] != '': return gr[2]
    
    return False

level = 0
def f(n, player, lvl):
    if len(n.lista_figli) == 0 or lvl == 0: return n.v
    if n.turn == player:
        res = -100
        for node in n.lista_figli:
            res = max(res, f(node, player, lvl-1))
    else:
        res = 100
        for node in n.lista_figli:
            res = min(res, f(node, player, lvl-1))
    return res




class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.turn = ''
        self.v = 0
    def tipo(self):
        '''inserire qui il vostro codice'''
        r = win(self.nome)
        if not r:
            for i in range(len(self.nome)):
                if self.nome[i] == '': return '?'
            return '-'
        return r
    
    def esiti(self):
        '''inserire qui il vostro codice'''
        res = self.tipo()
        x,y,z = 0,0,0
        if res != '?':
            return 1 if res == '-' else 0, 1 if res == 'o' else 0, 1 if res == 'x' else 0
        else:
            for n in self.lista_figli:
                x1,y1,z1 = n.esiti()
                x += x1
                y += y1
                z += z1
            return x,y,z
                
    def vittorie_livello(self, giocatore, h, lv = 0):
        '''inserire qui il vostro codice'''
        s = 0
        if lv == h: 
            if self.tipo() == giocatore: return 1
        else:
            for n in self.lista_figli:
                s += n.vittorie_livello(giocatore, h, lv + 1)
        return s
    
        
        
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        res = f(self, 'o', level)
        if res > 0 and giocatore != 'o': return False
        if res < 0 and giocatore == 'o': return False
        if res == 0 and (giocatore == 'o' or giocatore == 'x'): return False
        return True
        

def recursiveTree(gr, lp, lvl=0):
    global level
    Nodo = NodoTris(gr)
    Nodo.turn = lp
    if lvl > level: level = lvl
    res = win(gr)
    if res: 
        Nodo.v = 100 if res == 'o' else -100
        return Nodo
    else:
        for n in range(9):
            pos = n % 3 + int(n / 3)*3
            if gr[pos] == '':
                gr2 = copy(gr)
                gr2[pos] = lp 
                Nodo.lista_figli.append(recursiveTree(gr2, 'o' if lp == 'x' else 'x', lvl+1))
        return Nodo
def choosePlayer(grid):
    p1, p2 = 0, 0
    for x in grid:
        if x == 'x': p1 +=1
        elif x == 'o': p2 += 1
    if p1 == p2: return 'o'
    elif p2 > p1: return 'x'
def gen_tree(griglia):
    gr = []
    for l in griglia: gr += l
    return recursiveTree(gr, choosePlayer(gr))