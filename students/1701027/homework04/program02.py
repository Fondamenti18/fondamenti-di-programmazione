
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.esito = ''
        self.score = 0
    
    def tipo(self):
        return self.esito
        
    def esiti(self):
        lista = [0,0,0]
        lista = calcesiti(self,lista)
        return(lista[0],lista[1],lista[2])
    
    def vittorie_livello(self, giocatore, h):
        h1 = 0
        c = vliv(self,giocatore,h,h1)
        return c
    
    def strategia_vincente(self,giocatore):
        nowplay = 'o'
        opponent = 'x'
        l = []
        sv(self,giocatore,nowplay,opponent,l)
        return True in l
        
        
        
def sv(nodo,giocatore,nowplay,opponent,l):
    maxx = 1
    app = nodo
    if nodo.lista_figli != []:
        for figlio in nodo.lista_figli:
            c = 0
            h = 0
            t = calcscore(figlio,c,h)
            if nowplay == 'o':
                if maxx < t:
                    maxx = t
                    app = figlio
            else:
                if maxx > t:
                    maxx = t
                    app = figlio
        sv(app,giocatore,opponent,nowplay,l)
    else:
        ris = nodo.esito == giocatore or nodo.esito == '-'
        l.append(ris)
        return l
    return l
    
        
def calcscore(nodo,c,h):
    c += nodo.score-h
    h += 1
    for figlio in nodo.lista_figli:
        c = calcscore(figlio,c,h)
    return c
     
        
def vliv(nodo,giocatore,h,h1):
    c = 0
    if h == h1:
        if nodo.esito == giocatore: 
            c += 1
        return c
    h1 += 1
    for figlio in nodo.lista_figli:
        c += vliv(figlio,giocatore,h,h1)
    return c
    
        
def calcesiti(n,lista):
    if n.lista_figli == []:
        if n.esito == 'x': lista[2] += 1
        if n.esito == 'o': lista[1] += 1
        if n.esito == '-': lista[0] += 1
    for child in n.lista_figli:
        lista = calcesiti(child,lista)
    return lista
        
        
def gen_tree(griglia):
    r = NodoTris(griglia)
    if wincol(griglia) == False and winraw(griglia) == False and windiag(griglia) == False:
        c = griglia[0].count('') + griglia[1].count('') + griglia[2].count('')
        if c != 0:
            r.esito = '?'
            for y,i in enumerate(griglia):
                for x,j in enumerate(i):
                    if j == '':
                        griglia2 = [x[:] for x in griglia]
                        if c % 2 != 0:
                            griglia2[y][x] = 'o'
                        elif c % 2 == 0: 
                            griglia2[y][x] = 'x'
                        r.lista_figli += [gen_tree(griglia2)]
        else:
            r.esito = '-'
    else:
        l = [wincol(griglia) , winraw(griglia) , windiag(griglia)]
        if 'o' in l:
            r.esito = 'o'
            r.score = 10
        elif 'x' in l:
            r.esito = 'x'
            r.score = -10
    return r
    
    
            

def winraw(griglia):
    for i in range(3):
        if '' not in set(griglia[i]) and len(set(griglia[i])) == 1 :
            return griglia[i][0]
    return False
        
def wincol(griglia):
    for i in range(3):
        if griglia[0][i] != '' and (griglia[0][i] == griglia[1][i] == griglia[2][i]):
            return griglia[0][i]
    return False
        
def windiag(griglia):
    if  griglia[0][0] != '' and (griglia[0][0] == griglia[1][1] == griglia[2][2]):
        return griglia[0][0]
    if  griglia[0][2] != '' and (griglia[0][2] == griglia[1][1] == griglia[2][0]):
        return griglia[0][2]
    return False