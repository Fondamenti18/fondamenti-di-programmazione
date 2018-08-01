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

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] 
    
    def tipo(self):
        if self.nome[0][0]==self.nome[0][1]==self.nome[0][2] and self.nome[0][0]!='' :
            return self.nome[0][0]
        elif self.nome[1][0]==self.nome[1][1]==self.nome[1][2] and self.nome[1][0]!='' :
            return self.nome[1][0]
        elif self.nome[2][0]==self.nome[2][1]==self.nome[2][2] and self.nome[2][0]!='':
            return self.nome[2][0]    

        elif self.nome[0][0]==self.nome[1][0]==self.nome[2][0] and self.nome[0][0]!='' :
            return self.nome[0][0]            
        elif self.nome[0][1]==self.nome[1][1]==self.nome[2][1] and self.nome[0][1]!='':
            return self.nome[0][1]
        elif self.nome[0][2]==self.nome[1][2]==self.nome[2][2] and self.nome[0][2]!='' :
            return self.nome[0][2]

        elif self.nome[0][0]==self.nome[1][1]==self.nome[2][2] and self.nome[0][0]!='' :
            return self.nome[0][0]

        elif self.nome[0][2]==self.nome[1][1]==self.nome[2][0] and self.nome[0][2]!='':
            return self.nome[0][2]
        
        for x in self.nome:
            if '' in x:
                return '?'
        else:
            return '-'
            

    def esiti(self):
        self.radice=gen_tree(self.nome)
        self.x=0
        self.p=0
        self.o=0
        self.p,self.o,self.x=conta(self.p,self.o,self.x,self.radice)
        return (self.p,self.o,self.x)

    def vittorie_livello(self, giocatore, h):
        self.pos=0
        self.diz={}
        self.diz[0]=[gen_tree(self.nome).nome]
        self.diz_f=livelli(self.pos,self.diz,self)
        self.num=0
        self.num=conta_v(self.diz_f,giocatore,h,self.num)
        return self.num
    

    def strategia_vincente(self,giocatore):
        i=0
        a=strat(self,giocatore)
        return a











def gen_tree(griglia):
    radice=NodoTris(griglia)
    giocatore=mossa(griglia)
    radice.lista_figli=ins_tree(griglia,radice,giocatore)
    return radice



def ins_tree(griglia,radice,giocatore):
    if radice.tipo()=='?':   
        for x in spazi(griglia):
            grr=figli(griglia,x,giocatore)    
            figlio=NodoTris(grr)
            radice.lista_figli.append(figlio)
    for z in radice.lista_figli:
        
        if mossa(z.nome)=='x':
            z.lista_figli=ins_tree(z.nome,z,'x')
        if mossa(z.nome)=='o':
            z.lista_figli=ins_tree(z.nome,z,'o')
    return radice.lista_figli


def mossa(griglia):
    g_x=0
    g_o=0
    for x in griglia:
        for y in x:
            if y=='x':
                g_x+=1
            if y=='o':
                g_o+=1
    if g_x==g_o:
        return 'o'
    if g_o>g_x:
        return 'x'

def spazi(griglia): 
    y=0
    ins=set()
    while y<len(griglia):
        x=0
        while x<len(griglia[y]):
            if griglia[y][x]=='':
                ins.add((y,x))
            x+=1
        y+=1
    
    return ins
    

from copy import deepcopy
def figli(griglia,x,giocatore): 
    g=deepcopy(griglia)
    g[x[0]][x[1]]=giocatore
    return g
    








def conta(p,o,x,nodo):  
        if nodo.tipo()=='x':
            x+=1
        if nodo.tipo()=='o':
            o+=1
            
        if nodo.tipo()=='-':
            p+=1
        i=0
        while i<len(nodo.lista_figli):
            p,o,x=conta(p,o,x,nodo.lista_figli[i])
            i+=1

        return (p,o,x)

def livelli(pos,diz,nodo): 
        for y in nodo.lista_figli:
            
            pos_f=pos+1
            if pos_f not in diz.keys():
                diz[pos_f]=[]
            diz[pos_f].append(y.nome)
            livelli(pos_f,diz,y)
        return diz
def conta_v(diz_f,giocatore,h,num):
        for x in diz_f[h]:
            if NodoTris(x).tipo()==giocatore:
                num+=1
        
        return num



def strat(self,giocatore):
    
    l=gen_tree(self.nome).esiti()
    if mossa(self.nome)==giocatore:
        if l[1]!=0:
            return True
        else:
            return False
    else:
        if l[1]==0:
            return True
        else:
            return False
