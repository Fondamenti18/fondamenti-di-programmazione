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
        self.caselle_bianche=[]
        self.altezza=0
        self.listavittorie=[]
        self.risultato=''
    def tipo(self):
        '''inserire qui il vostro codice'''
        contocasellebianche=0
        contoO=0
        contoX=0
        for riga in self.nome:
            contoO=0
            contoX=0
            for colonna in riga:
                if colonna=='o':
                    contoO+=1
                elif colonna=='x':
                    contoX+=1
                elif colonna=='':
                    contocasellebianche+=1
            if contoO==3:
                return 'o'
            if contoX==3:
                return 'x'
        x=0
        while x<=2:
            riga=0
            if self.nome[riga][x]=='o'and self.nome[riga+1][x]=='o'and self.nome[riga+2][x]=='o':
                return 'o'
            elif self.nome[riga][x]=='x'and self.nome[riga+1][x]=='x'and self.nome[riga+2][x]=='x':
                return 'x' 
            x=x+1         
          
        if self.nome[0][0]=='o'and self.nome[2][2]=='o'and self.nome[1][1]=='o':
            return 'o'
        if self.nome[0][0]=='x'and self.nome[2][2]=='x'and self.nome[1][1]=='x':
            return 'x'
        
        if contocasellebianche!=0:
            return '?'
        
        return '-'        
                    
    def esiti(self):
        '''inserire qui il vostro codice'''
        conteggioX=0
        conteggioO=0
        conteggioP=0
        
        lista=self.analisifigli()
        #print(lista)
        
        for el in lista:
            if el=='x':
                conteggioX+=1
            if el=='o':
                conteggioO+=1
            if el=='-':
                conteggioP+=1
        #print(conteggioP,conteggioO,conteggioX)
        return (conteggioP,conteggioO,conteggioX)
    
    def analisifigli(self):  #test6
        listarisultati=[]
        if self.caselle_bianche==[] or self.tipo()=='x' or self.tipo()=='o': #aggiungere alla classe caselle bianche
                listarisultati.append((self.tipo()))
                listarisultati.append('p')
                
        else:
            for el in self.lista_figli:
                lista2=el.analisifigli()
                listarisultati+=lista2
        return listarisultati
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        i=0
        radice=funzione2(self.nome,giocatore,h,i)
        lista=radice.listavittorie
        risultato=len(lista)
        return risultato
        
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        radice=funzione3(self.nome,giocatore)
        if radice.risultato==True:
            risultato=True
        else:
            risultato=False
        
        return risultato
    

        
    def analisi(self):  #ok
        conteggioX=0
        conteggioO=0
        r=0
        c=0
        for riga in self.nome:
            c=0
            for colonna in riga:
                if colonna=='x':
                    conteggioX+=1
                elif colonna=='o':
                    conteggioO+=1
                else:
                    self.caselle_bianche.append((r,c))
                if c<=1:
                    c+=1
            if r<=1:
                r+=1
        if conteggioX==conteggioO:
            turno='o'
        else:
            turno='x'
        return self.caselle_bianche,turno
    
def aggiungi(casellebianche,turno,griglia):
    import copy
    listafigli=[]
    griglia1=copy.deepcopy(griglia)
    if turno=='o':
        for el in casellebianche:
            riga=el[0]
            colonna=el[1]
            griglia1[riga][colonna]='o'
            listafigli.append(griglia1)     #prova
            griglia1=copy.deepcopy(griglia) 
    else:
        for el in casellebianche:
            riga=el[0]
            colonna=el[1]
            griglia1[riga][colonna]='x'
            listafigli.append(griglia1)
            griglia1=copy.deepcopy(griglia)
    return listafigli
    
def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    radice=funzione(griglia)
    #print(radice.nome)
    #print(radice.strategia_vincente('x'))
    return radice

def funzione(griglia):
    nodo=NodoTris(griglia)
    listacasellebianche,turno=nodo.analisi()
    if listacasellebianche==[] or nodo.tipo()=='x' or nodo.tipo()=='o':
        return nodo
    else:
        listafigli=aggiungi(listacasellebianche,turno,griglia)
        for el in listafigli:
            nodo1=funzione(el) 
            nodo.lista_figli.append(nodo1)
    return nodo
def funzione2(griglia,giocatore,h,i):
    nodo=NodoTris(griglia)
    listacasellebianche,turno=nodo.analisi()
    if listacasellebianche==[] or nodo.tipo()=='x' or nodo.tipo()=='o'or i==h:
        if nodo.tipo()==giocatore:
            if i==h:
                nodo.listavittorie.append('v')
        return nodo
    else:
        listafigli=aggiungi(listacasellebianche,turno,griglia)
        i=i+1
        for el in listafigli:
            nodo1=funzione2(el,giocatore,h,i) 
            nodo.lista_figli.append(nodo1) 
            nodo.listavittorie+=nodo1.listavittorie
    return nodo
def funzione3(griglia,giocatore):
    nodo=NodoTris(griglia)
    listacasellebianche,turno=nodo.analisi()
    if listacasellebianche==[] or nodo.tipo()=='x' or nodo.tipo()=='o':
        if nodo.tipo()==giocatore:
            nodo.risultato=True
        else:
            nodo.risultato=False
        return nodo
    else:
        listafigli=aggiungi(listacasellebianche,turno,griglia)
        if turno==giocatore:
            i=0
            for el in listafigli:
                nodo1=funzione3(el,giocatore)
                if nodo1.risultato==True:
                    nodo.risultato=True
                    return nodo
                else:
                    nodo.risultato=False
        if turno!=giocatore:
            i=0
            for el in listafigli:
                nodo2=NodoTris(el)
                listacasellebianche,turno=nodo2.analisi()
                listafigli2=aggiungi(listacasellebianche,turno,griglia)
                for figlio in listafigli:
                    nodo3=funzione3(figlio,giocatore)
                if nodo3.risultato==True:
                    i+=1
            if i==len(listafigli2):
                nodo.risultato=True
                return nodo
            else:
                
                nodo.risultato=False
                return nodo
                    
                
            
    return nodo
#print(gen_tree([['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]))
