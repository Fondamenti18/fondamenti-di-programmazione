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
            player='o'
            #---print('controllo orizzontale o')
            c=0
            for sub_l in self.nome:
                if c==3: return player
                c=0
                for db_sub_l in sub_l:
                    #print(db_sub_l,c)
                    if db_sub_l==player:
                         c+=1
            #---print('controllo verticale o')
            for fix_pl in range(0,3):
                #---print('azz c',c)
                c=0
                for check in range(0,3):
                    #---print(self.nome[check][fix_pl],'==',player)
                    if self.nome[check][fix_pl]==player:
                        c+=1
                        #---print('c inc',c)
                if c==3: return player
            #---print('controllo diagonale sx->dx o')
            c=0
            for _ in range(0,3):
               if self.nome[_][_]==player: c+=1
            if c==3: return player

            #---print('controllo diagonale dx->sx o')
            w=2
            c=0
            for _ in range(0,3):
                if self.nome[_][w]==player: c+=1
                w-=1
            if c==3: return player

            return(self.check_player2('o'))

            '''print('controllo parita')
            patta=True
            for sub_l in self.nome:
                for db_sub_l in sub_l:
                    if db_sub_l=='': patta=False
            if patta==True: return '-'



            print('running')
            #restituisce '?' se la partita è ancora in esecuzione
            return '?   '''

    def check_player2(self,player):
        player='x'
        #---print('controllo orizzontale x')
        c=0
        for sub_l in self.nome:
            if c==3: return player
            c=0
            for db_sub_l in sub_l:
                #print(db_sub_l,c)
                if db_sub_l==player:
                     c+=1
        #---print('controllo verticale x')
        for fix_pl in range(0,3):
            #---print('azz c',c)
            c=0
            for check in range(0,3):
                #---print(self.nome[check][fix_pl],'==',player)
                if self.nome[check][fix_pl]==player:
                    c+=1
                    #---print('c inc',c)
            if c==3: return player

        #---print('controllo diagonale sx->dx x')
        c=0
        for _ in range(0,3):
           if self.nome[_][_]==player: c+=1
        if c==3: return player

        #---print('controllo diagonale dx->sx x')
        w=2
        c=0
        for _ in range(0,3):
            if self.nome[_][w]==player: c+=1
            w-=1
        if c==3: return player

        #---print('controllo parita ')

        stop=False
        for sub_l in self.nome:
            for db_sub_l in sub_l:
                if db_sub_l=='':
                    stop=True
                    break
            if stop==True: break
        if stop==False: return '-'


        '''patta=True
        for sub_l in self.nome:
            for db_sub_l in sub_l:
                if db_sub_l=='': patta=False
        if patta==True: return '-'''



        #---print('running')
        #restituisce '?' se la partita è ancora in esecuzione
        return '?'  #richiamata da tipo() #richiamata da tipo()



    def esiti(self):
        '''inserire qui il vostro codice'''
        if self.lista_figli==[]:
            if self.tipo()=='x': return (0,0,1)
            if self.tipo()=='o': return (0,1,0)
            if self.tipo()=='-': return (1,0,0)

        res=self.check_res((0,0,0))
        return res
        #print('ris',res)

    def check_res(dad,triple):
        #print('\nenrtro con triple',triple)
        tie,w_o,w_x=triple

        for child in  dad.lista_figli:
            #print('in check',child.nome)
            res=child.tipo()
            if res=='?':
                #---print('?')
                tie,w_o,w_x=triple
                triple=child.check_res((tie,w_o,w_x))
            if res=='o':
                #---print('o')
                tie,w_o,w_x=triple
                triple=child.check_res((tie,w_o+1,w_x))
            if res=='x':
                #---print('x')
                tie,w_o,w_x=triple
                #print('triplediora',triple)
                triple=child.check_res((tie,w_o,w_x+1))
            if res=='-':
                #---print('')
                tie,w_o,w_x=triple
                triple=child.check_res((tie+1,w_o,w_x))
        #print('ritorno triple',triple)
        return triple #richiamata da esiti()

    def num_livelli(self,giocatore,h,level,win_player):
        if h==0 and self.tipo()==giocatore:
            win_player=0
            return win_player

        for child in self.lista_figli:
            #---print(child.nome,'vince',giocatore,'-',level,'=',h)
            if child.tipo()==giocatore and level==h:
                win_player+=1
                #print('incrementato',win_player)
            win_player=child.num_livelli(giocatore,h,level+1,win_player)

        return win_player #richiamata da vittorie_livello()

    def vittorie_livello(self, giocatore, h):
        print('VITTORIE LIVELLO')
        '''inserire qui il vostro codice'''
        res=self.num_livelli(giocatore,h,1,0)
        print(res)
        return res

    def strategia_vincente1(self,giocatore,ag_player,vinc):   #richiamata da strategia_vincente()
        #print('entro con',self.nome)
        c=True
        win_giocatore=False
        for child in self.lista_figli: #per ogni figlio in listafigli del padre
            if child.tipo()==ag_player:  #se il figlio ha un tris di vs player
                c=False
            if child.tipo()==giocatore: #se il figlio ha un tris di I_player
                win_giocatore=True
        if c==False: return False
        if c==True:
            if win_giocatore==True: return True
            else:
                for child in self.lista_figli: #per ogni figlio in listafigli del padre
                    vinc=child.strategia_vincente1(giocatore,ag_player,vinc)
        return vinc

    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        if giocatore=='x': ag_player='o'
        if giocatore=='o': ag_player='x'
        res=self.strategia_vincente1(giocatore,ag_player,False)
        print('prova strategia',res)

        return res



