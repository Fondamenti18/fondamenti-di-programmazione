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

from copy import deepcopy

import sys
sys.setrecursionlimit(999999999)

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []  # lista dei nodi figli
        self.turno = ''  # da il turno al gocatore
        self.stato = ''  # stato della partita
        self.altezza = 0  # altezza del nodo

    def tipo(self):
        '''torna il tipo di condizione'''
        return self.stato

    def esiti(self):
        '''torna la tripla dei possibili esiti'''
        p = stima_esiti_patta(self)
        x = stima_esiti_x(self)
        o = stima_esiti_o(self)
        return p, o, x

    def vittorie_livello(self, giocatore, h):
        '''torna il numero di vittorie del giocatore al livello h'''
        return stima_vittorie(self, giocatore, h)

    def strategia_vincente(self,giocatore):
        '''torna True se e' una strategia vincente per il giocatore'''
        if giocatore == self.turno:
            v = minmax(self, True)
        else:
            v = minmax(self, False)
        if v == 1:
            return True
        else:
            return False


def gen_tree(griglia):
    '''funzione che genera l'albero partedno dalla griglia'''
    n = NodoTris(griglia)
    set_turno(n)
    set_stato(n)
    if n.stato == '?':
        set_lista_figli(n)
        for nodo in n.lista_figli:
            generated_tree(nodo, 1)
    return n


def generated_tree(nodo, c):
    '''funzione ricorsiva per generare l'albero'''
    set_turno(nodo)
    set_stato(nodo)
    nodo.altezza = c
    if nodo.stato == '?':
        set_lista_figli(nodo)
        for n in nodo.lista_figli:
            generated_tree(n, c + 1)

def minmax(node, player):
    '''algortmo goloso minmax'''
    if len(node.lista_figli) == 0:
        a = valore(node)
    elif player:
        a = -1
        for figlio in node.lista_figli:
            a = max(a, minmax(figlio, False))
            if a == 1:
                break
    else:
        a = 1
        for figlio in node.lista_figli:
            a = min(a, minmax(figlio, True))
            if a == -1:
                break
    return a

def valore(node):
    '''torna il valore euristico del nodo'''
    if node.stato == 'x':
        return -1
    elif node.stato == 'o':
        return 1
    else:
        return 0

def stima_vittorie(node, giocatore, h):
    cnt = 0
    if node.stato == giocatore and node.altezza == h:
        cnt += 1
    if len(node.lista_figli) > 0:
        for child in node.lista_figli:
            cnt += stima_vittorie(child, giocatore, h)
    return cnt

def stima_esiti_patta(node):
    p = 0
    if node.stato == '-':
        p += 1
    if len(node.lista_figli)>0:
        for child in node.lista_figli:
            p += stima_esiti_patta(child)
    return p

def stima_esiti_x(node):
    p = 0
    if node.stato == 'x':
        p += 1
    if len(node.lista_figli)>0:
        for child in node.lista_figli:
            p += stima_esiti_x(child)
    return p

def stima_esiti_o(node):
    p = 0
    if node.stato == 'o':
        p += 1
    if len(node.lista_figli)>0:
        for child in node.lista_figli:
            p += stima_esiti_o(child)
    return p

def set_lista_figli(n):
    '''lista di nodi con possibili mosse'''
    l = []
    g = n.nome
    m = n.turno
    for i in range(3):
        for j in range(3):
            if g[i][j] == '':
                gg = deepcopy(g)
                gg[i][j] = m
                nn = NodoTris(gg)
                l.append(nn)
    n.lista_figli = l


def set_turno(n):
    '''decide quale mossa fare'''
    g = n.nome
    co, cx = 0, 0
    for i in range(3):
        for j in range(3):
            if g[i][j] == 'x':
                cx += 1
            if g[i][j] == 'o':
                co += 1
    if cx >= co:
        n.turno = 'o'
    else:
        n.turno = 'x'
    
def set_stato(n):
    '''torna la condizione(tipo) della griglia'''
    griglia=n.nome
    if griglia[0][0]==griglia[0][1]==griglia[0][2]=='o' or griglia[0][0]==griglia[0][1]==griglia[0][2]=='x':
        n.stato = griglia[0][0]
    elif griglia[1][0]==griglia[1][1]==griglia[1][2]=='o' or griglia[1][0]==griglia[1][1]==griglia[1][2]=='x':
        n.stato = griglia[1][0]
    elif griglia[2][0]==griglia[2][1]==griglia[2][2]=='o' or griglia[2][0]==griglia[2][1]==griglia[2][2]=='x':
        n.stato = griglia[2][0]
    elif griglia[0][0]==griglia[1][0]==griglia[2][0]=='o' or griglia[0][0]==griglia[1][0]==griglia[2][0]=='x':
        n.stato = griglia[0][0]
    elif griglia[0][1]==griglia[1][1]==griglia[2][1]=='o' or griglia[0][1]==griglia[1][1]==griglia[2][1]=='x':
        n.stato = griglia[0][1]
    elif griglia[0][2]==griglia[1][2]==griglia[2][2]=='o' or griglia[0][2]==griglia[1][2]==griglia[2][2]=='x':
        n.stato = griglia[0][2]
    elif griglia[0][0]==griglia[1][1]==griglia[2][2]=='o' or griglia[0][0]==griglia[1][1]==griglia[2][2]=='x':
        n.stato = griglia[0][0]
    elif griglia[0][2]==griglia[1][1]==griglia[2][0]=='o' or griglia[0][2]==griglia[1][1]==griglia[2][0]=='x':
        n.stato = griglia[0][2]
    else:
        if '' in griglia[0] or '' in griglia[1] or '' in griglia[2]:
            n.stato = '?'
        else:
            n.stato = '-'  
