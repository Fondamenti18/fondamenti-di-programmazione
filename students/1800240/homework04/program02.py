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

        #Controlli verticali e orizzontali.
        for x in range(0,3):
            
            if self.nome[0][x] == 'o' and self.nome[1][x] == 'o' and self.nome[2][x] == 'o':
                return 'o'
        
            if self.nome[0][x] == 'x' and self.nome[1][x] == 'x' and self.nome[2][x] == 'x':
                return 'x'
            
            if self.nome[x][0] == 'o' and self.nome[x][1] == 'o' and self.nome[x][2] == 'o':
                return 'o'
        
            if self.nome[x][0] == 'x' and self.nome[x][1] == 'x' and self.nome[x][2] == 'x':
                return 'x'
                
        #Contolli diagonali
        if self.nome[0][0] == 'o' and self.nome[1][1] == 'o' and self.nome[2][2] == 'o':
            return 'o'
        if self.nome[0][0] == 'x' and self.nome[1][1] == 'x' and self.nome[2][2] == 'x':
            return  'x'  
            
        if self.nome[2][0] == 'o' and self.nome[1][1] == 'o' and self.nome[0][2] == 'o':
            return 'o'
        if self.nome[2][0] == 'x' and self.nome[1][1] == 'x' and self.nome[0][2] == 'x':
            return  'x' 
            
        #Controllo se la partita e' finita.
        for y in range(0, 3):
            for x in range(0, 3):
                if self.nome[y][x] == '':
                    return '?'
                
        #Altrimenti e' patta.
        return '-'
    
    def mossa(self):
        
        #Calcola quale giocatore deve giocare e ne resitutisce il simbolo. 
        count = 0
    
        for y in range(0, 3):
            for x in range(0, 3): 
                if self.nome[y][x] == '':
                    count += 1
        if count % 2 == 0:
            return 'x'
        else:
            return 'o'
    
    def conta_tipo(self, tipo):
        
        #Conta quante configurazioni di un determinato tipo sono presenti
        #nell' albero che ha come radice il nodo.
        if self.lista_figli == []:
           if self.tipo() == tipo:
              return 1
        count = 0  
        for figlio in self.lista_figli:
            count += figlio.conta_tipo(tipo)
            
        return count
    
    def esiti(self):
        
        return (self.conta_tipo('-'), self.conta_tipo('o'), self.conta_tipo('x'))
    
    def vittorie_livello(self, giocatore, h):
        
        if h == 0:
            if self.tipo() == giocatore:
                return 1   
        count = 0   
        if h != 0:
            for figlio in self.lista_figli:
                count += figlio.vittorie_livello(giocatore, h-1)
                
        return count
                    
    def strategia_vincente(self, giocatore):
        ''''''
def gen_tree(griglia):
    
    radice = NodoTris(griglia)
    
    if radice.tipo() == '?':    
        for y in range(0, 3):
            for x in range(0, 3):
                if radice.nome[y][x] == '':
                    griglia_new = deepcopy(griglia)
                    griglia_new[y][x] = radice.mossa()
                    radice.lista_figli += [gen_tree(griglia_new)]
    return radice