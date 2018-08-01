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
from copy import *

class NodoTris:

    def __init__(self, griglia, lista_figli = []):
        self.nome = griglia
        self.lista_figli = lista_figli

    def __str__(self):
        return '{} \n{} \n{}'.format(self.nome[0], self.nome[1], self.nome[2])
    
    def tipo(self):
        
        l=[]
        for y in range(3):
            for x in range(3):
                l.append(self.nome[y][x])
        
#===========================================================#
                                                            #
        if (l[0]=='o' and l[1]=='o' and l[2]=='o'):         # |--
            return 'o'                                      # |
        elif (l[3]=='o' and l[4]=='o' and l[5]=='o'):       # |-- combinazioni per soluzioni orizzontali del 'o'
            return 'o'                                      # |
        elif (l[6]=='o' and l[7]=='o' and l[8]=='o'):       # |--
            return 'o'                                      # 
        elif (l[0]=='o' and l[3]=='o' and l[6]=='o'):       # |--
            return 'o'                                      # |
        elif (l[1]=='o' and l[4]=='o' and l[7]=='o'):       # |-- combinazioni per soluzioni verticali del 'o'
            return 'o'                                      # |
        elif (l[2]=='o' and l[5]=='o' and l[8]=='o'):       # |--
            return 'o'                                      # 
        elif (l[0]=='o' and l[4]=='o' and l[8]=='o'):       # |--
            return 'o'                                      # |   combinazioni per soluzioni diagonali del 'o'
        elif (l[2]=='o' and l[4]=='o' and l[6]=='o'):       # |--
            return 'o'                                      # 
                                                            #
        elif (l[0]=='x' and l[1]=='x' and l[2]=='x'):       # |--
            return 'x'                                      # |
        elif (l[3]=='x' and l[4]=='x' and l[5]=='x'):       # |-- combinazioni per soluzioni orizzontali della 'x'
            return 'x'                                      # |
        elif (l[6]=='x' and l[7]=='x' and l[8]=='x'):       # |--
            return 'x'                                      # 
        elif (l[0]=='x' and l[3]=='x' and l[6]=='x'):       # |--
            return 'x'                                      # |
        elif (l[1]=='x' and l[4]=='x' and l[7]=='x'):       # |-- combinazioni per soluzioni verticali della 'x'
            return 'x'                                      # |
        elif (l[2]=='x' and l[6]=='x' and l[8]=='x'):       # |--
            return 'x'                                      # 
        elif (l[0]=='x' and l[4]=='x' and l[8]=='x'):       # |--
            return 'x'                                      # |   combinazioni per soluzioni diagonali della 'x'
        elif (l[2]=='x' and l[4]=='x' and l[6]=='x'):       # |--
            return 'x'                                      # 
                                                            #
        else:                                               # | se c'e' una casella vuota dopo i vari controlli allora la partita ancora ha un esito sconosciuto
            if '' in l:                                     # | nel caso tutte le caselle siano piene e nessuno dei risultati precedenti e'
                return '?'                                  # | confermato allora e' patta
            return '-'                                      # | -
                                                            #
#===========================================================#
        
    def esiti(self):
        '''
        dato un nodo radice di un albero di gioco, restituisce una tripla con i possibili 
        esiti della partita che ha come configurazione iniziale quella rappresentata dal nodo. 
        Piu' precisamente: il primo elemento della tripla  e' il numero di  patte possibili, 
        il secondo e' il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento 
        e' il numero di possibili vittorie per il giocatore 'x'.
        '''
        a=self.lista_figli
        a.insert(0, self.nome)
        cp=0
        co=0
        cx=0
        return calcolo_esiti(a, cp, co, cx) 
    
    def vittorie_livello(self, giocatore, h):
        lista=[]
        livello=1
        cont=set()
        cont.add(0)
        return liv_figli(self.nome, giocatore, 'o', lista, livello, h, cont)
    
    def strategia_vincente(self,giocatore):
        lista=[]
        return ha_vinto(self.nome, giocatore, 'o', lista)
        
def gen_tree(griglia):
    prossima_mossa='o'
    lista=[]
    l=gen_figli(griglia, prossima_mossa, lista)
    oggetto=NodoTris(griglia,l)
    return oggetto

def gen_figli(griglia, prossima_mossa, lista):
    a=NodoTris(griglia)
    if a.tipo()=='?':
        for y in range(3):
            for x in range(3):
                if griglia[y][x]=='':
                    griglia[y][x]=prossima_mossa
                    lista.append(deepcopy(griglia))
                    b=NodoTris(griglia)
                    if prossima_mossa=='o' and b.tipo()=='?':
                        gen_figli(griglia, 'x', lista)
                    if prossima_mossa=='x' and b.tipo()=='?':
                        gen_figli(griglia, 'o', lista)
                    griglia[y][x]=''
    return lista

