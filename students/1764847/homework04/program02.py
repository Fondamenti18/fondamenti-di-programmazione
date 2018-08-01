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
    
    def __str__(self):
        return str(self.nome)
    
    def tipo(self):        
        # Controlla la configurazione di vittoria per le diagonali
        if self.nome[1][1] != '':
            if (self.nome[1][1] == self.nome[0][0] and self.nome[1][1] == self.nome[2][2]) or (self.nome[1][1] == self.nome[0][2] and self.nome[1][1] == self.nome[2][0]):
                return self.nome[1][1]
        
        # Controlla la configurazione di vittoria per le righe e le colonne
        for i in range(3):
            if self.nome[i][0] != '' and self.nome[i][1] == self.nome[i][0] and self.nome[i][2] == self.nome[i][0]:
                return self.nome[i][0]
        
        for j in range(3):
            if self.nome[0][j] != '' and self.nome[0][j] == self.nome[1][j] and self.nome[0][j] == self.nome[2][j]:
                return self.nome[0][j]
        
        # Controlla se la partita e' patta o non e' ancora terminata
        for i in range(3):
            for j in range(3):
                if self.nome[i][j] == '':
                    return '?' # Non terminato
        
        # Patta
        return '-'
    
    def esiti(self):
        patte = 0
        o_win = 0
        x_win = 0
        
        esito = self.tipo()
        if esito == '-':
            patte += 1
        elif esito == 'o':
            o_win += 1
        elif esito == 'x':
            x_win += 1
        
        for figlio in self.lista_figli:
            (p, o, x) = figlio.esiti()
            patte += p
            o_win += o
            x_win += x
        
        return (patte, o_win, x_win)
    
    def vittorie_livello(self, giocatore, h):
        if h == 0:
            if self.tipo() == giocatore:
                return 1
            return 0
        count = 0
        for figlio in self.lista_figli:
            count += figlio.vittorie_livello(giocatore, h - 1)
        return count
    
    def strategia_vincente(self,giocatore):        
        self_tipo = self.tipo()
        if self_tipo == giocatore:
            return True # partita terminata e il vincitore e' giocatore
        elif self_tipo != '?':
            return False # partita terminata e il vincitore NON e' giocatore
        if next_player(self.nome) == giocatore:
            # giocatore ha la prossima mossa, controllo se c'e' una mossa che fa vincere giocatore
            for figlio in self.lista_figli:
                if figlio.strategia_vincente(giocatore) == True:
                    return True
            return False
        else:
            # Controllo se c'e' una strategia vincente per ogni possibile mossa dell'avversario
            for figlio in self.lista_figli:
                if figlio.strategia_vincente(giocatore) == False:
                    return False
            return True

def next_player(griglia):
    count = {'x': 0, 'o': 0, '': 0}
    for i in range(3):
        for j in range(3):
            count[griglia[i][j]] += 1
    if count['x'] != count['o']:
        return 'x'
    return 'o'

def gen_tree(griglia):
    radice = NodoTris(griglia)
    if radice.tipo() == '?':
        player = next_player(griglia)
        for i in range(3):
            for j in range(3):
                if griglia[i][j] == '':
                    nuova_griglia = [row[:] for row in griglia]
                    nuova_griglia[i][j] = player
                    figlio = gen_tree(nuova_griglia)
                    radice.lista_figli.append(figlio)
    return radice
    
