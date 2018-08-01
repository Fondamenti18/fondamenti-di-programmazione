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

import copy 
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli

    
    def tipo(self):
        l=[[self.nome[0][0],self.nome[1][1],self.nome[2][2]],[self.nome[2][0],self.nome[1][1],self.nome[0][2]]]
        for i in range(3):
            l.append([self.nome[0][i],self.nome[1][i],self.nome[2][i]])
        l+=self.nome
     
        c=pieni(self.nome)[0]
     
        for el in l:
            
            if el[0]==el[1]==el[2] and el[0]!='':
              
                return str(el[0])
        if c==9:
            return'-'
        else:
            return '?'
        
    def esiti(self):
        return tuple(self.es_ric([0,0,0]))   
        
    def vittorie_livello(self, giocatore, h):
        return self.lev(0,h,giocatore,0)
  
    def es_ric(self,l):
        if self.tipo()=='?': 
            for el in self.lista_figli: 
                el.es_ric(l)
        if self.tipo()=='-':
            l[0]+=1
            
        if self.tipo()=='o':
            l[1]+=1
            
        if self.tipo()=='x':
            l[2]+=1
        
        return l  

    def ramo(self,l,turno):
      if  self.tipo()=='x' or self.tipo()=='o' or self.tipo()=='-':
          return        
      for i in l:
        griglia=copy.deepcopy(self.nome)
        l_nuova=copy.deepcopy(l)
        y=i[0]
        x=i[1]
        if turno:
          griglia[y][x]='o'
          boo=False
        else:
          griglia[y][x]='x'
          boo=True
        l_nuova.remove((y,x))
        nodo=NodoTris(griglia)
        self.lista_figli.append(nodo)
        nodo.ramo(l_nuova,boo)   
    

  

    
    def lev(self,cont,alt,giocatore,l): 
      if self.tipo()==giocatore and l==alt:
          cont+=1  
      if alt>l:
        l+=1
        for i in self.lista_figli:
          cont=i.lev(cont,alt,giocatore,l)
      
      return cont
      
  
    
    
    
    def chivince(self,M,giocatore): 
       if self.tipo()==giocatore:
           return True
       if M>0:
         self.strategia_vincente(giocatore) 
    
    def strategia_vincente(self,giocatore):
        if self.tipo()==giocatore:
            return True
        M=len(self.lista_figli)
        for indx in range(1,M):
          if self.lista_figli[indx].chivince(M,giocatore)==True and self.tipo()!='-':
              return True
        return False      
    
    

def turno(griglia):
    c=9-pieni(griglia)[0]
    if c%2==0:
        return 'o' 
    else: 
        return 'x'
    
def pieni(griglia):
    c=0
    vuoti=[]
    for y in range(3):
        for x in range(3):
            if griglia[y][x]!='':
                c+=1
            else: vuoti+=[(y,x)]
    return c,vuoti

def gen_tree(griglia):
    l=pieni(griglia)[1]      
    t=turno(griglia)
    albero=NodoTris(griglia)
    albero.ramo(l,t)
    return albero

    














g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]

lista=[g1, g2, g3, g4]
lista1=[gen_tree(x) for x in lista]  
print([x.esiti() for x in lista1])


'''g5=[['', 'x', ''], ['', 'o', ''], ['', '', '']]
g6=[['', 'o', ''], ['', 'x', ''], ['', '', '']]
g7=[['', 'x', 'o'], ['', '', ''], ['', '', '']]
g8=[['', 'o', 'x'], ['', '', ''], ['', '', '']]
listab=[g5, g6, g7, g8]
lista1=[gen_tree(x) for x in listab]
print([y.strategia_vincente('o') for y in lista1])'''  
