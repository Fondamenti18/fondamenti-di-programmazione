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

    padre_figlio = {}

    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.amount_o = 0
        self.amount_x = 0
        self.empty_boxes = []
        self.up_next = ''
        self.esito = [0,0,0]
        self.dict_levels = {'-':[],'o':[],'x':[]}


    
    def amount(self):
        for y in range(3):
            for x in range(3):
                if self.nome[y][x] == 'o':
                    self.amount_o+=1
                elif self.nome[y][x] == 'x':
                    self.amount_x+=1
                else:
                    self.empty_boxes.append((x,y))


    
    def tree(self, griglia, count = 0):
        nodo = NodoTris(griglia)

        str_griglia = str(griglia)

        NodoTris.padre_figlio[str_griglia] = []

        tipo = nodo.tipo()


        if not tipo == '?':

        
            if tipo == '-':
                self.dict_levels['-'].append(count)
                self.esito[0]+=1
            elif tipo == 'o':
                self.dict_levels['o'].append(count)
                self.esito[1]+=1
            elif tipo == 'x':
                self.dict_levels['x'].append(count)
                self.esito[2]+=1



            return 
        
        nodo.amount()
        
        

        if nodo.amount_o == nodo.amount_x:
            nodo.up_next = 'o'
        else: nodo.up_next = 'x'

    

        for x, y in nodo.empty_boxes: #for subnode in empty_boxes

            next_grid = deepcopy(griglia)
            
            next_grid[y][x] = nodo.up_next

            NodoTris.padre_figlio[str_griglia].append(next_grid)

            nodo.lista_figli.append(next_grid)

            self.tree(next_grid, count+1)
        
       

    
    # TIPO
    
    def tipo(self):
        return self.calcola_tipo()
        

    def calcola_tipo(self):
        for y in range(3):
            current_box = self.nome[y][0]
            equal = True
            for x in range(3):
                if self.nome[y][x] != current_box:
                    equal = False
            if equal and current_box != '':
                return current_box
        for x in range(3):
            current_box = self.nome[0][x]
            equal = True
            for y in range(3):
                if self.nome[y][x] != current_box:
                    equal = False
            if equal and current_box != '':
                return current_box
        return self.calcola_tipo2()
    
    def calcola_tipo2(self):
        current_box = self.nome[0][0]
        equal = True
        for i in range(3):
            if self.nome[i][i] != current_box:
                equal = False
        if equal and current_box != '':
                return current_box
        current_box = self.nome[0][2]
        equal = True
        for i in range(3):
            if self.nome[i][2-i] != current_box:
                equal = False
        if equal and current_box != '':
                return current_box
        return self.calcola_tipo3()

    def calcola_tipo3(self):
        for y in range(3):
            for x in range(3):
                if self.nome[y][x] == '':
                    return '?'
        return '-'
            
    # ESITI
    def esiti(self, n=0):
        result = []
        result = self.check_esiti(result)
        return result[0], result[1], result[2]
    

    def check_esiti(self, result, n=0):
        if n == 2:
            result.append(self.esito[n])
            return result
        result.append(self.esito[n])
        return self.check_esiti(result, n+1)


        
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        occorrenze = 0     
        n = len(self.dict_levels[giocatore])
        occorrenze = self.check_levels(h, occorrenze, giocatore)
        occorrenze = self.livelli(giocatore, h, occorrenze, n)     
        
        return occorrenze


    def livelli(self, giocatore, h, occorrenze, n):
        if len(self.dict_levels[giocatore]) < n:
            return occorrenze
        if occorrenze > n:
            occorrenze-=1
        n += 1
        return self.livelli(giocatore, h, occorrenze, n)
               
    
    def strategia(self, giocatore, avversario, griglia, n):
        nodo = NodoTris(griglia)
        
        tipo = nodo.tipo()


        if tipo == '?':


            nodo.amount()
            
            if nodo.amount_o == nodo.amount_x:
                nodo.up_next = 'o'
            else: nodo.up_next = 'x'


            if nodo.up_next == giocatore:
                all_opponent = True

                
                for x, y in nodo.empty_boxes: #for subnode in empty_boxes

                    next_grid = deepcopy(griglia)
                    
                    next_grid[y][x] = nodo.up_next

                    child_node = NodoTris(next_grid)

                
                    if child_node.tipo() == giocatore:
                        #print(child_node.nome)
                        return True
                    
                    
                    
                    
                    
                    #all_opponent = False
                    
                #if all_opponent: 
                    #return False

            else:
                all_player = True
                if n==1:
                    n+=1
                    self.strategia(giocatore, avversario, griglia, n)
                for x, y in nodo.empty_boxes: #for subnode in empty_boxes

                    next_grid = deepcopy(griglia)
                    
                    next_grid[y][x] = nodo.up_next

                    child_node = NodoTris(next_grid)

                
                    if child_node.tipo() == avversario or child_node.tipo() == '-':
                        return False


                    
                    all_player = False
                    
                if all_player: 
                    return True
            
            
            
            for x, y in nodo.empty_boxes: #for subnode in empty_boxes

                next_grid = deepcopy(griglia)
                
                next_grid[y][x] = nodo.up_next
                self.strategia(giocatore, avversario, next_grid, n)

                return self.strategia(giocatore, avversario, next_grid, n)
          
            
                


    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        if giocatore == 'o': 
            
            return self.strategia('o','x', self.nome, 1)
            #return self.strategia_o
        else:
           
            return self.strategia('x','o', self.nome, 1)
            #return self.strategia_x

 



        '''
        if self.amount_o == self.amount_x:
            self.up_next = 'o'
        else: self.up_next = 'x'

        print(self.up_next)

        print(self.lista_figli)
        if giocatore == self.up_next:
            for figlio in self.lista_figli:
                print(figlio)'''
        
        
        '''
        dict_types = {}

        for level in range(last_level):
            current = level+1
            dict_types[current]=[]
            if current in self.dict_levels['-']:
                dict_types[current].append('-')
            if current in self.dict_levels['o']:
                dict_types[current].append('o')
            if current in self.dict_levels['x']:
                dict_types[current].append('x')
        
        print(self.dict_levels)
        print(dict_types)
        strategia = True
        for key in dict_types:
            print('trying...')
            if giocatore not in dict_types[key]:
                print('nope')
                strategia = False
        
        
      
        print(strategia)
        return strategia'''


    def check_levels(self, h, occorrenze, giocatore):
        for livello in self.dict_levels[giocatore]:
            if livello == h:
                occorrenze +=1
        return occorrenze
    

    def last_level(self):
        last_level = 0
        for key in self.dict_levels:
            if self.dict_levels[key]:
                if max(self.dict_levels[key]) > last_level:
                    last_level = max(self.dict_levels[key])
        return last_level




def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    '''
    Scrivere prima la funzione gen_tree e poi le funzioni nella classe. Il grade prenderà nodi generati da gen_tree e li metterà nelle
    funzioni della classe per testarle
    '''

    
    nodo = NodoTris(griglia)

    nodo.tree(nodo.nome)

   
    return nodo


