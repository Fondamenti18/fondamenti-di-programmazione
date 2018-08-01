p,o,x = 0,0,0

class NodoTris:
    def __init__(self, griglia, win_o, win_x, spaces):
        'Costruttore'
        self.nome = griglia
        self.lista_figli = []
        self.win_o = win_o
        self.win_x = win_x
        self.spaces = spaces

    def add_info(self, win_o, win_x, spaces):
        'Metodo usato per aggiungere in un secondo momento info aggiuntive'
        self.win_o = win_o
        self.win_x = win_x
        self.spaces = spaces

    def tipo(self):
        'Metodo tipo'
        if self.win_o: return 'o'
        elif self.win_x: return 'x'
        elif self.spaces: return '?'
        return '-'

    def esiti(self):
        "Metodo main usato per passare come argomento la lista dell'istanza a cerca_esiti"
        global p,o,x
        p,o,x = 0,0,0
        return self.cerca_esiti([self])

    def cerca_esiti(self, ls):
        'Metodo usato per cercare esiti'
        global p,o,x
        for el in ls:
            if el.win_o: o += 1
            elif el.win_x: x += 1
            elif not el.spaces: p += 1
            self.cerca_esiti(el.lista_figli)
        return p,o,x

    def vittorie_livello(self, giocatore, h):
        'Metodo main usato per vittorie_livello'
        if giocatore == 'o': return self.cerca_livello_o(giocatore, h, [self], 0, 0)
        return self.cerca_livello_x(giocatore, h, [self], 0, 0)

    def cerca_livello_o(self, giocatore, h, ls, found, alt):
        'Metodo che cerca il livello di o'
        if not ls: return found
        lista = []
        for child in ls:
            lista += child.lista_figli
            if alt == h and child.win_o: found += 1
        alt += 1
        found = self.cerca_livello_o(giocatore, h, lista, found, alt)
        return found

    def cerca_livello_x(self, giocatore, h, ls, found, alt):
        'Metodo che cerca il livello di x'
        if not ls: return found
        lista = []
        for child in ls:
            lista += child.lista_figli
            if alt == h and child.win_x: found += 1
        alt += 1
        found = self.cerca_livello_x(giocatore, h, lista, found, alt)
        return found

    def strategia_vincente(self,giocatore):
        ''' Metodo principale che richiama strategia_vincente_o o strategia_vincente_x in base al giocatore
        scelto. Assegna ad alpha un valore di default piccolissimo, mentre a beta un valore gigante.'''
        spazi = self.spaces%2
        if giocatore == 'o':
            if spazi:
                return self.strategia_vincente_o(self, 1, -99, 99) == 5
            else:
                return self.strategia_vincente_o(self, 0, -99, 99) == 5
        else:
            if not spazi:
                return self.strategia_vincente_x(self, 1, -99, 99) == 5
            else:
                return self.strategia_vincente_x(self, 0, -99, 99) == 5

    def strategia_vincente_o(self, nodo, g, alpha, beta):
        'Metodo utilizzato per valutare la strategia di o'
        if not nodo.lista_figli: return self.check_o_win(nodo)
        if g:
            val_default = -10
            for child in nodo.lista_figli:
                val_massimo = self.strategia_vincente_o(child, 0, alpha, beta)
                val_default = self.max_val(val_massimo, val_default)
                alpha = max(alpha, val_default)
                if beta <= alpha: break
            return val_default
        else:
            val_default = 10
            for child in nodo.lista_figli:
                val_minimo = self.strategia_vincente_o(child, 1, alpha, beta)
                val_default = self.min_val(val_minimo, val_default)
                beta = min(beta, val_default)
                if beta <= alpha: break
            return val_default

    def strategia_vincente_x(self, nodo, g, alpha, beta):
        'Metodo utilizzato per valutare la strategia di x'
        if not nodo.lista_figli: return self.check_x_win(nodo)
        if g:
            val_default = -10
            for child in nodo.lista_figli:
                val_massimo = self.strategia_vincente_o(child, 0, alpha, beta)
                val_default = self.max_val(val_massimo, val_default)
                alpha = max(alpha, val_default)
                if beta <= alpha:
                    break
            return val_default
        else:
            val_default = 10
            for child in nodo.lista_figli:
                val_minimo = self.strategia_vincente_o(child, 1, alpha, beta)
                val_default = self.min_val(val_minimo, val_default)
                beta = min(beta, val_default)
                if beta <= alpha:
                    break
            return val_default
    
    def max_val(self, val_massimo, val_default):
        if val_massimo > val_default:
            return val_massimo
        return val_default
    
    def min_val(self, val_minimo, val_default):
        if val_minimo < val_default:
            return val_minimo
        return val_default

    def check_o_win(self, nodo):
        'Check sulla vittoria di o'
        if nodo.win_o: return 5
        elif nodo.win_x: return -5
        else: return 0

    def check_x_win(self, nodo):
        'Check sulla vittoria di x'
        if nodo.win_x: return 5
        elif nodo.win_o: return -5
        else: return 0

