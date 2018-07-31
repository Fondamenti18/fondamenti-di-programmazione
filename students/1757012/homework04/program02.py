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


class NomeFinal:
    def __init__(self,griglia):
        self.nome=griglia






class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    
    def tipo(self):
        contaspazi=0
        for x in self.nome:
            contax=0
            contay=0
            for mossa in x:
                if mossa=="":
                    contaspazi=contaspazi+1
                if mossa=="x":
                    contax=contax+1
                if mossa=="o":
                    contay=contay+1
                if contax==3:
                    return"x"
                if contay==3:
                    return "o"
        for a in range(0,3):
            contax=0
            contay=0
            for x in self.nome:
                if x[a]=="x":
                    contax=contax+1
                if x[a]=="o":
                    contay=contay+1
                if contax==3:
                    return"x"
                if contay==3:
                    return "o"
        if self.nome[0][0]==self.nome[1][1]==self.nome[2][2]:
            if self.nome[0][0]=="x":
                return"x"
            elif self.nome[0][0]=="o":
                return "o"
            elif self.nome[0][0]=="":
                return "?"
        if self.nome[0][2]==self.nome[1][1]==self.nome[2][0]:
            if self.nome[0][2]=="x":
                return"x"
            elif self.nome[0][2]=="o":
                return "o"
            elif self.nome[0][2]=="?":
                return "?"
        if contaspazi!=0:
            return "?"
        return "-"
            

    def trovavittorie(self, giocatore):
        contavittorie=0
        if giocatore=="x":
            if self.tipo()==giocatore:
                return 1
            else:
                for figlio in self.lista_figli:
                    contavittorie=contavittorie+figlio.trovavittorie("x")
            return contavittorie
        if giocatore=="o":
            if self.tipo()==giocatore:
                return 1
            else:
                for figlio in self.lista_figli:
                    contavittorie=contavittorie+figlio.trovavittorie("o")
            return contavittorie
        if giocatore=="-":
            if self.tipo()=="-":
                return 1
            else:
                for figlio in self.lista_figli:
                    contavittorie=contavittorie+figlio.trovavittorie("-")
            return contavittorie

      
    def esiti(self):
        a=self
        return(a.trovavittorie("-"),a.trovavittorie("o"),a.trovavittorie("x"))
        
        
    def vittorie_livello(self, giocatore, h, default=0):
        contatore=default
        contavittorie=0
        if contatore<h:
            for figlio in self.lista_figli:
                contavittorie=contavittorie+figlio.vittorie_livello(giocatore, h,default=contatore+1)
        if contatore==h:
            if self.tipo()==giocatore:
                return 1
            else:
                return 0
        return contavittorie 
            
    
    def strategia_vincente(self,giocatore):
        esito=True
        if self.tipo()!="?" and self.tipo()!=giocatore:
            return False
        if self.tipo()=="?":
            if turno(self.nome)==giocatore:
                for figlio in self.lista_figli:
                    if figlio.tipo()==giocatore:
                        return True
            
            for figlio in self.lista_figli:
                esito=figlio.strategia_vincente(giocatore)
                if esito==False:
                    break
        return esito


def turno(partita):
    contax=0
    contay=0
    for x in partita:
        for y in x:
            if y=="x":
                contax=contax+1
            if y=="o":
                contay=contay+1
    if contax+contay==9:
        return "-"
    if contax>contay:
        return"o"
    elif contax<contay:
        return"x"
    elif contax==contay:
        return "o"



def copya(a):
    c=[]
    for riga in a:
        c.append(list(riga))
    return c

def listafigli(partita,partitafissa):
    listaout=[]
    listafinal=[]
    nuovagriglia=[]
    for a in partitafissa:
        listafinal.append(a)
    if partita.tipo()=="?":
        for rige in range(0,3):
            for posto in range(0,3):
                if listafinal[rige][posto]=="":
                    if turno(partitafissa)=="x":
                        listafinal[rige][posto]="x"
                        nuovagriglia=copya(listafinal)
                        listaout.append(NodoTris(nuovagriglia))
                        listafinal[rige][posto]=""
                    else:
                        listafinal[rige][posto]="o"
                        nuovagriglia=copya(listafinal)
                        listaout.append(NodoTris(nuovagriglia))
                        listafinal[rige][posto]=""
        partita.lista_figli=listaout
        for elem in listaout:
            listafigli(elem,elem.nome)
    else:
        return []

def gen_tree(griglia):
    listarige=[]
    for riga in griglia:
        listarige.append(riga)
    nodo=NodoTris(griglia)
    listafigli(nodo,listarige)
    return nodo
    
    
    
     

    







