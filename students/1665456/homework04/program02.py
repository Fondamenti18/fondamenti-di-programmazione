# -*- coding: utf-8 -*-
'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3x—3 caselle.
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
        self.lista_figli = [] #lista dei nodi figli
        self.CountO=0
        self.CountX=0
        self.CountN=0
        self.winner=""
        
        
        turno=""
        for x in griglia:
            u=x.count("x")
            v=x.count("o")
            self.CountX=self.CountX+u
            self.CountO=self.CountO+v
            
        self.CountN=9-(self.CountO+self.CountX)
        if self.CountO==self.CountX:
            turno="o"
        else:
            turno="x"
        
        for y in range(len(griglia)):
            
            for z in range(len(griglia[y])):
                griglia1=griglia
                if griglia[y][z]=="":
                    griglia1[y][z]=turno
                self.lista_figli.append(griglia1)
                
        
        
        if griglia[0][0] == griglia[0][1] and griglia[0][1] == griglia[0][2]:
            self.winner=griglia[0][0]
        elif griglia[2][0] == griglia[2][1] and griglia[2][1] == griglia[2][2]:
            self.winner=griglia[2][0]
        elif griglia[0][0] == griglia[1][0] and griglia[1][0] == griglia[2][0]:
            self.winner=griglia[0][0]
        elif griglia[0][0] == griglia[1][1] and griglia[1][1] == griglia[2][2]:
            self.winner=griglia[0][0]
        elif griglia[2][2] == griglia[1][2] and griglia[1][2] == griglia[0][2]:
            self.winner=griglia[2][2]
        elif griglia[2][1] == griglia[1][1] and griglia[1][1] == griglia[0][1]:
            self.winner=griglia[2][1]
        elif griglia[2][0] == griglia[1][1] and griglia[1][1] == griglia[0][2]:
            self.winner=griglia[2][0]
        elif griglia[1][0] == griglia[1][1] and griglia[1][1] == griglia[1][2]:
            self.winner=griglia[1][0]
        
        
        
                    
            
    
    def tipo(self):
        '''inserire qui il vostro codice'''
        if self.winner=="x":
            return("x")
        elif self.winner=="o":
            return("o")
        elif self.winner=="" and self.CountN==0:
            return("-")
        else:
            return("?")
        
        
        
        
    def esiti(self):
        '''inserire qui il vostro codice'''
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
    

def creagen_tree(s):
    if s.CountN==0 or s.winner!="":
        return(s)
    else:
        for x in s.lista_figli:
            creagen_tree(x)
    
def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    
    listafoglie=[]
    s=NodoTris(griglia)
    for t in s.lista_figli:
        y=creagen_tree(t)
        if y not in listafoglie:
            listafoglie.append(y)
    print(listafoglie)
    
    
    
    
#gen_tree([['', '', ''], ['', '', ''], ['', '', '']])
gen_tree([['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']])
    