def create_child(grid,state,level):
    nodo=NodoTris(grid)
    ##print(nodo.nome,'>',nodo.tipo())#importante for debug
    for sub_l in grid:#scorro lista sub
        #print(sub_l)
        c=0
        for db_sub_l in sub_l: #scorro carattere lista sub
            #print('itero',db_sub_l)
            if ''==db_sub_l:    #se il carattere è '' allora...
                if state==True:
                    next_grid=copy.deepcopy(grid)
                    next_grid[grid.index(sub_l)][c]='o'
                    #print('creato o',next_grid)
                    if nodo.tipo()=='?':
                        nodo.lista_figli.append(create_child(next_grid,False,level))
                else:
                    next_grid=copy.deepcopy(grid)
                    next_grid[grid.index(sub_l)][c]='x'
                    #print('creato x',next_grid)
                    if nodo.tipo()=='?':
                        nodo.lista_figli.append(create_child(next_grid,True,level))

            c+=1
    #print('nodo',nodo)
    return nodo  #crea lista_figli per ogni nodo padre, lista di nodi


def print_tree(nodo,level):
    for child in nodo.lista_figli:
        #if child!=None:  #perchè creava child di nonetype
        print(' '*level*2,child.nome)
        #if child.lista_figli==[]: print('pappppppppa')
        print_tree(child,level+1)

def _1_player2move(grid):
    c=0
    for sub_l in grid:
        c+=sub_l.count('')
    app=c%2
    #print('app',app)
    if c%2==0:
        player=False
    else:
        player=True
    return player

def gen_tree(griglia):
    player=_1_player2move(griglia)#funziona per capire chi inizia
    #print('play',player)
    radice=create_child(griglia,True,1) #crea albero


    print('\n\n\n ALBERO CREATO')
    #print('rad--\n',radice.nome)
    #---------print_tree(radice,1)    #stampa albero
    #print('\n')
    #----res=prova.tipo() #prpva di tipo()
    #----radice.vittorie_livello('o',3)   #prova di vittorie_livello
    #----res=radice.esiti()   #prova di esiti()
    #print(res)
    #return radice
    #----radice.strategia_vincente('o')   #prova di strategie vincenti
    return radice
    '''prove di tipo()
    prova=NodoTris([['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', 'o']])
    res=prova.tipo()
    print('\nres->',res)'''


g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
gen_tree(g1)
