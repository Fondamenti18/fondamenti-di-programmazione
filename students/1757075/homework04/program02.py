

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []       # lista dei nodi figli
    
    def tipo(self):
        ''' Metodo che ritorna 'o' se vince o, 'x' se vince x, '-' se patta,
            '?' se da giocare
        '''
        # vittoria riga orizzontale
        #print(1)
        if self.vittoria(self.nome[0][0],self.nome[0][1],self.nome[0][2]):
            return self.nome[0][0]
        #print(2)
        if self.vittoria(self.nome[1][0],self.nome[1][1],self.nome[1][2]):
            return self.nome[1][0]
        #print(3)
        if self.vittoria(self.nome[2][0],self.nome[2][1],self.nome[2][2]):
            return self.nome[2][0]
        # vittoria colonna verticale
        #print(4)
        if self.vittoria(self.nome[0][0],self.nome[1][0],self.nome[2][0]):
            return self.nome[0][0]
        #print(5)
        if self.vittoria(self.nome[0][1],self.nome[1][1],self.nome[2][1]):
            return self.nome[0][1]
        #print(6)
        if self.vittoria(self.nome[0][2],self.nome[1][2],self.nome[2][2]):
            return self.nome[0][2]
        # vittoria diagonale
        #print(7)
        if self.vittoria(self.nome[0][0],self.nome[1][1],self.nome[2][2]):
            return self.nome[0][0]
        #print(8)
        if self.vittoria(self.nome[0][2],self.nome[1][1],self.nome[2][0]):
            return self.nome[0][2]
        
        # partita da giocare
        if self.casellaVuota(self.nome):
            return '?'
        
        return '-'      # patta
        
    def casellaVuota(self, griglia):
        ''' metodo che restituisce True se le griglia ha caselle vuote 
            altrimenti False
        '''
        # per ogni riga
        for i in griglia:
            # per ogni colonna
            for j in i:
                # se c'e' casella vuota
                if j == '':
                    return True      # da giocare
        return False        # partita completa
        
    def vittoria(self, a,b,c):
        ''' metodo che controlla a == b == c e controlla se sono 'x' o 'o' 
            in caso di ugualgianza ritorna vittoria
        '''
        #print(a,b,c, type(c))
        if (a=='o' or a=='x') and a==b and b==c:
            return True
        return False
        
        
    def esiti(self):
        ''' metodo che ritorna tripla (patte, vittorie o, vittorie x) '''
        p,o,x = 0,0,0         # contatori
        if self.tipo() == '-':      # patta
            p += 1                  # incremento
        elif self.tipo() == 'o':    # vittoria o
            o += 1
        elif self.tipo() == 'x':    # vittoria x
            x += 1
        # se ci sono altre griglie da analizzare
        if self.lista_figli != []:
            # per ogni griglia
            for n in self.lista_figli:
                p,o,x = self.esiti2(p,o,x, n)  # ricorsione
        return (p,o,x)
                
    def esiti2(self, p,o,x, n):
        ''' metodo che incrementa contatori a se seconda del risultato '''

        if n.tipo() == '-':      # patta
            p += 1                  # incremento
        elif n.tipo() == 'o':    # vittoria o
            o += 1
        elif n.tipo() == 'x':    # vittoria x
            x += 1
        # se ci sono altre griglie da analizzare
        if n.lista_figli != []:
            # per ogni griglia
            for nodo in n.lista_figli:
                p,o,x = self.esiti2(p,o,x, nodo)  # ricorsione
        return p,o,x
    
    def vittorie_livello(self, giocatore, h):
        ''' metodo che restituisce il numero di possibili vittorie del giocatore
            in h mosse
        '''
        o,x = 0,0       # contatori
        # se sono arrivato al livello corretto
        if h == 0:
            # se vince o
            if self.tipo() == 'o':
                o += 1
                # se vince x
            elif self.tipo() == 'x':
                x += 1
        # se mosse non sono finite e ci sono altre griglie da visionare
        if h>0 and self.lista_figli!=[]:
            # per ogni griglia
            for n in self.lista_figli:
                o,x = self.vittorie_livello2(o,x, n, h-1)    # ricorsione
        # cambia risultato a seconda di giocatore
        if giocatore == 'o':
            return o
        return x
    
    def vittorie_livello2(self, o,x, n, h):
        ''' metodo che calcola in numero di possibili vittorie del giocatore
            in h mosse
        '''
        # se sono arrivato al livello corretto
        if h == 0:
            # se vince o
            if n.tipo() == 'o':
                o += 1
            # se vince x
            elif n.tipo() == 'x':
                x += 1
        # se mosse non sono finite e ci sono altre griglie da visionare
        if h>0 and n.lista_figli!=[]:
            # per ogni griglia
            for nodo in n.lista_figli:
                o,x = self.vittorie_livello2(o,x, nodo, h-1)    # ricorsione
        
        return o,x
            
    
    
    
    def strategia_vincente(self,giocatore):
        ''' metodo che restituisce se giocatore riesce a vincere per primo
            rispetto a griglia di partenza
        '''
        # partita terminata
        v = self.vincitore(giocatore)
        if v != None:
            return v
        # per ogni griglia
        for n in self.lista_figli:
            # se partita termina alla prox mossa
            v = n.vincitore(giocatore)
            if v != None:
                return v
        #per ogni griglia
        for n in self.lista_figli:
            # se c'e' possibilita' di doppia minaccia
            if n.doppiaMinaccia(n.nome, giocatore) == True:
                return True
        
        # per ogni griglia
        for n in self.lista_figli:
            f = n.mossaForzante(n.nome, giocatore)
            # se tra le combinazioni ci sono mosse forzanti
            if f[0] == True:
                # per ogni possibile griglia
                for n2 in n.lista_figli:
                    # controllo solo grigla in cui avversario si difende
                    if n2.nome[f[1]][f[2]] != '':
                        # controlla risultato
                        return n2.strategia_vincente2(giocatore)
            
    def strategia_vincente2(self, gioc):
        # partita terminata
        v = self.vincitore(gioc)
        if v != None:
            return v
        # per ogni griglia
        for nodo in self.lista_figli:
            # se partita termina alla prox mossa
            v = nodo.vincitore(gioc)
            if v != None:
                return v
        #per ogni griglia
        for nodo in self.lista_figli:
            # se c'e' possibilita' di doppia minaccia
            if nodo.doppiaMinaccia(nodo.nome, gioc) == True:
                return True
        
        # per ogni griglia
        for nodo in self.lista_figli:
            f = nodo.mossaForzante(nodo.nome, gioc)
            # se tra le combinazioni ci sono mosse forzanti
            if f[0] == True:
                # per ogni possibile griglia
                for nodo2 in nodo.lista_figli:
                    # controllo solo grigla in cui avversario si difende
                    if nodo2.nome[f[1]][f[2]] != '':
                        # controllo se avversario ha risposto con una mossa forzante a sua volta
                        gioc2 = self.opposto(gioc)
                        f2 = nodo2.mossaForzante(nodo2.nome, gioc2)
                        if f2[0] == True:
                            # controllo solo griglia in cui giocatore si difende
                            for nodo3 in nodo2.lista_figli:
                                if nodo3.nome[f2[1]][f2[2]] != '':
                                    # controllo risultato
                                    return nodo3.strategia_vincente2(gioc)
                        # controlla risultato
                        return nodo2.strategia_vincente2(gioc)
    
    def opposto(self, gioc):
        if gioc == 'o':
            return 'x'
        return 'o'
    
    def vincitore(self, giocatore):
        ''' metodo che ritorna se il vincitore e' uguale al giocatore, se patta
            ritorna false se da giocare none
        '''
        t = self.tipo()     # risultato attuale
        if giocatore == 'o':
            if t == 'o':
                return True
            if t=='x' or t=='-':
                return False
        if giocatore == 'x':
            if t == 'x':
                return True
            if t=='o' or t=='-':
                return False
        
    
    def doppiaMinaccia(self, g, gioc):
        ''' controllo se giocatore con una mossa puo' effettuare una doppia 
            minaccia di vittoria
        '''
        if g[0][0]==gioc and g[0][0]==g[1][0] and g[1][0]==g[1][1] and g[2][0]=='' and g[2][0]==g[1][2]:
            print(1)
            return True
        return self.dm2(g,gioc)
    
    def dm2(self, g,gioc):
        if g[1][0]==gioc and g[1][0]==g[2][0] and g[2][0]==g[1][1] and g[0][0]=='' and g[0][0]==g[1][2]:
            print(2)
            return True
        return self.dm3(g,gioc)
    
    def dm3(self, g,gioc):
        if g[2][0]==gioc and g[2][0]==g[2][1] and g[2][1]==g[1][1] and g[2][2]=='' and g[2][2]==g[0][1]:
            print(3)
            return True
        return self.dm4(g,gioc)
    
    def dm4(self, g,gioc):
        if g[2][1]==gioc and g[2][1]==g[2][2] and g[2][1]==g[1][1] and g[2][0]=='' and g[2][0]==g[0][1]:
            print(4)
            return True
        return self.dm5(g,gioc)
    
    def dm5(self, g,gioc):
        if g[2][2]==gioc and g[2][2]==g[1][2] and g[2][2]==g[1][1] and g[0][2]=='' and g[0][2]==g[1][0]:
            print(5)
            return True
        return self.dm6(g,gioc)
    
    def dm6(self, g,gioc):
        if g[0][2]==gioc and g[0][2]==g[1][2] and g[0][2]==g[1][1] and g[2][2]=='' and g[2][2]==g[1][0]:
            print(6)
            return True
        return self.dm7(g,gioc)
    
    def dm7(self, g,gioc):
        if g[0][1]==gioc and g[0][1]==g[0][2] and g[0][2]==g[1][1] and g[0][0]=='' and g[0][0]==g[2][1]:
            print(7)
            return True
        return self.dm8(g,gioc)
    
    def dm8(self, g,gioc):
        if g[0][0]==gioc and g[0][0]==g[0][1] and g[0][1]==g[1][1] and g[0][2]=='' and g[0][2]==g[2][1]:
            print(8)
            return True
        # NB ci sono ulteriori doppie minaccie da implementare
        return False
    
    
    def mossaForzante(self, g, gioc):
        ''' metodo che ritorna se una mossa e' forzante (ovvero crea una 
            situazione che minaccia vittoria alla prossima mossa) e ritorna
            casella da difendere per interrompere minaccia
        '''
        # righe orizzontali caso xx-
        for r in range(0,3):
            if g[r][0]==gioc and g[r][0]==g[r][1] and g[r][2]=='':
                return (True, r,2)
        # righe orizzontali caso x-x
        for r in range(0,3):
            if g[r][0]==gioc and g[r][0]==g[r][2] and g[r][1]=='':
                return (True, r,1)
        # righe orizzontali caso xx-
        for r in range(0,3):
            if g[r][1]==gioc and g[r][1]==g[r][2] and g[r][0]=='':
                return (True, r,0)
        return self.colonnaForzante(g, gioc)
    
    def colonnaForzante(self, g, gioc):
        # colonna verticale caso xx-
        for c in range(0,3):
            if g[0][c]==gioc and g[0][c]==g[1][c] and g[2][c]=='':
                return (True, 2,c)
        # colonna verticale caso x-x
        for c in range(0,3):
            if g[0][c]==gioc and g[0][c]==g[2][c] and g[1][c]=='':
                return (True, 1,c)
        # colonna verticale caso -xx
        for c in range(0,3):
            if g[1][c]==gioc and g[1][c]==g[2][c] and g[0][c]=='':
                return (True, 0,c)
        return self.diagonale1Forzante(g, gioc)
    
    def diagonale1Forzante(self, g, gioc):
        # diagonale xx-
        if g[0][0]==gioc and g[0][0]==g[1][1] and g[2][2]=='':
            return (True, 2,2)
        # diagonale x-x
        if g[0][0]==gioc and g[0][0]==g[2][2] and g[1][1]=='':
            return (True, 1,1)
        # diagonale -xx
        if g[1][1]==gioc and g[1][1]==g[2][2] and g[0][0]=='':
            return (True, 1,1)
        return self.diagonale2Forzante(g, gioc)
    
    def diagonale2Forzante(self, g, gioc):
        # diagonale2 xx-
        if g[0][2]==gioc and g[0][2]==g[1][1] and g[2][0]=='':
            return (True, 2,0)
        # diagonale2 x-x
        if g[0][2]==gioc and g[0][2]==g[2][0] and g[1][1]=='':
            return (True, 1,1)
        # diagonale2 -xx
        if g[1][1]==gioc and g[1][1]==g[2][0] and g[0][2]=='':
            return (True, 0,2)
        return (False, 0,0)
        
def gen_tree(griglia):
    ''' Metodo che genera tutti i possibili esiti della griglia di partenza '''
    r = NodoTris(griglia)               # creo nodo radice
    # se partita non e' ancora finita
    if r.tipo() == '?':
        # per ogni riga
        for i in range(0,3):
            # per ogni colonna
            for j in range(0,3):
                # se mossa ancora da fare
                if griglia[i][j] == '':
                    g = copia(griglia)
                    g[i][j] = 'o'         # muove giocatore o
                    r.lista_figli.append(gen_treeX(g))    # ricorsione
    return r
                    
        
def gen_treeX(griglia):
    r = NodoTris(griglia)               # creo nodo radice
    # se partita non e' ancora finita
    if r.tipo() == '?':
        # per ogni riga
        for i in range(0,3):
            # per ogni colonna
            for j in range(0,3):
                # se mossa ancora da fare
                if griglia[i][j] == '':
                    g = copia(griglia)
                    g[i][j] = 'x'         # muove giocatore x
                    r.lista_figli.append(gen_tree(g))    # ricorsione
    return r

def copia(griglia):
    ''' metodo che restituisce copia della griglia '''
    g = []      # copia griglia
    for i in griglia:
        g.append(i[:])      # copio elementi
    return g
