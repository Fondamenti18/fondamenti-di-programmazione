'''
    
def controllo(self,cont):         #successivamente va dentro la classe      it works!
    x=0
    if cont<2:
        while x<3:
            if cont==0 and self.nome[x][0]!='':
                if (self.nome[x][0]== self.nome[x][1] and self.nome[x][0]==self.nome[x][2]):    #controlli verticali ed orizzontali
                    self.winner=self.nome[x][0]
              
                    return(0)
            elif cont==1 and self.nome[0][x]!='':
                 if (self.nome[0][x]== self.nome[1][x] and self.nome[0][x]==self.nome[2][x]):
                    self.winner=self.nome[0][x]
     
                    return(0)
            x=x+1
    elif cont==2:                 #controllo obliquo
        if self.nome[1][1]!='' and ((self.nome[0][0]== self.nome[1][1] and self.nome[0][0]==self.nome[2][2]) or (self.nome[0][2]==self.nome[1][1] and self.nome[0][2]==self.nome[2][0])):
            self.winner=self.nome[1][1]

            return(0)
    if cont>2:
        x,o=self.conta()
        if o==5:
            self.winner="-"

        else:
            self.winner="?"

        return(0)
            
        
    cont=cont+1
    controllo(self,cont)  

    
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata 
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
def testtt():
	start=(time.perf_counter())
	g7=[['', '', ''], ['', '', ''], ['', '', '']]
	l=gen_tree(g7)
	end=(time.perf.counnter())
	print("tempo ",end-start)

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.

ATTENZIONE: i test vengono eseguiti con un timeout globale di 2*N secondi (se il grader esegue N test).
gen_tree([['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']])
print (self.lista_figli) appena sotto self.lista_figli, in __init__ , o print NodoTris(oggetto).lista_figli esterno alla classe
boh([['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']])


            if x.winner==giocatore:
                print("entro",c,x.nome,x.winner)
                c+=1
                if c>1:
                    return(True)
            elif x.winner!=giocatore and x.winner!='?'  and x.winner!='-':
                print("esco",x.nome,x.winner)
                c=0
        for x in self.lista_figli:
            x.strategia_vincente(giocatore)
        return(False)











lista=list(self.nome)
        j=0
        x=0
        peso=0
        while x<3:
            print("x = ",x)
            peso=0
            j=0
            while j<3:
             

             print("j = ",j)
                            if (j+1 <3) and (lista[x][j]==lista[x][j+1]):      #controllo in orizzontale
                                
                                peso=peso+1
                                print("p",peso)
                           # else:
                                #peso=0
                            j=j+1
                        if peso==2:
                            print(lista[x])
                            break
                        x=x+1







                         while x<3:                  
        j=0
        peso=0
        peso1=0
        while j<3:
            if (j+1<3) and lista[x][j]==lista[x][j+1] and lista[x][j]!='':   #controllo orizzontale
                peso=peso+1
                b=lista[x][j]
            else:
                peso=0
            j+=1
            if peso==2 or peso1==2:
                return(b)
        x+=1
    return(0)





 for x in self.lista_figli:
            if x.winner=='o':
                NodoTris.o+=1
                #NodoTris.o=o
            elif x.winner=='x':
                NodoTris.y+=1
            elif x.winner=='-':
                NodoTris.pat+=1
            x.es()
















              def tipo(self):
        x=0
        
        while x<3:
            if self.nome[x][0]!='':
                if (self.nome[x][0]== self.nome[x][1] and self.nome[x][0]==self.nome[x][2]):    #controlli verticali ed orizzontali
                    self.winner=self.nome[x][0]
                    #print("£sa")
                    return(self.winner)
            if self.nome[0][x]!='':
                 if (self.nome[0][x]== self.nome[1][x] and self.nome[0][x]==self.nome[2][x]):
                    self.winner=self.nome[0][x]
                    #print("aaa",self.winner)
                    return(self.winner)
            x=x+1
        if self.nome[1][1]!='' and ((self.nome[0][0]== self.nome[1][1] and self.nome[0][0]==self.nome[2][2]) or (self.nome[0][2]==self.nome[1][1] and self.nome[0][2]==self.nome[2][0])):
            self.winner=self.nome[1][1]

            return(self.winner)
        
        x,o=self.conta()
        if o==5:
            self.winner="-"

        else:
            self.winner="?"

        return(self.winner)
            
'''      #presupporto: se o=x: in corso o vittoria delle x. se o>x: patta oppure vittoria delle o
from copy import deepcopy
import time
elementi=[]
class NodoTris:
    o=0
    y=0
    pat=0
    c1=0
    c=0
    c2=0
    def __init__(self, griglia):      #init è un costruttore, tipo list(oggetto), set(oggetto)
        #griglia1=[x[:] for x in griglia] 
        self.nome = griglia
        self.lista_figli = []           #lista dei nodi figli
        winner=""
        #h=0
        #print(self.lista_figli)

            
           
    def conta(self):    #funzione per calcolare la mossa
        cont=0
        cont1=0
        for v in self.nome:
            for b in v:
                if b=='x':
                    cont=cont+1
                elif b=='o':
                    cont1+=1
        #if cont>=cont1:
           # first='o'
      #  elif cont1>cont:
           # first='x'
        #print(cont,cont1)
        return(cont,cont1)    #restituisce quante x e quante o ci sono. in quest ordine
    
            

    def tipo(self):
        x=0
        
        while x<3:
            if self.nome[x][0]!='':
                if (self.nome[x][0]== self.nome[x][1] and self.nome[x][0]==self.nome[x][2]):    #controlli verticali ed orizzontali
                    self.winner=self.nome[x][0]
                    #print("£sa")
                    return(self.winner)
            if self.nome[0][x]!='':
                 if (self.nome[0][x]== self.nome[1][x] and self.nome[0][x]==self.nome[2][x]):
                    self.winner=self.nome[0][x]
                    #print("aaa",self.winner)
                    return(self.winner)
            x=x+1
        if self.nome[1][1]!='' and ((self.nome[0][0]== self.nome[1][1] and self.nome[0][0]==self.nome[2][2]) or (self.nome[0][2]==self.nome[1][1] and self.nome[0][2]==self.nome[2][0])):
            self.winner=self.nome[1][1]

            return(self.winner)
        
        x,o=self.conta()
        if o==5:
            self.winner="-"

        else:
            self.winner="?"

        return(self.winner)
        
    
        
    def esiti(self):
        #print(self.winner)
        NodoTris.o=0
        NodoTris.y=0
        NodoTris.pat=0
        #self.es(0,0,0)
        self.es()
        a=NodoTris.o
        b=NodoTris.y
        c=NodoTris.pat
        #print(a,b,c)
        u=()
        u+=(c,a,b)
        return(u)
        

    def es(self):
        if self.winner=='o':
            NodoTris.o+=1
            #NodoTris.o=o
        elif self.winner=='x':
            NodoTris.y+=1
        elif self.winner=='-':
            NodoTris.pat+=1
        for x in self.lista_figli:
            x.es()

      
        
    
    def vittorie_livello(self, giocatore, h):
        NodoTris.c=0
        c=self.livello(giocatore,h,0)
        return(NodoTris.c)
            
    def livello(self,giocatore,h,manz):
        
        if h==0:
            if self.winner==giocatore:
                return(1)
        for x in self.lista_figli:
            manz+=1      #IMPORTANTE
            if x.winner==giocatore:
                if h==manz:
                   NodoTris.c+=1
            x.livello(giocatore,h,manz)
            manz-=1
        return()
        
            
    def strategia_vincente(self,giocatore):
        NodoTris.cand=0
        a=""
        #ora=self.winner
        a=self.vincente(giocatore)
        if a==1:
           # print(a)
            return(True)
        else:
           # print(a)
            return(False)
    def vincente(self,giocatore):
        c=0
       # print("entro",self.nome)
        for x in self.lista_figli:
           # print("for",x.nome,x.winner)
            y,o=x.conta()
           # print(y,o)
            if o>y and giocatore=='o':     #prima mossa del cerchio, muove e vince
                if x.winner=='o':
                    return(1)
            if y==o and giocatore=='o':   #muove x
                if x.winner=='x':      #se vince x esco
                    return(0)
                #print("camnio")
                x.vincente(giocatore)
                    
            if y<o and giocatore=='x':
                if x.winner==giocatore:
                    return(1)
            if o>=y and giocatore=='x':
                if x.winner=='o':
                    return(0)
                x.vincente(giocatore)
            #return(1)
        
        for x in self.lista_figli:
            NodoTris.c1=0
            #print("cambio",x.nome)
            x.vincente(giocatore)
        #if NodoTris.cand==1:
            #print("we")
            #return(1)
        #else:
            #return(0)
                 
    #def vincente(self,giocatore):
        
    
        
            

            

