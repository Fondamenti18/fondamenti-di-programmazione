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
from copy import deepcopy
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        self.p=''
        if self.nome[0][0] == self.nome[0][1]  and self.nome[0][1] == self.nome[0][2]:
            self.p=self.nome[0][0]
        if self.nome[1][0] == self.nome[1][1] and self.nome[1][1] == self.nome[1][2]:
            self.p=self.nome[1][0]
        if self.nome[2][0] == self.nome[2][1]  and self.nome[2][1]== self.nome[2][2]:
            self.p=self.nome[2][0]
        if self.nome[2][0] == self.nome[2][1]  and self.nome[2][1]== self.nome[2][2]:
            self.p=self.nome[2][0]        
        if self.nome[0][0] == self.nome[1][1]  and self.nome[1][1]== self.nome[2][2]:
            self.p=self.nome[0][0]    
        if self.nome[0][2] == self.nome[1][1]  and self.nome[1][1]== self.nome[2][0]:
            self.p=self.nome[2][0]    
        if self.nome[0][0] == self.nome[1][0]  and self.nome[1][0]== self.nome[2][0]:
            self.p=self.nome[2][0] 
        if self.nome[0][1] == self.nome[1][1]  and self.nome[1][1]== self.nome[2][1]:
            self.p=self.nome[0][1]    
        if self.nome[0][2] == self.nome[1][2]  and self.nome[1][2]== self.nome[2][2]:
            self.p= self.nome[2][2]
        trovato = False
        if self.p=='':
            for x in self.nome:
                for y in x:
                    if y == '':
                        trovato= True
                        break
            if trovato == True:
                 self.p='?'
            else: self.p= '-'
        return self.p    
 
        
    def esiti(self):
        self.patta= 0
        self.x= 0
        self.o= 0
        self.patta,self.o,self.x= contaesiti(self.patta,self.o,self.x,self)
        return self.patta,self.o,self.x
    
    def vittorie_livello(self, giocatore, h):
        self.vittorie=0
        self.vittorie= livelli(self,0,giocatore,self.vittorie,h)
        return self.vittorie
    
    def strategia_vincente(self,giocatore):
        for x in self.lista_figli:
            o,x= strategia(x,giocatore,0,0)
        if giocatore == 'x':
            if x > o:
                return True
            else: return False
        else: 
            if o > x:
                return True
            else: return False
        
        
def gen_tree(griglia):
    radice= NodoTris(griglia)
    spazi= spazivuoti(griglia)
    if spazi %2 != 0:
        radice.lista_figli=figli(griglia,'o',radice)
    else:
        radice.lista_figli=figli(griglia,'x',radice)
    return radice       
        
def figli(griglia,giocatore,alb):
    i=0
    '''print(alb.tipo(),'alb.nome:',alb.nome)'''
    
    while i < 3:
        j=0
        while j < 3:

            if controlla(alb.nome) == False:
                if griglia[i][j] == '':  
                    ripa= deepcopy(griglia)
                    ripa[i][j]= giocatore
                    figlio=NodoTris(ripa)
                    alb.lista_figli+=[figlio]
                    spazi=spazivuoti(ripa)
                    
                    if spazi %2 != 0:     
                        figlio.lista_figli=figli(ripa,'o',figlio)
                        
                    else:
                        figlio.lista_figli=figli(ripa,'x',figlio)
                       
            
            j+=1
        i+=1    
    
    return alb.lista_figli 
        
def contaesiti(patta,o,x,nodo):  
      
    if nodo.tipo() == '-':
       patta+=1

    elif nodo.tipo() == 'x':   
         x+=1

    elif nodo.tipo() == 'o':
        o+=1

    i=0
    while i< len(nodo.lista_figli):
        
        patta,o,x=contaesiti(patta,o,x,nodo.lista_figli[i])
        i+=1
    return patta,o,x     

