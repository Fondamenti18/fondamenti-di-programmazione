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

class NodoTris:
    def __init__(self, griglia): 
        self.nome = griglia #griglia del nodo
        self.lista_figli = [] #lista dei nodi figli
        self.vuoti=None #numero spazi vuoti della griglia
        self.turn='' #turno del giocatore
        self.win='' #lo stato della griglia
        self.height=0 #l'altezza nell'albero del nodo

    
    def tipo(self): #funzione che torna se vince
        return vitt(self)
        
    def esiti(self):#funzione che trova tutti gli esiti di una configurazione
        n_s=0
        n_x=0
        n_o=0
        if self.win=='':
            for i in self.lista_figli:
                t2=i.esiti()
                n_s+=t2[0]
                n_o+=t2[1]
                n_x+=t2[2]
        else:
            if self.win=='-':
                n_s+=1
            elif self.win=='o':
                n_o+=1
            elif self.win=='x':
                n_x+=1
        return (n_s,n_o,n_x)
    
    def vittorie_livello(self, giocatore, h): #funzione che conta il numero di vittorie per un giocatore ad un livello dell'albero specifico
        l=h+self.height
        return conta_vitt(self,giocatore,l)
    
    def strategia_vincente(self,giocatore): #funzione che indica se un giocatore ha una strategia vincente
        if self.turn!=giocatore:
            v = strategia(self, self.turn)
            if v == -1:
                return True
            else:
                return False
        else:
            v = strategia(self, self.turn)
            if v==1:
                return True
            else:
                return False

def strategia(nodo, g): #funzione che trova se un giocatore ha la possibilita' di vincere qualsiasi mossa faccia l'avversario
    v=0
    if len(nodo.lista_figli)==0:
        if nodo.win=='o':
                v=1
        elif nodo.win=='x':
                v=-1
        elif nodo.win=='-':
                v=0
    elif g=='o':
        v=-1
        for c in nodo.lista_figli:
            v=max(v,strategia(c,'x'))
    else:
        v=1
        for c in nodo.lista_figli:
            v=min(v,strategia(c,'o'))
    return v

def conta_vitt(radice,g,l): #funzione che conta il numero di vittorie di un giocatore
    c=0
    if radice.height!=l:
        for i in radice.lista_figli:
            c+=conta_vitt(i,g,l)
    else:
        if radice.win==g:
            c+=1
    return c

def vitt(radice): #funzione che combina tutti i possibili tipi di vittoria
    v1=win_diag(radice.nome)
    v2=win_vert(radice.nome)
    v3=win_oriz(radice.nome)
    if v1==None:
        if v2==None:
            if v3==None:
                if radice.vuoti==0:
                    return '-'
                else:
                    return '?'
            else:
                return v3
        else:
            return v2
    else:
        return v1


def stallo(griglia):#funzione che indica se si e' in uno stato di stallo
    v='-'
    for y in range(3):
        for x in range(3):
            if griglia[y][x]=='':
                v='?'
                break
    return v

def win_oriz(griglia):#funzione che indica se un giocatore ha vinto in orizontale
    linea_x=['x','x','x']
    linea_o=['o','o','o']
    v=None
    for y in range(3):
        if griglia[y]==linea_x:
            v='x'
        elif griglia[y]==linea_o:
            v='o'
    return v

def win_vert(griglia):#funzione che indica se un giocatore ha vinto in verticale
    v = None
    for x in range(3):
        if griglia[0][x]=='x':
            if griglia[1][x]=='x' and griglia[2][x]=='x':
                v='x'
        elif griglia[0][x]=='o':
            if griglia[1][x] == 'o' and griglia[2][x] == 'o':
                v='o'
    return v



def win_diag(griglia): #funzione che indica se un giocatore ha vinto in diagonale
    if griglia[1][1]=='x':
        if griglia[0][0]=='x' and griglia[2][2]=='x':
            return 'x'
        elif griglia[0][2]=='x' and griglia[2][0]=='x':
            return 'x'
        else:
            return None
    elif griglia[1][1]=='o':
        if griglia[0][0]=='o' and griglia[2][2]=='o':
            return 'o'
        elif griglia[0][2]=='o' and griglia[2][0]=='o':
            return 'o'
        else:
            return None
    else:
        return None


def successivo(griglia, turn, vuote): #funzione che crea tutte le possibili combinazioni di mosse successive
    l=[]
    if vuote!=0:
        for y in range(3):
            for x in range(3):
                if griglia[y][x]=='':
                    lista = [['', '', ''], ['', '', ''], ['', '', '']]
                    for k in range(3):
                        for j in range(3):
                            lista[k][j] += griglia[k][j]
                    lista[y][x]+=turn
                    r=NodoTris(lista)
                    l+=[r]
    return l


def vuoti(griglia): #funzione che stabilisce quanti spazi vuoti ci sono nella griglia
    vuote=0
    for y in range(3):
        for x in range(3):
            if griglia[y][x]!='x' and griglia[y][x]!='o':
                vuote+=1
    return vuote

def turno(griglia): #funzione che stabilisce il turno
    c_x=0
    c_o=0
    for y in range(3):
        for x in range(3):
            if griglia[y][x]=='x': c_x+=1
            elif griglia[y][x]=='o':c_o+=1
    if c_x==c_o:
        return 'o'
    elif c_o>c_x:
        return 'x'


def ins_tree(r,radice): #funzione che inserisce i nodi nell'albero
    v=radice.vuoti-1
    r.vuoti=v
    r.height=radice.height+1
    if r.vuoti==0:
        r.win=vitt(r)
    else:
        w=vitt(r)
        if w!='?':
            r.win=w
        else:
            if radice.turn=='o': r.turn='x'
            else: r.turn='o'
            r.lista_figli=successivo(r.nome,r.turn,r.vuoti)
            for i in r.lista_figli:
                ins_tree(i,r)

def gen_tree(griglia): #funzione che genera l'albero
    v=vuoti(griglia)
    radice=NodoTris(griglia)
    radice.vuoti=v
    if radice.vuoti==0:
        radice.win=vitt(radice)
    else:
        w=vitt(radice)
        if w!='?':
            radice.win=w
        else:
            radice.turn=turno(radice.nome)
            radice.lista_figli=successivo(radice.nome,radice.turn,radice.vuoti)
            for i in radice.lista_figli:
                ins_tree(i,radice)
    return radice