def gen_tree(matrix):
    "Funzione main usata per generare l'albero"
    n_matrix = []
    for el in matrix:
        n_matrix += el
    oWin, xWin = winner(n_matrix)
    cells = n_matrix.count('')
    root = NodoTris(n_matrix, oWin, xWin, cells)
    tree_nodes([root])
    return root

def tree_nodes(nodes):
    "Funzione ricorsiva che costruire l'albero"
    ls_nodes = []
    count = nodes[0].nome.count('')
    if count % 2: pg = 'o'
    else: pg = 'x'
    for node in nodes:
        winnerO, winnerX = winner(node.nome)
        if winnerO or winnerX: continue
        if '' in node.nome: 
            ls_figli = look_for_childs(node.nome, pg)
            node.lista_figli += ls_figli
        node.add_info(winnerO, winnerX, count)
        ls_nodes += node.lista_figli
    if not ls_nodes: return
    tree_nodes( ls_nodes )
        
def look_for_childs(matrix, pg):
    'Funzione che cerca i figli dei nodi'
    c_matrix = matrix[:]
    count = c_matrix.count('')
    if count == 1:
        c_matrix[c_matrix.index('')] = pg
        return [NodoTris(c_matrix, *winner(c_matrix) , count)]
    ls_figli = []
    for j in range(9):
        if not c_matrix[j]:
            c_matrix[j] = pg
            winO, winX = winner(c_matrix)
            ls_figli.append( NodoTris(c_matrix, winO, winX, count) )
            c_matrix = matrix[:]
    return ls_figli
    
def winner(matrix):
    "Funzione main usata per determinare l'esito della partita"
    xx, yy = winner_righe(matrix)
    if xx or yy: return xx,yy
    xxx, yyy = winner_colonne(matrix)
    if xxx or yyy: return xxx,yyy
    xxxx, yyyy = winner_diagonale(matrix)
    if xxxx or yyyy: return xxxx, yyyy
    return False, False

def winner_righe(matrix):
    for i in range(0,7,3):
        if matrix[0+i] == 'o':
            if matrix[0+i] == matrix[1+i] == matrix[2+i]: return True, False
        elif matrix[0+i] == 'x':
            if matrix[0+i] == matrix[1+i] == matrix[2+i]: return False, True
    return False, False

def winner_colonne(matrix):
    for i in range(3):
        if matrix[0+i] == 'o':
            if matrix[0+i] == matrix[3+i] == matrix[6+i] : return True, False
        elif matrix[0+i] == 'x':
            if matrix[0+i] == matrix[3+i] == matrix[6+i] : return False, True
    return False, False    

def winner_diagonale(matrix):
    if matrix[4] == 'o':
        if matrix[0] ==  matrix[4] == matrix[8]: return True, False
        elif matrix[2] == matrix[4] == matrix[6]: return True, False
    elif matrix[4] == 'x':
        if matrix[0] == matrix[4] == matrix[8]: return False, True
        elif matrix[2] == matrix[4] == matrix[6]: return False, True
    return False, False