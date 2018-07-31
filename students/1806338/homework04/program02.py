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
import copy
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []  
        self.stato = ''        
    def figli(self):
        for x in self.lista_figli:
            " "
    def tipo(self):        
        if self.nome[2][0] == self.nome[2][1] and self.nome[2][1] == self.nome[2][2] and self.nome[2][0]!='':
            self.stato=self.nome[2][0]
            return self.nome[2][0]
        if self.nome[0][0] == self.nome[1][0] and self.nome[1][0] == self.nome[2][0] and self.nome[0][0]!='':
            self.stato=self.nome[0][0]
            return self.nome[0][0]        
        if self.nome[2][2] == self.nome[1][2] and self.nome[1][2] == self.nome[0][2] and self.nome[2][2]!='':
            self.stato=self.nome[2][2]
            return self.nome[2][2]
        if self.nome[2][1] == self.nome[1][1] and self.nome[1][1] == self.nome[0][1] and self.nome[2][1]!='':
            self.stato=self.nome[2][1]
            return self.nome[2][1]        
        if self.nome[1][0] == self.nome[1][1] and self.nome[1][1] == self.nome[1][2] and self.nome[1][0]!='':
            self.stato=self.nome[1][0]
            return self.nome[1][0]
        if self.nome[0][0] == self.nome[0][1] and self.nome[0][1] == self.nome[0][2] and self.nome[0][0]!='':
            self.stato=self.nome[0][0]
            return self.nome[0][0]
        if self.nome[0][0] == self.nome[1][1] and self.nome[1][1] == self.nome[2][2] and self.nome[0][0]!='':
            self.stato=self.nome[0][0]
            return self.nome[0][0]
        if self.nome[2][0] == self.nome[1][1] and self.nome[1][1] == self.nome[0][2] and self.nome[2][0]!='':
            self.stato=self.nome[2][0]
            return self.nome[2][0]
        else:                    
            return(self.pat_ncomp())                        
    def pat_ncomp(self):  
        t=0
        for p in range(0,3):
            for e in range(0,3):
                if self.nome[e][p] == 'x': 
                    t+=1
                if self.nome[e][p] == 'o':
                    t+=1
        if t==9:
            self.stato=('-')
            return('-')
        if t<9:
            self.stato=('?')
            return('?')           
    def esiti(self):
        NodoTris.o=0
        NodoTris.x=0
        NodoTris.p=0                
        return (self.contaes())    
    def contaes(self):
        if self.stato=='o':
            NodoTris.o+=1
        if self.stato=='x':
            NodoTris.x+=1
        if self.stato=='-':
            NodoTris.p+=1
        else:
            NodoTris.p+=0          
        return self.ri()
    def ri(self):
        for b in self.lista_figli:
            b.contaes()
        o=NodoTris.o
        x=NodoTris.x
        p=NodoTris.p  
        u=(p,o,x)     
        return u          
    def vittorie_livello(self, giocatore, h):
        NodoTris.c=0
        self.li(giocatore,h,0)
        return(NodoTris.c)                
    def li(self,giocatore,h,m):        
        if h==0:
            if not self.stato!=giocatore:
                m=1
                return(m)        
        if h!=0:
            self.rico(m,giocatore,h)            
    def rico(self,m,giocatore,h):     
        for x in self.lista_figli:
            m+=1
            if x.stato==giocatore and h==m:
                   NodoTris.c+=1
            x.li(giocatore,h,m)
            m-=1            
        return(m)    
    def strategia_vincente(self,giocatore):
        """ """    
def gen_tree(griglia):
    gri=copy.deepcopy(griglia)
    e=NodoTris(gri)                                   
    e.tipo()
    if e.stato!='o':
        if e.stato!='x':
            e=NodoTris(gri)                                   
            e.tipo()
            cont_o=0
            cont_x=0
            m=mossa(cont_o,cont_x,gri)            
            for x in range(len(griglia)):      
                for y in range(len(griglia)):                 
                    if gri[x][y]=='':                                  
                        gri[x][y]=m          
                        e.lista_figli+=[gen_tree(gri)]       
                        gri[x][y]=''
    return(e)
def mossa(cont_o,cont_x,gri):
    for v in gri:
                for b in v:
                    if b=='x':
                        cont_x+=1
                    if b=='o':
                        cont_o+=1
    if cont_x>=cont_o:
        m='o'
        return(m)
    if cont_o>cont_x:
        m='x' 
        return(m)