def gen_tree(griglia):
    gri=deepcopy(griglia)
    elemento=NodoTris(gri)        
                           
    elemento.tipo()
    if elemento.winner!='o' and elemento.winner!='x':
        j=0
        x=0

        #elemento=NodoTris(gri)        
                           
        elemento.tipo()
        cont=0
        cont1=0
        for v in gri:
                for b in v:
                    if b=='x':
                        cont=cont+1
                    elif b=='o':
                        cont1+=1
        if cont>=cont1:
                first='o'
        elif cont1>cont:
                first='x'
      

        #if elemento.winner=='?': #or elemento.winner=='-'
        while x <3:      
            j=0
        
            while j<3:
                 
                if gri[x][j]=='':               #se c'è posto vuoto nella griglia:
                   
                    gri[x][j]=first          
                    elemento.lista_figli.append(gen_tree(gri))         #importante: lista_figli è una lista di liste, con append gli allego la/le liste figli
                                                #ricorsione!
                    gri[x][j]=''

                j=j+1
            x=x+1

           
    return(elemento)           #ritorna la radice ma di tipo Nodo Tris
                
       
       

        

        
   

    
   




def testtt():
	start=(time.perf_counter())
	g7=[['', '', ''], ['', '', ''], ['', '', '']]
	l=gen_tree(g7)
	end=(time.perf_counter())
	print("tempo ",end-start)
    
    
    


def stampa(self):
        #self1=gen_tree(self)
        #rint("-----_",self.nome)
        for x in self.lista_figli:
            print(x.nome, x.winner)
            stampa(x)

def prova(griglia):                      #stampa i figli della radice. così
    a=gen_tree(griglia)
    print(type(a.nome))
    stampa(a)
    #a.tipo()







    
    
