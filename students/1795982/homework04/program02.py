'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3×3 caselle.
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
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        '''inserire qui il vostro codice'''
        for x in range(3):
            if self.nome[x][0]==self.nome[x][1]==self.nome[x][2]:
                if self.nome[x][0]=='x':
                    return 'x'
                if self.nome[x][0]=='o':
                    return 'o'
        for y in range(3):
            if self.nome[0][y]==self.nome[1][y]==self.nome[2][y]:
                if self.nome[0][y]=='x':
                    return 'x'
                if self.nome[0][y]=='o':
                    return 'o'
        if self.nome[0][0]==self.nome[1][1]==self.nome[2][2]:
            if self.nome[0][0]=='x':
                return 'x'
            if self.nome[0][0]=='o':
                return 'o'
        if self.nome[0][2]==self.nome[1][1]==self.nome[2][0]:
            if self.nome[0][2]=='x':
                return 'x'
            if self.nome[0][2]=='o':
                return 'o'
        for x in  range(3):
            for y in range(3):
                if self.nome[x][y]=='':
                    return '?'
        return '-'
        
                
    def esiti(self):
        '''inserire qui il vostro codice'''
        tipo=self.tipo()
        if tipo=='-':
            return(1,0,0)
        if tipo=='o':
            return(0,1,0)
        if tipo=='x':
            return(0,0,1)
        lista=[0,0,0]
        for figlio in self.lista_figli:
            esito=figlio.esiti()
            lista[0]+=esito[0]
            lista[1]+=esito[1]
            lista[2]+=esito[2]
        return tuple(lista)
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        if h==0:
            if self.tipo()==giocatore:
                return 1
            else:
                return 0
        vittorie=0
        for figlio in self.lista_figli:
            vittorie+=figlio.vittorie_livello(giocatore,h-1)
        return vittorie
            
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        
def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    radice=NodoTris(griglia)
    if radice.tipo()!='?':
        return radice
    cont_x=0
    cont_o=0
    for x in radice.nome:
        for i in x:
            if i=='o':
                cont_o+=1
            if i=='x':
                cont_x+=1
    prossimo=None
    if cont_o>cont_x:
        prossimo='x'
    else:
        prossimo='o'
    lista=[]
    for x in range(3):
        for i in range(3):
            if radice.nome[x][i]=='':
                copiagriglia=copy.deepcopy(griglia)
                copiagriglia[x][i]=prossimo
                lista.append(gen_tree(copiagriglia))
    radice.lista_figli=lista
    return radice
    
    
    
