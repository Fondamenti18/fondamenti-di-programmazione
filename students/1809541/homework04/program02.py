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
from copy import deepcopy
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        if (self.nome[0][0]!=''):
            if (self.nome[0][0]==self.nome[0][1] and self.nome[0][0]==self.nome[0][2]) or (self.nome[0][0]==self.nome[1][0] and self.nome[0][0]==self.nome[2][0]) or (self.nome[0][0]==self.nome[1][1] and self.nome[0][0]==self.nome[2][2]):
                return self.nome[0][0]
        if (self.nome[1][1]!=''):
            if (self.nome[1][1]==self.nome[0][2] and self.nome[1][1]==self.nome[2][0]) or (self.nome[1][1]==self.nome[0][1] and self.nome[1][1]==self.nome[2][1]) or (self.nome[1][1]==self.nome[1][0] and self.nome[1][1]==self.nome[1][2]):
                return self.nome[1][1]
        if (self.nome[2][2]!=''):
            if (self.nome[2][2]==self.nome[2][1] and self.nome[1][1]==self.nome[2][0]) or (self.nome[2][2]==self.nome[1][2] and self.nome[2][2]==self.nome[0][2]):
                return self.nome[2][2]
        for y in [0,1,2]:
            for x in [0,1,2]:
                if self.nome[y][x]=='':
                    return '?'
        return '-'

    def esiti(self):
        end=[0,0,0]
        if self.tipo()=='-':
            end[0]+=1
        elif self.tipo()=='o':
            end[1]+=1
        elif self.tipo()=='x':
            end[2]+=1
        end_figli=[]
        for figlio in self.lista_figli:
            end_figli=figlio.esiti()
            end[0]+=end_figli[0]
            end[1]+=end_figli[1]
            end[2]+=end_figli[2]
        return (end[0],end[1],end[2])
        

            
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        count=0
        if self.tipo()==giocatore:
            if h==0:
                count+=1
                return count
        if h-1>=0:
            for figlio in self.lista_figli:
                count+=figlio.vittorie_livello(giocatore,h-1)
        return count

    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        avversario='o'
        if giocatore=='o':
            avversario='x'
        if self.tipo()==giocatore:
            return True
        if self.tipo()=='-':
            return False
        if self.tipo() == avversario:
            return False
        for figli in self.lista_figli:
            return figli.strategia_vincente(giocatore)
            
        

def primamossa(griglia):
    count=0
    for y in [0,1,2]:
        for x in [0,1,2]:
            if griglia[y][x]=='':
                count+=1
    if count%2==0:
        return 'x'
    else:
        return 'o'

def gen_tree(griglia):
    RAD=NodoTris(griglia)
    figli=RAD.lista_figli
    if RAD.tipo()=='?':
        listalibera=[]
        for y in [0,1,2]:
            for x in [0,1,2]:
                if RAD.nome[y][x]=='':
                    listalibera.append((x,y))
        for i in listalibera:
            grigliacopiata=deepcopy(griglia)
            grigliacopiata[i[1]][i[0]]=primamossa(griglia)
            figli.append(gen_tree(grigliacopiata))
    return RAD
    
