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
        self.possibili = []
    
    def tipo(self):
        '''inserire qui il vostro codice'''
        #RIGHE
        if self.nome[0][0] == self.nome[0][1] and self.nome[0][0] == self.nome[0][2] and self.nome[0][0] != '':
            return self.nome[0][0]
        if self.nome[1][0] == self.nome[1][1] and self.nome[1][0] == self.nome[1][2] and self.nome[1][0] != '':
            return self.nome[1][0]
        if self.nome[2][0] == self.nome[2][1] and self.nome[2][0] == self.nome[2][2] and self.nome[2][0] != '':
            return self.nome[2][0]
        #COLONNE
        if self.nome[0][0] == self.nome[1][0] and self.nome[0][0] == self.nome[2][0] and self.nome[0][0] != '':
            return self.nome[0][0]
        if self.nome[0][1] == self.nome[1][1] and self.nome[0][1] == self.nome[2][1] and self.nome[0][1] != '':
            return self.nome[0][1]
        if self.nome[0][2] == self.nome[1][2] and self.nome[0][2] == self.nome[2][2] and self.nome[0][2] != '':
            return self.nome[0][2]
        #DIAGONALI
        if self.nome[0][0] == self.nome[1][1] and self.nome[0][0] == self.nome[2][2] and self.nome[0][0] != '':
            return self.nome[0][0]
        if self.nome[2][0] == self.nome[1][1] and self.nome[2][0] == self.nome[0][2] and self.nome[2][0] != '':
            return self.nome[2][0]
        #pareggio
        p = True
        for r in self.nome:
            for c in r:
                if c == '':
                    p = False
                    break
        if p == True:
            return '-'
        else:
            return '?'
    
    
    def esiti(self,t=(0,0,0)):
        '''inserire qui il vostro codice'''
        if self.lista_figli == []:
            if self.tipo() == '-':
                t = (t[0]+1,t[1],t[2])
            elif self.tipo() == 'o':
                t = (t[0],t[1]+1,t[2])
            elif self.tipo() == 'x':
                t = (t[0],t[1],t[2]+1)
 
        for figlio in self.lista_figli:
            t = figlio.esiti(t)
        
        return t
        
    
    def vittorie_livello(self, giocatore, h, l = 0, v = 0):
        '''inserire qui il vostro codice'''
        if l == h and self.tipo() == giocatore:
            v += 1
        if l < h:
            for figlio in self.lista_figli:
                v = figlio.vittorie_livello(giocatore,h,l+1,v)
        return v
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        
        

"""g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
def gen_tree(griglia,l = 0,radice = None):
    '''inserire qui il vostro codice'''
    print("livello ",l)
    if radice == None:
        radice = NodoTris(griglia)
        nodo = copy.deepcopy(radice)
    else:
        figlio = NodoTris(griglia)
        radice.lista_figli.append(figlio)
        nodo = copy.deepcopy(figlio)
    x = 0
    o = 0
    
    if nodo.nome[0][0] == nodo.nome[0][1] and nodo.nome[0][0] == nodo.nome[0][2] and nodo.nome[0][0] != '':
        return nodo
    elif nodo.nome[1][0] == nodo.nome[1][1] and nodo.nome[1][0] == nodo.nome[1][2] and nodo.nome[1][0] != '':
        return nodo
    elif nodo.nome[2][0] == nodo.nome[2][1] and nodo.nome[2][0] == nodo.nome[2][2] and nodo.nome[2][0] != '':
        return nodo
    elif nodo.nome[0][0] == nodo.nome[1][0] and nodo.nome[0][0] == nodo.nome[2][0] and nodo.nome[0][0] != '':
        return nodo
    elif nodo.nome[0][1] == nodo.nome[1][1] and nodo.nome[0][1] == nodo.nome[2][1] and nodo.nome[0][1] != '':
        return nodo
    elif nodo.nome[0][2] == nodo.nome[1][2] and nodo.nome[0][2] == nodo.nome[2][2] and nodo.nome[0][2] != '':
        return nodo
    elif nodo.nome[0][0] == nodo.nome[1][1] and nodo.nome[0][0] == nodo.nome[2][2] and nodo.nome[0][0] != '':
        return nodo
    elif nodo.nome[2][0] == nodo.nome[1][1] and nodo.nome[2][0] == nodo.nome[0][2] and nodo.nome[2][0] != '':
        return nodo
    
    for i in range(0,len(nodo.nome)):
        for j in range(0,len(nodo.nome[i])):
            if nodo.nome[i][j] == "x":
                x += 1
            elif nodo.nome[i][j] == "o":
                o += 1
            else:
                nodo.possibili.append((i,j))
    
    if o == x:
        for ramo in nodo.possibili:
            app = copy.deepcopy(griglia)
            app[ramo[0]][ramo[1]] = "o"
            gen_tree(app,l+1,nodo)
    elif o > x and o < 5:
        for ramo in nodo.possibili:
            app = copy.deepcopy(griglia)
            app[ramo[0]][ramo[1]] = "x"
            gen_tree(app,l+1,nodo)
    return nodo"""
    
def controlla(nome):
    if nome[0][0] == nome[0][1] and nome[0][0] == nome[0][2] and nome[0][0] != '':
        return True
    elif nome[1][0] == nome[1][1] and nome[1][0] == nome[1][2] and nome[1][0] != '':
        return True
    elif nome[2][0] == nome[2][1] and nome[2][0] == nome[2][2] and nome[2][0] != '':
        return True
    elif nome[0][0] == nome[1][0] and nome[0][0] == nome[2][0] and nome[0][0] != '':
        return True
    elif nome[0][1] == nome[1][1] and nome[0][1] == nome[2][1] and nome[0][1] != '':
        return True
    elif nome[0][2] == nome[1][2] and nome[0][2] == nome[2][2] and nome[0][2] != '':
        return True
    elif nome[0][0] == nome[1][1] and nome[0][0] == nome[2][2] and nome[0][0] != '':
        return True
    elif nome[2][0] == nome[1][1] and nome[2][0] == nome[0][2] and nome[2][0] != '':
        return True
    return False #non ancora finita

def figli(griglia):
    lista = []
    listaPossibili = []
    n = 0
    x = 0
    o = 0 
    for r in range(0,3):
        for c in range(0,3):
            if griglia[r][c] == 'x':
                x += 1
            elif griglia[r][c] == 'o':
                o += 1
            else:
                n += 1
                listaPossibili.append((r,c))
                
    if x == o:
        for i in range(0,n):
            app = copy.deepcopy(griglia)
            app[listaPossibili[i][0]][listaPossibili[i][1]] = 'o'
            lista.append(app)
    if o > x and o < 5:
        for i in range(0,n):
            app = copy.deepcopy(griglia)
            app[listaPossibili[i][0]][listaPossibili[i][1]] = 'x'
            lista.append(app)
    
    return lista,n

def gen_tree(griglia):
    nodo = NodoTris(griglia)
    if controlla(nodo.nome) == False:
        a,b = figli(nodo.nome)
        for x in range(0,b):
            nodo.lista_figli.append(gen_tree(a[x]))
    return nodo
            
