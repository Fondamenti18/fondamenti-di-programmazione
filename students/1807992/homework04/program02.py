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

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        if (self.nome[0][0] == 'x' and self.nome[0][1] == 'x' and self.nome[0][2] == 'x') or (self.nome[1][0] == 'x' and self.nome[1][1] == 'x' and self.nome[1][2] == 'x') or (self.nome[2][0] == 'x' and self.nome[2][1] == 'x' and self.nome[2][2] == 'x') or (self.nome[0][0] == 'x' and self.nome[1][0] == 'x' and self.nome[2][0] == 'x') or (self.nome[0][1] == 'x' and self.nome[1][1] == 'x' and self.nome[2][1] == 'x') or (self.nome[0][2] == 'x' and self.nome[1][2] == 'x' and self.nome[2][2] == 'x') or (self.nome[0][0] == 'x' and self.nome[1][1] == 'x' and self.nome[2][2] == 'x') or (self.nome[0][2] == 'x' and self.nome[1][1] == 'x' and self.nome[2][0] == 'x'):
            return 'x'
        elif (self.nome[0][0] == 'o' and self.nome[0][1] == 'o' and self.nome[0][2] == 'o') or (self.nome[1][0] == 'o' and self.nome[1][1] == 'o' and self.nome[1][2] == 'o') or (self.nome[2][0] == 'o' and self.nome[2][1] == 'o' and self.nome[2][2] == 'o') or (self.nome[0][0] == 'o' and self.nome[1][0] == 'o' and self.nome[2][0] == 'o') or (self.nome[0][1] == 'o' and self.nome[1][1] == 'o' and self.nome[2][1] == 'o') or (self.nome[0][2] == 'o' and self.nome[1][2] == 'o' and self.nome[2][2] == 'o') or (self.nome[0][0] == 'o' and self.nome[1][1] == 'o' and self.nome[2][2] == 'o') or (self.nome[0][2] == 'o' and self.nome[1][1] == 'o' and self.nome[2][0] == 'o'):
            return 'o'
        elif '' in self.nome[0] or '' in self.nome[1] or '' in self.nome[2]:
            return '?'
        else:
            return '-'
               
    def esiti(self, patte = 0, vitt_o = 0, vitt_x = 0):
        numero_x = 0
        numero_o = 0
        prossimo = ''
        if self.tipo() == '-':
            patte += 1
        if self.tipo() == 'o':
            vitt_o += 1
        if self.tipo() == 'x':
            vitt_x += 1
        if self.tipo() == '?':
            for i in self.lista_figli:
                patte,vitt_o,vitt_x = i.esiti(patte,vitt_o,vitt_x)
        return (patte,vitt_o,vitt_x)

            
    def vittorie_livello(self, giocatore, h, x = 1):
        contatore = 0
        for i in self.lista_figli:
            if i.tipo() == giocatore and x == h:
                contatore += 1
            contatore += i.vittorie_livello(giocatore, h,x+1)
        return contatore

    
    def strategia_vincente(self,giocatore,h = 1):
        if giocatore == 'x':
            opposto = 'o'
        else:
            opposto = 'x'
        if self.vittorie_livello(opposto,h) == 0:
            if self.vittorie_livello(giocatore,h) > 0:
                return True
            else:
                for i in self.lista_figli:
                    if i.tipo() == '?':
                        return self.strategia_vincente(giocatore, h+1)
        else:
            return False
        
def gen_tree(griglia):
    nodo = NodoTris(griglia)
    numero_x = 0
    numero_o = 0
    prossimo = ''
    for i in nodo.nome:
        numero_x += i.count('x')
        numero_o += i.count('o')
    if numero_x < numero_o:
        prossimo = 'x'
    else:
        prossimo = 'o'
    if nodo.tipo() == '-':
        return nodo
    if nodo.tipo() == 'o':
        return nodo
    if nodo.tipo() == 'x':
        return nodo
    if nodo.tipo() == '?':
        griglia1 = []
        for i in nodo.nome:
            for x in i:
                griglia1.append(x)
        for i in range(9):
            if griglia1[i] == '':
                griglia1[i] = prossimo
                nodo.lista_figli += [gen_tree([griglia1[x:x+3] for x in range(0, len(griglia1),3)])]
                griglia1[i] = ''
    return nodo