def liv_figli(griglia, giocatore, prossima_mossa, lista, livello, h, cont):
    a=NodoTris(griglia)
    for y in range(3):
        for x in range(3):
            if griglia[y][x]=='':
                griglia[y][x]=prossima_mossa
                lista.append(deepcopy(griglia))
                b=NodoTris(griglia)
                if b.tipo()==giocatore and livello==h:
                    cont.add(1)
                elif prossima_mossa=='o' and b.tipo()=='?':
                    liv_figli(griglia,giocatore, 'x', lista,livello+1,h,cont)
                elif prossima_mossa=='x' and b.tipo()=='?':
                    liv_figli(griglia,giocatore, 'o', lista,livello+1,h,cont)
                griglia[y][x]=''
    contatore=0
    for i in cont:
        contatore+=1
    return contatore-1

def ha_vinto(griglia, giocatore, prossima_mossa, lista):
    a=NodoTris(griglia)
    for y in range(3):
        for x in range(3):
            if griglia[y][x]=='':
                griglia[y][x]=prossima_mossa
                lista.append(deepcopy(griglia))
                b=NodoTris(griglia)
                if b.tipo()==giocatore:
                    return True
                elif prossima_mossa=='o' and b.tipo()=='?':
                    ha_vinto(griglia,giocatore, 'x', lista)
                elif prossima_mossa=='x' and b.tipo()=='?':
                    ha_vinto(griglia,giocatore, 'o', lista)
                griglia[y][x]=''
    return False

def calcolo_esiti(lista, cp ,co ,cx):
    if len(lista)==0:
        return (cp,co,cx)
    if len(lista)>0:
        a=esito(lista[0])
        if a == '-':
            cp+=1
        if a == 'o':
            co+=1
        if a == 'x':
            cx+=1
        return calcolo_esiti(lista[1:], cp, co, cx)

def esito(griglia):
        l=[]
        for y in range(3):
            for x in range(3):
                l.append(griglia[y][x])

        
#===========================================================#
                                                            #
        if (l[0]=='o' and l[1]=='o' and l[2]=='o'):         # |--
            return 'o'                                      # |
        elif (l[3]=='o' and l[4]=='o' and l[5]=='o'):       # |-- combinazioni per soluzioni orizzontali del 'o'
            return 'o'                                      # |
        elif (l[6]=='o' and l[7]=='o' and l[8]=='o'):       # |--
            return 'o'                                      # 
        elif (l[0]=='o' and l[3]=='o' and l[6]=='o'):       # |--
            return 'o'                                      # |
        elif (l[1]=='o' and l[4]=='o' and l[7]=='o'):       # |-- combinazioni per soluzioni verticali del 'o'
            return 'o'                                      # |
        elif (l[2]=='o' and l[5]=='o' and l[8]=='o'):       # |--
            return 'o'                                      # 
        elif (l[0]=='o' and l[4]=='o' and l[8]=='o'):       # |--
            return 'o'                                      # |   combinazioni per soluzioni diagonali del 'o'
        elif (l[2]=='o' and l[4]=='o' and l[6]=='o'):       # |--
            return 'o'                                      # 
                                                            #
        elif (l[0]=='x' and l[1]=='x' and l[2]=='x'):       # |--
            return 'x'                                      # |
        elif (l[3]=='x' and l[4]=='x' and l[5]=='x'):       # |-- combinazioni per soluzioni orizzontali della 'x'
            return 'x'                                      # |
        elif (l[6]=='x' and l[7]=='x' and l[8]=='x'):       # |--
            return 'x'                                      # 
        elif (l[0]=='x' and l[3]=='x' and l[6]=='x'):       # |--
            return 'x'                                      # |
        elif (l[1]=='x' and l[4]=='x' and l[7]=='x'):       # |-- combinazioni per soluzioni verticali della 'x'
            return 'x'                                      # |
        elif (l[2]=='x' and l[5]=='x' and l[8]=='x'):       # |--
            return 'x'                                      # 
        elif (l[0]=='x' and l[4]=='x' and l[8]=='x'):       # |--
            return 'x'                                      # |   combinazioni per soluzioni diagonali della 'x'
        elif (l[2]=='x' and l[4]=='x' and l[6]=='x'):       # |--
            return 'x'                                      # 
                                                            #
        else:                                               # | se c'e' una casella vuota dopo i vari controlli allora la partita ancora ha un esito sconosciuto
            if '' in l:                                     # | nel caso tutte le caselle siano piene e nessuno dei risultati precedenti e'
                return '?'                                  # | confermato allora e' patta
            return '-'                                      # | -
                                                            #
#===========================================================#

if __name__=='__main__':
    None
