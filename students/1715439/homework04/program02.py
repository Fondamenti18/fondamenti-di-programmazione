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
        self.stringa=''
        #crea una stringa con tutti gli elementi (ordinati) della griglia, e riempie gli spazi vuoti con 'W'
        for j in range (len(griglia)):
            for i in range(len(griglia[0])):
                if griglia[j][i]=='':
                    self.stringa+='W'
                else:
                    self.stringa+=griglia[j][i]
        self.lista_wcomb=[]
        #ritorna una lista che contiene le stringhe interessanti per determinare il tipo di nodo
        st_nome=self.stringa
        str1=st_nome[:3]
        str2=st_nome[3:6]
        str3=st_nome[6:]
        str4=st_nome[0]+st_nome[3]+st_nome[6]
        str5=st_nome[1]+st_nome[4]+st_nome[7]
        str6=st_nome[2]+st_nome[5]+st_nome[8]
        str7=st_nome[0]+st_nome[4]+st_nome[8]
        str8=st_nome[2]+st_nome[4]+st_nome[6]
        self.lista_wcomb+=str1, str2, str3, str4, str5, str6, str7, str8
    
    def tipo(self):
        if 'xxx' in self.lista_wcomb:
            return 'x'
        elif 'ooo' in self.lista_wcomb:
            return 'o'
        elif 'W' in self.stringa:
            return '?'
        else:
            return '-'
    
    def next_player(self):
        if self.stringa.count('o')>self.stringa.count('x'):
            return 'x'
        else:
            return 'o'
        
    def esiti(self):
        #conta quante volte c'� tipo '-', tipo'o', tipo 'x'. 
        lista=[]
        lista=c_tipi(self, lista)
        patte=lista.count('-')
        Vo=lista.count('o')
        Vx=lista.count('x')
        tripla=(patte, Vo, Vx)
        return tripla
    
    def vittorie_livello(self, giocatore, h):
        H=0
        n_vittorie=0
        n_vittorie=is_vl(self, H, h, giocatore, n_vittorie)
        return n_vittorie  
    
    
    def strategia_vincente(self,giocatore):
        print(listX)
        if has_hand(self, giocatore)==1 and 0 not in listX:
            print(listX)
            return True
        else:
            return False
            
        
        
''' fuori dalla classe'''
    
def c_tipi(nodo, lista):
    #funzione esterna alla classe, che dice EDDAJE ogni volta che c'� da processare un nodo.Ricorsiva su 
    #gen_tree(nodo.nome).lista_figli. 
    if nodo.tipo()!='?':
        lista.append(nodo.tipo())
    else:
        for el in gen_tree(nodo.nome).lista_figli:
            #print(el.nome, p, o, x, 'ok')
            lista=c_tipi(el, lista)
            #print(el.nome, p,o,x, 'dopo')
    #print(p, o, x, 'nodo')
    return lista
       
        
        
def is_vl(nodo,H, h, giocatore, n_vittorie):#verifica se il nodo e a livello h, e se e di vittoria
    #print(H, h, n_vittorie, 'figlio', nodo.nome)
    if H==h:#se e' il livello giusto
        #print('ok', nodo.nome)
        if nodo.tipo()==giocatore:
            n_vittorie+=1 
            #print(n_vittorie, 'vitt')
    else:
        H+=1
        #print(nodo.nome, 'padre')
        for el in gen_tree(nodo.nome).lista_figli:
            n_vittorie=is_vl(el, H, h, giocatore, n_vittorie) #aggiorna il contatore delle vittorie 
            #con le vittorie che ci sono nei nodi figli
    return n_vittorie
        
        
        
def gen_tree(griglia):
    root=NodoTris(griglia)
    #print(root.nome, 'entra')
    #print(root.tipo())
    if root.tipo()=='?':
        #se la partita non e terminata
        W_in_root=[]
        n=1
        m=0
        mossa=root.next_player()
        while n<=root.stringa.count('W'):
            #cerco quanti spazi vuoti ci sono
            pos=root.stringa.find('W', m)
            W_in_root.append(pos)
            m=pos+1
            n+=1
            #print(pos, 'pos')
        #print(W_in_root)
        for el in W_in_root:
            new_griglia=build_ng(griglia, el,mossa)
            #print(root.nome, 'nome')
            #print(root.lista_figli, 'figli')
            root.lista_figli+=[gen_tree(new_griglia)]
            #riempio uno spazio nuovo alla volta con il gicatore seguente
    return root

def build_ng(griglia, c,mossa ):
    new_g=[['','',''],['','',''],['','','']]
    for j in range(3):
        for i in range(3):
            new_g[j][i]=griglia[j][i]
    new_g[c//3][c%3]=mossa
    return new_g

def print_gen_tree(nodo, level):
    #print('    '*level+str(nodo.nome))
    for el in nodo.lista_figli:
        print_gen_tree(el, level+1)
    return

def has_hand(nodo, giocatore,):
    #metto in una lista tutte le foglie ottenute da quella radice
    global listX
    listX=[]
    if nodo.tipo()=='?': 
        lista=gen_tree(nodo.nome).lista_figli
        if giocatore==nodo.next_player() and nodo.next_player() in tipi_figli(lista):
            #se posso vincere con una mossa e fatta.
            print('vinco')
            return 1
        elif giocatore==nodo.next_player():
            #se sono io a giocare ma non posso vincere, ricomincio la funzione.
            print('ricominciamo')
            for el in lista:
                    has_hand(el, giocatore)
        else: #se tocca a lui.
            print('suo turno')
            for el in lista:
                listX.append(has_hand(el, giocatore))
                
    else:
        print('finita')
        return 0
    
    
def tipi_figli(lista):
    tipi_f=[]        
    for el in lista:
        tipi_f.append(el.tipo())
    return tipi_f

'''

test_program2_6                ok       173786.940 ms   
si applica il metodo esiti() al nodo radice dell'albero di gioco che 
    rappresenta la configurazione iniziale dove tutte le celle sono libere.'''