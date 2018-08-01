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



import importlib
import copy


class NodoTris:
    
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.dizionario_livelli={}
        
    def tipo(self):
        end = 0
        
        end, esito = self.regole_tris()
            
        return esito
    
    def esiti(self,p=0,o=0,x=0,h=0):
        
        a=sorted(self.dizionario_livelli.keys())[-1]
        
        
        
        if h > a:
            
            return p, o, x
        
        if h not in self.dizionario_livelli:
            return self.esiti(p,o,x,h+1)
        
        p += len(self.dizionario_livelli[h]['p'])
        o += len(self.dizionario_livelli[h]['o'])    
        x += len(self.dizionario_livelli[h]['x'])
        
        p,o,x = self.esiti(p,o,x,h+1)
        
        return p,o,x
       
    def vittorie_livello(self, giocatore,h,H=0):
        
        if H != h:
            return self.vittorie_livello(giocatore,h,H+1)
        else:            
            try:               
                return len(self.dizionario_livelli[H][giocatore])           
            except KeyError:
                return 0
    
    def strategia_vincente(self,giocatore):
        
        strategia = best_move(self.nome,giocatore)
        
        try:
            
            lista = self.dizionario_livelli[1][giocatore]
            
            if lista != []:
                return True
            else:
                return False
        
        except KeyError:
        
  
            who = sorted(list(strategia.dizionario_livelli.keys()))[0]
        
        
            if strategia.dizionario_livelli[who][giocatore] != []:
                return True
            else:
                return False
    

    def regole_tris(self):
        
        end=0
        
        if self.nome[0][0] == self.nome[0][1] == self.nome[0][2] == 'x':
            return 1 , 'x'
        elif self.nome[0][0] == self.nome[0][1] == self.nome[0][2] == 'o':
            return 1 , 'o'
        elif self.nome[1][0] == self.nome[1][1] == self.nome[1][2] == 'x':
            return 1 , 'x'
        elif self.nome[1][0] == self.nome[1][1] == self.nome[1][2] == 'o':
            return 1 , 'o'            
        elif self.nome[2][0] == self.nome[2][1] == self.nome[2][2] == 'x':
            return 1 , 'x'
        elif self.nome[2][0] == self.nome[2][1] == self.nome[2][2] == 'o':
            return 1 , 'o'
        elif self.nome[0][0] == self.nome[1][0] == self.nome[2][0] == 'x':
            return 1, 'x'
        elif self.nome[0][0] == self.nome[1][0] == self.nome[2][0] == 'o':
            return 1, 'o'
        elif self.nome[0][1] == self.nome[1][1] == self.nome[2][1] == 'x':
            return 1, 'x'
        elif self.nome[0][1] == self.nome[1][1] == self.nome[2][1] == 'o':
            return 1, 'o'
        elif self.nome[0][2] == self.nome[1][2] == self.nome[2][2] == 'x':
            return 1, 'x'
        elif self.nome[0][2] == self.nome[1][2] == self.nome[2][2] == 'o':
            return 1, 'o'
        elif self.nome[0][0] == self.nome[1][1] == self.nome[2][2] == 'x':
            return 1, 'x'
        elif self.nome[0][0] == self.nome[1][1] == self.nome[2][2] == 'o':
            return 1, 'o'
        elif self.nome[0][2] == self.nome[1][1] == self.nome[2][0] == 'x':
            return 1, 'x'
        elif self.nome[0][2] == self.nome[1][1] == self.nome[2][0] == 'o':
            return 1, 'o'
        elif (self.nome[0][0] and self.nome[0][1] and self.nome[0][2] and self.nome[1][0] and self.nome[1][1] and self.nome[1][2] and self.nome[2][0] and self.nome[2][1] and self.nome[2][2]) != '':
            return 1, '-'
        else:
            return 0 , '?'
        
 
