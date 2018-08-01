import sys
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def vittoria_giocatore(self,simbolo):
        
        if (self.nome[0][0] == simbolo ):
            if (self.nome[1][0] == simbolo and self.nome[2][0] == simbolo ):
                return True
            elif (self.nome[1][1] == simbolo and self.nome[2][2] == simbolo ):
                return True
            elif (self.nome[0][1] == simbolo and self.nome[0][2] == simbolo ):
                return True
        if (self.nome[1][0] == simbolo and self.nome[1][1] == simbolo and self.nome[1][2] == simbolo):
            return True
        if (self.nome[2][0] == simbolo):
            if(self.nome[2][1] == simbolo and self.nome[2][2] == simbolo ):
                return True
            elif(self.nome[1][1] == simbolo and self.nome[0][2] == simbolo ):
                return True
        if( self.nome[0][1] == simbolo and self.nome[1][1] == simbolo  and self.nome[2][1] == simbolo ):
            return True
        if(self.nome[0][2] == simbolo and self.nome[1][2] == simbolo  and self.nome[2][2] == simbolo):
            return True
        
        return False
    
    def tipo(self):
        if ( self.vittoria_giocatore('x')):
            return 'x'
        if (self.vittoria_giocatore('o')):
            return 'o'
        griglia = self.nome
        dim = len(griglia)
        for i in range(dim):
            for j in range(dim):
                if (griglia[i][j] == ''):
                    return '?'
        return '-'
                
    
    
    def esiti_ricorsivo(self,esiti):
        
        
        numero_patte = esiti[0]
        vittorie_o = esiti[1]
        vittorie_x = esiti[2]
        
       
        esito = self.tipo()
        if esito == "x":
            vittorie_x = vittorie_x+1
        elif esito =="o":
            vittorie_o = vittorie_o+1
        elif esito == '-':
            numero_patte = numero_patte+1
            
        my_esiti = (numero_patte,vittorie_o,vittorie_x)
        
        for figlio in self.lista_figli:
            esiti_figlio = figlio.esiti_ricorsivo(my_esiti)
            my_esiti = esiti_figlio
        return my_esiti
        
    def esiti(self):
        return self.esiti_ricorsivo((0,0,0))


    def vittorie_livello_ric(self,giocatore,h,conta_lvl,conta_vittorie):
        if conta_lvl == h:
            if self.tipo() == giocatore:
                conta_vittorie += 1
            return conta_vittorie
        elif conta_lvl > h:
            return conta_vittorie
        for figlio in self.lista_figli:
            conta_vittorie = figlio.vittorie_livello_ric(giocatore,h,conta_lvl+1,conta_vittorie)
        return conta_vittorie
        
        
    def vittorie_livello(self, giocatore, h):
        return self.vittorie_livello_ric(giocatore,h,0,0)
        
      
    def min_livello_vittoria(self,giocatore,livello,minimo):
        if self.tipo() == giocatore:
            return livello
        for figlio in self.lista_figli:
            my_min = figlio.min_livello_vittoria(giocatore,livello+1,minimo)
            if my_min < minimo:
                minimo = my_min
        return minimo
        
        
    def strategia_vincente(self,giocatore):
        sym1 = giocatore
        if giocatore == 'x':
            sym2 = 'o'
        else:
            sym2 = 'x'
        min_gioc_1 = self.min_livello_vittoria(sym1,0,sys.maxsize)
        min_gioc_2 = self.min_livello_vittoria(sym2,0,sys.maxsize)
        
        return min_gioc_1 < min_gioc_2
        
     
    def aggiungi_figlio (self,nodo):
        self.lista_figli.append(nodo)


def gen_tree_ricorsivo(griglia,caselle_disponibili,simbolo):
    nodo_corrente = NodoTris(griglia)
    if nodo_corrente.tipo() != '?':
        return nodo_corrente
    if (simbolo == 'o'):
        new_simbolo = 'x'
    else:
        new_simbolo = 'o'
    for my_casella in caselle_disponibili:
        new_griglia =[row[:] for row in griglia]
        new_griglia[my_casella[0]][my_casella[1]] = simbolo
        new_lista = caselle_disponibili.copy()
        new_lista.remove(my_casella)
        nodo = (gen_tree_ricorsivo(new_griglia,new_lista,new_simbolo))
        nodo_corrente.aggiungi_figlio(nodo)
    return  nodo_corrente
        

        
def gen_tree(griglia):
    lista_caselle_vuote = []
    dim = len(griglia)
    for i in range(dim):
            for j in range(dim):
                if (griglia[i][j] == ''):
                    lista_caselle_vuote.append((i,j))
    radice = gen_tree_ricorsivo(griglia,lista_caselle_vuote,'o')
    return radice
'''
g0=[['', '', ''], ['', '', ''], ['', '', '']]
g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]

g5=[['', 'x', ''], ['', 'o', ''], ['', '', '']]
g6=[['', 'o', ''], ['', 'x', ''], ['', '', '']]
g7=[['', 'x', 'o'], ['', '', ''], ['', '', '']]
g8=[['', 'o', 'x'], ['', '', ''], ['', '', '']]

listaa=[g1, g2, g3, g4]
listab=[g5, g6, g7, g8]
listac=[gen_tree(x) for x in listaa]

expected    = [0, 1, 0, 1]
lista=[listac[0].vittorie_livello('o',h) for h in range(4)]
lista2=[listac[0].strategia_vincente('x'), listac[0].strategia_vincente('o')]
print(lista2)
'''