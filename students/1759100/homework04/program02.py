'''
Il tris e' un popolarissimo gioco. 
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


import sys
sys.setrecursionlimit(5000)
import json

class NodoTris:
    def __init__(self, griglia,primo,secondo,terzo):
        self.nome = griglia
        self.primo=primo
        self.secondo=secondo
        self.terzo=terzo
        self.lista_figli = [] #lista dei nodi figli
    def print_tree(self):
    	stringa=''
    	stringa+=self.nome
    	stringa+=' '+self.lista_figli
    	return stringa
    
#    def built(self):
    	#if self.primo.count('')>=1:

   

   # def controllo():
    def __str__(self):
    	return str(self.nome)
    def print_lista(self):
        for x in self:
          	return str(x)
    def winner(self):
        win=''
        vuoto=''
        for index in self.primo:
            if index==self.primo[0]:
                win+=index
            else:
                win+='&'
            if index=='':vuoto+='a'
        if win.count('&')<1:
            return win[0]
        for index in self.secondo:
            if index==self.secondo[0]:
                win+=index
            else:
                win+='&'
            if index=='':vuoto+='a'
        if win.count('&')<1:
            return win[0]
        for index in self.terzo:
            if index==self.terzo[0]:
                win+=index
            else :
                win+='&'
            if index=='':vuoto+='a'
        if win.count('&')<1:
            return win[0]
        for index in range(3):
            if self.primo[index]==self.secondo[index] and self.secondo[index]==self.terzo[index] :
                if self.primo[index]=='': vuoto+='a'
                return self.primo[index]
        if self.primo[0]== self.secondo[1] and self.secondo[1]==self.terzo[2]:
            if self.primo[0]=='': vuoto+='a'
            else: return self.primo[0]
        elif self.primo[2]== self.secondo[1] and self.secondo[1]==self.terzo[0]:
            if self.primo[2]=='': vuoto+='a'
            else: return self.primo[2]
        elif self.primo=='' or self.secondo=='' or self.terzo=='':vuoto+='a'
        if vuoto.count('a')<1:
            return '-'
        else:return '?'

    def tipo(self):#OK
        ''''o' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'o'
 'x' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'x'
 '-' se la configurazione rappresentata dal nodo e' una configurazione di patta
 '?' se la configurazione rappresentata dal nodo e' una configurazione di gioco non ancora terminato'''    
        if self.winner()=='o':
        	return('o')
        elif self.winner()=='x':
            return 'x'
        elif self.winner()=='?':
        	return '?'
        else:return '-'
    #def controlla_vittoria(self):
    def stampa(self,livello=0):
        if self.lista_figli==[]:
       	    print('    '*livello,self.nome)
        else:
            self.lista_figli=list(set(self.lista_figli))
            for x in self.lista_figli:
                x.stampa(livello+1)
    def esiti(self):
        ''' dato un nodo radice di un albero di gioco, restituisce una tripla con i possibili 
esiti della partita il primo elemento della tripla  e' il numero di  patte possibili, 
il secondo e' il numero di possibili vittorie  per  'o' mentre  il terzo elemento 
e' il numero di possibili vittorie per  'x'.'''
        vt_o=0
        vt_x=0
        vt_p=0
       # print(self.nome)
        self.built()
        if self.lista_figli==[]:
            if self.tipo()=='o':
                vt_o+=1
            elif self.tipo()=='x':
                vt_x+=1
            elif self.tipo()=='-':
                vt_p+=1
            return (vt_p,vt_o,vt_x)
        for x in self.lista_figli: 
           # print(x)
          #  print(x.tipo(),x)
            if x.tipo()=='o':
                vt_o=vt_o+1
            elif x.tipo()=='x':
                vt_x=vt_x+1
            elif x.tipo()=='?':
                pass
            else:vt_p=vt_p+1
            if x.lista_figli!=[]:
                x.esiti()
        return (vt_p,vt_o,vt_x)

    
    def vittorie_livello(self, giocatore, h):
        '''dato un nodo radice di un albero di gioco, uno dei due giocatori ed un intero h,
restituisce il numero di nodi che rappresentano una vittoria per il giocatore e si 
trovano ad altezza h nell'albero.'''
        self.built()
        c=0
        l=[]
        vitt=0
        self.trova(h,c,l)
       # print(l)
        #print(l,'dsfg')
        for x in l:
            if x!=[]:
               print(x)
               print(x.tipo())
    def trova(self,h,c,l):
        for x in self.lista_figli:
            if c==h:
                l.append(self.nome)
            else:x.trova(h,c+1,l)
        
    
    def strategia_vincente(self,giocatore):
        '''dato un nodo radice di un albero di gioco ed uno dei due giocatori, restituisce True o False.
        True  se  giocatore ha una strategia vincente  nella partita 
che ha come configurazione iniziale quella rappresentata dal nodo radice, False altrimenti.'''
        m,n=self.mossa()
        self.built()
        f=[]
        strategia=''
        if (self.primo.count('')==3 and self.secondo.count('')==0 and self.terzo.count('')==0) or (self.primo.count('')==0 and self.secondo.count('')==3 and self.terzo.count('')==0) or (self.primo.count('')==0 and self.secondo.count('')==0 and self.terzo.count('')==3):
            for x in range(3):
                if self.primo[x]=='':
                    l=self.primo[:]
                    l[x]=m
                    child=NodoTris([l,self.secondo,self.terzo],l,self.secondo,self.terzo)
                elif self.secondo[x]=='':
                    l=self.secondo[:]
                    l[x]=m
                    child=NodoTris([self.primo,l,self.terzo],self.primo,l,self.terzo)   
                elif self.terzo[x]=='':
                    l=self.terzo[:]
                    l[x]=m
                    child=NodoTris([self.primo,self.secondo,l],self.primo,self.secondo,l)
                f.append(child)
            for y in f:
                strategia+=y.tipo()
            if giocatore in strategia:
                return True
            else:
            	return False
        else:
            s=[]
            self.cerca_nodo(s)
            s=list(set(s))
            for x in s:
                strategia+=x.tipo()
            if strategia.count('o')>strategia.count('x') and 'o'==giocatore:
                return True
            if strategia.count('x')>strategia.count('o') and 'x'==giocatore:
                return True
            else: 
                return False
    
    def cerca_nodo(self,l):
        self.built()
        for x in self.lista_figli:
            if x.lista_figli!=[]:
               # print(x,'con')
                x.cerca_nodo(l)
            else:l.append(x) 
    def mossa(self):
        x=0
        o=0
        for sign in self.primo:
            if sign=='x':
                x+=1
            elif sign=='o':
                o+=1
        for sign in self.secondo:
            if sign=='x':
                x+=1
            elif sign=='o':
                o+=1
        for sign in self.terzo:
            if sign=='x':
                x+=1
            elif sign=='o':
                o+=1
        if x<o:
            prima_mossa,n='x',x
        else:
            prima_mossa,n='o',o
        return prima_mossa,n

    def built(self):
        m,n=self.mossa()
        if n<4:
            figli=self.lista_figli
            if m=='o':
                self.mossa_o(self.primo,1,figli)  
                self.mossa_o(self.secondo,2,figli)
                self.mossa_o(self.terzo,3,figli)
            elif m=='x':
                self.mossa_x(self.primo,1,figli)
                self.mossa_x(self.secondo,2,figli)
                self.mossa_x(self.terzo,3,figli)
            for y in figli:
                y.built()
    def mossa_o(self,lst,ID,figli):
        i=0
        while i<3:
            if lst[i]=='':
                l=lst[:]
                l[i]='o'
                if ID==1:
                    child=NodoTris([l,self.secondo,self.terzo],l,self.secondo,self.terzo)
                elif ID==2:
                    child=NodoTris([self.primo,l,self.terzo],self.primo,l,self.terzo)
                elif ID==3:
                    child=NodoTris([self.primo,self.secondo,l],self.primo,self.secondo,l)
                figli.append(child)
            i+=1
            
    def mossa_x(self,lst,ID,figli):
        i=0
        while i<3:
            if lst[i]=='':
                l=lst[:]
                l[i]='x'
                if ID==1:
                    child=NodoTris([l,self.secondo,self.terzo],l,self.secondo,self.terzo)
                elif ID==2:
                    child=NodoTris([self.primo,l,self.terzo],self.primo,l,self.terzo)
                elif ID==3:
                    child=NodoTris([self.primo,self.secondo,l],self.primo,self.secondo,l)
                figli.append(child)
            i+=1

def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    g=griglia
    griglia=NodoTris(griglia,griglia[0],griglia[1],griglia[2])
    s=griglia.built()
    return griglia