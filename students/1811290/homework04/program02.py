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
    
    def tipo(self):
        griglia_situazione=[]
        for x in self.nome:
            griglia_situazione+=[x]
        #griglia_situazione=copy.deepcopy(self.nome)
        if griglia_situazione[1][1]!='':
            if griglia_situazione[1][1]==griglia_situazione[0][0] and griglia_situazione[1][1]==griglia_situazione[2][2]:# or griglia_situazione[1][1]==griglia_situazione[2][0] and griglia_situazione[1][1]==griglia_situazione[0][2]:
                return griglia_situazione[1][1]
            elif griglia_situazione[1][1]==griglia_situazione[2][0] and griglia_situazione[1][1]==griglia_situazione[0][2]:
                    #print(griglia_situazione[1][1])
                    return griglia_situazione[1][1]
        for y in range(3):
            if griglia_situazione[y][0]!='':
                if griglia_situazione[y][0]==griglia_situazione[y][1] and griglia_situazione[y][0]==griglia_situazione[y][2]:
                    #print(griglia_situazione[y][0])
                    return griglia_situazione[y][0]
                    break
            if griglia_situazione[0][y]!='':
                if griglia_situazione[0][y]==griglia_situazione[1][y] and griglia_situazione[0][y]==griglia_situazione[2][y]:
                    #print(griglia_situazione[0][y])
                    return griglia_situazione[0][y]
                    break
        if celle_vuote(griglia_situazione)!=[]:
            #print('?')
            return '?'
        else:
            #print('-')
            return '-'
        
    def esiti(self,conto_patta=0,conto_O=0,conto_X=0):
        '''inserire qui il vostro codice'''
        for figlio in self.lista_figli:
            conto_patta,conto_O,conto_X = figlio.esiti(conto_patta,conto_O,conto_X)
        #if celle_vuote(self.nome)==[]:
        if self.tipo()=='o':
            conto_O+=1
        elif self.tipo()=='x':
            conto_X+=1
        elif self.tipo()=='-':
            conto_patta+=1
        result=(conto_patta,conto_O,conto_X)
        return result
        
    def vittorie_livello(self, giocatore='o', h=0, somma_esiti=0,k_mossa=0):
        '''inserire qui il vostro codice'''
        for figlio in self.lista_figli:
            #print('FOR')
            somma_esiti = figlio.vittorie_livello(giocatore,h,somma_esiti, k_mossa+1)
        #print('K_MOSSE',k_mossa,'\nSOMMA_ESITI',somma_esiti)
        if k_mossa==h:
            if self.tipo()==giocatore:
                somma_esiti+=1
                #result=(k_mossa,somma_esiti)
        #result=(k_mossa,somma_esiti)
        return somma_esiti
        
        
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        pass
    
def gen_tree(griglia):
    radice = NodoTris(griglia)
    cellevuote=celle_vuote(griglia)
    for x,y in cellevuote:
        griglia2=[]
        for linea in griglia:
            riga=[]
            for elemento in linea:
                riga+=[elemento]
            griglia2+=[riga]
        #griglia2 = copy.deepcopy(griglia)
        #print(griglia2)
        #questo andrebbe messo fuori dal ciclo poiché cosi sarebbe con le coordinate di 
        griglia2[y][x] = prossimo_giocatore(griglia)
        if radice.tipo()=='?':
            radice.lista_figli += [gen_tree(griglia2)]
    #print('RADesiti',radice.esiti(),'\nRADvittorie',radice.vittorie_livello())
    return radice

def somma_tuple(result):
    if celle_vuote(griglia)==[]:
        griglia2 = copy.deepcopy(griglia)
        griglia2[y][x] = prossimo_giocatore(griglia)
        radice.lista_figli += [gen_tree(griglia2)]
        
def prossimo_giocatore(griglia):
    contoX=0
    contoO=0
    for y in range(len(griglia)):
        for x in range(len(griglia[0])):
            if griglia[y][x]=='x':
                contoX+=1
            elif griglia[y][x]=='o':
                contoO+=1
    if contoX==contoO:
        return 'o'
    if contoX<contoO:
        return 'x'

def celle_vuote(griglia):
    vuote = []
    for y in range(3):
        for x in range(3):
            if griglia[y][x] == '': 
                vuote.append((x,y))
    return vuote
'''
def stampa_albero(radice,h=0):
    print (' '*h*4,radice.nome,\
           ' '*h*4,radice.tipo())
    for figlio in radice.lista_figli:
        stampa_albero(figlio,h+1)
    print(radice.esiti())
'''
#stampa_albero(gen_tree([['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]),h=0)
#gen_tree([['x', 'x', 'o'], ['o', '', 'x'], ['x', 'o', 'x']])
