# -*- coding: utf-8 -*-
'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3Ã—3 caselle.
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
import functools
import time

def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]

    return memoizer


class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self._turno = ''

    @memoize
    def tipo(self):
        # verifica se un giocatore ha vinto in orizziontale
        for row in self.nome:
            if all_x(row): return 'x'
            if all_o(row): return 'o'

        # verifica se un giocatore ha vinto in verticale
        for col in zip(*self.nome):
            if all_x(col): return 'x'
            if all_o(col): return 'o'

        # verifica se un giocatore ha vinto in diagonale
        diag1 = [self.nome[0][0], self.nome[1][1], self.nome[2][2]] #[self.nome[i][i]     for i in range(3)]
        diag2 = [self.nome[0][2], self.nome[1][1], self.nome[2][0]] #[self.nome[i][2 - i] for i in range(3)]

        if all_x(diag1) or all_x(diag2): return 'x'
        if all_o(diag1) or all_o(diag2): return 'o'

        # verifica se ci sono caselle vuote
        if any(y == '' for x in self.nome for y in x):
            return '?'

        return '-'

    def esiti(self):
        result = (0,0,0)

        tipo = self.tipo()
        if tipo == '-': result = (1, 0, 0)
        if tipo == 'o': result = (0, 1, 0)
        if tipo == 'x': result = (0, 0, 1)

        for child in self.lista_figli:
            child_result = child.esiti()
            result = (result[0] + child_result[0],
                      result[1] + child_result[1],
                      result[2] + child_result[2])

        return result

    def vittorie_livello(self, giocatore, h):
        if h == 0:
            return 1 if self.tipo() == giocatore else 0

        vict_count = 0

        for child in self.lista_figli:
            vict_count += child.vittorie_livello(giocatore, h - 1)

        return vict_count

    '''
    Considerando che ad ogni mossa di un giocatore ci si sposta su un ramo dell'albero con una possibilità ridotta di nuovi movimenti, 
    l'idea della strategia vincente è vedere se per ogni spostamento che fa l'avversario nell'albero è comunque possibile spostarsi nuovamente su un ramo che porta alla vittoria del giocatore 
    (controbilanciando così la mossa dell'avversario).
    La funzione in se è divisa in due blocchi: uno per il turno del giocatore e uno per il turno dell'avversario. Per il turno del giocatore si verifica se può vincere in una mossa, 
    se non è così si chiama ricorsivamente strategia_vincente per ogni figlio e si verifica se in almeno un caso (funzione any()) restituisce True. Per il turno dell'avversario si verifica 
    se può portare la partita in una mossa a una vittoria per se stesso o ad una patta, in quel caso restituisce False, altrimenti 
    si chiama ricorsivamente strategia_vincente e si verifica se in tutti i casi (funzione all()) restituisce True 
    (quindi il giocatore ha sempre modo di controbilanciare la mossa dell'avversario, non importa quale essa sia, riportando la partita su una strada che termina in vittoria per lui).
    '''
    def strategia_vincente(self, giocatore):
        avversario = 'x' if giocatore == 'o' else 'o'

        # se il caso iniziale  una partita finita verifica se ha vinto giocatore
        if self.tipo() != '?':
            return self.tipo() == giocatore

        if self.turno() == giocatore:
            acc = []
            for child in self.lista_figli:
                if child.tipo() == giocatore:
                    return True
                if child.tipo() == '?':
                    acc.append(child.strategia_vincente(giocatore))
            return any(acc)
        else: # turno avversario
            acc = []
            for child in self.lista_figli:
                if child.tipo() == avversario:
                    return False
                if child.tipo() == '-':
                    return False
                if child.tipo() == '?':
                    acc.append(child.strategia_vincente(giocatore))

            return len(acc) > 0 and all(acc)

    @memoize
    def turno(self):
        count = 0

        # itera righe e colonne incrementando il contatore per 'x' e 'o'
        for row in self.nome:
            for col in row:
                if col == 'x' or col == 'o':
                    count += 1

        # con un numero dispari di turni giocati tocca a 'x', con un numero pari tocca a 'o'
        if count % 2: return 'x'
        else:         return 'o'

    def __str__(self):
        res = ''

        for row in self.nome:
            res += str(row) + '\n'

        return res

def gen_tree(griglia):
    node = NodoTris(griglia)

    if node.tipo() != '?':
        return node

    for i in range(3):
        for j in range(3):
            if griglia[i][j] == '':
                griglia_figlio = manual_deep_copy(griglia)
                griglia_figlio[i][j] = node.turno()
                node.lista_figli.append(gen_tree(griglia_figlio))

    return node

def all_x(list):
    return list[0] == 'x' and list[1] == 'x' and list[2] == 'x'

def all_o(list):
    return list[0] == 'o' and list[1] == 'o' and list[2] == 'o'

def manual_deep_copy(l):
    return [[l[0][0], l[0][1], l[0][2]],
            [l[1][0], l[1][1], l[1][2]],
            [l[2][0], l[2][1], l[2][2]]]

def print_tree(node):
    print(node)
    print('childs: ', len(node.lista_figli))
    print('-------------------')
    for f in node.lista_figli:
        print_tree(f)

def startTimer():
    return time.time()

def stopTimer(start, f):
    print('The function ',f ,' ran for', time.time() - start)


if __name__ == '__main__':
    g0=[['', '', ''], ['', '', ''], ['', '', '']]
    g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
    #g1=[['', 'x', ''], ['', 'o', ''], ['', '', '']]
    #g1=[['', 'o', ''], ['', 'x', ''], ['', '', '']]
    #g1=[['', '', ''], ['', '', ''], ['', '', '']]
    t = startTimer()
    root = gen_tree(g0)
    stopTimer(t, "gen_tree")
    #print_tree(root)
    t = startTimer()
    print(root.esiti())
    stopTimer(t, "esiti")
    #print(root.strategia_vincente('o'))