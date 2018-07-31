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
        self.livello=0
        
    def conto_vuoti(self):
        cont=0
        for row in self.nome:
            cont+=row.count("")
        return cont
    
    def spazi_vuoti(self):
        lista=[]
        for y in range(3):
            if "" in self.nome[y]:
                for x in range(3):
                    if self.nome[y][x]=="":
                        lista.append((x,y))
        return lista
    
    def prossima_mossa(self):
        countO=0
        countX=0
        for y in range(3):
            countO+=self.nome[y].count("o")
            countX+=self.nome[y].count("x")
        if countO == countX:
            return "o"
        if countO>countX:
            return "x"
        else:
            return "o"
    
    def tipo(self):
        #check diagonali
        if self.nome[0][0]!="" :
            if self.nome[0][0] == self.nome[1][1] == self.nome[2][2]:
                return self.nome[0][0]
        if self.nome[2][0]!="" :
            if self.nome[2][0] == self.nome[1][1] == self.nome[0][2]:
                return self.nome[2][0]
        #controllo righe
        for y in range(3):
            if self.nome[y].count("x")==3:
                return "x"
            if self.nome[y].count("o")==3:
                return "o"
        #controllo colonne
        for y in range(3):
            if self.nome[0][y]!="":
                if self.nome[0][y] == self.nome[1][y] == self.nome[2][y] :
                    return self.nome[0][y]
        #se nessuno ha vinto controllo se e' patta o in corso
        if self.conto_vuoti()==0:
            return "-"
        else:
            return "?"
       

    def esiti(self):    
        
        patte=0
        oo=0
        xx=0
        
        for figlio in self.lista_figli:
            p1,oo1,xx1 = figlio.esiti()
            patte+=p1
            oo+=oo1
            xx+=xx1
        esito=self.tipo()
        
        if esito=="-" :
            patte+=1
    
        if esito=="o":
            oo+=1
    
        if esito=="x":
            xx+=1
        return (patte,oo,xx)
           
    def vittorie_livello(self, giocatore, h,cont=0):
        if self.livello==h:
            if self.tipo()==giocatore:
                cont+=1
        for figlio in self.lista_figli:
            cont=figlio.vittorie_livello(giocatore,h,cont)
        return cont
    
    def prelevaoutputs(self,listaout=[]):
        for figli in self.lista_figli:
            figli.prelevaoutputs(listaout)
        if self.tipo()!="-" and self.tipo()!="?" :
            listaout.append((self.livello,self.tipo()))
            
        return listaout
    
    def strategia_vincente(self,giocatore):
        lista=self.prelevaoutputs()
        vittorialvlmingioc=()
        vittoriaenemy=()
        for elem1 in lista:
            if elem1[1]==giocatore:
                if vittorialvlmingioc==():
                    vittorialvlmingioc=elem1
                else:
                    if elem1[0]<vittorialvlmingioc[0]:
                        vittorialvlmingioc=elem1
            else:
                if vittoriaenemy==():
                    vittoriaenemy=elem1
                else:
                    if elem1[0]<vittoriaenemy[0]:
                        vittoriaenemy=elem1
        if vittorialvlmingioc[0]<vittoriaenemy[0]:
            return True
        else:
            return False

        
        
def gen_tree(griglia, lvl=0):
    nodo=NodoTris(griglia)
    nodo.livello=lvl
    if nodo.tipo()=="?":
        giocatore=nodo.prossima_mossa()
        
        for coord in nodo.spazi_vuoti():
            appoggio=copy.deepcopy(nodo.nome)
            appoggio[coord[1]][coord[0]]=giocatore
            nodo.lista_figli.append(gen_tree(appoggio,lvl+1))
    return nodo

def printtree(nodo,cont):
    print("   "*cont,nodo.livello, nodo.nome)
    if nodo.lista_figli!=[]:
        for child in nodo.lista_figli:
            printtree(child,cont+1)
