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

    def tipo(self):
        griglia = self.nome
        turno, numero_spazi_vuoti = controlla_turno(griglia)
        if turno == 'x':
            if (griglia[0][0] == griglia[0][1] == griglia[0][2] != '') or (griglia[0][0] == griglia[1][0] == griglia[2][0] != '') or (griglia[0][1] == griglia[1][1] == griglia[2][1] != '') or (griglia[0][2] == griglia[1][2] == griglia[2][2] != '') or (griglia[1][0] == griglia[1][1] == griglia[1][2] != '') or (griglia[2][0] == griglia[2][1] == griglia[2][2] != '') or (griglia[0][0] == griglia[1][1] == griglia[2][2] != '') or (griglia[0][2] == griglia[1][1] == griglia[2][0] != ''):
                return 'o'
            elif numero_spazi_vuoti == 0:
                r = '-'
            else:
                r = '?'
        elif turno == 'o':
            if (griglia[0][0] == griglia[0][1] == griglia[0][2] != '') or (griglia[0][0] == griglia[1][0] == griglia[2][0] != '') or (griglia[0][1] == griglia[1][1] == griglia[2][1]  != '') or (griglia[0][2] == griglia[1][2] == griglia[2][2] != '') or (griglia[1][0] == griglia[1][1] == griglia[1][2]  != '') or (griglia[2][0] == griglia[2][1] == griglia[2][2] != '') or (griglia[0][0] == griglia[1][1] == griglia[2][2] != '') or (griglia[0][2] == griglia[1][1] == griglia[2][0] != ''):
                r = 'x'
            elif numero_spazi_vuoti == 0:
                r = '-'
            else:
                r = '?'
        return r

    def esiti(self):
        patte = 0
        x = 0
        o = 0
        l = []
        if self.tipo() == 'x':
            x += 1
        elif self.tipo() == 'o':
            o += 1
        elif self.tipo() == '-':
            patte += 1
        else:
            nodo = gen_tree(self.nome)
            for n in nodo.lista_figli:
                nodo2 = gen_tree(n)
                if nodo2.tipo() == 'x':
                    x += 1
                elif nodo2.tipo() == 'o':
                    o += 1
                elif nodo2.tipo() == '-':
                    patte += 1
                else:
                    l.append(n)
        for g in l:
            patte,o,x = numero_esiti(patte, o, x, g)
        return patte,o,x

    def vittorie_livello(self, giocatore, h):
        r = 0
        if h == 0:
            if self.tipo() == giocatore:
                r  += 1
            return r
        d = dict()
        count = 0
        d = crea_liv(d, count, h, self)
        for g in d[h]:
            if gen_tree(g).tipo() == giocatore:
                r += 1
        return r


    def strategia_vincente(self,giocatore):
        d = dict()
        r = False
        turno, numero_spazi_vuoti = controlla_turno(self.nome)
        d = crea_liv(d,0,numero_spazi_vuoti,self)
        if giocatore == turno:
            for g in d[1]:
                nd = gen_tree(g)
                if nd.tipo() == giocatore:
                    return True
        elif giocatore != turno and numero_spazi_vuoti>1:
            for g in d[1]:
                nd = gen_tree(g)
                if nd.tipo() == turno:
                    return False
            for i in d[2]:
                nd = gen_tree(i)
                if nd.tipo() == giocatore:
                    return True
        return False


def crea_liv(d,count,h,g):
    if count == 0:
        nodo = gen_tree(g.nome)
        d[0] = nodo.nome
    elif count == 1:
        n = gen_tree(d[0])
        d[1] = n.lista_figli
    else:
        for g in d[count-1]:
            nodo = gen_tree(g)
            if count not in d:
                d[count] = nodo.lista_figli
            else:
                d[count] += nodo.lista_figli
    if count == h:
        return d
    else:
        return crea_liv(d,count+1,h,g)

def numero_esiti(patte, o, x, g):
    nodo3 = ''
    nodo = gen_tree(g)
    for n in nodo.lista_figli:
        nodo2 = gen_tree(n)
        if nodo2.tipo() == 'x':
            x += 1
        elif nodo2.tipo() == 'o':
            o += 1
        elif nodo2.tipo() == '-':
            patte += 1
        else:
            nodo3 = gen_tree(n)
    if nodo3 != '' :
        return numero_esiti(patte,o,x,nodo3.nome)
    return patte,o,x




def gen_tree(griglia):
    a = NodoTris(griglia)
    if a.tipo() == '?':
        turno, numero_spazi_vuoti = controlla_turno(griglia)
        a.lista_figli = genera_figli(griglia, [], turno, [])
        for g in a.lista_figli:
            gen_tree(g)
    return a


def genera_figli(griglia, l, turno, l2):
    n = NodoTris(griglia)
    if n.tipo() == '?':
        i = 0
        while i < 3:
            for j in range(len(griglia[i])):
                if griglia[i][j] == '':
                    l2.append((i, j))
            i += 1
            for p in l2:
                app = copy.deepcopy(griglia)
                app[p[0]][p[1]] = turno
                l.append(app)
    return l


def controlla_turno(griglia):
    count = 0
    for turno in griglia:
        for turni in turno:
            if turni != '':
                count += 1
    if count%2 == 0 or count == 0:
        t = 'o'
    else:
        t = 'x'
    return t, 9-count