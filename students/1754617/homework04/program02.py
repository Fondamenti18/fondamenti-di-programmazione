'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3x3 caselle.
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
def visita_in_ordine(radice):
        if( not  radice.lista_figli ):
            if(radice.tipo()=='x'):
                return (0,0,1)
            elif(radice.tipo()=='o'):
                return (0,1,0)
            elif(radice.tipo()=='-'):
                return (1,0,0)
            return (0,0,0)
        patte=0
        vitt_o=0
        vitt_x=0
        for nodo in radice.lista_figli:
            risultato=visita_in_ordine(nodo)
            patte+=risultato[0]
            vitt_o+=risultato[1]
            vitt_x+=risultato[2]
        return (patte,vitt_o,vitt_x)



def bfs(radice, giocatore, h):
    if h==0:
        return 1 if radice.tipo()==giocatore else 0
    if not radice.lista_figli:
        return 0
    else:
        somma=0
        for nodo in radice.lista_figli:
             somma+=bfs(nodo,giocatore,h-1)
        return somma
    


def funzione(radice,giocatore):
        if ( not radice.lista_figli):
               return  radice.tipo()==giocatore
        numeri_o=0
        numeri_x=0
        for riga in range(3):
            for colonna in range(3):
                if(radice.nome[riga][colonna]=="x"):
                    numeri_x+=1
                elif(radice.nome[riga][colonna]=="o"):
                    numeri_o+=1
        prossimo="o" if numeri_o==numeri_x else 'x'
        if(prossimo==giocatore):
            for nodo in radice.lista_figli:
                if(funzione(nodo,giocatore)):
                     return True
            return False
        else:
             for nodo in radice.lista_figli:
                 if not(funzione(nodo,giocatore)):
                     return False
             return True

                        
                        
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
	
    def __str__(self):
        return str(self.nome)

    def __repr__(self):
        return str(self.nome)
    
    def tipo(self):
        '''inserire qui il vostro codice'''
        if( self.nome[0][0]=='x' and self.nome[1][0]=='x' and self.nome[2][0]=='x'):
            return 'x'
        elif( self.nome[0][0]=='o' and self.nome[1][0]=='o' and self.nome[2][0]=='o'):
            return 'o'
        elif( self.nome[0][0]=='o' and self.nome[0][1]=='o' and self.nome[0][2]=='o'):
            return 'o'
        elif( self.nome[0][0]=='x' and self.nome[0][1]=='x' and self.nome[0][2]=='x'):
            return 'x'
        elif( self.nome[0][0]=='o' and self.nome[1][1]=='o' and self.nome[2][2]=='o'):
            return 'o'
        elif( self.nome[0][0]=='x' and self.nome[1][1]=='x' and self.nome[2][2]=='x'):
            return 'x'
        elif( self.nome[0][2]=='x' and self.nome[1][1]=='x' and self.nome[2][0]=='x'):
            return 'x'
        elif( self.nome[0][2]=='o' and self.nome[1][1]=='o' and self.nome[2][0]=='o'):
            return 'o'
        elif( self.nome[1][0]=='x' and self.nome[1][1]=='x' and self.nome[1][2]=='x'):
            return 'x'
        elif( self.nome[1][0]=='o' and self.nome[1][1]=='o' and self.nome[1][2]=='o'):
            return 'o'
        elif( self.nome[2][0]=='x' and self.nome[2][1]=='x' and self.nome[2][2]=='x'):
            return 'x'
        elif( self.nome[2][0]=='o' and self.nome[2][1]=='o' and self.nome[2][2]=='o'):
            return 'o'
        elif( self.nome[0][1]=='x' and self.nome[1][1]=='x' and self.nome[2][1]=='x'):
            return 'x'
        elif( self.nome[0][1]=='o' and self.nome[1][1]=='o' and self.nome[2][1]=='o'):
            return 'o'
        elif( self.nome[0][2]=='x' and self.nome[1][2]=='x' and self.nome[2][2]=='x'):
            return 'x'
        elif( self.nome[0][2]=='o' and self.nome[1][2]=='o' and self.nome[2][2]=='o'):
            return 'o'
        else:
            if( ('' in self.nome[0]) or ('' in self.nome[1]) or ('' in self.nome[2])):
                return '?'
            elif( not '' in self.nome):
                return '-'
                    
        
    def esiti(self):
        '''inserire qui il vostro codice'''
        albero=gen_tree(self.nome)
        tupla=visita_in_ordine(albero)
        return tupla
            
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        albero=gen_tree(self.nome)
        return bfs(albero,giocatore,h)


    def chiave(self):
        return tuple( self.nome[i][j] for i in range(3)
                      for j in range(3))

        
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        return funzione(gen_tree(self.nome), giocatore)
                        
def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    numeri_o=0
    numeri_x=0
    for riga in range(3):
        for colonna in range(3):
            if(griglia[riga][colonna]=="x"):
                numeri_x+=1
            elif(griglia[riga][colonna]=="o"):
                numeri_o+=1
    nodo=NodoTris(griglia)
    return costruisci_tree(nodo,"o" if numeri_o==numeri_x else "x")

tree_cache = {}

def costruisci_tree(nodoTris,next_giocatore):
    if(nodoTris.chiave() in tree_cache):
            return tree_cache[nodoTris.chiave()]
    tipo=nodoTris.tipo()
    if( tipo=='?'):
        for riga in range(3):
            for colonna in range(3):
                if(nodoTris.nome[riga][colonna]==''):
                    griglia=[riga[:] for riga in nodoTris.nome]
                    griglia[riga][colonna]=next_giocatore
                    nodo=NodoTris(griglia)
                    if nodo.chiave() in tree_cache:
                            nodo = tree_cache[nodo.chiave()]
                            nodoTris.lista_figli.append(nodo)
                            continue
                
                    costruisci_tree(nodo, "o" if next_giocatore=='x' else 'x')
                    tree_cache[nodo.chiave()]=nodo
                    nodoTris.lista_figli.append(nodo)
                    
    return nodoTris

