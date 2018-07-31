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

Data una configurazione C del gioco, l'albero di gioco per 
 e' l'albero che 
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
import copy 

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []
        
    
    def dia(self,carattere):
       if self.nome[0][0]==carattere and self.nome[1][1]==carattere and self.nome[2][2]==carattere:
           return True
       if self.nome[0][2]==carattere and self.nome[1][1]==carattere and self.nome[2][0]==carattere:
           return True
       return False
    
    def tipo(self):
      indice=self.ti()
      maxi=9
      if self.orizzontale(0,0,'x')==1 or self.verticale(0,0,'x')==1 or self.dia('x'):
          return 'x' 
      if self.orizzontale(0,0,'o')==1 or self.verticale(0,0,'o')==1 or self.dia('o'):
          return 'o'
      if len(indice)!=maxi:
          return '?'
      return'-'    
     
    def ti(self):
        return [(colonna,riga) for colonna in range(3) for riga in range(3) if self.nome[colonna][riga]!='']
    
    def turno(self,vuoti):
      if len(vuoti)%2==0:return 'o' 
      else: return 'x'
           
    def coplout(self,lista):
      lout=[]
      for el in lista:
        lout.append(el)
      return lout   
    
    def copgri(self):
      griglia=[]
      for h in range(3):
        lout=[]
        for w in range(3):
            lout.append(self.nome[h][w])
        griglia.append(lout)  
      return griglia     
    
    def orizzontale(self,colonna,riga,carattere):
        w,q=1,2
        if (self.nome[colonna][riga]==carattere) and (self.nome[colonna][riga+w]==carattere) and (self.nome[colonna][riga+q]==carattere):
            return 1            
        if ((colonna+w<3 )and (self.orizzontale(colonna+w,riga,carattere))): 
            return 1
        return 0           
          
    def verticale(self,colonna,riga,carattere):
       if self.nome[colonna][riga]==carattere and self.nome[colonna+1][riga]==carattere and self.nome[colonna+2][riga]==carattere:
           return 1            
       if riga+1<3 and self.verticale(colonna,riga+1,carattere): 
           return 1 
       return 0 
    
    def contresi(self,combinazione):
        if self.tipo()=='?': 
          for no in self.lista_figli: no.contresi(combinazione)
        if self.tipo()=='-':combinazione[0]+=1    
        elif self.tipo()=='o':combinazione[1]+=1
        elif self.tipo()=='x':combinazione[2]+=1
        return combinazione
    
    def esiti(self):
      combinazione=self.contresi([0,0,0])
      return tuple(combinazione) 
    
    def vittorie_livello(self, giocatore, h):
      cont=0
      level=0
      return self.levelwin(giocatore,h,level,cont)
    
    def levelwin(self,giocatore,h,level,cont): 
      if self.tipo()==giocatore and level==h:
          cont+=1  
      if level<h:
        level+=1
        for no in self.lista_figli:
          cont=no.levelwin(giocatore,h,level,cont)
      return cont
                 
    def to_tree(self):
      vuoti=self.lvuoti()
      carattere=self.turno(vuoti)
      self.son(vuoti,carattere)   
      return

    def lvuoti(self):
        return [(riga,colonna) for riga in range(3) for colonna in range(3) if self.nome[riga][colonna]=='']
    
    def son(self,none,carattere):
      if  self.tipo()=='x' or self.tipo()=='o' or self.tipo()=='-':return        
      self.boh(none,carattere)
      
    def boh(self,none,carattere):
        for el in none:
            griglia=self.copgri()
            lagg=self.coplout(none)
            riga=el[0]
            colonna=el[1]
            if carattere:
              griglia[riga][colonna]='o'
              agg=False
            else:
              griglia[riga][colonna]='x'
              agg=True
            lagg.remove((riga,colonna))
            appo=NodoTris(griglia)
            self.lista_figli.append(appo)
            appo.son(lagg,agg) 
    
    def strategia_vincente(self,giocatore):
        if self.tipo()==giocatore:
            return True
        for y in range(len(self.lista_figli)-1):
          if  self.tipo()!='-':  
              if self.tipo()==giocatore: return True      
              self.strategia_vincente(giocatore)
              
        return False        
    
def gen_tree(griglia):
  '''inserire qui il vostro codice'''
  griglia=NodoTris(griglia)
  griglia.to_tree()
  return griglia


def count_fstree( node): 
    ''' Ritorna il numero di nodi dell'albero di radice root''' 
    count = 1
    for child in node.content:
        count += count_fstree( child) 
    return count

def find_fstree( node, name):
    ret = [] 
    if os.path.basename( node.path) == name: 
        ret += [node] 
        for child in node.content: 
            ret += find_fstree( child, name) 
        return ret


  
  
  
  
