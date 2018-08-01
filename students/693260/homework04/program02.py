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

patte = 0
    
vittorie_o = 0
   
vittorie_x = 0

altezza = 0
    
class NodoTris:

    def __init__(self, griglia):
        
        self.nome = griglia
        
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        '''inserire qui il vostro codice'''
        
        return controllavincitore(self)
        
    def esiti(self):
        '''inserire qui il vostro codice'''
        
        global patte
        
        patte = 0
    
        global vittorie_o
                
        vittorie_o = 0
            
        global vittorie_x
        
        vittorie_x = 0
        
        gen_tree(self.nome)
                
        return (patte, vittorie_o, vittorie_x)
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        
        
        
        
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        
    def stampa_griglia(self):
        
        print(str(self.nome[0]) + "\n" + str(self.nome[1]) + "\n" + str(self.nome[2]))
                        
def gen_tree(griglia):
    '''inserire qui il vostro codice''' 
    
    global patte
    
    global vittorie_o
    
    global vittorie_x
    
    global altezza
            
    Nodo = NodoTris(griglia)

    altezza +=1

    esito = controllavincitore(Nodo)
    
    if esito != '?':
        
        if esito == '-':
            
            patte += 1
            
        elif esito == 'o':
            
            vittorie_o += 1
            
        else:
            
            vittorie_x += 1
                       
        return Nodo
    
    else:
        
        # Per Ogni cella vuota fai una mossa con lo stesso giocatore e metti la griglia con la mossa
        # fatta nella lista dei figli del Nodo di questa chiamata di gen_tree, dopodicche chiama gen_tree per ogni
        # griglia della lista_figli
        
        giocatore = scegligiocatore(Nodo.nome)
        
        for colonna in range(0, 3):
            
            for riga in range(0, 3):
                
                if Nodo.nome[riga][colonna] == '':
                    
                    NuovoNodo = NodoTris([['', '', ''],['', '', ''],['', '', '']])
                    
                    NuovoNodo.nome = copy.deepcopy(Nodo.nome)
                    
                    NuovoNodo.nome[riga][colonna] = giocatore
                    
                    Nodo.lista_figli.append(NuovoNodo)
                    
        for ogniNodo in Nodo.lista_figli:
            
            ogniNodo.lista_figli.append(gen_tree(ogniNodo.nome))
        
    return Nodo
        
def scegligiocatore(griglia):
    
    conta_x = 0
    
    conta_o = 0
    
    for colonna in range(0, 3):
        
        for riga in range (0, 3):
            
            if griglia[riga][colonna] == 'x':
                
                conta_x += 1
                
            elif griglia[riga][colonna] == 'o':
                
                conta_o += 1
                
    if conta_x >= conta_o:
        
        return 'o'
        
    else:
        
        return 'x'

def controllavincitore(NodoDaControllare):
    
    '''
    
    Controllo se la griglia ha una configurazione di vittoria per uno dei due giocatori
    La funzione ritorna:
    - o per vittoria o;
    - x per vittoria x;
    - ? partita ancora da terminare;
    - p per partita patta.
    
    '''
    
    griglia = NodoDaControllare.nome
    
    # Prima riga        
    if griglia[0][0] == griglia[0][1] == griglia[0][2]:
        
        if griglia[0][0] == 'o' or griglia[0][0] == 'x':
           
            return griglia[0][0]
        
    # Seconda riga        
    if griglia[1][0] == griglia[1][1] == griglia[1][2]:
                
        if griglia[1][0] == 'o' or griglia[1][0] == 'x':
            
            return griglia[1][0]    
    
    # Terza riga        
    if griglia[2][0] == griglia[2][1] == griglia[2][2]:
                
        if griglia[2][0] == 'o' or griglia[2][0] == 'x':
        
            return griglia[2][0]
        
    # Prima colonna        
    if griglia[0][0] == griglia[1][0] == griglia[2][0]:
        
        if griglia[0][0] == 'o' or griglia[0][0] == 'x':
            
            return griglia[0][0]   
    
    # Seconda colonna        
    if griglia[0][1] == griglia[1][1] == griglia[2][1]:
        
        if griglia[0][1] == 'o' or griglia[0][1] == 'x':
            
            return griglia[0][1]     
  
    # Terza colonna        
    if griglia[0][2] == griglia[1][2] == griglia[2][2]:
        
        if griglia[0][2] == 'o' or griglia[0][2] == 'x':
            
            return griglia[0][2]         
  
    # Diagonale da AS a BD
    if griglia[0][0] == griglia[1][1] == griglia[2][2]:
        
        if griglia[0][0] == 'o' or griglia[0][0] == 'x':
            
            return griglia[0][0]         
    
    # Diagonale da AD a BS
    if griglia[0][2] == griglia[1][1] == griglia[2][0]:
        
        if griglia[0][2] == 'o' or griglia[0][2] == 'x':
            
            return griglia[0][2]            
    
    # Se sono qui non ha vinto nessuno
    # controllo se tutte le celle sono piene altrimenti la partita 
    # e ancora in corso
    
    for r in range(0, 3):
        
        for c in range(0, 3):
            
            if griglia[r][c] == '':
               
                return '?'
    
    return '-'
