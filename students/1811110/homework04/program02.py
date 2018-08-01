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
che la cella della griglia appartenente all'iesima rig e j-ma col sia ancora libera, 
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

class NodoTris:#
    def __init__(self, griglia):#
        self.nome = griglia
        self.esito, self.prossimo, self.libere = self.ynfo()
        self.figli = self.find_chi()

    def tipo(self):#
        return self.esito

    def t_trovaesiti(self,inn):
        for sche in self.figli:
            sche.find_e(inn)
        return inn
    def find_e(self, inn):
        a='-'
        b='o'
        c='x'
        if self.esito is a:
            inn[0] += 1
        if self.esito is b:
            inn[1] += 1
        if self.esito is c:
            inn[2] += 1
        inn=self.t_trovaesiti(inn)
        return (inn)
    
    def esiti(self): #
        namb = [0, 0, 0]
        self.find_e(namb)
        return tuple(namb)








    def t_v(self,scont,sukno):
        if self.esito is sukno:
            scont[0] += 1
        return scont[0]
    def find_win(self, sukno, level, train, scont): #
        if level != train:
            for node in self.figli:
                level = level + 1
                node.find_win(sukno, level, train, scont)
        else:
            scont[0]=self.t_v(scont,sukno)
        return scont[0]

    def vittorie_livello(self, gioca, ah):#
        actual = 0
        ls = [0]
        fine = self.find_win(gioca, actual, ah, ls)
        return fine







    def p_u_g(self,gioca):
        for node in self.figli:
                if node.find_catan(gioca) == True:
                    return True
        return False
    
    def find_catan(self, gioca):
        a='?'
        if self.esito != a:
            scont = self.esito != gioca
            return scont
        if self.prossimo == gioca:
            che=self.p_u_g(gioca)
            return che
        else:
            for node in self.figli:
                if node.find_catan(gioca) == False:
                    return False
            return True

    def strategia_vincente(self, gioca):
        return self.find_catan(gioca)


    
    def  t_figli(self,nruter):
        for xxx in self.libere:    
            sche_nuovo = []
            sche_nuovo.append(self.nome[0][:])
            sche_nuovo.append(self.nome[1][:])
            sche_nuovo.append(self.nome[2][:])
            sche_nuovo[xxx[0]][xxx[1]] = self.prossimo
            nruter.append(NodoTris(sche_nuovo))
        return nruter
    
    def find_chi(self):
        nruter = []
        a="?"
        if self.esito == a:
            nruter=self.t_figli(nruter)
        return nruter


    def ass(self,col,rig):
        col.append("")
        rig.append("")
        col[3] += self.nome[0][0]
        col[3] += self.nome[1][1]
        col[3] += self.nome[2][2]
        rig[3] += self.nome[0][2]
        rig[3] += self.nome[1][1]
        rig[3] += self.nome[2][0]

        return rig,col

    
    def controllo(self,xco,occo,fri,rig,col):
        if xco == occo:
            nxt = "o"
        else:
            nxt = "x"

        if "xxx" in rig or "xxx" in col:
            rop = "x"
        elif "ooo" in rig or "ooo" in col:
            rop = "o"
        elif len(fri) == 0:
            rop = "-"
        else:
            rop = "?"
        return rop,nxt
        

    def ynfo(self):
        col = ['', '', '']
        rig = ['', '', '']
        xco = 0
        occo = 0
        fri = []
        a='x'
        b='o'
        c=''
        for y in range(3):
            for x in range(3):
                if self.nome[y][x] is a:
                    rig[y] += a
                    col[x] += a
                    xco += 1
                if self.nome[y][x] is b:
                    rig[y] += b
                    col[x] += b
                    occo += 1
                if self.nome[y][x] is c:
                    fri.append((y, x))

        rig,col=self.ass(col,rig)
        rop,nxt=self.controllo(xco,occo,fri,rig,col)
        

        return rop, nxt, fri


def gen_tree(griglia):
    return NodoTris(griglia)


