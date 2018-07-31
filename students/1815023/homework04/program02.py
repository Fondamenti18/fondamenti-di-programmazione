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
import time
class NodoTris:
    def __init__(self, griglia, turno=''):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.vincitore = self.tipo()
        
        if turno:
            self.turno = turno
        else:
            self.turno = self.mossa()
        
    def tipo(self):
        vuote = len(self.celle_vuote())
        if vuote <= 4: #Se ci sono piu' di 4 caselle vuote, la partita sicuramente non e' ancora finita
            for y in range(3):
                if self.nome[y][0] != '' and self.nome[y][0] == self.nome[y][1] and self.nome[y][0] == self.nome[y][2]:
                    return self.nome[y][0]
            
            for x in range(3):
                if self.nome[0][x] != '' and self.nome[0][x] == self.nome[1][x] and self.nome[0][x] == self.nome[2][x]:
                    return self.nome[0][x]
                
            if self.nome[0][0] != '' and self.nome[0][0] == self.nome[1][1] and self.nome[0][0] == self.nome[2][2]:
                return self.nome[0][0]
            
            if self.nome[2][0] != '' and self.nome[2][0] == self.nome[1][1] and self.nome[2][0] == self.nome[0][2]:
                return self.nome[2][0]
            
            if vuote == 0:
                return '-'
            else:
                return '?'
        else:
            return '?'
        
    def esiti(self, patte=0,vinceO=0,vinceX=0):
        '''inserire qui il vostro codice'''
        if self.vincitore == '-':
            return (patte+1,vinceO,vinceX)
        elif self.vincitore == 'o':
            return (patte,vinceO+1,vinceX)
        elif self.vincitore == 'x':
            return (patte,vinceO,vinceX+1)
            
        if self.vincitore == '?':
            for figlio in self.lista_figli:
                patte, vinceO, vinceX = figlio.esiti(patte,vinceO,vinceX)
                
        return (patte,vinceO,vinceX)
    
    def vittorie_livello(self, giocatore, h, corrente=0, conta=0):
        '''inserire qui il vostro codice'''
        if corrente <= h:        
            if self.vincitore == giocatore and corrente == h: #Se vince il giocatore dopo h mosse
                return conta+1
            
            for figlio in self.lista_figli:
                conta = figlio.vittorie_livello(giocatore,h,corrente+1, conta)
            
        return conta
    

    def strategia_vincente(self, giocatore):

        if giocatore == 'o': avversario = 'x'
        else: avversario = 'o'

        #caso base
        if self.vincitore == giocatore:
            return True
        elif self.vincitore == avversario or self.vincitore == '-':
            return False

        if self.turno == giocatore: #Se tocca al giocatore,
            for figlio in self.lista_figli:
                if figlio.strategia_vincente(giocatore) == True: #Basta che uno dei suoi figlio abbia una strategia vincente e puo' vincere
                    return True
            return False
        else:  #Se tocca all'avversario              
            for figlio in self.lista_figli:
                if figlio.strategia_vincente(giocatore) == False:  #Se solo un figlio non puo' vincere, non ha una strategia vincente
                    return False
            return True
        
            
        
        
        
        
    #------ Metodi aggiuntivi -------
        
    def mossa(self):
        '''Ritorna a chi tocca il turno ('x' o 'o')'''
        count = 0
        for riga in self.nome:
            for cella in riga:

                if cella != '':
                    count += 1
                    
        if count % 2 == 0:
            return 'o'
        else: 
            return 'x'
        
    def celle_vuote(self):
        '''Ritorna una lista con gli indici delle celle vuote di una griglia'''
        ris = []
        for y in range(len(self.nome)):
            for x in range(len(self.nome[0])):
                if self.nome[y][x] == '':
                    ris.append((x,y))
        return ris
    
def copiagriglia(lista):
    x0 = lista[0][:]
    x1 = lista[1][:]
    x2 = lista[2][:]
    return [x0]+[x1]+[x2]

def gen_tree(griglia, simbolo=''):
    '''inserire qui il vostro codice'''
    radice = NodoTris(griglia, simbolo)
    if radice.turno == 'x':
        simbolo = 'o'
    elif radice.turno == 'o':
        simbolo = 'x'

    if radice.vincitore == '?':
        for x,y in radice.celle_vuote():
            copia = copiagriglia(griglia)
            copia[y][x] = radice.turno
            radice.lista_figli.append(gen_tree(copia,simbolo))
    return radice
    
    