def gen_tree(self,H=0,i=0,dic={}):  
    start=0
    end=0 
    import program02
    import copy
    
    
    
    radice = NodoTris(self)
  
    for riga in range(len(radice.nome)):
        for colonna in range(len(radice.nome[0])):
            if radice.nome[riga][colonna] == '':
                start+=1
                
    end, risultato =radice.regole_tris()
    
    if end == 1:
        
        if H not in dic:
            dic[H]={'p': [] ,'o': [] , 'x': []}
            
        if risultato == 'x':
         
            dic[H]['x'].append(radice.nome)
            radice.dizionario_livelli = dic.copy()
            
        if risultato == 'o':
            
            dic[H]['o'].append(radice.nome)
            radice.dizionario_livelli = dic.copy()
            
        if risultato == '-':
            
            dic[H]['p'].append(radice.nome)
            radice.dizionario_livelli = dic.copy()
        
        if H==0:
            dic.clear()
            return radice
        
        return dic
     
    elif (start % 2) == 0:
        start = 'x'
    else:
        start = 'o'
        
    for riga in range(len(radice.nome)):
        for colonna in range(len(radice.nome[0])):
            if (radice.nome[riga][colonna] == ''):
                radice.nome[riga][colonna] = start
                if radice.nome not in radice.lista_figli:
                    radice.lista_figli += [copy.deepcopy(radice.nome)]
                    radice.nome[riga][colonna] = ''
                    continue                   
                else:
                    radice.nome[riga][colonna] = ''
                    continue
                
    for figli in radice.lista_figli:
        dic.update(gen_tree(figli,H+1,dic))
           
    radice.dizionario_livelli = dic.copy()      
    if H == 0:
        
        dic.clear()
        return radice
    
    return dic


    if __name__ == "__main__":
        gen_tree(self)


def check_Bestmove(lista,nM):
    
    
    
    
    for nodo in lista:
          check = gen_tree(nodo)
          if check.dizionario_livelli[sorted(list(check.dizionario_livelli.keys()))[0]][nM] == []:
              lista.remove(nodo)
    
    
    return lista
    
    
def best_move(self,giocatore,H=0,i=0,dic={}):
        nM = 1
        start=0
        end=0 
        import copy
        import program02
        
    
        radice=NodoTris(self)
        
        for riga in range(len(radice.nome)):
            for colonna in range(len(radice.nome[0])):
                if radice.nome[riga][colonna] == '':
                    start+=1
                    nM+=1
                                 
        end, risultato = radice.regole_tris()
        
        if end == 1:
    
            if H not in dic:
                dic[H]={'p': [] ,'o': [] , 'x': []}
        
            if risultato == 'x':
        
                dic[H]['x'].append(radice.nome)
                radice.dizionario_livelli = dic.copy()
            
            if risultato == 'o':
            
                dic[H]['o'].append(radice.nome)
                radice.dizionario_livelli = dic.copy()
            
            if risultato == '-':
            
                dic[H]['p'].append(radice.nome)
                radice.dizionario_livelli = dic.copy()
    
            if H==0:       
                dic.clear()            
                return radice        
            return dic
     
        elif (start % 2) == 0:
            start = 'x'
            nM = 'o'
        else:
            start = 'o'
            nM = 'x'
        
        for riga in range(len(radice.nome)):
            for colonna in range(len(radice.nome[0])):
                if (radice.nome[riga][colonna] == ''):
                    radice.nome[riga][colonna] = start
                    if radice.nome not in radice.lista_figli:
                        radice.lista_figli += [copy.deepcopy(radice.nome)]
                        radice.nome[riga][colonna] = ''
                        continue                   
                    else:
                        radice.nome[riga][colonna] = ''
                        continue
        
        
        
        radice.lista_figli=check_Bestmove(radice.lista_figli,nM)
        
        
        
        for figli in radice.lista_figli:
    
            dic.update(best_move(figli,giocatore,H+1,dic))

        radice.dizionario_livelli = dic.copy()  
        if H == 0:
            
            dic.clear()
            return radice
        
        return dic