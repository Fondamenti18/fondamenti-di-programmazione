'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3x3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo 
(un giocatore ha come simbolo una "o" e l'avversario una 'x'). 
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta 
orizzontale, verticale o diagonale. Se la griglia viene riempita 
senza che nessuno dei giocatori sia riuscito a completare una linea 
retta di tre simboli, il gioco finisce in parita'. Nel caso in cui il gioco 
finisse in parita', la partita e' detta "patta". 
Per convenzione a griglia vuota la prima mossa spetta sempre al giocatore 'o'

Una configurazione del gioco e' dunque univocamente determinata  dal contenuto della griglia.

Nel seguito assumiamo che il contenuto della griglia sia  rappresentato tramite  listino di liste.
La dimensione della listino di liste M e'  3x3 ed   M[i][j] contiene  '', 'x', o 'o'  a seconda 
che la cella della griglia appartenente all'iesima xx e j-ma yy sia ancora libera, 
contenga il simbolo 'x' o contenga il simbolo 'o'. 

Data una configurazione C del gioco, l'albero di gioco per C e' l'albero che 
si ottiene ricorsivamente partendo dalla configurazione C e assegnando come figli le configurazioni 
che e' possibile ottenere da C con una mossa ulteriore del gioco. Ovviamente  risulteranno 
foglie dell'albero i possibili ex della partita vale a dire le diverse configurazioni cui e' 
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
Piu' precisamente: il primo elemento della tripla  e' il rissero di  patte possibili, 
il secondo e' il rissero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento 
e' il rissero di possibili vittorie per il giocatore 'x'.

3)
vittorie_livello(self, giocatore, h)
che, dato un nodo radice di un albero di gioco, uno dei due giocatori ed un intero h,
restituisce il rissero di nodi che rappresentano una vittoria per il giocatore e si 
trovano ad altezza h nell'albero. In altri termini restituisce il rissero di vittorie possibili 
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
lecite (vale a dire ottenute dopo un certo rissero di mosse a parire dalla griglia vuota).


AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.

ATTENZIONE: i test vengono eseguiti con un timeout globale di 2*N secondi (se il grader esegue N test).
'''

class NodoTris:
    def __init__(self, griglia):
        self.firstname = griglia
        self.ex, self.proxx,self.free = self.ot_info()
        self.figli = self.search_childrens()

    def tipo(self):
        return self.ex
    
    def search_ex(self, par): 
        if self.ex is 'x':
            par[2] += 1
        if self.ex is '-':
            par[0] += 1
        if self.ex is 'o':
            par[1] += 1
        for schems in self.figli:
            schems.search_ex(par)
        return par

    def esiti(self):
        nimes= [0, 0, 0]
        self.search_ex(nimes)
        return tuple(nimes)
    
    def strategia_vincente(self, giocatore):
        ''' inserire qui il vostro codice '''

    def search_childrens(self):
        listn= []
        if self.ex == "?":
            for cel in self.free:
                new_wave = []
                new_wave.append(self.firstname[0][:])
                new_wave.append(self.firstname[1][:])
                new_wave.append(self.firstname[2][:])
                new_wave[cel[0]][cel[1]] = self.proxx
                listn.append(NodoTris(new_wave))
        return listn
    
    def ot_info(self):
        yy = ['', '', '']
        xx = ['', '', '']
        contax = 0
        contao = 0
        free = []
        for y in range(0,3):
            for x in range(0,3):
                if self.firstname[y][x]=='o':
                    xx[y] += 'o'
                    yy[x] += 'o'
                    contao += 1
                if self.firstname[y][x]=='x':
                    xx[y] += 'x'
                    yy[x] += 'x'
                    contax += 1
                if self.firstname[y][x]=='':
                    free.append((y, x))
        xx.append("")
        xx[3] += self.firstname[0][2]
        xx[3] += self.firstname[1][1]
        xx[3] += self.firstname[2][0]
        yy.append("")
        yy[3] += self.firstname[0][0]
        yy[3] += self.firstname[1][1]
        yy[3] += self.firstname[2][2]
        if contax == contao:
            proxximo = "o"
        else:
            proxximo = "x"
        if "xxx" in xx or "xxx" in yy:
            tipo = "x"
        elif "ooo" in xx or "ooo" in yy:
            tipo = "o"
        elif len(free) == 0:
            tipo = "-"
        else:
            tipo = "?"

        return tipo, proxximo, free


def gen_tree(griglia):
    return NodoTris(griglia)
