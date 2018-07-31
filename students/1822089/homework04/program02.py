'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3Ã—3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo 
(un giocatore ha come simbolo una "o" e l'avversario una 'x'). 
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta 
orizzontale, verticale o diagonale. Se la griglia viene riempita 
senza che nessuno dei giocatori sia riuscito a completare una linea 
retta di tre simboli, il gioco finisce in parita'. Nel caso in cui il gioco 
finisse in parita', la partita e' detta "patta". 
Per convenzione a griglia vuota la prima mossa spetta sempre al giocatore 'o'

Una configurazione del gioco e' dunque univocamente determinata  dal contenuto della griglia.

Nel seguito assumiamo che il contenuto della griglia sia rappresentato tramite  lista di liste.
La dimensione della lista di liste M e'  3x3 ed   M[i][j] contiene  '', 'x', o 'o'  a seconda 
che la cella della griglia appartenente all'iesima riga e j-ma colonna sia ancora libera, 
contenga il simbolo 'x' o contenga il simbolo 'o'. 

Data una configurazione C del gioco, l'albero di gioco per C e' l'albero che 
si ottiene ricorsivamente partendo dalla configurazione C e assegnando come figli le configurazioni 
che e' possibile ottenere da C con una mossa ulteriore del gioco. Ovviamente  risulteranno 
foglie dell'albero i possibili esiti della partita vale a dire le diverse configurazioni cui e' 
possibile arrivare partendo da C e che rappresentano patte, vittorie per 'o' o vittorie per 'x'.
Si veda ad esempio l'immagine albero_di_gioco.png che mostra l' albero di gioco che si ottiene a partire 
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
della classe NodoTris che dovete comunque implementare: 

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
Restituisce True se giocatore ha una strategia vincente  nella partita 
che ha come configurazione iniziale quella rappresentata dal nodo radice, False altrimenti.

Nota che un giocatore ha una strategia vincente rispetto ad una certa configurazione se, 
qualunque siano le mosse dell'avversario ha sempre la possibilita' di rispondere in modo 
che la partita termini con la sua vittoria.

Potete ovviamente definire ulteriori  funzioni e altri metodi per la Classe NodiTris 
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
        res=tris(self.nome)
        #Se False, la partita' e' patta o non e' ancora terminata
        if res==False:
            blanks=('' in self.nome[r] for r in range(3))
            #Se trova '' allora la partita non e' ancora terminata
            if True in blanks: return '?'
            return '-'
        #Se Lista, allora ritorna anche il vincitore
        return res[1]
    
    #Inserisco None come parametro opzionale, altrimenti, essendo un oggetto mutabile, ad ogni chiamata
    #della funzione, somma tutti i valori precedenti a quelli attuali
    def esiti(self,all_esiti=None):
        if all_esiti is None:
            all_esiti={"-":0, "o":0,"x":0}
        #Se non ha figli e' una foglia
        if len(self.lista_figli)==0:
            #Trovo il tipo della configurazione foglia e lo incremento nel dizionario
            all_esiti[self.tipo()]=all_esiti[self.tipo()]+1
        for figlio in self.lista_figli:
            figlio.esiti(all_esiti)
                
        return (all_esiti["-"], all_esiti["o"] ,all_esiti["x"])
    
    def vittorie_livello(self, giocatore, h,livello=0,tot=0):
        #Controllo livello e giocatore
        if livello==h and self.tipo()==giocatore:
            tot+=1
        for figlio in self.lista_figli:
            tot=max(tot,figlio.vittorie_livello(giocatore, h,livello+1,tot))
        return tot
    
    def strategia_vincente(self,giocatore):
        best_score=False
        best_move=self.nome
        #Scorre i figli della configurazione iniziale
        for figlio in self.lista_figli:
            nome=figlio.nome
            #Ritorna bool che indica strategia
            strategia=figlio.minPlay(giocatore)
            if strategia > best_score:
                best_score = strategia
        return best_score
    
    #Entrambi i giocatori cercano di vincere
    #Giocatore principale
    def minPlay(self,giocatore):
        nome=self.nome
        avversario='x' if giocatore=='o' else 'o'
        if self.tipo()==giocatore:
            return True
        best_score=True
        for figlio in self.lista_figli:
            score=figlio.maxPlay(avversario)
            if score < best_score:
                best_score = score
        return False
    
    #Avversario
    def maxPlay(self,avversario):
        nome=self.nome
        if self.tipo()==avversario:
            return False
        best_score=False
        for figlio in self.lista_figli:
            score=figlio.minPlay(avversario)
            if score > best_score:
                best_score=score
        return False


def gen_tree(griglia):
    #Controlli per la prima mossa
    #mosse disponibili ==>  dispari='o'  pari='x'
    if (griglia[0] + griglia[1] + griglia[2]).count("")%2==0:
        #Gli passo l'opposto perche' all'inizio della funzione cambio il turno
        nodo = recurs_griglia(griglia,'o')
    else:
        nodo = recurs_griglia(griglia,'x')
    #print(nodo.nome)
    #stampa_tree_indentations(nodo)
    return nodo

#Data una griglia e una mossa iniziale, genera l'albero
def recurs_griglia(griglia,m):
    nodo = NodoTris(griglia)
    #nomegriglia = nodo.nome
    #Controlla tris in griglia
    if tris(griglia)==False:
        m='x' if m=='o' else 'o'
        for i in range(3):
            for j in range(3):
                if griglia[i][j]=='':
                    new_griglia=[]
                    new_griglia+=[griglia[r][:] for r in range(3)]
                    new_griglia[i][j]=m
                    nodo.lista_figli += [recurs_griglia(new_griglia,m)]
    return nodo

#Controlla eventuale tris
def tris(griglia):
    for x in row_tris(griglia):
        if x[0]==True: return x
    for x in col_tris(griglia):
         if x[0]==True: return x
    d=diag_tris(griglia)
    if d[0]==True: return d
    
    return False

def row_tris(griglia):
    #Se e' l'unico valore diverso nella riga e' diverso da "" allora abbiamo un TRIS
    #Ritorno True/False e item vincente in caso di True
    return ( [( len(set(griglia[r]))==1 and griglia[r][0]!="" ),griglia[r][0]] for r in range(3)  )

def col_tris(griglia):
    return ( [(griglia[0][c]==griglia[1][c]==griglia[2][c] and griglia[0][c]!="" ),griglia[0][c]] for c in range(3) )

def diag_tris(griglia):
    return [((griglia[0][0]==griglia[1][1]==griglia[2][2] and griglia[0][0]!="")
                or (griglia[2][0]==griglia[1][1]==griglia[0][2] and griglia[2][0]!="")),griglia[1][1]]

#def stampa_tree_indentations(nodo,livello=0):
#    #Aggiunge 2*livello spazi prima del file
#    print("  "*2*livello + str(nodo.nome))
#    for figlio in nodo.lista_figli:
#        stampa_tree_indentations(figlio, livello+1)

#g0=[['', '', ''], ['', '', ''], ['', '', '']]
#g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
#g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
#g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
#g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]

#ªg5=[['', 'x', ''], ['', 'o', ''], ['', '', '']]
#g6=[['', 'o', ''], ['', 'x', ''], ['', '', '']]
#g7=[['', 'x', 'o'], ['', '', ''], ['', '', '']]
#g8=[['', 'o', 'x'], ['', '', ''], ['', '', '']]
        
#radice=gen_tree(g1)
#print(radice.tipo())
#print(radice.esiti())
#print(radice.vittorie_livello('x',2))
#print(radice.strategia_vincente('x'))





