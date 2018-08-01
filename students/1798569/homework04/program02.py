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
vittorie=0
vittorie2=0
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.tipologia=''
        self.livello=0
    def tipo(self):
        '''inserire qui il vostro codice'''
        return self.tipologia
        
    def esiti(self):
        '''inserire qui il vostro codice'''
        x= contaLivelli(self, [0,0,0])
        return(x[0],x[1],x[2])
    
    def vittorie_livello(self, giocatore, h):
        global vittorie
        vittorie=0
        return(contaLivelli2(self,giocatore,h))
        '''inserire qui il vostro codice'''
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        global vittorie2
        vittorie2=0
        return(contaLivelli3(self,giocatore))
        
def gen_tree(griglia,start='o',cnt=0):
    '''inserire qui il vostro codice'''
    nodo=NodoTris(griglia)
    nodo.livello=cnt
    if nodo.nome[0][0]=='x' and nodo.nome[0][1]=='x' and nodo.nome[0][2]=='x':
        nodo.tipologia='x'
    if nodo.nome[1][0]=='x' and nodo.nome[1][1]=='x' and nodo.nome[1][2]=='x':
        nodo.tipologia='x'
    if nodo.nome[2][0]=='x' and nodo.nome[2][1]=='x' and nodo.nome[2][2]=='x':
        nodo.tipologia='x'    
    if nodo.nome[0][0]=='x' and nodo.nome[1][0]=='x' and nodo.nome[2][0]=='x':
        nodo.tipologia='x'
    if nodo.nome[0][1]=='x' and nodo.nome[1][1]=='x' and nodo.nome[2][1]=='x':
        nodo.tipologia='x'
    if nodo.nome[0][2]=='x' and nodo.nome[1][2]=='x' and nodo.nome[2][2]=='x':
        nodo.tipologia='x'
    if nodo.nome[0][0]=='x' and nodo.nome[1][1]=='x' and nodo.nome[2][2]=='x':
        nodo.tipologia='x'
    if nodo.nome[0][2]=='x' and nodo.nome[1][1]=='x' and nodo.nome[2][0]=='x':
        nodo.tipologia='x'
        
    if nodo.nome[0][0]=='o' and nodo.nome[0][1]=='o' and nodo.nome[0][2]=='o':
        nodo.tipologia='o'
    if nodo.nome[1][0]=='o' and nodo.nome[1][1]=='o' and nodo.nome[1][2]=='o':
        nodo.tipologia='o'
    if nodo.nome[2][0]=='o' and nodo.nome[2][1]=='o' and nodo.nome[2][2]=='o':
        nodo.tipologia='o'    
    if nodo.nome[0][0]=='o' and nodo.nome[1][0]=='o' and nodo.nome[2][0]=='o':
        nodo.tipologia='o'
    if nodo.nome[0][1]=='o' and nodo.nome[1][1]=='o' and nodo.nome[2][1]=='o':
        nodo.tipologia='o'
    if nodo.nome[0][2]=='o' and nodo.nome[1][2]=='o' and nodo.nome[2][2]=='o':
        nodo.tipologia='o'
    if nodo.nome[0][0]=='o' and nodo.nome[1][1]=='o' and nodo.nome[2][2]=='o':
        nodo.tipologia='o'
    if nodo.nome[0][2]=='o' and nodo.nome[1][1]=='o' and nodo.nome[2][0]=='o':
        nodo.tipologia='o'
        
    conta=0
    for x in range(3):
        for y in range(3):
            if nodo.nome[x][y]!='':
                conta+=1
    if conta==9 and nodo.tipologia=='':
        nodo.tipologia='-'
    elif nodo.tipologia=='':
        nodo.tipologia='?'
    
    if nodo.tipologia == '?':
        k=deepcopy(nodo.nome)
        lista=[]
        for x in range(3):
            for y in range(3):
                if nodo.nome[x][y]=='':
                    k=deepcopy(nodo.nome)
                    k[x][y]=start
                    lista.append(k)
        if start=='o':
            start='x'
        else:
            start='o'
            
        for x in lista:
            nodo.lista_figli.append(gen_tree(x,start,cnt+1))
        return nodo
    else:
        return nodo



#x=gen_tree([['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']])

#y=gen_tree([['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']])
'''
print ('nome di x',x.livello)

y=x.lista_figli
print(y[0].livello)

k=y[0].lista_figli
print(k[0].livello)
j=k[0].lista_figli
print(j[0].livello)

'''

def contaLivelli(x,esito=[0,0,0]):
    if x.tipologia=='-':
        esito[0]+=1
    if x.tipologia=='o':
        esito[1]+=1
    if x.tipologia=='x':
        esito[2]+=1    
    if x.lista_figli ==[]:
        return esito
    for y in x.lista_figli:
         contaLivelli(y,esito) 
    return esito



def contaLivelli2(x,vincitore,liv):
    global vittorie    
    if x.tipologia==vincitore and x.livello==liv:
        vittorie+=1  
    if x.lista_figli ==[]:
        return vittorie
    for y in x.lista_figli:
         contaLivelli2(y,vincitore,liv) 
    return vittorie

def contaLivelli3(x,vincitore,liv):
    global vittorie    
    if x.tipologia==vincitore and x.livello==liv:
        vittorie+=1  
    if x.lista_figli ==[]:
        return vittorie
    for y in x.lista_figli:
         contaLivelli2(y,vincitore,liv) 
    return vittorie

#print(contaLivelli2(x,'x',2))
#print(contaLivelli2(y,'x',3))

