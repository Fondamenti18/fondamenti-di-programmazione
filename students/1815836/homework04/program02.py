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
import copy

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.var_vict = check_vittoria(self.nome)
        self.var_patta = patta(self.nome)
        self.var_turno = contaturno(self.nome)

    def tipo(self):
        griglia2=self.nome
        vittoria=self.var_vict
        if vittoria!=None:
            return(vittoria)
        if vittoria==None:
            listavuote2=[]
            for x in range(0,len(griglia2)):
                for y in range(0,len(griglia2)):
                    if (griglia2[x][y]==''):
                        listavuote2+=[[x]+[y]]
            if listavuote2!=[]:
                return('?')
            if listavuote2==[]:
                return('-')
        
    def esiti(self,pp=0,vo=0,vx=0):
        vittoria=self.var_vict
        if vittoria=='o':
            vo+=1
            return(pp,vo,vx)
        if vittoria=='x':
            vx+=1
            return(pp,vo,vx)
        if vittoria==None:
            if self.var_patta=='p':
                pp+=1
                return(pp,vo,vx)
        for nodes in self.lista_figli:
            pp,vo,vx=nodes.esiti(pp,vo,vx)
        return(pp,vo,vx)

    def vittorie_livello(self, giocatore, h,level=0):
        vittoria=self.var_vict
        val=0
        if vittoria==giocatore and level==h:
            return(1)
        for nodes in self.lista_figli:
            val+=nodes.vittorie_livello(giocatore,h,level+1)
        return(val)
            
    def strategia_vincente(self,giocatore):
        val=0
        for nodes in self.lista_figli:
            if nodes.var_vict==giocatore:
                val+=1
            nodes.strategia_vincente(giocatore)
        if val>=1:
            return True
        else:
            return False

        
        
        
        
      
def gen_tree(griglia):
    nodo=NodoTris(griglia)
    turno=contaturno(griglia)    
    vittoria=check_vittoria(griglia)
    listavuote=[]
    if vittoria!=None:
        return nodo
    for x in range(0,len(griglia)):
        for y in range(0,len(griglia)):
            if (griglia[x][y]==''):
                listavuote+=[[x]+[y]]
    for c in listavuote:
        grigliat=copy.deepcopy(griglia)
        grigliat[c[0]][c[1]]=turno
        nodo.lista_figli+=[gen_tree(grigliat)] 
    return nodo

def contaturno(griglia):
    n_x=0
    n_o=0
    for x in range(0,len(griglia)):
        for y in range(0,len(griglia)):
            if (griglia[x][y]=='x'):
                n_x+=1
            if (griglia[x][y]=='o'):
                n_o+=1
    if(n_o==n_x):
        return('o')
    if(n_o>n_x):
        return('x')
        
def check_vittoria(griglia):
    for x in range(0,len(griglia)):
        if(griglia[x][0] == griglia[x][1] == griglia[x][2] and griglia[x][0]!=''):
            return(griglia[x][0])
        if(griglia[0][x] == griglia[1][x] == griglia[2][x] and griglia[0][x]!=''):
            return(griglia[0][x])
        if(griglia[0][0] == griglia[1][1] == griglia[2][2] and griglia[1][1]!=''):
            return(griglia[1][1])
        if(griglia[0][2] == griglia[1][1] == griglia[2][0] and griglia[1][1]!=''):
            return(griglia[1][1])
    return(None)
    
def patta(griglia):
    listavuote2=[]
    for x in range(0,len(griglia)):
        for y in range(0,len(griglia)):
            if (griglia[x][y]==''):
                listavuote2+=[[x]+[y]]
    if listavuote2==[]:
        return('p')
    return('errore')
   

























