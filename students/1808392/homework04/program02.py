'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 
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
import sys
sys.setrecursionlimit = 999999999999999999999999999999999999999999999999999999
 

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        #vincita
        if len(set([self.nome[0][0],self.nome[0][1],self.nome[0][2]])) == 1:
            if self.nome[0][0] != '':
                return self.nome[0][0]
        elif len(set([self.nome[1][0],self.nome[1][1],self.nome[1][2]])) == 1:
            if self.nome[1][0] != '':
                return self.nome[1][0]
        elif len(set([self.nome[2][0],self.nome[2][1],self.nome[2][2]])) == 1:
            if self.nome[2][0] != '':
                return self.nome[2][0]
        elif len(set([self.nome[0][0],self.nome[1][0],self.nome[2][0]])) == 1:
            if self.nome[0][0] != '':
                return self.nome[0][0]
        elif len(set([self.nome[0][1],self.nome[1][1],self.nome[2][1]])) == 1:
            if self.nome[0][1] != '':
                return self.nome[0][1]
        elif len(set([self.nome[0][2],self.nome[1][2],self.nome[2][2]])) == 1:
            if self.nome[0][2] != '':
                return self.nome[0][2]
        elif len(set([self.nome[0][0],self.nome[1][1],self.nome[2][2]])) == 1:
            if self.nome[0][0] != '':
                return self.nome[0][0]
        elif len(set([self.nome[2][0],self.nome[1][1],self.nome[0][2]])) == 1:
            if self.nome[2][0] != '':
                return self.nome[2][0]
        
        # pareggio o ?
        for h in range(3):
            if '' in self.nome[h]:
                return '?'
        
        return '-'
        
    def esiti(self,utente='',contaX=0,contaO=0,contaP=0):
        if utente == '':
            utente = VerUtente(self.nome)
        elif utente == 'x':
            utente='o'
        elif utente== 'o':
            utente='x'
        
        ver = self.tipo()
        if ver != '?':
            if ver == 'x':
                contaX += 1
            elif ver == 'o':
                contaO +=1
            elif ver == '-':
                contaP +=1
        else:
            for el in self.lista_figli:
                (contaP,contaO,contaX)=el.esiti(utente,contaX,contaO,contaP)
                
        return (contaP,contaO,contaX)
    
    def vittorie_livello(self, giocatore, h,CountR=0,lst=None):
        
        if lst is None:
            lst = []
            global countE
            countE = self.Ver_Vuoti()
            
        while (CountR<h):
            CountR +=1
            for Nodo in self.lista_figli:
                
                if Nodo.Ver_Livello(countE) == h:
                    lst += [Nodo.nome] 
                else:
                    Nodo.vittorie_livello(giocatore,h,CountR,lst)
                   
                
        
        if CountR == 0:
           if self.nome == giocatore:
               return 1
           else:
               return 0
        else:    
            countV = 0
        
        for el in lst:
            Nodo = NodoTris(el)
            if Nodo.tipo() == giocatore:
                countV += 1
        return countV
    
    def strategia_vincente(self,giocatore,ris=None,Tipo=None):
        if ris is None:
            ris = False  # default senza strategia vincente
            
        utente = VerUtente(self.nome) # verifico utente di partenza
                   
        if utente == 'x': # controllo avversario
            avv ='o'
        else:
            avv='x'

        for son in self.lista_figli: # scendo ricorsivamente fino alla vittoria
            ver = son.tipo() 
            
            if ver == giocatore and Tipo is None and utente == giocatore: # vittoria al primo turno
                ris = True
            else: 
                if ver == avv:
                    ris = False
                if ver == utente:
                    ris = True
                
                ris = son.strategia_vincente(giocatore,ris,1)
                            
            
            
        return ris
    
    def Ver_Livello(Nodo,NumV=0):
        count = 0
        for h in range(3):
            for j in range(3):
                if Nodo.nome[h][j] == '':
                    count +=1
                    
         
        return 9 - (9-NumV) -count
    
    def Ver_Vuoti(Nodo):
        count = 0
        for h in range(3):
            for j in range(3):
                if Nodo.nome[h][j] == '':
                    count +=1
                    
        return count
def gen_tree(griglia,utente=''):
    
    if utente == '':
        utente = VerUtente(griglia)
    elif utente == 'x':
        utente='o'
    elif utente== 'o':
        utente='x'
    Nodo = NodoTris(griglia)
    for h in range(3):
        for j in range(3):
            if griglia[h][j] == '' and Nodo.tipo() == '?':
                grigliaC=[x[:] for x in griglia]
                grigliaC[h][j] = utente
                Nodo.lista_figli += [gen_tree(grigliaC,utente)]
                
    
    return Nodo

def VerUtente(griglia):
    countx = 0
    counto = 0
    for y in range(3):
        for x in range(3):
            if griglia[y][x] == 'x':
                countx +=1
            elif griglia[y][x] == 'o':
                counto +=1
                
    if counto >= countx:
        return 'o'
    else:
        return 'x'

               
