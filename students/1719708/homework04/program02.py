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
from time import time

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.o, self.x = self.conta_simboli()
        self.w_x = 0
        self.w_o = 0
        self.patte = 0
        self.punteggio = 0
        
    def conta_simboli(self):
        x_count = 0
        o_count = 0
        for y in range(len(self.nome)):
            for x in range(len(self.nome[y])):
                if self.nome[y][x] == 'x':
                    x_count += 1
                elif self.nome[y][x] == 'o':
                    o_count += 1
        return o_count, x_count
    
    def contenuto_casella(self, casella):
        if casella == 'x':
            return 'x'
        if casella == 'o':
            return 'o'
    
    def tipo(self):
        if self.nome[0][0] != '' and self.nome[0][0] == self.nome[1][1] == self.nome[2][2]:
            return self.contenuto_casella(self.nome[0][0])
        if self.nome[0][2] != '' and self.nome[0][2] == self.nome[1][1] == self.nome[2][0]:
            return self.contenuto_casella(self.nome[0][2])
        return controllo(self)
            
    def esiti(self):
        if self.tipo() == 'o':
            self.w_o += 1
        elif self.tipo() == 'x':
            self.w_x += 1
        elif self.tipo() == '-':
            self.patte += 1
        for son in self.lista_figli:
            tEsiti = son.esiti()
            self.patte += tEsiti[0]
            self.w_o += tEsiti[1]
            self.w_x += tEsiti[2]
        return self.patte, self.w_o, self.w_x
    
    def vittorie_livello(self, giocatore, h):
        w_lv = 0
        if h >= 1:
            for son in self.lista_figli:
                    w_lv += son.vittorie_livello(giocatore, h - 1)
                    if h == 1:
                        if son.tipo() == giocatore:
                            w_lv += 1
        return w_lv
    
    def strategia_vincente(self,giocatore):
        scorri_albero(self, giocatore)
        punteggio_radice(self, giocatore)
                
        if turno(self, giocatore):
            if self.punteggio == 0:
                return False
            else:
                return True
        else:
            for foglia in self.lista_figli:
                if foglia.punteggio == 0:
                    return False
            if self.punteggio == 0:
                return False
            return True
		
def scorri_albero(radice, giocatore):
    for foglia in radice.lista_figli:
        if foglia.tipo() == giocatore:
            foglia.punteggio = 1
        scorri_albero(foglia, giocatore)
		
def punteggio_radice(radice, giocatore):
    for foglia in radice.lista_figli:
        punteggio_radice(foglia, giocatore)
    radice.punteggio = max_punteggio(radice, giocatore)

def max_punteggio(radice, giocatore):
    if radice.lista_figli == []:
        if radice.punteggio == 1:
            return 1
        else:
            return 0
    for foglia in radice.lista_figli:
        if turno(radice, giocatore):
                if foglia.punteggio == 1:
                    return 1
        elif foglia.punteggio == 0:
            return 0
    if turno(radice, giocatore):
        return 0
    else:
        return 1
        
def turno(radice, giocatore):
    if giocatore == 'o':
        if radice.x < radice.o:
            return False
        else:
            return True
    if giocatore == 'x':
        if radice.o >= radice.x:
            return False
        else:
            return True
        
def controllo(radice):
    for r in range(3):
        if radice.nome[r][0] != '' and radice.nome[r][0] == radice.nome[r][1] == radice.nome[r][2]:
            return radice.contenuto_casella(radice.nome[r][0])
    for c in range(3):
        if radice.nome[0][c] != '' and radice.nome[0][c]== radice.nome[1][c] == radice.nome[2][c]:
            return radice.contenuto_casella(radice.nome[0][c])
    if radice.x + radice.o < 9:
        return '?'
    else:
        return '-'
		
def gen_tree(griglia):
    campo = NodoTris(griglia)
    for y in range(len(campo.nome)):
        for x in range(len(campo.nome[y])):
            if campo.nome[y][x] == '':
                g = copia(griglia)
                if campo.x >= campo.o :
                    g[y][x] = 'o'
                else:
                    g[y][x] = 'x'
                if campo.tipo() != 'x' and campo.tipo() != 'o':
                    campo.lista_figli += [gen_tree(g)]
    return campo

def copia(lista):
    copia_l = []
    for l in lista:
        copia_l += [copy(l)]
    return copia_l