def printa(padre,griglia,livello):
    print(livello,'padre:',gen_tree(griglia).nome)
    for x in gen_tree(griglia).lista_figli:
        print(livello,'figlio:',x.nome)
        printa(x,x.nome,livello+1)

def spazivuoti(griglia):
    i=0
    cont=0
    while i < 3:
        j=0
        while j<3:
            if griglia[i][j]=='':
                cont+=1
            j+=1    
        i+=1
    return cont   

def livelli(nodo,livello,giocatore,vittorie,h):
    if livello == h:
        if nodo.tipo() == giocatore:
            
            vittorie+=1
    elif livello < h:
        i=0

        while i < len(nodo.lista_figli):

            vittorie= livelli(nodo.lista_figli[i],livello+1,giocatore,vittorie,h)
            i+=1
       
    return vittorie    


def strategia(nodo,giocatore,o,x):
    
    if nodo.tipo() == 'o':
       o+=1
    elif nodo.tipo() == 'x':
       x+=1         
    i=0
    while i < len(nodo.lista_figli):
        o,x=strategia(nodo.lista_figli[i],giocatore,o,x)
        i+=1
    return o,x    
   
          
def printfigli(griglia):
    for x in gen_tree(griglia).lista_figli[1].lista_figli[0].lista_figli[0].lista_figli:
        print(x.nome)
                    
'''def gen_tree(griglia):
    nodo= NodoTris(griglia)
    if controlla(nodo.nome) == False:
        a,b=figli(nodo.nome)
        for x in range(0,b):
            nodo.lista_figli.append(gen_tree(a[x])) 
    return nodo

def figli(griglia):
    lista=[]
    possibili=[]
    n=0
    x=0
    o=0
    for r in range(0,3):
        for c in range(0,3):
            if griglia[r][c] == 'x':
                x+=1
            elif griglia[r][c] == 'o':
                o+=1
            else:
                n+=1
                possibili.append((r,c))
    if x == o:
        for i in range(0,n):
            app= deepcopy(griglia)
            app[possibili[i][0]][possibili[i][1]]= 'o'
            lista.append(app)  
            
    if o > x and o < 5:
        for i in range(0,n):
            app= deepcopy(griglia)
            app[possibili[i][0]][possibili[i][1]]= 'o'
            lista.append(app)  
    return lista,n      
'''
def controlla(nome):
        if nome[0][0] == nome[0][1]  and nome[0][1] == nome[0][2] and nome[0][0] != '':
            return True
        elif nome[1][0] == nome[1][1] and nome[1][1] == nome[1][2] and nome[1][0] != '':
            return True
        elif nome[2][0] == nome[2][1]  and nome[2][1]== nome[2][2] and nome[2][0] != '':
            return True
        elif nome[2][0] == nome[2][1]  and nome[2][1]== nome[2][2] and nome[2][0] != '':
            return True        
        elif nome[0][0] == nome[1][1]  and nome[1][1]== nome[2][2] and nome[0][0] != '':
            return True    
        elif nome[0][2] == nome[1][1]  and nome[1][1]== nome[2][0] and nome[0][2] != '':
            return True  
        elif nome[0][0] == nome[1][0]  and nome[1][0]== nome[2][0] and nome[0][0] != '':
            return True 
        elif nome[0][1] == nome[1][1]  and nome[1][1]== nome[2][1] and nome[0][1] != '':
            return True   
        elif nome[0][2] == nome[1][2]  and nome[1][2]== nome[2][2] and nome[0][2] != '':
            return True
        return False
    
def printO(nodo,cont=0):
    if nodo.tipo() == 'o':
        cont+=1
        print('nodo:',nodo.nome)
    for x in nodo.lista_figli:
        cont=printO(x,cont)
        
    return cont    
        
def printalivello(nodo,livello,cont):
    if livello == 5 and nodo.tipo()== 'o':
        print('griglia:',nodo.nome)
        cont+=1
    for x in nodo.lista_figli:
        cont=printalivello(x,livello+1,cont)
        
    return cont    