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
from copy import deepcopy
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
        res=self.tipo()
        if(res=='-' or res=='o' or res=='x'):
           return 
       
        carattere=cercaCarattere(self.nome)
        for i in range(len(self.nome)):
           for z in range(len(self.nome[0])):
               if(self.nome[i][z]==''):
                   figlio=deepcopy(self.nome)
                   figlio[i][z]=carattere
                   self.lista_figli+=[NodoTris(figlio)]
            
            
    def tipo(self):
       '''inserire qui il vostro codice'''
       l=['o','x']
       for p in l:
           #Verticali
           if(p == self.nome[0][0] and p== self.nome[1][0] and p == self.nome[2][0]):
               return p
           if(p == self.nome[0][1] and p== self.nome[1][1] and p == self.nome[2][1]):
               return p
           if(p == self.nome[0][2] and p== self.nome[1][2] and p == self.nome[2][2]):
               return p
           #Orizzontali
           if(p == self.nome[0][0] and p== self.nome[0][1] and p == self.nome[0][2]):
               return p
           if(p == self.nome[1][0] and p== self.nome[1][1] and p == self.nome[1][2]):
               return p
           if(p == self.nome[2][0] and p== self.nome[2][1] and p == self.nome[2][2]):
               return p
           #Obliqui
           if(p == self.nome[0][0] and p== self.nome[1][1] and p == self.nome[2][2]):
               return p
           if(p == self.nome[0][2] and p== self.nome[1][1] and p == self.nome[2][0]):
               return p
               
       for p in self.nome:
           for i in p:
               if(i==''):
                   return '?'
           
       return '-'
        
        
        
    def esiti(self,patta=0,vo=0,vx=0):
       '''inserire qui il vostro codice'''
       #print(self.nome)
       res=self.tipo()
       if(res =='-'):
           return(patta+1,vo,vx)
       if(res =='o'):
           return(patta,vo+1,vx)
       if(res =='x'):
           return(patta,vo,vx+1)
       
       for child in self.lista_figli:
           patta,vo,vx=child.esiti(patta,vo,vx)
       
       
       
       return patta,vo,vx
   
    def vittorie_livello(self, giocatore, h,vittoria=0,altezza=-1):
       '''inserire qui il vostro codice'''
       #print(h,altezza)
       if(altezza+1>h):
          return vittoria
       
       res=self.tipo()
       if(res==giocatore and h==altezza+1):
           return vittoria+1
       
       if(res=='-' or res=='o' or res=='x'):
           return vittoria
       
       for child in self.lista_figli:
           vittoria=child.vittorie_livello(giocatore,h,vittoria,altezza+1)
    
       return vittoria
   
    
    
    def strategia_vincente(self,giocatore):
       '''inserire qui il vostro codice'''
       p,o,x=self.esiti()
       
       if(giocatore=='o' and o>=1 ):
           return True
       if(giocatore=='x' and x>=1 ):
           return True
       
       return False
   
    def __str__(self):
       return str(self.nome)
   
    
def cercaCarattere(griglia):
   contO=0
   contX=0
   for p in griglia:
       for z in p:
           if(z=='o'):
               contO+=1
           elif(z=='x'):
               contX+=1
   
   car=''
   if(contO>contX):
       car='x'
   elif(contO==contX):
       car='o'
  
   return car

def gen_tree(griglia):
   '''inserire qui il vostro codice'''
   n=NodoTris(griglia)
   return n