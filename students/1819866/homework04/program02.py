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
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        lst = self.nome
        for i in range(3):
            if lst[i][0] == 'x' and lst[i][1] == 'x' and lst[i][2] == 'x': return 'x'
            if lst[i][0] == 'o' and lst[i][1] == 'o' and lst[i][2] == 'o': return 'o'
        for i in range(3):
            if lst[0][i] == 'x' and lst[1][i] == 'x' and lst[2][i] == 'x': return 'x'
            if lst[0][i] == 'o' and lst[1][i] == 'o' and lst[2][i] == 'o': return 'o'     
        if lst[0][0] == 'x' and lst[1][1] == 'x' and lst[2][2] == 'x': return 'x'
        if lst[0][0] == 'o' and lst[1][1] == 'o' and lst[2][2] == 'o': return 'o'
        if lst[0][2] == 'x' and lst[1][1] == 'x' and lst[2][0] == 'x': return 'x'
        if lst[0][2] == 'o' and lst[1][1] == 'o' and lst[2][0] == 'o': return 'o'
        for j in range(3):
            for i in range(3):
                if lst[j][i] == '': return '?'
        return '-'
        
        
    def esiti(self):
        if self.tipo() == '-': return (1,0,0)
        if self.tipo() == 'o': return (0,1,0)
        if self.tipo() == 'x': return (0,0,1)
        if self.tipo() == '?': 
            a, b, c = 0,0,0
            for griglia in self.lista_figli:
                x, y, z = griglia.esiti()
                a,b,c = a+x, b+y, c+z
        return (a,b,c)
                    
    
    def vittorie_livello(self, giocatore, h):
        result = 0
        if h == 0: 
            if self.tipo() == giocatore:
                result += 1
                return result
        else:
            for griglia in self.lista_figli:
                result += griglia.vittorie_livello(giocatore, h-1)
        return result
    
    
    def strategia_vincente(self,giocatore):
        if giocatore == 'x': other = 'o'
        else: other = 'x'
        if self.tipo() == giocatore: return True
        if self.tipo() == other: return False
        if self.tipo() == '-': return False
        if self.tipo() == '?':
            if turno(self.nome) == giocatore:
                result = False
                for child in self.lista_figli:
                    result = result or child.strategia_vincente(giocatore)
                return result
            if turno(self.nome) == other:
                result = True
                for child in self.lista_figli:
                    result = result and child.strategia_vincente(giocatore)
                return result

                
def gen_tree(griglia):
    nodo = NodoTris(griglia) 
    if nodo.tipo() == '?': 
        lstFree = free(griglia)
        sym = turno(griglia)
        for p in lstFree:
            griglia2 = deepcopy(griglia)
            j, i = p
            griglia2[j][i] = sym
            nodo.lista_figli.append(gen_tree(griglia2))
    return nodo

def free(griglia):
    lst = []
    for j in range(3):
        for i in range(3):
            if griglia[j][i] == '': lst += [(j, i)]
    return lst
  
def turno(lst):
    counto, countx = 0, 0
    for row in lst:
        counto += row.count('o')
        countx += row.count('x')
    if counto == countx: return 'o'
    else: return 'x'
