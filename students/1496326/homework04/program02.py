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
        self.nodiVittoria = set()
        
    
    def tipo(self):
        griglia = self.nome
        for cell in range(0, len(griglia)):
            #controllo orizzontale
            if griglia[cell][0] == 'x' and griglia[cell][1] == 'x' and griglia[cell][2] == 'x':
                return 'x'
            elif griglia[cell][0] == 'o' and griglia[cell][1] == 'o' and griglia[cell][2] == 'o':
                return 'o'
            #controllo verticale
            elif griglia[0][cell] == 'x' and griglia[1][cell] == 'x' and griglia[2][cell] == 'x':
                return 'x'
            elif griglia[0][cell] == 'o' and griglia[1][cell] == 'o' and griglia[2][cell] == 'o':
                return 'o'
        #controllo diagonale
        if griglia[0][0] == 'x' and griglia[1][1] == 'x' and griglia[2][2] == 'x':
            return 'x'
        elif griglia[0][0] == 'o' and griglia[1][1] == 'o' and griglia[2][2] == 'o':
            return 'o'
        elif griglia[2][0] == 'x' and griglia[1][1] == 'x' and griglia[0][2] == 'x':
            return 'x'
        elif griglia[2][0] == 'o' and griglia[1][1] == 'o' and griglia[0][2] == 'o':
            return 'o'
        
        #nessun vincitore controllo celle libere
        for row in range(0, len(griglia)):
            for col in range(0, len(griglia)):
                if griglia[row][col] == '':
                    return '?'
            
        return '-'
            
    def esiti(self):
        
        mappaEsiti = {'-' : 0, 'o' : 0, 'x' : 0, 'nodi' : 0}
        
        finaliPossibili(self, mappaEsiti)
        #print('nodi:' + str(mappaEsiti['nodi']))
        esiti = (mappaEsiti['-'], mappaEsiti['o'], mappaEsiti['x'])
        #print(esiti)
        return esiti
        
    def vittorie_livello(self, giocatore, h):
        #print('starting vittorie livello with h[' + str(h) + ']')
        vittorie = 0
        vittorie = vittoriePossibiliInH(self, giocatore, 0, h);
        return vittorie
    
    def strategia_vincente(self,giocatore):
        print(str(self.nome[0]) + ' ' + str(self.nome[1]) + ' ' +str(self.nome[2]))
        vittorie = False
        mosse = 10;
        vittorie, mosse = vittoriePossibili(self, giocatore, vittorie, mosse)
        print(vittorie)
        return vittorie
        
def gen_tree(griglia):
    mappaEsiti = {'nodi' : 0}
    nodo = NodoTris(griglia)
    player = startingPlayer(griglia)
    if player != '':
        updateGriglia(nodo, player, mappaEsiti)
    
    #print(mappaEsiti['nodi'])
    return nodo

def updateGriglia(padre, player, mappaEsiti):
    mappaEsiti['nodi'] += 1
    griglia = padre.nome
    for row in range(0, len(griglia)):
        for col in range(0, len(griglia)):
            if griglia[row][col] == '':
                nuovaGriglia = copy.deepcopy(griglia)
                nuovaGriglia[row][col] = player
                nodo = NodoTris(nuovaGriglia)
                padre.lista_figli.append(nodo)
                #print(nodo.nome[0],nodo.nome[1],nodo.nome[2])
                #print(nodo.tipo())
                if(nodo.tipo() == '?'):
                    #print(str(nodo.nome[0]) + ' ' + str(nodo.nome[1]) + ' ' +str(nodo.nome[2]))
                    updateGriglia(nodo, netx(player), mappaEsiti)
    
def finaliPossibili(nodo, mappaEsiti):
    #print('entro')
    mappaEsiti['nodi'] += 1
    if len(nodo.lista_figli) > 0:
        for figlio in nodo.lista_figli:
            finaliPossibili(figlio, mappaEsiti)
    else:
         winner = nodo.tipo()
         #print(nodo.nome[0],nodo.nome[1],nodo.nome[2])
         mappaEsiti[winner] += 1
    

def vittoriePossibili(nodo, player, vittorie, mosse):
    print(mosse)
    if len(nodo.lista_figli) > 0:
        for figlio in nodo.lista_figli:
               vittorie, mosse = vittoriePossibili(figlio, player, vittorie, mosse)
    
    elif nodo.tipo() != '?' and nodo.tipo() != '-':
        if celleLibere(nodo.nome) < mosse:
            mosse = celleLibere(nodo.nome)
            if player == nodo.tipo():
                #print('True per mosse:' + str(mosse))
                vittorie = True
            else:
                #print('False per mosse:' + str(mosse))
                vittorie = False
    return vittorie, mosse

# =============================================================================
# def vittoriePossibili(nodo, player, vittorie):
#     #print('entro')
#     if len(nodo.lista_figli) > 0:
#         for figlio in nodo.lista_figli:
#                vittorie = vittoriePossibili(figlio, player, vittorie)
#             #elif player == nodo.tipo():
#              #   print('vittoria trovata 2')
#               #  vittorie = True
#     elif player == nodo.tipo():
#         print('vittoria trovata')
#         vittorie = True
#     
#     return vittorie
# =============================================================================

def vittoriePossibiliInH(nodo, player, vittorie, h):
    #print('entro')
    #print(len(nodo.lista_figli))
    #print(str(nodo.nome[0]) + ' ' + str(nodo.nome[1]) + ' ' +str(nodo.nome[2]))
    #print('tipo:' + str(nodo.tipo()) + ' plaer:' + str(player) + ' h:' + str(h))
    if h > 0:
        if(len(nodo.lista_figli) > 0):
            for figlio in nodo.lista_figli:
                   vittorie = vittoriePossibiliInH(figlio, player, vittorie, h-1)
    elif h == 0:
        if player == nodo.tipo():
            vittorie +=1
            
    return vittorie

def netx(player):
    if player == 'x':
        return 'o'
    if player == 'o':
        return 'x'

def celleLibere(griglia):
    freeCell = 0
    for row in range(0, len(griglia)):
        for col in range(0, len(griglia)):
            if griglia[row][col] == '':
                freeCell += 1
    return freeCell

def startingPlayer(griglia):
    
    freeCell = celleLibere(griglia)
                
    if freeCell == 0:
        #print('game ended')
        return ''            
    elif freeCell%2 == 0:
        #print('Player X move')
        return 'x'
    else:
        #print('Player O move')
        return 'o'
    
# =============================================================================
# matrix = [['' for x in range(3)] for y in range(3)]
# print(matrix)
# nodo = gen_tree(matrix)        
# =============================================================================
