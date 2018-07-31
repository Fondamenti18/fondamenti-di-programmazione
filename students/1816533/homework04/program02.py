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
        
        for i in range(len(self.nome)):
            if(self.nome[i][0] == self.nome[i][1] and self.nome[i][1] == self.nome[i][2] and self.nome[i][0] != '' and self.nome[i][1] != '' and self.nome[i][2] != ''):
                return self.nome[i][0]

        for i in range(len(self.nome)):
            if(self.nome[0][i] == self.nome[1][i] and self.nome[1][i] == self.nome[2][i] and self.nome[0][i] != '' and self.nome[1][i] != '' and self.nome[2][i] != ''):
                return self.nome[0][i]
        
        if self.nome[0][0] == self.nome[1][1] and self.nome[1][1] == self.nome[2][2] and self.nome[0][0] != '' and self.nome[1][1] != '' and self.nome[2][2] != '':
            return self.nome[1][1]

        if self.nome[0][2] == self.nome[1][1] and self.nome[1][1] == self.nome[2][0] and self.nome[0][2] != '' and self.nome[1][1] != '' and self.nome[2][0] != '':
            return self.nome[1][1]

        for i in range(len(self.nome)):
            for j in range(len(self.nome[0])):
                if self.nome[i][j] == '':
                    return '?'

        return '-'
        
    def esiti(self):
        
        return getEsito(self, [0, 0, 0])
    
    def vittorie_livello(self, giocatore, h):
        
        return getVittorie(self, giocatore, h, 0, [0])
    
    def strategia_vincente(self,giocatore):

        if giocatore == 'x':
            if self.esiti()[1] == 0:
                return True
            else:
                return False
        else:
            if self.esiti()[2] == 0:
                return True
            else:
                return False

def getVittorie(nodo, giocatore, h, curLevel, vittorie):

    if nodo.tipo() == giocatore and h == curLevel:
        vittorie[0] += 1

    for i in nodo.lista_figli:
        getVittorie(i, giocatore, h, curLevel + 1, vittorie)

    return vittorie[0]

def getEsito(nodo, lista):

    if nodo.tipo() == '-':
        lista[0] += 1
    elif nodo.tipo() == 'o':
        lista[1] += 1
    elif nodo.tipo() == 'x':
        lista[2] += 1

    for i in nodo.lista_figli:
        getEsito(i, lista)

    return (lista[0], lista[1], lista[2])

def gen_tree(griglia):

    empty_spaces = []
    x_count = 0
    o_count = 0
    nextMove = None

    nodo = NodoTris(griglia)

    if(nodo.tipo() != '?'):
        return nodo
    else:
        for i in range(len(griglia)):
            for j in range(len(griglia[0])):
                if griglia[i][j] == '':
                    empty_spaces.append((i, j))
                elif griglia[i][j] == 'x':
                    x_count += 1
                else:
                    o_count += 1
        if o_count <= x_count:
            nextMove = 'o'
        else:
            nextMove = 'x'
        for i in empty_spaces:
            griglia_figlio = [[0 for x in range(3)] for x in range(3)]
            for j in range(len(griglia)):
                for k in range(len(griglia[0])):
                    if griglia[j][k] == 'x':
                        griglia_figlio[j][k] = 'x'
                    elif griglia[j][k] == 'o':
                        griglia_figlio[j][k] = 'o'
                    else:
                        griglia_figlio[j][k] = ''
            griglia_figlio[i[0]][i[1]] = nextMove
            figlio = NodoTris(griglia_figlio)
            nodo.lista_figli.append(gen_tree(figlio.nome))

    return nodo
        
        
'''g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
game1 = gen_tree(g1)
print(game1.nome)
print(game1.strategia_vincente('x'))'''