class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.numX, self.numO = self.conta()
    
    def print_tree(self, level=0):
        '''Stampa l'albero mostrando la struttura
        tramite indentazione'''
        print('  '*level + str(self.nome))
        for child in self.lista_figli:
            child.print_tree(level+1)
    
    def conta(self, numX=0, numO=0):
        '''Restituisce il numero di X e il numero di O nella griglia.'''
        for lista in self.nome:
            for el in lista:
                if el=='x': numX+=1
                if el=='o': numO+=1
        return numX, numO
    
    def calcola_turno(self):
        '''Ritorna 'x' se il prossimo turno è del giocatore x o 'o' se tocca al giocatore o.'''
        if self.numO == self.numX: return 'o'
        else: return 'x'
    
    def tipo(self):
        '''Restituisce 'x' se la partita è vinta dal giocatore x, 'o' se è vinta dalla o, '-' se è patta e '?' se è ancora in sospeso.'''
        #Si eseguono i controlli delle righe, delle colonne e delle righe.
        controlli = [self.tipo_righe(), self.tipo_colonne(), self.tipo_diagonali()]
        for funz in controlli:
            tentativo = funz
            if tentativo != None: return tentativo #la config indica una vittoria di uno dei due giocatori
        
        #Se le tre funzioni hanno returnato la vittoria di qualcuno, si returna quella vittoria; se la somma di 'x' e 'o' nella griglia non è 9, significa che ci sono caselle vuote quindi è in sospeso, altrimenti è patta
        if self.numX + self.numO!=9: return '?'  #la config indica una partita in sospeso
        return '-' #la config indica una partita patta
    
    def tipo_righe(self):
        '''Ogni iterazione si controlla se almeno una riga contiene lo stesso simbolo in tutte e 3 le caselle. Se è così, si controlla cosa succede nel punto lista[0] perche' e' il primo rappresentativo.'''
        for lista in self.nome:
            if len(set(lista))==1: 
                if lista[0]=='x': return 'x'
                elif lista[0]=='o': return 'o'
            
    def tipo_colonne(self):
        '''Ogni iterazione si controlla che gli elementi in posizione i di ogni riga sono uguali. Se è così, si controlla cosa succede nel punto griglia[0][i] perche' e' il primo rappresentativo.'''
        griglia = self.nome
        for i in range(3):
            if griglia[0][i]==griglia[1][i]==griglia[2][i]: 
                if griglia[0][i]=='x': return 'x'
                elif griglia[0][i]=='o': return 'o'
                
    def tipo_diagonali(self):
        '''Si controllano le caselle delle due diagonali. Se almeno una diagonale ha simboli uguali, si controlla cosa c'e' nel punto griglia[1][1] perche' e' quello in comune ai due or (e quindi sicuramente uno dei due e' rappresentativo)'''
        griglia = self.nome
        if griglia[0][0]==griglia[1][1]==griglia[2][2] or griglia[0][2]==griglia[1][1]==griglia[2][0]: 
            if griglia[1][1]=='x': return 'x'
            elif griglia[1][1]=='o': return 'o'

    def esiti(self):
        #attraverso il metodo ricorsivo gen_str_per_esiti, si ottiene una lista che contiene tutti gli esiti; in base ai caratteri contenuti, si incrementano le seguenti tre variabili (che andranno a formare la tupla in uscita)
        stringaEsiti = self.gen_stringa_esiti([])
        
        #si contano le occorrenze nella stringaEsiti dei caratteri che indicano parità o vittoria di uno o l'altro:
        tupla = stringaEsiti.count('-'), stringaEsiti.count('o'), stringaEsiti.count('x')
        return tupla
    
    def gen_stringa_esiti(self, stringa):
        '''Metodo ricorsivo che costruisce una lista con i tipi di tutti i figli/nipoti del nodo dato in input da esiti(self).'''
        #per ogni figlio nella lista dei figli, aggiungo alla lista il tipo() di quel figlio e ripeto la ricorsione
        
        stringa = self.tipo()
        for figlio in self.lista_figli:
            stringa += figlio.gen_stringa_esiti(stringa)
        return stringa

    def vittorie_livello(self, giocatore, h, livello=0, numVittorie=0):
        '''Metodo ricorsivo che, dato un nodo radice di un albero di gioco, uno dei due giocatori ed un intero h, restituisce il numero di nodi che rappresentano una vittoria per il giocatore e si trovano ad altezza h nell'albero.'''
        
        #si esplora l'albero (con il for successivo che richiama la ricorsiva) incrementando ogni volta il livello. Il primo controllo verifica se il livello è uguale a quello richiesto e se il nodo che ha quel livello rappresenta una vittoria di giocatore. 
        if livello==h and self.tipo() == giocatore:
            numVittorie = 1
        for figlio in self.lista_figli:
            numVittorie += figlio.vittorie_livello(giocatore, h, livello+1)
    
        return numVittorie
    
    def strategia_vincente(self,giocatore):
        '''Dato un nodo radice di un albero di gioco ed uno dei due giocatori, restituisce True se giocatore ha una strategia vincente nella partita che ha come configurazione iniziale quella rappresentata dal nodo radice, False altrimenti.'''
        risultato = self.minimax(giocatore)
        if risultato == 10: return True
        else: return False
        
    def minimax(self, giocatore):
        '''Metodo ricorsivo che ritorna il massimo o il minimo tra 10,-10 e 0 dove 10 = vittoria di giocatore, -10 = sconfitta del giocatore e 0 = partita patta.'''
        #Si ricava avversario e il turno della config in input
        if giocatore == 'o': avversario = 'x'
        else: avversario = 'o'
        turno = self.calcola_turno() 
        
        #Ciascun figlio del nodo in input aggiunge alla listaEsiti 10,-10 e 0 in base al tipo() in modo tale che ogni nodo rappresenti per giocatore quale può essere lo scenario PEGGIORE "sotto di lui" nel caso in cui il turno spetti all'avversario, oppure lo scenario MIGLIORE nel caso fosse il suo turno.
        listaEsiti = list()
        for figlio in self.lista_figli:
            ft = figlio.tipo()
            if ft == giocatore: listaEsiti.append(10)
            elif ft == avversario: listaEsiti.append(-10)
            elif ft == '-': listaEsiti.append(0)
            else: listaEsiti.append(figlio.minimax(giocatore))
        
        if turno == giocatore: return max(listaEsiti)
        else: return min(listaEsiti)
        

def gen_tree(griglia):
    '''Genera l'albero delle combinazioni partendo dalla configurazione griglia e ritorna il nodo radice.'''
#si crea il nuovo nodo a partire dalla matrice data in input, e si controlla se tale configurazione corrisponde ad una partita in sospeso. Nel caso, si esegue il calcolo del turno e si procede all'iterazione delle caselle.
    config = NodoTris(griglia)
    if config.tipo()=='?':
        turno = config.calcola_turno() #si calcola il turno di quel nodo
        
#si itera sulle caselle della matrice; per ogni casella vuota, si crea una copia della griglia con la casella vuota sostituta da turno. Infine si aggiunge alla lista_figli il risultato della funzione ricorsiva chiamata con la copia appena descritta.
        for riga, lista in enumerate(config.nome):
            for casella, simb in enumerate(lista):
                if simb=='':
                    copia = list()
                    for lista in config.nome:
                        copia.append(lista[:])
                    copia[riga][casella] = turno
                    config.lista_figli.append(gen_tree(copia))
                    
    return config