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

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        
        
    def tipo(self):
        matrice = self.nome
        #matrix = lista(matrice)
        #print(matrix)
        return vittoria(matrice)
    def esiti(self):
        matrice = self.nome
        #matrix = lista(matrice)
        albero = gen_tree(matrice)
        esiti=contaEsiti([],albero)
        return(esiti.count('-'),esiti.count('o'),esiti.count('x'))
        
    
    def vittorie_livello(self, giocatore, h):
        matrice=self.nome
        lista=gen_tree3(matrice,h,giocatore)
        return len(lista)
    

    def strategia_vincente(self,giocatore):
        matrice = self.nome
        albero = gen_tree(matrice)
        return strategia(albero,giocatore,False)
        
        
def lista(matrice):
    lista = []
    for x in matrice:
        for y in x:
            if y == '':
                y = 'v'
            lista.append(y)
    return lista
        

        
def gen_tree(griglia):
    griglia = lista(griglia)
    nodo = NodoTris(griglia)
    #print(nodo.nome)
    vuoti = 0
    tic='v'
    #print(nodo.nome)
    for riga in nodo.nome:
        
            if riga == 'v':
                vuoti += 1
    if vuoti % 2 == 0:
        tic = 'o'
    else:
        tic = 'x'
    return gen_tree1(griglia,tic)
    
def gen_tree1(griglia,tic):
    if tic == 'o':
        tic = 'x'
    elif tic == 'x':
        tic = 'o'
    nodo = NodoTris(griglia)
    matrice = nodo.nome
    #print(matrice)
    if vittoria(matrice) == '?':
        #print(len(matrice),matrice)
        for riga in range(0,9):
                    if matrice[riga] == 'v' :
                        matrice1 = matrice[:]
                        matrice1[riga] = tic
                        (nodo.lista_figli).append(gen_tree1(matrice1,tic))
    #print(matrice,vittoria(matrice))
    #print(matrice)
    #print(numero)
    return nodo
 
counter = 0 
def contaNodi(nodo,contatore,lista):
    figli = nodo.lista_figli
    if len(figli)==0:
        lista.append('a')
    else:
        for figlio in figli:
            contaNodi(figlio,contatore,lista)
    return len(lista)

        
def vittoriaVerticale(matrice,posizione):
    if matrice[posizione] == matrice[posizione+3] == matrice[posizione+6] and matrice[posizione] != 'v' :
        return True
    else:
        return False
    
def vittoriaOrizzontale(matrice,posizione):
    #print(matrice)
    if matrice[posizione] == matrice[posizione+1] == matrice[posizione+2]  and matrice[posizione] != 'v':
        return True
    else:
        return False
    
def vittoriaDiagonale1(matrice,posizione):
    if matrice[posizione] == matrice[posizione+4] == matrice[posizione+8]  and matrice[posizione] != 'v':
        return True
    else:
        return False
    
def vittoriaDiagonale2(matrice,posizione):
    if matrice[posizione] == matrice[posizione+2] == matrice[posizione+4]  and matrice[posizione] != 'v':
        return True
    else:
        return False

def vittoria(matrice):
    risultato=''
    #matrice = lista(matrice)
    #print(matrice)
    if vittoriaOrizzontale(matrice,0) or vittoriaVerticale(matrice,0) or vittoriaDiagonale1(matrice,0):
        risultato=matrice[0]
        #print(matrice[0])
    elif vittoriaOrizzontale(matrice,3):
        risultato=matrice[3]
        #print(matrice[3])
    elif vittoriaOrizzontale(matrice,6):
        risultato=matrice[6]
        #print(matrice[6])
    elif vittoriaVerticale(matrice,1):
        risultato=matrice[1]
        #print(matrice[1])
    elif vittoriaVerticale(matrice,2):
        risultato=matrice[2]
        #print(matrice[2])
    elif vittoriaDiagonale2(matrice,2):
        risultato=matrice[2]
        #print(risultato)
    else:
        for x in matrice:
                if 'v' not in matrice:
                    risultato = '-'
                else:
                    risultato = '?'
    return risultato
    
   
def contaEsiti(lista,albero):
    rad = albero.nome
    figli = albero.lista_figli
    #print(figli)
    #print(vittoria(rad),rad)
    if len(figli)==0:
        lista.append(vittoria(rad))
        #print('cccccccccccccc')
    else:
        for matrice in figli:
            #print('vvvvvvvvvvvvvvvvv')
            #print('cacca')
            contaEsiti(lista,matrice)
    return lista
    
    


def gen_tree3(griglia,H,giocatore):
    livello = 0
    griglia = lista(griglia)
    nodo = NodoTris(griglia)
    vuoti = 0
    tic=''
    #print(nodo.nome)
    for riga in nodo.nome:
        for casella in riga:
            if riga == 'v':
                vuoti += 1
    if vuoti % 2 == 0:
        tic = 'o'
    else:
        tic = 'x'
    return gen_tree4(griglia,tic,livello,H,[],giocatore)
    
def gen_tree4(griglia,tic,livello,H,listaNodi,giocatore):
    nodo = NodoTris(griglia)
    matrice = nodo.nome
    if livello != H:
        livello+=1
        if tic == 'o':
            tic = 'x'
        elif tic == 'x':
            tic = 'o'
        
        #print(matrice)
        if vittoria(matrice) == '?':
            for riga in range(0,9):
                        if matrice[riga] == 'v' :
                            matrice1 = matrice[:]
                            matrice1[riga] = tic
                            (nodo.lista_figli).append(gen_tree4(matrice1,tic,livello,H,listaNodi,giocatore))
    else:
        if vittoria(matrice) == giocatore:
            listaNodi.append(matrice)
        
    #print(matrice)
    #print(numero)
    return listaNodi

def strategia(radice,giocatore,vit):
    for nodo in radice.lista_figli:
        if vittoria(nodo.nome) == giocatore :
            #print ('entrooooooo')
            #print(vittoria(nodo.nome))
            vit=True
            return vit
        else:
            vit = strategia(nodo,giocatore,vit)
            if vit:
                return vit
            #print(vit)
    #print(vit)
        return vit
    return vit
