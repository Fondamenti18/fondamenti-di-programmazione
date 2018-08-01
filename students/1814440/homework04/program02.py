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
        '''inserire qui il vostro codice'''
        return controllaTris(self)
        
    def esiti(self):
        '''inserire qui il vostro codice'''
        radice,patta,vinceo,vincex=step(self,'o',0,0,0)
        return (patta,vinceo,vincex)
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        tot=step2(self, giocatore, h,0)
        return tot/2
            
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        return vincente(self,giocatore,'o','x')

def vincente(nodo,giocatore,turno,prossimo):
    lista=[]
    figli=nodo.lista_figli
    for figlio in figli:
        lista.append(vincente(figlio,giocatore,prossimo,turno))
    if figli==[]: lista=[giocatore==controllaTris(nodo)]
    if giocatore==turno: return True in lista
    else: return not False in lista
    
def controllaTris(nodo):
    ''' verifica se in quel nodo c'e un tris'''
    a=nodo.nome[0]
    b=nodo.nome[1]
    c=nodo.nome[2]
    if a[0]==a[1]==a[2]!='': return a[0]
    if b[0]==b[1]==b[2]!='': return b[0]
    if c[0]==c[1]==c[2]!='': return c[0]
    if a[0]==b[0]==c[0]!='': return a[0]
    if a[1]==b[1]==c[1]!='': return a[1]
    if a[2]==b[2]==c[2]!='': return a[2]
    if a[0]==b[1]==c[2]!='': return a[0]
    if a[2]==b[1]==c[0]!='': return a[2]
    if '' in a or '' in b or '' in c: return '?'
    return '-'

def step2(nodo, giocatore, h,tot,livello=0):
    if livello==h:
        if controllaTris(nodo)==giocatore: # vuol dire che stiamo al livello giusto e tocca a giocatore
            tot+=1
            return tot
    for el in nodo.lista_figli:
        tot=step2(el,giocatore,h,tot,livello+1)
    return tot

    
def step(radice,segno,patta,vinceo,vincex):
    ''' funzione che mi genera i nodi figli a partire dal nodo padre '''
    esito=controllaTris(radice)
    if esito!='?' and esito!='-':
        if esito=='o': vinceo+=1
        else: vincex+=1
        return radice,patta,vinceo,vincex
    for a in range(3):
        for b in range(3):
            if radice.nome[a][b]=='': # il segno va messo se la casella e vuota
                gr=[]
                gr.append(radice.nome[0].copy()) # devo fare cosi perche senno le liste interne puntano allo stessa memoria
                gr.append(radice.nome[1].copy())
                gr.append(radice.nome[2].copy())
                gr[a][b]=segno # metto il segno
                nuovo=NodoTris(gr)
                if segno=='o':
                    nuovo,patta,vinceo,vincex=step(nuovo,'x',patta,vinceo,vincex)
                else:
                    nuovo,patta,vinceo,vincex=step(nuovo,'o',patta,vinceo,vincex)
                radice.lista_figli.append(nuovo) # creo il nodo figlio
    if controllaTris(radice)=='-': patta+=1
    return radice,patta,vinceo,vincex
    
def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    radice=NodoTris(griglia) # genero l'albero
    radice,patta,vinceo,vincex=step(radice,'o',0,0,0)
    return radice