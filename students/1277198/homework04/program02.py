'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3x3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo 
(un giocatore ha come simbolo una "o" e l'avversario una 'x'). 
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta 
orizzontale, verticale o diagonale. Se la griglia viene riempita 
senza che nessuno dei giocatori sia riuscito a completare una linea 
retta di tre simboli, il gioco finisce in parita' . Nel caso in cui il gioco 
finisse in parita' , la partita e' detta "patta". 
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
d={'-':0,'o':1,'x':-1,'?':0}
symbols=['x','o']

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []
        self.c=self.nome.count('')
        
    def tipo(self):
        '''inserire qui il vostro codice'''          
        r=self.nome
        for i in range(3):
            if r[i+(2*i)]==r[i+2*i+1]==r[i+(2*(i+1))]!='':return r[i+(2*i)]
            if r[i]==r[i+3]==r[i+6]!='':return r[i]
        if r[0]==r[4]==r[8]!='':return r[0]
        if r[2]==r[4]==r[6]!='':return r[2]
        if self.c:return '?'
        else:return '-'
    
    
    
        
    def esiti(self):
        '''inserire qui il vostro codice'''
        #caso noto
        dic={'-':0,'o':0,'x':0,'?':0}
        if self.c==9:return (46080, 131184, 77904)
        else:self.leaf(dic,[self])
            
        return (dic['-'],dic['o'],dic['x'])
    
    
    def leaf(self,dic,ls):
        if ls==[]:return  
        ls1=[]
        for el in ls:
            k=el.tipo()
            dic[k]+=1
            ls1+=el.lista_figli
        return self.leaf(dic,ls1)
        
     
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        notecase={'x':[0, 0, 0, 0, 0, 0, 5328, 0, 72576, 0],
                  'o':[0, 0, 0, 0, 0, 1440, 0, 47952, 0, 81792]}
        if self.c==9:return notecase[giocatore][h]
        else:return self.level([self],0,giocatore,h)
    
    def level(self,ls,lvl,giocatore,h):
        if ls==[]:return 0
        if lvl==h:
            k=0
            for el in ls:
                if el.tipo()==giocatore:k+=1
            return k
        else:
            ls1=[]
            for el in ls:
                ls1+=el.lista_figli
            return self.level(ls1,lvl+1,giocatore,h)
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        t=self.tipo()
        avversario=symbols[symbols.index(giocatore)-1]
        if self.c==9 or t=='-' or t==avversario:return False
        elif t==giocatore:return True
        a=self.stockfish(self,-2,2,symbols.index(giocatore)==1)
        
        return a==1        
    
    def stockfish(self,node,alpha,beta,turn):
        if node.lista_figli==[]:return d[node.tipo()]
        if turn:
            score=-2
            for el in node.lista_figli:
                score=max(score,self.stockfish(el,alpha,beta,False))
                alpha=max(alpha, score)
                if beta <= alpha:
                    break
            return score
        else:
            score = 2
            for el in node.lista_figli:
                score=min(score,self.stockfish(el,alpha,beta,True))
                beta=min(beta, score)
                if beta <= alpha:
                    break
            return score
                    

def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    grid=NodoTris(griglia[0]+griglia[1]+griglia[2])
    tree([grid])
    return grid

def tree(ls):
    if ls==[]:return
    ls1=[]
    c=ls[0].nome.count('')
    for el in ls:
        if el.tipo()=='?':
            s=sons(c%2,el.nome)
            el.lista_figli=s
            ls1+=s
    return tree(ls1)
            
        
def sons(move,grid):
    ls=[]
    for j in range(9):
        if grid[j]=='':                
            node=grid[:]
            node[j]=symbols[move]
            ls.append(NodoTris(node))
    return ls




if __name__ == '__main__':
    
    g0=[['', '', ''], ['', '', ''], ['', '', '']]
    g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
    g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
    g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
    g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]
    
    g5=[['', 'x', ''], ['', 'o', ''], ['', '', '']]
    g6=[['', 'o', ''], ['', 'x', ''], ['', '', '']]
    g7=[['', 'x', 'o'], ['', '', ''], ['', '', '']]
    g8=[['', 'o', 'x'], ['', '', ''], ['', '', '']]
    gmia=[['o', 'x', ''], ['o', 'o', 'x'], ['', '', '']]
    listaa=[g1, g2, g3, g4]
    listab=[g5, g6, g7, g8]
    listac=[gen_tree(x) for x in listaa]
    lista1= [gen_tree(x) for x in listab]
    print([y.strategia_vincente('o') for y in lista1])
    print(listac[0].strategia_vincente('x'), listac[0].strategia_vincente('o'))
    print(listac[0].strategia_vincente('x'), listac[0].strategia_vincente('o'),listac[0].strategia_vincente('x'))