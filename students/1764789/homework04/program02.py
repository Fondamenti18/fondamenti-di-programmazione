'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3Ã—3 caselle.
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
        # Il metodo esamina in successione le righe, le colonne e le diagonali,  
        # interrompendo l'elaborazione quando ne individua una costituita da 
        # simboli tutti uguali a 'o' oppure a 'x'.
        # Il metodo sfrutta la caratteristica della funzione set(), che se 
        # invocata con in argomento una lista allora ritorna l'insieme degli 
        # elementi distinti della lista.
        # Pertanto la funzione set() invocata con argomento una riga, una colonna 
        # o una diagonale di simboli tutti uguali ritorna un insieme costituito 
        # da un simbolo soltanto.
        completa = True
        for i in range(3):
            simboli_riga = set(self.nome[i])
            if '' in simboli_riga:
                completa = False
            elif len(simboli_riga) == 1:
                return self.nome[i][0]
        for j in range(3):
            simboli_colonna = set([self.nome[0][j],self.nome[1][j],self.nome[2][j]])
            if len(simboli_colonna) == 1 and '' not in simboli_colonna:
                return self.nome[0][j]
        simboli_diagonale_1 = set([self.nome[0][0],self.nome[1][1],self.nome[2][2]])
        if len(simboli_diagonale_1) == 1 and '' not in simboli_diagonale_1:
            return self.nome[0][0]
        simboli_diagonale_2 = set([self.nome[0][2],self.nome[1][1],self.nome[2][0]])
        if len(simboli_diagonale_2) == 1 and '' not in simboli_diagonale_2:
            return self.nome[0][2]
        if completa == True:
            return '-'
        return '?'
    
    def esiti(self):
        patte = 0
        vittorie_o = 0
        vittorie_x = 0
        tipo_nodo = self.tipo()
        if tipo_nodo == '?':
            for figlio in self.lista_figli:
                esito = figlio.esiti()
                patte += esito[0]
                vittorie_o += esito[1]
                vittorie_x += esito[2]
        elif tipo_nodo == '-':
            patte += 1
        elif tipo_nodo == 'o':
            vittorie_o += 1
        elif tipo_nodo == 'x':
            vittorie_x += 1
        return (patte, vittorie_o, vittorie_x)
    
    def vittorie_livello(self, giocatore, h):
        configurazioni_livello_h = self.configurazioni_livello(h)
        if giocatore == 'o':
            return configurazioni_livello_h[0]
        else:
            return configurazioni_livello_h[1]
        
    def strategia_vincente(self, giocatore):
        tipo_configurazione = self.tipo()
        if tipo_configurazione == '?':
            if self.giocatore_di_turno() == giocatore:
                valore = False
                for figlio in self.lista_figli:
                    valore = valore or figlio.strategia_vincente(giocatore)
                return valore
            else:
                valore = True
                for figlio in self.lista_figli:
                    valore = valore and figlio.strategia_vincente(giocatore)
                return valore
        elif tipo_configurazione == giocatore:
            return True
        else:
            return False
        
    # ########################################################################
    # UTILITY
    # ########################################################################
    
    # Questo metodo di utilità determina il simbolo del giocatore che deve 
    # effettuare la prossima mossa a quella rappresentata dal NodoTris corrente.
    # Il metodo è basato sul conteggio dei simboli 'o' e 'x' presenti nella 
    # configurazione del NodoTris (griglia) corrente.
    # Il metodo ritorna il simbolo '-' nel caso di una configurazione finale 
    # del gioco, non essendoci in questo caso alcuna mossa successiva.
    def giocatore_di_turno(self):
        conteggio_o = 0
        conteggio_x = 0
        for i in range(3):
            conteggio_o += self.nome[i].count('o')
            conteggio_x += self.nome[i].count('x')
        if 9 == (conteggio_o + conteggio_x):
            return '-'
        if conteggio_o == conteggio_x:
            return 'o'
        return 'x'
    
    # Questo metodo di utilità costruisce la lista dei NodiTris corrispondenti 
    # alle prossime mosse a partire da quella corrente.
    # Il metodo è richiamato iterativamente sui NodiTris figli in modo da 
    # completare l'albero di gioco che ha come radice il NodoTris corrente.
    # Il metodo ha come parametro il simbolo del giocatore di turno, ovvero 
    # il simbolo del giocatore che deve effettuare la prossima mossa. 
    # Pur se le regole del gioco assegnano univocamente a uno dei due
    # giocatori la prossima mossa in funzione della configurazione corrente, 
    # si sceglie di implementare questo parametro per garantire migliori 
    # performance nella costruzione dell'albero di gioco.
    # Il metodo è in effetti un metodo "interno" della classe e non dovrebbe
    # essere richiamato da altri oggetti che utilizzano la classe NodoTris.
    def aggiungi_figli(self, giocatorediturno):
        if self.tipo() != '?':
            return
        # 
        prossimogiocatore = 'o'
        if giocatorediturno == 'o':
            prossimogiocatore = 'x'
        # Si cercano le caselle vuote della griglia associata 
        # al NodoTris corrente (self) ...
        for i in range(3):
            for j in range(3):
                if self.nome[i][j] == '':
                    # ... e se si individua una casella vuota, allora viene 
                    # creata una copia della griglia corrente ...
                    g = list(map(list,self.nome))
                    # ... e in questa copia si occupa la casella vuota 
                    # trovata con il simbolo del giocatore di turno.
                    g[i][j] = giocatorediturno
                    # La griglia così ottenuta è utilizzata per la creazione 
                    # del NodoTris che corrisponde alla mossa eseguita ...
                    F = NodoTris(g)
                    # ... che quindi viene aggiunto alla lista delle possibili 
                    # mosse successive a quella corrente (lista figli).
                    self.lista_figli += [F]
                    # Si richiama iterativamente il metodo sul NodoTris
                    # appena creato, passando in argomento al metodo il 
                    # giocatore che deve effettuare la prossima mossa.
                    # Questo giocatore è chiaramente lo stesso per tutte le 
                    # prossime mosse (ciò conferma la convenienza della scelta 
                    # di passare in argomento al metodo il giocatore di turno),
                    # in modo da completare infine l'albero di gioco.
                    F.aggiungi_figli(prossimogiocatore)
                    
    def configurazioni_livello(self, h):
        if h == 0:
            tipo_griglia = self.tipo()
            if tipo_griglia == 'o':
                return tuple([1,0,0,0])
            elif tipo_griglia == 'x':
                return tuple([0,1,0,0])
            elif tipo_griglia == '-':
                return tuple([0,0,1,0])
            else:
                return tuple([0,0,0,1])
        else:
            configurazioni_h = [0,0,0,0]
            for figlio in self.lista_figli:
                configurazioni_h_1 = figlio.configurazioni_livello(h - 1)
                for i in range(4):
                    configurazioni_h[i] += configurazioni_h_1[i]
            return tuple(configurazioni_h)
        return tuple([0,0,0,0])
    
    def stampa_albero(self, h=9, indentazione=0):
        if h < 0:
            return
        self.stampa_griglia(indentazione)
        for figlio in self.lista_figli:
            figlio.stampa_albero(h - 1, indentazione + 1)
        
    def stampa_griglia(self, indentazione):
        print('')
        for i in range(3):
            print(' ' * 9 * indentazione, end='')
            self.stampa_riga_griglia(i)
                
    def stampa_riga_griglia(self, i):
        for j in range(3):
            self.stampa_cella_griglia(i, j)
        if i == 1:
            tipo_griglia = ' (' + self.tipo() + ')'
            print(tipo_griglia, end='')
        print('')
            
    def stampa_cella_griglia(self, i, j):
        if self.nome[i][j] == '':
            print('[ ]', end='')
        else:
            print('[' + self.nome[i][j] + ']', end='')
          
def gen_tree(griglia):
    N = NodoTris(griglia)
    g = N.giocatore_di_turno()
    N.aggiungi_figli(g)
    return N
