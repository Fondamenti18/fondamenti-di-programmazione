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
from copy import deepcopy


def trova_esiti(radice,lista):
    if radice.situazione=='-':lista[0]+=1
    elif radice.situazione=='o':lista[1]+=1
    elif radice.situazione=='x':lista[2]+=1
    else:
        for r in radice.lista_figli:
            trova_esiti(r,lista)


def trova_vittorie_livello(radice,g,h,lista):
    if radice.livello<h:
        for r in radice.lista_figli:
            trova_vittorie_livello(r,g,h,lista)
    elif radice.livello==h and radice.situazione==g:lista[0]+=1


def strategiaV(radice,g):
    tot=True
    ntot=False
    if g=='o':
        if radice.situazione=='o':return True
        elif radice.situazione=='x' or radice.situazione=='-':return False
        elif radice.c%2==0:
            for r in radice.lista_figli:
                tot=tot and strategiaV(r,g)
                if tot==False:break
            return tot
        else:
            for r in radice.lista_figli:
                ntot= ntot or strategiaV(r,g)
                if ntot==True:break
            return ntot
    else:
        if radice.situazione=='x':return True
        elif radice.situazione=='o' or radice.situazione=='-':return False
        elif radice.c%2==0:
            for r in radice.lista_figli:
                ntot= ntot or strategiaV(r,g)
                if ntot==True:break
            return ntot
        else:
            for r in radice.lista_figli:
                tot=tot and strategiaV(r,g)
                if tot==False:break
            return tot


def crea_albero(radice,g):
    if not '' in radice.nome[0] and not '' in radice.nome[1] and not '' in radice.nome[2]:
        radice.situazione= '-'
        return radice
    j=0
    while j<3:
        i=0
        while i<3:
            if radice.nome[j][i]=='' and g=='o':
                r=NodoTris(deepcopy(radice.nome),radice.livello+1)
                r.nome[j][i]='o'
                if r.nome[0]==['o','o','o'] or r.nome[1]==['o','o','o'] or r.nome[2]==['o','o','o'] or (r.nome[0][0]=='o' and r.nome[1][0]=='o' and r.nome[2][0]=='o') or (r.nome[0][1]=='o' and r.nome[1][1]=='o' and r.nome[2][1]=='o') or (r.nome[0][2]=='o' and r.nome[1][2]=='o' and r.nome[2][2]=='o') or (r.nome[0][0]=='o' and r.nome[1][1]=='o' and r.nome[2][2]=='o') or (r.nome[0][2]=='o' and r.nome[1][1]=='o' and r.nome[2][0]=='o'):
                    r.situazione='o'
                else:
                    r=crea_albero(r,'x')
                radice.lista_figli+=[r]
            if radice.nome[j][i]=='' and g=='x':
                r=NodoTris(deepcopy(radice.nome),radice.livello+1)
                r.nome[j][i]='x'
                if r.nome[0]==['x','x','x'] or r.nome[1]==['x','x','x'] or r.nome[2]==['x','x','x'] or (r.nome[0][0]=='x' and r.nome[1][0]=='x' and r.nome[2][0]=='x') or (r.nome[0][1]=='x' and r.nome[1][1]=='x' and r.nome[2][1]=='x') or (r.nome[0][2]=='x' and r.nome[1][2]=='x' and r.nome[2][2]=='x') or (r.nome[0][0]=='x' and r.nome[1][1]=='x' and r.nome[2][2]=='x') or (r.nome[0][2]=='x' and r.nome[1][1]=='x' and r.nome[2][0]=='x'):
                    r.situazione='x'
                else:
                    r=crea_albero(r,'o')
                radice.lista_figli+=[r]
            i+=1
        j+=1
    return radice


class NodoTris:
    def __init__(self, griglia,l=0):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.situazione='?'
        self.livello=l
        self.c=self.nome[0].count('')+self.nome[1].count('')+self.nome[2].count('')
        
        
    def tipo(self):
        '''inserire qui il vostro codice'''
        return self.situazione
        

    def esiti(self):
        '''inserire qui il vostro codice'''
        lista=[0,0,0]
        trova_esiti(self,lista)
        return tuple(lista)
    
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        lista=[0]
        trova_vittorie_livello(self,giocatore,h,lista)
        return lista[0]

        
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        return strategiaV(self,giocatore)
 

def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    radice=NodoTris(deepcopy(griglia))
    if radice.nome[0]==['o','o','o'] or radice.nome[1]==['o','o','o'] or radice.nome[2]==['o','o','o'] or (radice.nome[0][0]=='o' and radice.nome[1][0]=='o' and radice.nome[2][0]=='o') or (radice.nome[0][1]=='o' and radice.nome[1][1]=='o' and radice.nome[2][1]=='o') or (radice.nome[0][2]=='o' and radice.nome[1][2]=='o' and radice.nome[2][2]=='o') or (radice.nome[0][0]=='o' and radice.nome[1][1]=='o' and radice.nome[2][2]=='o') or (radice.nome[0][2]=='o' and radice.nome[1][1]=='o' and radice.nome[2][0]=='o'):
        radice.situazione= 'o'
    elif radice.nome[0]==['x','x','x'] or radice.nome[1]==['x','x','x'] or radice.nome[2]==['x','x','x'] or (radice.nome[0][0]=='x' and radice.nome[1][0]=='x' and radice.nome[2][0]=='x') or (radice.nome[0][1]=='x' and radice.nome[1][1]=='x' and radice.nome[2][1]=='x') or (radice.nome[0][2]=='x' and radice.nome[1][2]=='x' and radice.nome[2][2]=='x') or (radice.nome[0][0]=='x' and radice.nome[1][1]=='x' and radice.nome[2][2]=='x') or (radice.nome[0][2]=='x' and radice.nome[1][1]=='x' and radice.nome[2][0]=='x'):
        radice.situazione= 'x'
    else:
        if '' in radice.nome[0] or '' in radice.nome[1] or '' in radice.nome[2]:
            if radice.c%2==0:
                radice=crea_albero(radice,'x')
            else:
                radice=crea_albero(radice,'o')
        else:
            radice.situazione= '-'
    return radice