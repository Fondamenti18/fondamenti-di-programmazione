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

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        L = self.nome
        winX = 'xxx'
        winO = 'ooo'
        
        w1 = L[0][0]+L[0][1]+L[0][2]
        w2 = L[1][0]+L[1][1]+L[1][2]
        w3 = L[2][0]+L[2][1]+L[2][2]
        w4 = L[0][0]+L[1][0]+L[2][0]
        w5 = L[0][1]+L[1][1]+L[2][1]
        w6 = L[0][2]+L[1][2]+L[2][2]
        w7 = L[0][0]+L[1][1]+L[2][2]
        w8 = L[0][2]+L[1][1]+L[2][0]
        check = w1+w2+w3+w4+w5+w6+w7+w8
        lista_check = [w1,w2,w3,w4,w5,w6,w7,w8]
        for x in lista_check:
            if x == winX:
                return 'x'
            elif x == winO:
                return 'o'
        if len(check) < 24:
            return '?'
        else:
            return '-'
        
    def esiti(self):
        F = self.lista_figli
        x = 0
        o = 0
        patta = 0
        if self.tipo() == 'x':
            x += 1
        elif self.tipo() == 'o':
            o += 1
        elif self.tipo() == '-':
            patta += 1        
        else:
            for k in F:
                esiti = k.esiti()
                x += esiti[2]
                o += esiti[1]
                patta += esiti[0]
        return ( patta, o, x)
        
    
    def vittorie_livello(self, giocatore, h, livello=0):
        F = self.lista_figli
        vittorie = 0
        if livello == h:
            if self.tipo() == giocatore:
                vittorie += 1
        else:
            for x in F:
                vittorie += x.vittorie_livello(giocatore, h, livello+1)
        return vittorie

    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        
def gen_tree(griglia):
    nodo = NodoTris(griglia)
    countX = griglia[0].count('x')+griglia[1].count('x')+griglia[2].count('x')
    countO = griglia[0].count('o')+griglia[1].count('o')+griglia[2].count('o')
    n = 0
    if nodo.tipo() == '?':
        while n < 3:
            k = 0
            while k < 3:
                if griglia[n][k] == '':
                    new_gr = gen_figlio(griglia)
                    if countX == countO:
                        new_gr[n][k] = 'o'
                        nodo.lista_figli += [gen_tree(new_gr)]
                    else:
                        new_gr[n][k] = 'x'
                        nodo.lista_figli += [gen_tree(new_gr)]
                k += 1
            n += 1
    return nodo


def gen_figlio(griglia):
    figlio = []
    for x in range(len(griglia)):
        figlio += [griglia[x][:]]
    return figlio
        



    
#g0=[['', '', ''], ['', '', ''], ['', '', '']]
#g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
#g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
#g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
#g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]
#
#g5=[['', 'x', ''], ['', 'o', ''], ['', '', '']]
#g6=[['', 'o', ''], ['', 'x', ''], ['', '', '']]
#g7=[['', 'x', 'o'], ['', '', ''], ['', '', '']]
#g8=[['', 'o', 'x'], ['', '', ''], ['', '', '']]

#print ((gen_tree(g1)))