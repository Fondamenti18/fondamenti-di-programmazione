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
    def copy2(self,lista):
      l_out=[]
      for i in lista:
        l_out.append(i)
      return l_out   
    
    def copy1(self):
      griglia=[]
      for i in range(3):
        l_out=[]
        for j in range(3):l_out.append(self.nome[i][j])
        griglia.append(l_out)  
      return griglia     
    
    def ori(self,col,rig,g):
      if self.nome[col][rig]==g and self.nome[col][rig+1]==g and self.nome[col][rig+2]==g:return True            
      if col+1<3 and self.ori(col+1,rig,g): return True
      return False           
          
    def ver(self,col,rig,g):
       if self.nome[col][rig]==g and self.nome[col+1][rig]==g and self.nome[col+2][rig]==g:return True            
       if rig+1<3 and self.ver(col,rig+1,g): return True 
       return False     
              
    def dia(self,g):
       if self.nome[0][0]==g and self.nome[1][1]==g and self.nome[2][2]==g:return True
       if self.nome[0][2]==g and self.nome[1][1]==g and self.nome[2][0]==g:return True
       return False
    
    def tipo(self):
      '''inserire qui il vostro codice'''
      index_mat=[(col,rig) for col in range(3) for rig in range(3) if self.nome[col][rig]!='']  
      if self.ori(0,0,'x') or self.ver(0,0,'x') or self.dia('x'):return 'x' 
      if self.ori(0,0,'o') or self.ver(0,0,'o') or self.dia('o'):return 'o'
      if len(index_mat)!=9:return '?'
      return'-'    
     
    
    def chi_tocca(self,l_vuoti):
      if len(l_vuoti)%2==0:return 'o' 
      else: return 'x'
           
    
    def gen_alb(self):
      '''inserire qui il vostro codice'''
      x=0
      o=0
      l_vuoti=[(riga,col) for riga in range(3) for col in range(3) if self.nome[riga][col]=='']
      m_c=[(riga,col) for riga in range(3) for col in range(3)]
      g=self.chi_tocca(l_vuoti)
      self.figli(l_vuoti,g)   
      return

    
    def figli(self,l_s_vuoti,g):
      if  self.tipo()=='x' or self.tipo()=='o' or self.tipo()=='-':return        
      for i in l_s_vuoti:
        griglia=self.copy1()
        l_s_agg=self.copy2(l_s_vuoti)
        riga=i[0]
        col=i[1]
        if g:
          griglia[riga][col]='o'
          g_agg=False
        else:
          griglia[riga][col]='x'
          g_agg=True
        l_s_agg.remove((riga,col))
        appo=NodoTris(griglia)
        self.lista_figli.append(appo)
        appo.figli(l_s_agg,g_agg)
        
           
    def esit_i(self,t):
        if self.tipo()=='?': 
          for i in self.lista_figli: i.esit_i(t)
        if self.tipo()=='-':t[0]+=1    
        elif self.tipo()=='o':t[1]+=1
        elif self.tipo()=='x':t[2]+=1
        return t
    
    def esiti(self):
      '''inserire qui il vostro codice'''
      t=[0,0,0]
      t=self.esit_i(t)
      return tuple(t) 
    
    def vittorie_livello(self, giocatore, h):
      '''inserire qui il vostro codice'''  
      
      c=int()
      l=int()
      c=0
      l=0
      return self.v_l(giocatore,h,l,c)
      
    
    def v_l(self,giocatore,h,l,c): 
      if self.tipo()==giocatore and l==h:c+=1  
      if l<h:
        l+=1
        for i in self.lista_figli:
          c=i.v_l(giocatore,h,l,c)
      
      return c
       
    def s_t_r(self,giocatore,mas): 
       
 
       if self.tipo()==giocatore:return True
       
       mas_agg=mas-1
       if mas>0:
         self.strategia_vincente(giocatore) 
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        l=str()
        if self.tipo()==giocatore:return True
        mas=len(self.lista_figli)
        for i in range(1,mas):
          if self.lista_figli[i].s_t_r(giocatore,mas) and self.tipo()!='-':  return True
        return False        
          

def gen_tree(griglia):
  '''inserire qui il vostro codice'''
  griglia=NodoTris(griglia)
  griglia.gen_alb()
  return griglia

g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]

lista=[g1, g2, g3, g4]
lista1=[gen_tree(x) for x in lista]  
print([lista1[0].strategia_vincente('x'), lista1[0].strategia_vincente('o')])


'''g5=[['', 'x', ''], ['', 'o', ''], ['', '', '']]
g6=[['', 'o', ''], ['', 'x', ''], ['', '', '']]
g7=[['', 'x', 'o'], ['', '', ''], ['', '', '']]
g8=[['', 'o', 'x'], ['', '', ''], ['', '', '']]
listab=[g5, g6, g7, g8]
lista1=[gen_tree(x) for x in listab]
print([y.strategia_vincente('o') for y in lista1])'''  
  
  
  
  
  
  
  
