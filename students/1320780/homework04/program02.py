def player_turn(griglia):
    countO = 0
    countX = 0
    
    sPl = 1
    
    for i in range(3):
        for j in range(3):
            if griglia[i][j] == 'o':
                countO += 1
            if griglia[i][j] == 'x':
                countX += 1
                
    if countO == countX:
        sPl = 0
    return sPl
    
def esiti_update(node, triple):
    t = node.tipo()
    if t == '-':
        triple[0] += 1
    elif t == 'o':
        triple[1] += 1
    elif t == 'x':
        triple[2] += 1
    else:
        for cNode in node.lista_figli:
            esiti_update(cNode, triple)
            
def vict_by_level(node, pl, lev, fLev):
    cnt = 0
    
    if lev < fLev:
        for cNode in node.lista_figli:
            cnt += vict_by_level(cNode, pl, lev + 1, fLev)
    elif lev == fLev and node.tipo() == pl:
        cnt += 1
    
    return cnt
    
def notie_esiti_update(node, doppie):
    t = node.tipo()
    
    if t == 'o':
        doppie[0] += 1
    elif t == 'x':
        doppie[1] += 1
    else:
        for cNode in node.lista_figli:
            notie_esiti_update(cNode, doppie)

def calcPeso(esiti, pl):
    if pl == 'o':
        return esiti[0] - esiti[1]
    return esiti[1] - esiti[0]

def bestMove(node):

    if not node.lista_figli:
        return node
    pls = ['o','x']
    crnt = pls[player_turn(node.nome)]
    pls.remove(crnt)
    enemy = pls[0]
    
    cEsiti = []
    
    winner = None
    
    for cNode in node.lista_figli:
        es = [0,0]
        notie_esiti_update(cNode, es)
        cEsiti.append(calcPeso(es, crnt))
    
    maxEs = max(cEsiti)
    
    for i in range(len(node.lista_figli)):
        if maxEs != 0 and cEsiti[i] == maxEs:
            winner = bestMove(node.lista_figli[i])
    
    return winner
        
def rowWin(node):
    result = '?'
    for i in range(3):
        if (node.nome[i][0] == node.nome[i][1] and node.nome[i][1] == node.nome[i][2]) and (node.nome[i][0] != ''):
            result = node.nome[i][0]
            break
    return result
    
def columnWin(node):
    result = '?'
    for i in range(3):
        if (node.nome[0][i] == node.nome[1][i] and node.nome[1][i] == node.nome[2][i]) and (node.nome[0][i] != ''):
            result = node.nome[0][i]
            break
    return result
    
def firstDiagWin(node):
    result = '?'
    if (node.nome[0][0] == node.nome[1][1] and node.nome[1][1] == node.nome[2][2]) and (node.nome[0][0] != ''):
        result = node.nome[0][0]
    return result
    
def secDiagWin(node):
    result = '?'
    if (node.nome[2][0] == node.nome[1][1] and node.nome[1][1] == node.nome[0][2]) and (node.nome[2][0] != ''):
        result = node.nome[2][0]
    return result

def fullOrTie(node):
    result = '-'
    for i in range(3):
        for j in range(3):
            if node.nome[i][j] == '':
                result = '?'
                break
    return result
        
            
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []
    
    def tipo(self):
        result = rowWin(self)
        if result == '?':
            result = columnWin(self)
            if result == '?':
                result = firstDiagWin(self)
                if result == '?':
                    result = secDiagWin(self)
                    if result == '?':
                        result = fullOrTie(self)
        
        return result
    
    def esiti(self):
        triple = [0, 0, 0]
        esiti_update(self, triple)
        return tuple(triple)
    
    def vittorie_livello(self, giocatore, h):
        return vict_by_level(self, giocatore, 0, h)            
    
    def strategia_vincente(self,giocatore):
        end = bestMove(self)
        return end != None and giocatore == end.tipo()
        
def gen_tree_player(griglia, pl, pls):
    node = NodoTris(griglia)
    
    if node.tipo() == '?':
        for i in range(3):
            for j in range(3):
                if griglia[i][j] == '':
                    sGrid = []
                    for row in griglia:
                        sGrid.append(row.copy())
                    sGrid[i][j] = pls[pl]
                    node.lista_figli.append(gen_tree_player(sGrid, (pl + 1) % 2, pls))
                    
    return node
        
def gen_tree(griglia):
    return gen_tree_player(griglia, player_turn(griglia), ['o', 'x'])