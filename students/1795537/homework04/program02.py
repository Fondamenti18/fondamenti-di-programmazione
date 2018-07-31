'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3Ã—3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo 
(un giocatore ha come simbolo una "o" e l'avversario una 'x'). 
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta 
orizzontale, verticale o diagonale. Se la griglia viene riempita 
senza che nessuno dei giocatori sia riuscito a completare una linea 
retta di tre simboli, il gioco finisce in paritÃ . Nel caso in cui il gioco 
finisse in paritÃ , la partita Ã¨ detta "patta". 
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
Piu' precisamente: il primo elemento della tripla  Ã¨ il numero di  patte possibili, 
il secondo Ã¨ il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento 
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
#--------------------------------------------------------------------dichiarazione classe-------------------------------------------------------------------# 
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.esito = '-'
    
    def tipo(self):
        '''returno l'esito di un nodo dato'''
        return self.esito
            
    def esiti(self):
        '''dato un nodo, returno una tupla contenente il numero di patte, vittorie per x e o che si ottengono partendo da quella configurazione'''
        patta = 0
        vitto = 0
        vittx = 0
        ris = trovaEsiti(self, patta, vitto, vittx)
        return ris
        
    def vittorie_livello(self, giocatore, h):
        '''conto quante volte può vincere un determinato giocatore dopo h mosse, h rappresenta anche il livello dell'albero'''
        diz = {}
        for lvl in range(h+1):
            diz[lvl] = 0
        diz = trovaLivelliEsiti(self, diz, giocatore, h)
        ris = list(diz.values())
        return(ris[-1])
    
    def strategia_vincente(self,giocatore):
        a = trovaStrategiaVincente(self, giocatore)
        return (a)
        
        

def trovaStrategiaVincente(nodo, giocatore, lvl=0):
    ris= []
    car, ag = inizio(nodo.nome)
#    ag = car + '?'
    ag += '-'
#    print('-'*lvl, nodo.esito)
    if car == giocatore :
#        for figlio in nodo.lista_figli:
#            print('-'*lvl,figlio.esito)
            if nodo.esito == giocatore:
#                print(figlio.esito, giocatore, car, ag)
                return True
            if nodo.esito in ag:
                return(False)
    else:
#        for figlio in nodo.lista_figli:
#            print('-'*lvl,figlio.esito)
            if nodo.esito in car+'-' : 
#                print(figlio.esito, giocatore, car, ag)
                return(False)
            if nodo.esito == giocatore:
                return(True)        
    for figlio in nodo.lista_figli:
        return(trovaStrategiaVincente(figlio, giocatore, lvl+1))
        

#--------------------------------------------------------------------trova livelli esiti--------------------------------------------------------------------#
def trovaLivelliEsiti(nodo, diz, giocatore, h, lvl=0):
    '''fino a quando non supero il livello richiesto conto quante possibilità si hanno di pareggiare o vittoria i giocatori a ogni livello'''
    if lvl < h+1 :
        if nodo.esito == giocatore:
            diz[lvl] += 1
        for figlio in nodo.lista_figli:
            diz = trovaLivelliEsiti(figlio, diz, giocatore, h , lvl+1)
    return diz





#------------------------------------------------------------------------trova esiti------------------------------------------------------------------------#
def trovaEsiti(nodo, patta, vitto, vittx):
    '''incremento il numero di patte/vittorie per giocatore, partendo dal nodo dato fino alle sue foglie'''
    if nodo.esito == '-' : patta += 1
    elif nodo.esito == 'o' : vitto += 1
    elif nodo.esito == 'x' : vittx += 1
    for figlio in nodo.lista_figli:
        patta, vitto, vittx = trovaEsiti(figlio, patta, vitto, vittx)
    return (patta, vitto, vittx)





#-----------------------------------------------------------------------trova simbolo-----------------------------------------------------------------------#     
def inizio(griglia):
    '''trovo il prossimo segno da inserire nella griglia'''
    o = 0
    x = 0
    for el in griglia:
        o += el.count('o')
        x += el.count('x')
    if x==o : return ('o', 'x')
    return ('x', 'o')
     



       
#--------------------------------------------------------------------controlli caso base--------------------------------------------------------------------#   
def cellepiene(griglia, nodo):
    '''controllo se nella griglia ci sono celle ancora vuote'''
    for riga in griglia:
        if '' in riga : 
            nodo.esito = '?'
            return (False)
    return(True)
    
def controlloVittoriaV(griglia, nodo):
    '''controllo se c'è stata una vittoria verticale e memorizzo il vincitore in esito'''
    if griglia[0][0] == griglia[1][0] == griglia[2][0] and griglia[0][0] != '': 
        nodo.esito = griglia[0][0]
        return (True)
    elif griglia[0][1] == griglia[1][1] == griglia[2][1] and griglia[0][1] != '': 
        nodo.esito = griglia[0][1]
        return (True)
    elif griglia[0][2] == griglia[1][2] == griglia[2][2] and griglia[0][2] != '': 
        nodo.esito = griglia[0][2]
        return (True)
    return (False)
        
def controlloVittoriaO(griglia, nodo):
    '''controllo se c'è stata una vittoria orizzontale e memorizzo il vincitore in esito'''
    if griglia[0][0] == griglia[0][1] == griglia[0][2] and griglia[0][0] != '': 
        nodo.esito = griglia[0][0]
        return (True)
    elif griglia[1][0] == griglia[1][1] == griglia[1][2] and griglia[1][0] != '': 
        nodo.esito = griglia[1][0]
        return (True)
    elif griglia[2][0] == griglia[2][1] == griglia[2][2] and griglia[2][0] != '': 
        nodo.esito = griglia[2][0]
        return (True)
    return (False)
    
def controlloVittoriaT(griglia, nodo):
    '''controllo se c'è stata una vittoria trasversale e memorizzo il vincitore in esito'''
    if griglia[0][0] == griglia[1][1] == griglia[2][2] and griglia[0][0] != '': 
        nodo.esito = griglia[0][0]
        return (True)
    elif griglia[0][2] == griglia[1][1] == griglia[2][0] and griglia[0][2] != '': 
        nodo.esito = griglia[0][2]
        return (True)
    return (False)
    
def vittoria(griglia, nodo):
    '''richiamo le 3 funzioni di controllo vittoria in modo da ottenere un unico esito complessivo'''
    if controlloVittoriaT(griglia, nodo) or controlloVittoriaO(griglia, nodo) or controlloVittoriaV(griglia, nodo): return(True)
    
    
    
    
    
#-----------------------------------------------------------------------genero albero-----------------------------------------------------------------------#

def gen_tree(griglia, lvl=1):
    '''controllo se il nodo fa parte dei casi base, altrimenti ricorsivamente creo e controllo i vari figli'''
    nodo = NodoTris(griglia)
    if vittoria(nodo.nome, nodo) or cellepiene(nodo.nome, nodo): 
        return nodo
    car, _ = inizio(nodo.nome)
    for posr, riga in enumerate(griglia):
        for posc, cella in enumerate(griglia[posr]):
            if cella == '':
                copia = copy.deepcopy(nodo.nome)
                copia[posr][posc] = car
                nodo.lista_figli.append((gen_tree(copia, lvl+1)))
    return nodo       
            
