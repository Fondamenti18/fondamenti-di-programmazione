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
    
    def tipo(self):
        cont=0
        g=self.nome
        x=vittoria(g)
        if x==0:
            for r in g:
                for c in r:
                    if c=="":
                        cont+=1
                        break
            if cont==0: return "-"
            else: return "?"
        else: return x
        
    def esiti(self):

        x,o,pa=0,0,0
        nodo,pa,o,x=scorri_esiti(self,x,o,pa)
        tripla=(pa,o,x)
        return tripla
    
    def vittorie_livello(self, giocatore, h):
        turno=0
        cont=0
        cont=scorri_vittorie_livello(self,giocatore,h,turno,cont)
        return cont
    
    def strategia_vincente(self,giocatore):
        diz={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        diz=genera_diz(self,diz)
        for i in diz:
            for x in diz[i]:
                if (x.tipo()=="x" and giocatore=="o") or (x.tipo()=="o" and giocatore=="x"):
                    return False
                if x.tipo()==giocatore:
                    return True
        return False        
        
def genera_diz(nodo,diz):
    g=nodo.nome
    cont=0
    for r in g:
        for c in g[0]:
            if c=="x" or c=="o":
                cont+=1
    if cont>=5:
        diz[cont]+=[nodo]
    for i in nodo.lista_figli:
        diz=genera_diz(i,diz)
    return diz
   
def scorri_vittorie_livello(nodo,giocatore,h,turno,cont):
    if turno==h and nodo.tipo()==giocatore:
        cont+=1
    if nodo.lista_figli==[]:
        return cont
    
    for i in nodo.lista_figli:
        cont=scorri_vittorie_livello(i,giocatore,h,turno+1,cont)
    return cont

        
def scorri_esiti(nodo,x,o,pa):
    y=False
    if nodo.tipo()=="x":
        x+=1
        y=True
    elif nodo.tipo()=="o":
        o+=1
        y=True
    elif nodo.tipo()=="-":
        pa+=1
        y=True
    if nodo.lista_figli==[] or y==True:
        return nodo,pa,o,x
    for i in nodo.lista_figli:
        nodo,pa,o,x=scorri_esiti(i,x,o,pa)
    return nodo,pa,o,x
        
        
def vittoria(g):
        if (g[0][2]==g[1][2]==g[2][2] or g[2][0]==g[2][1]==g[2][2]) and (g[2][2]=="o" or g[2][2]=="x"):
            return g[2][2]
        if (g[0][1]==g[1][1]==g[2][1] or g[1][0]==g[1][1]==g[1][2] or g[0][0]==g[1][1]==g[2][2] or g[2][0]==g[1][1]==g[0][2]) and (g[1][1]=="x" or g[1][1]=="o"):
            return g[1][1]
        if (g[0][0]==g[1][0]==g[2][0] or g[0][0]==g[0][1]==g[0][2]) and (g[0][0]=="x" or g[0][0]=="o"):
            return g[0][0]
        return 0
   
def gen_tree(griglia):
    n=0
    nodo=NodoTris(griglia)
    genera(nodo,n,0)
    #stampa(nodo)
    return nodo
    
    
def genera(nodo,n,ins):
    l=[]
    es=[]
    righe=len(nodo.nome)
    colonne=len(nodo.nome[0])
    if n==0:
        contx,conto=0,0
        for riga in range(righe):
            for colonna in range(colonne):
                if nodo.nome[riga][colonna]=="x":
                    contx+=1
                elif nodo.nome[riga][colonna]=="o":
                    conto+=1
        if conto>contx:
            ins="x"
        else:
            ins="o"
            
    for riga in range(righe):
        for colonna in range(colonne):
            if nodo.nome[riga][colonna]=="":
                es+=[(riga,colonna)]
   
    for i in es:
        r,c=i[0],i[1]
        g=deepcopy(nodo.nome)
        g[r][c]=ins
        l+=[g]
        nodo.lista_figli+=[g]
    for i in range(len(l)):
        nodo.lista_figli[i]=NodoTris(l[i])
    for i in nodo.lista_figli:
        if ins=="x" and i.tipo()!="x":
            genera(i,n+1,"o")
        if ins=="o" and i.tipo()!="o":
            genera(i,n+1,"x")
    
'''def stampa(nodo):
    if nodo.lista_figli==[]:
        return nodo
    print("***")
    print(nodo.nome)
    print("***")
    print("---")
    for i in nodo.lista_figli:
        print(i.nome)
    print("---")
    
    for i in nodo.lista_figli:
        stampa(i)
    return nodo

nodo=gen_tree([['o', 'o', 'x'], ['o', 'x', 'x'], ['', '', '']])
stampa(nodo)
print(nodo.esiti())'''

'''def main():
    a=gen_tree([["","",""],["","",""],["","",""]])
    for i in a.lista_figli:
        print(i.nome)

main()'''
