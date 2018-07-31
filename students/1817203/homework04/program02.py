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
        nx=0
        no=0
        l=0
        for el in self.nome:
            nx+=el.count('x')
            no+=el.count('o')
            l+=el.count('')
        if self.lista_figli!=[]:
            return '?'
        if no>=3:
            for i in range(3):    
                for j in range(3):
                    if self.nome[i][j]=='o':
                        if j==0:
                            if self.nome[i][1]=='o' and self.nome[i][2]=='o':
                                return 'o'
                            elif i==0:
                               if self.nome[1][1]=='o' and self.nome[2][2]=='o':
                                   return 'o'
                               if self.nome[1][0]=='o' and self.nome[2][0]=='o':
                                   return 'o' 
                            elif i==2:   
                                if self.nome[1][1]=='o' and self.nome[0][2]=='o': 
                                   return 'o'
                        elif j==1 and i==0:
                            if self.nome[1][1]=='o' and self.nome[2][1]=='o':
                                return 'o'
                        elif j==2 and i==0:
                            if self.nome[1][2]=='o' and self.nome[2][2]=='o':
                                return 'o'
        if nx>=3:
            for i in range(3):    
                for j in range(3):
                    if self.nome[i][j]=='x':
                        if j==0:
                            if self.nome[i][1]=='x' and self.nome[i][2]=='x':
                                return 'x'
                            elif i==0:
                                if self.nome[1][1]=='x' and self.nome[2][2]=='x':
                                    return 'x'
                                if self.nome[1][0]=='x' and self.nome[2][0]=='x':
                                    return 'x' 
                            elif i==2:   
                                if self.nome[1][1]=='x' and self.nome[0][2]=='x': 
                                    return 'x'
                        elif j==1 and i==0:
                            if self.nome[1][1]=='x' and self.nome[2][1]=='x':
                                return 'x'
                        elif j==2 and i==0:
                            if self.nome[1][2]=='x' and self.nome[2][2]=='x':
                                return 'x'                    
        return '-'
        
    def esiti(self):        
        z=self.tipo()
        cx=0
        co=0
        cp=0
        if z=='x':
            cx+=1
        if z=='o':
            co+=1
        if z=='-':
            cp+=1
        if self.lista_figli==[]:
            return(cp,co,cx)
        for el in self.lista_figli:
            tripla=el.esiti()
            cp+=tripla[0]
            co+=tripla[1]
            cx+=tripla[2]
        return (cp,co,cx)    

    def vittorie_livello(self, giocatore, h):
        n=0
        if h==0:
            z=self.tipo()
            if z==giocatore:
                n+=1
                return n 
            else:
                return n
        if self.lista_figli==[]:
            return n
        for el in self.lista_figli:
            n+=el.vittorie_livello(giocatore,h-1)
        return n 
    
    def strategia_vincente(self,giocatore,lv=0):
        if giocatore=='o' and lv//2==0:
            if self.vittorie_livello('o',lv+1)!=0:
                return True
            elif self.vittorie_livello('?',lv+1)==0:
                return False
            else:
                return self.strategia_vincente('o',lv+1)
        elif giocatore=='o' and lv//2!=0:
            if self.vittorie_livello('x',lv+1)!=0:
                return False
            elif self.vittorie_livello('?',lv+1)==0:
                return False
            else:
                return self.strategia_vincente('o',lv+1)
        elif giocatore=='x' and lv//2==0:
            if self.vittorie_livello('o',lv+1)!=0:
                return False
            elif self.vittorie_livello('?',lv+1)==0:
                return False
            else:
                return self.strategia_vincente('x',lv+1)
        elif giocatore=='x' and lv//2!=0:
            if self.vittorie_livello('x',lv+1)!=0:
                return True
            elif self.vittorie_livello('?',lv+1)==0:
                return False
            else:
                return self.strategia_vincente('x',lv+1)    
                
                
            

                   
            
        
def gen_tree(griglia):
    nodo=NodoTris(griglia)
    if nodo.tipo()=='x' or nodo.tipo()=='o':
        return nodo
    nx=0
    no=0
    for el in nodo.nome:
        nx+=el.count('x')
        no+=el.count('o')   
    for i in range(3):    
        for j in range(3):
            if nodo.nome[i][j]=='':
                if nx<no:  
                    nodo.lista_figli+=[gen_tree(griglia[:i]+[griglia[i][:j]+['x']+griglia[i][j+1:]]+griglia[i+1:])]           
                else:                        
                    nodo.lista_figli+=[gen_tree(griglia[:i]+[griglia[i][:j]+['o']+griglia[i][j+1:]]+griglia[i+1:])]
    return nodo


            


LL=0     
def stampa(radice,LL):
    print(radice.tipo())
    for el in radice.nome:
        print('    '*LL,el)
    for el in radice.lista_figli:
        stampa(el,LL+1)   
    

albero=gen_tree([['x', 'o', 'o'], ['x', '', ''], ['', '', '']])
##stampa(albero,LL)

g='x'
n=albero.strategia_vincente(g)
print(n)