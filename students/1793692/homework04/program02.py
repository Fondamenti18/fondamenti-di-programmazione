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
        self.count=0
    def tipo(self):
        '''inserire qui il vostro codice'''
        if vittoria(self.nome,'x'):
            return 'x'
        if vittoria(self.nome,'o'):
            return 'o'
        if not vittoria(self.nome,'x') and not vittoria(self.nome,'o') and contaxo(self.nome)==9:
            return '-'
        if not vittoria(self.nome,'x') and not vittoria(self.nome,'o') and contaxo(self.nome)<9:
            return '?'
        
    def esiti(self):
        '''inserire qui il vostro codice'''
        esi=[0,0,0]
        if self.tipo()=='x':
            esi[2]+=1
        if self.tipo()=='o':
            esi[1]+=1
        if self.tipo()=='-':
            esi[0]+=1
        t=rec_esiti(self,esi)
        return t
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        v=[0]
        return rec_vl(self,giocatore,h,v)
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        l=[]
        g1=str_vin(self,giocatore,l)
        if giocatore=='x':
            g2=str_vin(self,'x',l)
        else:
            g2=str_vin(self,'o',l)
        if g1<g2:
            return True
        else:
            return False
        
def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    nodo=NodoTris(griglia)
    if not vittoria(griglia,'x') and not vittoria(griglia,'o'):
        for i in range(3):
            for j in range(3):
                if griglia[i][j]=='':
                    mossa=tipomossa(contaxo(griglia))
                    new=deepcopy(griglia)
                    new[i][j]=mossa
                    nodo.lista_figli.append(gen_tree(new))
    return nodo
     
    
def contaxo(matrice):
    count=0
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j]=='': 
                count+=1
    return 9-count
            
def tipomossa(x):
    if x%2==0:
        return 'o'
    return 'x'
    
def vittoria(griglia,g):
    #Prima riga
    if griglia[0][0] == g and griglia[0][1] == g and griglia[0][2] == g:
        return True
    #Seconda riga
    if griglia[1][0] == g and griglia[1][1] == g and griglia[1][2] == g:
        return True
     #Terza riga
    if griglia[2][0] == g and griglia[2][1] == g and griglia[2][2] == g:
        return True
    #Prima colonna
    if griglia[0][0] == g and griglia[1][0] == g and griglia[2][0] == g:
        return True
    #Seconda colonna 
    if griglia[0][1] == g and griglia[1][1] == g and griglia[2][1] == g:
        return True
    #Terza colonna
    if griglia[0][2] == g and griglia[1][2] == g and griglia[2][2] == g:
        return True
    #Diagonale
    if griglia[0][0] == g and griglia[1][1] == g and griglia[2][2] == g:
        return True
    #Diagonale
    if griglia[0][2] == g and griglia[1][1] == g and griglia[2][0] == g:
        return True
    return False

def vincitore(griglia):
    if vittoria(griglia,'x'):
        return 'x'
    if vittoria(griglia,'o'):
        return 'o'
    if not vittoria(griglia,'x') and not vittoria(griglia,'o') and contaxo(griglia)==9:
        return '-'
    if not vittoria(griglia,'x') and not vittoria(griglia,'o') and contaxo(griglia)<9:
        return '?'
def rec_esiti(nodo,esi):
    if nodo.lista_figli==[]:return(esi[0],esi[1],esi[2]) 
    for figlio in nodo.lista_figli:
        if figlio.tipo()=='x':
            esi[2]+=1
        if figlio.tipo()=='o':
            esi[1]+=1
        if figlio.tipo()=='-':
            esi[0]+=1
        rec_esiti(figlio,esi)
    return (esi[0],esi[1],esi[2])
def rec_vl(nodo,g,h,v):
    alt=1
    if alt==h:
        if nodo.tipo()==g:
            v[0]+=1
    for figlio in nodo.lista_figli:
        alt = max(alt, rec_vl(figlio,g,h,v) + 1)
    return v[0]
def str_vin(nodo,g,l):
    alt=1
    if nodo.tipo()==g:
        l.append(alt)
    for figlio in nodo.lista_figli:
        alt = max(alt, str_vin(figlio,g,l) + 1)  
    return min(l)
        
        