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

import copy

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli

    def tipo(self):
        controll = fine_controll(self.nome)
        #print(controll)
        if controll == 'x':
            return 'x'
        if controll == 'o':
            return 'o'
        if controll == '-':
            return '-'
        if controll == '?':
            return '?'


    def esiti(self):
        x = 0
        o = 0
        patte = 0
        lista=[]
        self.ricorsione(patte,x,o,lista)
        #print(lista)
        for i in lista:
            if i == 'x': x+=1
            if i == 'o': o+=1
            if i == 'patte': patte+=1
            
        return((patte,o,x))
        
    def ricorsione(self,patte,x,o,lista):
        controll = fine_controll(self.nome)
        
        if controll != '?':  
            if controll == 'x':
                x+=1
                lista.append('x')
                #print('x',x)
                
            if controll == 'o':
                o+=1
                lista.append('o')
                #print('o',o)
                
            if controll == '-':
                lista.append('patte')
                patte+=1
                #print('patte',patte)
                
        else:
            
            for child in self.lista_figli: 
                child.ricorsione(patte,x,o,lista)
                
                
                
    def vittorie_livello(self, giocatore, h):
        lvl_ctr = 0
        lista = []
        a = self.ricorsiva_vittorie(h,giocatore,lvl_ctr,lista)
        return(a)
        
    def ricorsiva_vittorie(self,h,giocatore,lvl_ctr,lista):
        
        controll=fine_controll(self.nome)
      
        if lvl_ctr == h and controll == giocatore:
            lista.append(1)
        for child in self.lista_figli:
            
            child.ricorsiva_vittorie(h,giocatore,lvl_ctr+1,lista)
        return len(lista)
         


    def strategia_vincente(self,giocatore):
        
        #ins_profondita = set()
        #prof = 0
        a = 0
        Nodo = self.nome
        #p = self.profondita(prof,ins_profondita) #profondita
        #depth = print(max(ins_profondita)) #DEPTH = PROFONDITA
        #depth2=copy.copy(depth)
        
        step = 0
        ret = self.minmax(Nodo,giocatore,step,a)
        
        #print(ret)
        if ret == 100: return True
        if ret != 100: return False
        

    def profondita(self,prof,ins_profondita):
        controll= fine_controll(self.nome)
        if controll != '?':
            
            return ins_profondita
        else:
            for child in self.lista_figli:
                ins_profondita.add(prof)
                
                child.profondita(prof+1,ins_profondita)
                
                
    def minmax(self,Nodo,giocatore,step,a):
        value =['o','x']
    
        t = value[step % 2]
        
        controll= fine_controll(self.nome)
        if controll != '?' :#or depth == 0
            print(self.nome)
            if controll == giocatore: return 100
            else: return 10
            
            
        if t != giocatore:
            a =1
            for child in self.lista_figli:
                a = min(a,child.minmax(Nodo,giocatore,step+1,a))
        else:
            a =1
            #print(a)
            for child in self.lista_figli:
                a = max(a,child.minmax(Nodo,giocatore,step+1,a))
        return a
            
            


def gen_tree(griglia,step = 0):
    
    lista =[]
    
    for i in griglia:
        for x in i:
            lista.append(x)
    
    matrix =[]
    Nodo = NodoTris(lista)
    a = ricorsione(lista,matrix,Nodo)
    return(a)
    
    
def ricorsione(lista,matrix,Nodo,step = 0):
    Nodo = NodoTris(lista)
    matrix = Nodo.nome
    value =['o','x']
    
    t = value[step % 2]
    
    
    controll = fine_controll(matrix)
    
    
    if controll != 'x' and controll != 'o' and controll != '-':    
        for j in range(len(matrix)):
            if matrix[j] == '':
                matrix2=matrix[:]
                matrix2[j] = t
                
                Nodo.lista_figli.append((ricorsione(matrix2,matrix,Nodo,step+1)))
                    
    
    return Nodo
    
    





def fine_controll(matrix):
    
    if matrix[0] == 'x' and matrix[1] == 'x' and matrix[2] == 'x': return ('x')
    if matrix[3] == 'x' and matrix[4] == 'x' and matrix[5] == 'x': return ('x')
    if matrix[6] == 'x' and matrix[7] == 'x' and matrix[8] == 'x': return ('x')
    if matrix[0] == 'o' and matrix[1] == 'o' and matrix[2] == 'o': return ('o')
    if matrix[3] == 'o' and matrix[4] == 'o' and matrix[5] == 'o': return ('o')
    if matrix[6] == 'o' and matrix[7] == 'o' and matrix[8] == 'o': return ('o')  #controllo RIGHE
    
    if matrix[0] == 'x' and matrix[3] == 'x' and matrix[6] == 'x': return ('x')
    if matrix[1] == 'x' and matrix[4] == 'x' and matrix[7] == 'x': return ('x')
    if matrix[2] == 'x' and matrix[5] == 'x' and matrix[8] == 'x': return ('x')
    if matrix[0] == 'o' and matrix[3] == 'o' and matrix[6] == 'o': return ('o')
    if matrix[1] == 'o' and matrix[4] == 'o' and matrix[7] == 'o': return ('o')
    if matrix[2] == 'o' and matrix[5] == 'o' and matrix[8] == 'o': return ('o')  #controllo COLONNE
    
    if matrix[0] == 'x' and matrix[4] == 'x' and matrix[8] == 'x': return ('x')
    if matrix[2] == 'x' and matrix[4] == 'x' and matrix[6] == 'x': return ('x')
    if matrix[0] == 'o' and matrix[4] == 'o' and matrix[8] == 'o': return ('o')
    if matrix[2] == 'o' and matrix[4] == 'o' and matrix[6] == 'o': return ('o')
        
    #Controllo PATTE
    
    if '' not in matrix:
        #print('patte')
        return '-'
    
    #Controllo non terminate
    if '' in matrix:
        return '?'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
