import copy 
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
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        griglia=self.nome #la griglia del Nodo
        void=False
        possibleWins=[griglia[0],griglia[1],griglia[2],[griglia[i][0] for i in range(3)],[griglia[i][1] for i in range(3)],[griglia[i][2] for i in range(3)],[griglia[i][i] for i in range(3)],[griglia[i][2-i] for i in range(3)]] 
        for i in possibleWins:
            if '' in i:
                void=True
            if i.count('x')==3 or i.count('o')==3:
                return i[0]
        return '?' if void else '-'
        
            
             
    def esiti(self,dizionario={}):
        tipo=self.tipo()       #il tipo del nodo
        key=getKey(self.nome)
        if key in dizionario.keys():
            return dizionario[key]
        if tipo!='?':
            if tipo=='-':
                return (1,0,0)
            else:
                return  (0,1,0) if tipo=='o' else (0,0,1)
        sons=self.lista_figli
        results=(0,0,0)
        for son in sons:
            results=tuple(map(sum, zip(results, son.esiti(dizionario))))      #somma tra la tupla del padre e quella di tutti i figli
        dizionario[key]=results
        return results


           
    def vittorie_livello(self, giocatore, h):
        if h==0:
            return 1 if self.tipo()==giocatore else 0
        else:
            h-=1
            sons=self.lista_figli
            result=0
            for son in sons:
                result+=son.vittorie_livello(giocatore,h)
        return result
    
    def strategia_vincente(self,giocatore):
        sons=self.lista_figli     #figli del nodo
        tipo=self.tipo()          #situazione di gioco
        turno= len(possibleMoves(self.nome))%2!=0 if giocatore=='o' else len(possibleMoves(self.nome))%2==0 #se il prossimo a giocare è il giocatore che a noi interessa
        result=True
        if tipo!='?':
            result= tipo==giocatore
        else:
            if turno:
                for i in range(len(sons)):
                    if sons[i].strategia_vincente(giocatore):
                        result=True
                        break
                    if not(sons[i].strategia_vincente(giocatore)) and i==(len(sons)-1):
                        result=False
            else:
                for i in sons:
                    if not(i.strategia_vincente(giocatore)):
                        result=False
                        break
        return result
        
def gen_tree(griglia):
    node=NodoTris(griglia)         #nodo generato con la griglia passata in input
    griglieSon=genSon(griglia)     #variabile con dentro le griglie di tutte le possibili mosse
    if len(griglieSon)>0 and node.tipo()!='x' and node.tipo()!='o' :
        for i in griglieSon:
            node.lista_figli+=[gen_tree(i)]
    return node
            

def genSon(griglia):
    voidPlace=possibleMoves(griglia)                 #variabile con tutti gli indirizzi degli spazi vuoti sulla griglia
    griglieSon=[]                                    #lista delle griglie di tutte le possibili mosse
    turn='o' if len(voidPlace)%2!=0 else 'x'         #il simbolo da appendere in base al turno
    for i in voidPlace:
        grigliaTemp=copy.deepcopy(griglia)
        grigliaTemp[i[0]][i[1]]=turn
        griglieSon.append(grigliaTemp)
    return griglieSon

def possibleMoves(griglia):
    moves=[]
    for i in range(len(griglia)):
        for x in range(len(griglia[0])):
            if griglia[i][x]=='':
                moves.append([i,x])
    return moves 

def getKey(griglia):
    return tuple(griglia[0]+griglia[1]+griglia[2])
