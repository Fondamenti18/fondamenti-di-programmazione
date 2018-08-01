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

class NodoTris:
    def __init__(self, griglia):
        self.nome = deepcopy(griglia)
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        '''inserire qui il vostro codice'''
        v_o = vincita_o(self.nome)
        v_v = vincita_v(self.nome)
        v_obl = vincita_obl(self.nome)
        if v_o: return v_o
        elif v_v: return v_v
        elif v_obl: return v_obl
        else:
            for y in self.nome:
                if '' in y: return '?'
            return '-'
    
    def esiti(self):
        '''inserire qui il vostro codice'''
        lista = conta(self)
        return (lista.count(0), lista.count(1), lista.count(2))
    
    def vittorie_livello(self, giocatore, h, cont = 0):
        '''inserire qui il vostro codice'''
        totale = 0
        if cont == h and vincita(self.nome):
            v_o = vincita_o(self.nome)
            v_v = vincita_v(self.nome)
            v_obl = vincita_obl(self.nome)
            if v_o == giocatore: return 1
            elif v_v == giocatore: return 1
            elif v_obl == giocatore: return 1
        if cont < h:
            for x in self.lista_figli:
                totale += x.vittorie_livello(giocatore, h, cont + 1)
        return totale
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        if self.lista_figli == []:
            v_o = vincita_o(self.nome)
            v_v = vincita_v(self.nome)
            v_obl = vincita_obl(self.nome)
            if giocatore in [v_o, v_v, v_obl]:
                return True
            elif v_o != False or v_v != False or v_obl != False: return False
            return 1
        for x in self.lista_figli:
            if x.lista_figli == []:
                ris = x.strategia_vincente(giocatore)
                if ris in [True,False]:
                    break
        try:
            return ris
        except:
            for x in self.lista_figli:
                if x.lista_figli != []:
                    ris = x.strategia_vincente(giocatore)
                    if ris in [True,False]:
                        break
            return ris

def turno(griglia):
    nx = 0
    no = 0
    for y in range(3):
        for x in range(3):
            if griglia[y][x] == 'o': no+=1
            elif griglia[y][x] == 'x': nx+=1
    if nx < no: return 'o'
    else: return 'x'

def conta(nodo):
    if nodo.lista_figli == []:
        v_o = vincita_o(nodo.nome)
        v_v = vincita_v(nodo.nome)
        v_obl = vincita_obl(nodo.nome)
        if v_o == v_v == v_obl: return [0]
        if 'o' in [v_o,v_v,v_obl]: return [1]
        if 'x' in [v_o,v_v,v_obl]: return [2]
    totale = []
    for x in nodo.lista_figli:
        totale += conta(x)
    return totale

def gioca(griglia):
    nx = 0
    no = 0
    for y in range(3):
        for x in range(3):
            if griglia[y][x] == 'o': no+=1
            elif griglia[y][x] == 'x': nx+=1
    if nx < no: return 'x'
    else: return 'o'

def vincita_o(griglia):
    for y in range(3):
        if griglia[y][0] == griglia[y][1] == griglia[y][2]:
            if griglia[y][0] != '': 
                return griglia[y][0]
    return False

def vincita_v(griglia):
    for x in range(3):
        if griglia[0][x] == griglia[1][x] == griglia[2][x]:
            if griglia[0][x] != '': 
                return griglia[0][x]
    return False

def vincita_obl(griglia):
    if griglia[1][1] != '': 
        if griglia[0][0] == griglia[1][1] == griglia[2][2]: return griglia[1][1]
        if griglia[0][2] == griglia[1][1] == griglia[2][0]: return griglia[1][1]
    return False
    

def vincita(griglia):
    if vincita_o(griglia) or vincita_v(griglia) or vincita_obl(griglia):
        return True
    return False

def gen_tree(griglia, diz = dict()):
    '''inserire qui il vostro codice'''
    key = ''
    for y in range(3):
        for x in range(3):
            if griglia[y][x] == '':
                key += ' '
            else:
                key += griglia[y][x]
    if key not in diz:
        nodo = NodoTris(griglia)
        if vincita(griglia): 
            return nodo
        turno = gioca(griglia)
        
        for y in range(3):
            for x in range(3):
                if griglia[y][x] == '':
                    nuova_griglia = deepcopy(griglia)
                    nuova_griglia[y][x] = turno
                    nodo.lista_figli += [gen_tree(nuova_griglia, diz)]
        diz[key] = nodo
    else:
        nodo = diz[key]
    return nodo

'''
g0=[['', '', ''], ['', '', ''], ['', '', '']]
a = gen_tree(g0)
ris = a.esiti()
print(ris)

g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]

g5=[['', 'x', ''], ['', 'o', ''], ['', '', '']]
g6=[['', 'o', ''], ['', 'x', ''], ['', '', '']]
g7=[['', 'x', 'o'], ['', '', ''], ['', '', '']]
g8=[['', 'o', 'x'], ['', '', ''], ['', '', '']]

listaa=[g1, g2, g3, g4]
listac=[gen_tree(x) for x in listaa]
#lista=[y.tipo() for y in listac]
#lista=[y.esiti() for y in listac]
a = gen_tree(g1)
a.esiti()
a = gen_tree(g2)
a.esiti()
a = gen_tree(g3)
a.esiti()
a = gen_tree(g4)
a.esiti()
a = gen_tree(g5)
a.esiti()
a = gen_tree(g6)
a.esiti()
a = gen_tree(g7)
a.esiti()
a = gen_tree(g8)
a.esiti()

#print(lista)
'''