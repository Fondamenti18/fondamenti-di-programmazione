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

import ast

#provare a fare una iterazione con dentro una ricorsione per generare tutti i nodi dell'albero

class NodoTris:
    def __init__(self, griglia,X=0,O=0,P=0):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.X=0
        self.O=0
        self.P=0
    
    def tipo(self):
        result = victory(self.nome)
        return result
        
    def esiti(self):
        k = self
        prova(self,k)
        return (self.P,self.O,self.X)
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        
    def update_x(self,val,x,y):
        self.nome[x][y] = val
        
    def add_nodo(self, new_nodo):
        self.lista_figli.append(new_nodo)
        
    def __str__(self):
        return str(self.nome)
    
    def __repr__(self):
        return self.__str__()
    
    def somma(self,j,X=0,O=0,P=0):
        if j == 'x':
            self.X+=1
        elif j == 'o':
            self.O+=1
        elif j == '-':
            self.P+=1

def victory(stato):
    if (stato[0][0] == stato[1][1] == stato[2][2]) and stato[0][0]!='':
        return stato[0][0]
    if (stato[2][0] == stato[1][1] == stato[0][2]) and stato[2][0]!='':
        return stato[2][0]
    if (stato[0][0] == stato[1][0] == stato[2][0]) and stato[0][0]!='':
        return stato[0][0]
    if (stato[0][1] == stato[1][1] == stato [2][1]) and stato[0][1]!='':
        return stato[1][0]
    if (stato[0][2] == stato[1][2] == stato[2][2]) and stato[0][2]!='':
        return stato[0][2]
    if (stato[0][0] == stato[0][1] == stato[0][2]) and stato[0][0]!='':
        return stato[0][0]
    if (stato[1][0] == stato[1][1] == stato[1][2]) and stato[1][0]!='':
        return stato[1][0]
    if (stato[2][0] == stato[2][1] == stato[2][2]) and stato[2][0]!='':
        return stato[2][0],
    for x in range(0,3):
        for y in range(0,3):
            if stato[x][y]== '':
                return '?'
    else:
        return '-'

def gameover2(stato):
    for x in range(0,3):
        for y in range(0,3):
            if stato[x][y]!='x' or stato[x][y]!='o':
                return False
    return True

def turn(stato):
    xc=0
    oc=0
    for x in range(0,3):
        for y in range(0,3):
            if stato[x][y]=='x':
                xc+=1
            elif stato[x][y]=='o':
                oc+=1
    if xc>oc:
        return 'o'
    elif oc>xc:
        return 'x'
    elif oc==xc:
        return 'o'

def ska(griglia,n1,orig):
    g1 = ast.literal_eval(str(n1.nome))
    check = victory(g1)
    check2 = gameover2(g1)
    if check == True or check2 == True:
        return None
    val = turn(g1)
    for x in range(0,3):
        for y in range(0,3):
            if n1.nome[x][y] == '':
                g1 = ast.literal_eval(str(n1.nome))
                g1[x][y]=val
                new_nodo = NodoTris(g1)
                n1.add_nodo(new_nodo)
                b = n1.lista_figli[-1]
                ska(griglia,b,orig)
                
def prova(n1,k):
    g1 = ast.literal_eval(str(n1.nome))
    check = victory(g1)
    if check == 'x':
        k.somma(check)
    if check == 'o':
        k.somma(check)
    if check == '-':
        k.somma(check)
    check2 = gameover2(g1)
    if check == 'x' or check == 'o' or check == '-' or check2 == True:
        return None
    val = turn(g1)
    for x in range(0,3):
        for y in range(0,3):
            if n1.nome[x][y] == '':
                g1 = ast.literal_eval(str(n1.nome))
                g1[x][y]=val
                new_nodo = NodoTris(g1)
                n1.add_nodo(new_nodo)
                b = n1.lista_figli[-1]
                prova(b,k)
                    

def gen_tree(griglia):

    orig = griglia
    n1 = NodoTris(griglia)
    ska(griglia,n1,orig)
    return n1
