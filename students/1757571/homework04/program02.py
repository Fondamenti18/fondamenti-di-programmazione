'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3per3 caselle.
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
        self.foglie = []

    def checkRiga(self, griglia, i):
        #Controlla la riga i della griglia
        return griglia[i][0]+griglia[i][1]+griglia[i][2]

    def checkColonna(self, griglia, j):
        #Controlla la colonna j della griglia
        return griglia[0][j]+griglia[1][j]+griglia[2][j]

    def checkDiagonale(self, griglia, i, j):
        #Controlla la diagonale della griglia dalla cella (i,j)
        if (i,j)==(0,0) or (i,j)==(2,2):
            return griglia[0][0]+griglia[1][1]+griglia[2][2]

        elif (i,j)==(2,0) or (i,j)==(0,2):
            return griglia[0][2]+griglia[1][1]+griglia[2][0]

    def upTo(self):
        #Contando le occurences nella griglia, ritorna il giocatore a cui spetta
        #la prossima mossa
        count=0
        for lista in self.nome:
            for elemento in lista:
                if elemento=='o':
                    count+=1
                elif elemento=='x':
                    count-=1
        if count==0:
            return 'o'
        elif count==+1:
            return 'x'
        elif count==-1:
            return 'o'

    def getResults(self, lst, index, resLst):
        #Calcola una tripla contente il numero di risultati patti, vinti dal
        #giocatore O o vinti dal giocatore X
        if index < len(lst):
            result = lst[index][0].tipo()
            if result == 'x':
                resLst[2] += 1
            elif result == '-':
                resLst[0] += 1
            else:
                resLst[1] += 1
            self.getResults(lst, index + 1, resLst)

    def getLevelResults(self, lst, index, h, resLst, giocatore):
        #Calcola il numero di vittorie ottenute dal giocatore in input dopo un 
        #certo numero di mosse h
        if index < len(lst):
            if lst[index][1] == h and lst[index][0].tipo() == giocatore:
                resLst[0] += 1
            self.getLevelResults(lst, index + 1, h, resLst, giocatore)

    def tipo(self):
        '''inserire qui il vostro codice'''
        lenGriglia=range(3)
        overFlag=True
        myNode=self
        for index in lenGriglia:
            if index!=1:
                resRiga=myNode.checkRiga(myNode.nome, index)
                resColonna=myNode.checkColonna(myNode.nome, index)
                resDiagonale=myNode.checkDiagonale(myNode.nome, index, index)
                if resRiga=='xxx' or resColonna=='xxx' or resDiagonale=='xxx':    #Caso di vincita X
                    return 'x'

                elif resRiga=='ooo' or resColonna=='ooo' or resDiagonale=='ooo':    #Caso di vincita O
                    return 'o'
                else:
                    if len(resRiga)<3 or len(resColonna)<3 or len(resDiagonale)<3:
                        overFlag=False
            else:
                resRiga=myNode.checkRiga(myNode.nome, index)
                resColonna=myNode.checkColonna(myNode.nome, index)
                if resRiga=='xxx' or resColonna=='xxx':    #Caso di vincita X
                    return 'x'

                elif resRiga=='ooo' or resColonna=='ooo':    #Caso di vincita O
                    return 'o'
                else:
                    if len(resRiga)<3 or len(resColonna)<3:
                        overFlag=False

        if overFlag:        #Caso di parita'
            return '-'
        else:
            return '?'      #Caso di gioco non terminato


    def esiti(self):
        '''inserire qui il vostro codice'''
        res = [0, 0, 0]
        self.getResults(self.foglie, 0, res)
        return tuple(res)

    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        el = [0]
        self.getLevelResults(self.foglie, 0, h, el, giocatore)
        return el[0]


    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        createTree(self, self.foglie, 0)
        h = 0
        diz = {'x' : 'o', 'o' : 'x'}
        while True:
            user = self.vittorie_livello(giocatore, h)
            avv = self.vittorie_livello(diz[giocatore], h)
            if user > 0:
                return True
            if avv > 0:
                return False
            h += 1

def createTree(nodo, lst, liv):
    #Crea l'albero ottenuto dalla radice in input, tenendo traccia del livello
    #di ogni generazione
    if nodo.tipo() == '?':
        turno = nodo.upTo()
        liv += 1
        for riga in range(len(nodo.nome)):
            for colonna in range(len(nodo.nome[0])):
                if nodo.nome[riga][colonna] == '':
                    newGriglia = [i[:] for i in nodo.nome]
                    newGriglia[riga][colonna] = turno
                    figlio = NodoTris(newGriglia)
                    nodo.lista_figli.append(figlio)
                    createTree(figlio, lst, liv)
    else:
        lst.append((nodo, liv))

def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    myRoot = NodoTris(griglia)
    createTree(myRoot, myRoot.foglie, 0)
    return myRoot
