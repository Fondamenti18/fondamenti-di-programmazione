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

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        try:
            a=self.nome
        except AttributeError:
            a=self
        v='-'
        for x in a:
            if x[0]==x[1]==x[2] and x[0]!= '':
                v=x[0]
                return v
        for k in range(3):
            z=a[0][k]
            c=0
            for w in a:
                if w[k]==z and w[k]!='':
                    c+=1
                z=w[k]
                if c==3:
                    v=z
                    return v
        if (a[0][0]==a[1][1]==a[2][2] or a[0][2]==a[1][1]==a[2][0]) and a[1][1]!='':
            v=a[1][1]
            return v
        for x in a:
            if '' in x:
                v='?'
                return v
        return v
    
    def figli(self,lista):
        from copy import deepcopy
        co=cx=0
        a=self.nome
        self.lista_figli=[]
        if NodoTris.tipo(a)=='?':
            for x in a:
                if '' in x:
                    b=x.count('')
                    for k in x:
                        cx=cx+k.count('x')
                        co=co+k.count('o')
                    if cx>=co:
                        i=x.index('')
                        while b>0:
                            x[i]='o'
                            d1=deepcopy(a)
                            self.lista_figli+=[d1]
                            x[i]=''
                            try:
                                i=x.index('',i+1)
                            except ValueError:
                                b=0
                            b-=1
                    else:
                        i=x.index('')
                        while b>0:
                            x[i]='x'
                            d1=deepcopy(a)
                            self.lista_figli+=[d1]
                            x[i]=''
                            try:
                                i=x.index('',i+1)
                            except ValueError:
                                b=0
                            b-=1
            for w in self.lista_figli:
                lista.append(w)
                g=NodoTris(w)
                NodoTris.figli(g,lista)
            return lista
        
    def esiti(self):
        lista=[]
        tp=to=tx=0
        L=NodoTris.figli(self,lista)
        if L!=None:
            for k in L:
                q=NodoTris(k)
                esito=NodoTris.tipo(q)
                if esito=='-':
                    tp+=1
                elif esito=='o':
                    to+=1
                elif esito=='x':
                    tx+=1
            return(tp,to,tx)
        else:
            if NodoTris.tipo(self)=='x' or NodoTris.tipo(self)=='o' or NodoTris.tipo(self)=='-':
                if NodoTris.tipo(self)=='x':
                    tx+=1
                if NodoTris.tipo(self)=='o':
                    to+=1
                if NodoTris.tipo(self)=='-':
                    tp+=1
            return(tp,to,tx)

            
    
    def vittorie_livello(self, giocatore, h):
        lista=[]
        livelli={}
        c=c1=0
        L=NodoTris.figli(self,lista)
        if L!=None and h!=0:
            for k in L:
                c=0
                for w in k:
                    j=k.index(w)
                    i=0
                    for z in w:
                        i=w.index(z,i)
                        if z!=self.nome[j][i]:
                            c+=1
                try:
                    livelli[c].append(k)
                except KeyError:
                    livelli[c]=[k]
            try:
                for k1 in livelli[h]:
                    esito=NodoTris.tipo(k1)
                    if esito==giocatore:
                        c1+=1
                return c1
            except KeyError:
                return 0
        else:
            if NodoTris.tipo(self)==giocatore:
                return 1
            else:
                return 0
    
    def strategia_vincente(self,giocatore):
        h=0
        for k in self.nome:
            for w in k:
                if w=='':
                    h+=1
        if NodoTris.vittorie_livello(self,giocatore,h)>0:
            return True
        else:
            return False
        
def gen_tree(griglia):
    lista=[]
    nodo=NodoTris(griglia)
    l_figli=NodoTris.figli(nodo,lista)
    
    return nodo
