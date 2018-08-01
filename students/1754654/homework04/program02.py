

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []
        self.tree_configuration = dict()
        self.tree_esiti = {'x':0,'o':0,'-':0}
        self.level_win =  {'x':0,'o':0,'-':0}

    def caselle_vuote(self):
        caselle_vuote = []
        for _ in [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]:
            if self.nome[_[0]][_[1]] == '':
                caselle_vuote.append(_)
        return caselle_vuote

    def tipo(self):
        lst    = [[self.nome[0][0],self.nome[0][1],self.nome[0][2]],
                [self.nome[1][0],self.nome[1][1],self.nome[1][2]],
                [self.nome[2][0],self.nome[2][1],self.nome[2][2]],
                [self.nome[0][0],self.nome[1][0],self.nome[2][0]],
                [self.nome[0][1],self.nome[1][1],self.nome[2][1]],
                [self.nome[0][2],self.nome[1][2],self.nome[2][2]],
                [self.nome[0][0],self.nome[1][1],self.nome[2][2]],
                [self.nome[2][0],self.nome[1][1],self.nome[0][2]]]

        for configuration in lst:
            if configuration[0] != '' and configuration[0] == configuration[1] and configuration[0] == configuration[2]:
                return configuration[0]
        if self.num_caselle_vuote() >= 1:
            return '?'
        else:
            return '-'

    def num_caselle_vuote(self):
        counter = 0
        for box in [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]:
            if self.nome[box[0]][box[1]] == '':
                counter = counter + 1
        return counter

    def esiti(self):
        root = self.nome
        d_esiti = self.explore(root)
        tpl_esiti = (d_esiti['-'],d_esiti['o'],d_esiti['x'])
        return tpl_esiti

    def explore(self,root_):
        node = NodoTris(root_)
        key = node.tipo()
        if key != '?':
            self.tree_esiti[key] = self.tree_esiti[key] + 1
        else:
            all_conf = self.tree_configuration[str(root_)]
            for conf in all_conf:
                self.explore(conf)
        return self.tree_esiti

    def possibilities(self):
        to_fill = self.caselle_vuote()
        father_ = self.nome
        for box in to_fill:
            new_node_tris = NodoTris(self.make_copy(father_))
            new_node_tris.add_move(box)
            self.lista_figli.append(new_node_tris.nome)
        return self.lista_figli



    def add_move(self,where):
        if self.num_caselle_vuote() % 2 != 0:
            move = 'o'
        else: move = 'x'
        self.nome[where[0]][where[1]] = move
        return

    def make_copy(self, grill):
        f_l = []
        [f_l.append(grill[y][:]) for y in range(3)]
        return f_l

    def vittorie_livello(self, giocatore, h):
        victory = self.explore_with_height(self.nome,giocatore,0,h)
        self.level_win =  {'x':0,'o':0,'-':0}
        return victory[giocatore]


    def explore_with_height(self,root,gamer,height,h):
        nodo = NodoTris(root)
        key = nodo.tipo()
        if key != '?':
            if key == gamer and height == h:
                self.level_win[key] = self.level_win[key] + 1
                return
        else:
            if height < h:
                for conf in self.tree_configuration[str(root)]:
                    self.explore_with_height(conf,gamer,height+1,h)
        return self.level_win


    def add_element_empty_grill(self):
        root_ = self.nome
        lst_figli = []
        new_node_tris = NodoTris(self.make_copy(root_))
        lst_figli = new_node_tris.add_move((1,0))
        return lst_figli

    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        strategy = self.is_winne(self.nome,giocatore,0)
        return strategy


    def is_winne(self,root,giocatore,h):
        '''decidiamo se il giocatore ha una strategia vincente o meno'''
        l = {'x':'o','o':'x'}
        loser = l[giocatore]
        root_ = NodoTris(root)
        key = root_.tipo()
        end = True
        if key != '?':
            return
        else:
            for son in self.tree_configuration[str(root)]:
                tocheck = NodoTris(son)
                if tocheck.tipo() == loser:
                    end = False
                    break
            if end != False:
                for conf in self.tree_configuration[str(root)]:
                    self.is_winne(conf,giocatore,h+1)
        return end



gen_tree_dict = dict()
def gen_tree(griglia):
    '''inserire qui il vostro codice'''
    global gen_tree_dict
    root = NodoTris(griglia)
    if root.tipo() != '?':
        gen_tree_dict[str(root.nome)] = []
        return root
    else:
        lst = root.possibilities()
        gen_tree_dict[str(root.nome)] = lst
        for configuration in lst:
            gen_tree(configuration)

    root.tree_configuration = gen_tree_dict
    return root










if __name__ == '__main__':

    g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
    g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
    g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
    g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]

    lista=[g1, g2, g3, g4]
    lista1=[gen_tree(x) for x in lista]

    [y.tipo() for y in lista1]


    [y.esiti() for y in lista1]
    [lista1[0].vittorie_livello('o',h) for h in range(4)]
    [lista1[0].vittorie_livello('x',h) for h in range(4)]


    [lista1[0].strategia_vincente('x'), lista1[0].strategia_vincente('o')]


# def gen_from_empty_grill():
#     g1 = [['o', '', ''], ['', '', ''], ['', '', '']]
#     global gen_tree_dict
#     gen_tree(g1)
#     g1_dict = gen_tree_dict
#     g2_dict = dict()
#     for key in g1_dict:
#         print(rotate_strkey(key))


# def rotate_strkey(key):
#     alfa = [key[0],key[1],key[2]]
#     beta = [key[3],key[4],key[5]]
#     gamma =[key[6],key[7],key[8]]
#     return alfa,beta,gamma
