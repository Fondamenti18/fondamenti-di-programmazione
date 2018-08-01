import copy

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.mossa = ""

    def tipo(self):
        '''inserire qui il vostro codice'''
        griglia = self.nome
        # RIGHE
        for row in griglia:
            if row[0] == row[1] and row[1] == row[2] and row[0] != '':
                return row[0]
        # COLONNE
        for i in range(3):
            if griglia[0][i] == griglia[1][i] and griglia[1][i] == griglia[2][i] and griglia[0][i] != '':
                return griglia[0][i]
        # DIAGONALI
        if griglia[0][0] == griglia[1][1] and griglia[1][1] == griglia[2][2] and griglia[0][0] != '':
                return griglia[0][0]
        if griglia[0][2] == griglia[1][1] and griglia[1][1] == griglia[2][0] and griglia[0][2] != '':
                return griglia[0][2]
        # NON TERMINATO
        for row in griglia:
            if '' in row:
                return '?'
        return '-'

    def esiti(self):
        '''inserire qui il vostro codice'''
        res = [0, 0, 0]
        tipo = self.tipo()
        if tipo == 'o':
            res[1] = 1
        elif tipo == 'x':
            res[2] = 1
        elif tipo == '-':
            res[0] = 1
        if self.lista_figli != []:
            for x in self.lista_figli:
                ret = list(x.esiti())
                for i in range(3):
                    res[i] += ret[i]
        return (res[0], res[1], res[2])

    def livello(self, h):
        nodi = list()
        if h == 1:
            return self.lista_figli
        else:
            for x in self.lista_figli:
                nodi += x.livello(h-1)
            return nodi

    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        nodi = list()
        if h == 0:
            nodi.append(self)
        else:
            nodi = self.livello(h)
        res = 0
        for x in nodi:
            if x.tipo() == giocatore:
                res += 1
        return res

    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        t = self.tipo()
        if uguale(t, giocatore):
            return True
        if uguale(t, '?'):
            if not uguale(self.mossa, giocatore):
                for nodo in self.lista_figli:
                    if not nodo.strategia_vincente(giocatore):
                        return False
                return True
            else:
                for nodo in self.lista_figli:
                    if nodo.strategia_vincente(giocatore):
                        return True
                return False
        else:
            return False

def count_undefined(griglia):
    count = 0
    for x in griglia:
        for y in x:
            if y == '':
                count += 1
    return count

def uguale(a, b):
    return a == b

def posiziona(griglia, mossa, num):
    count = 0
    res = copy.deepcopy(griglia)
    for i,x in enumerate(griglia):
        for k,y in enumerate(x):
            if y == '':
                if count == num:
                    res[i][k] = mossa
                    return res
                count += 1

def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    tree = NodoTris(griglia)
    num = count_undefined(griglia)
    if num%2 == 0:
        mossa = 'x'
        tree.mossa = 'x'
    else:
        mossa = 'o'
        tree.mossa = 'o'
    figli = list()
    for x in range(num):
        if tree.tipo() == "?":
            child = posiziona(griglia, mossa, x)
            figli.append(gen_tree(child))
    tree.lista_figli = figli
    return tree
