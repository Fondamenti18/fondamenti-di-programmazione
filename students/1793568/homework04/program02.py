import copy

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli 
        self.mode = "o"

    def create_sub_tree(self):
        self.create_son_list()
        for el in self.lista_figli:
            if el.check_node() == False:
                el.create_sub_tree()

    def create_son_list(self):
        LS = copy.deepcopy(self.nome)
        Res = []
        for y in range(len(self.nome)):
            for x in range(len(self.nome[0])):
                if self.nome[y][x] == '':
                    SL = copy.deepcopy(self.nome)
                    SL[y][x] = self.mode
                    Son = NodoTris(SL)
                    Son.mode = self.change_mode()
                    self.lista_figli += [Son]

    def change_mode(self):
        if self.mode == 'o':
            return 'x'
        else:
            return 'o'

    def check_node(self):
        V = self.check_V()
        O = self.check_O()
        D = self.check_D()
        if V[0]:
            return True
        elif O[0]:
            return True
        elif D[0]:
            return True
        return False

    def check_V(self, history = set()):
        if (self.nome[0][0] == self.nome[1][0] and self.nome[1][0] == self.nome[2][0]) and self.nome[0][0] != '' and ((0,0),(1,0),(2,0)) not in history:
            history.update(((0,0),(1,0),(2,0)))
            return [True,self.nome[0][0]]
        elif (self.nome[0][1] == self.nome[1][1] and self.nome[1][1] == self.nome[2][1]) and self.nome[0][1] != '' and ((0,1),(1,1),(2,1)) not in history:
            history.update(((0,1),(1,1),(2,1)))
            return [True,self.nome[0][1]]
        elif (self.nome[0][2] == self.nome[1][2] and self.nome[1][2] == self.nome[2][2]) and self.nome[0][2] != '' and ((0,2),(1,2),(2,2)) not in history:
            history.update(((0,2),(1,2),(2,2)))
            return [True,self.nome[0][2]]
        return [False]

    def check_O(self, history = set()):
        if (self.nome[0][0] == self.nome[0][1] and self.nome[0][1] == self.nome[0][2]) and self.nome[0][0] != '' and ((0,0),(0,1),(0,2)) not in history:
            history.update(((0,0),(0,1),(0,2)))
            return [True,self.nome[0][0]]
        elif (self.nome[1][0] == self.nome[1][1] and self.nome[1][1] == self.nome[1][2]) and self.nome[1][0] != '' and ((1,0),(1,1),(1,2)) not in history:
            history.update(((1,0),(1,1),(1,2)))
            return [True,self.nome[1][0]]
        elif (self.nome[2][0] == self.nome[2][1] and self.nome[2][1] == self.nome[2][2]) and self.nome[2][0] != '' and ((2,0),(2,1),(2,2)) not in history:
            history.update(((2,0),(2,1),(2,2)))
            return [True,self.nome[2][0]]
        return [False]

    def check_D(self, history = set()):
        if (self.nome[0][0] == self.nome[1][1] and self.nome[1][1] == self.nome[2][2]) and self.nome[0][0] != '' and ((0,0),(1,1),(2,2)) not in history:
            #print("SET: ",history)
            history.update(((0,0),(1,1),(2,2)))
            return [True,self.nome[0][0]]
        elif (self.nome[2][0] == self.nome[1][1] and self.nome[1][1] == self.nome[0][2]) and self.nome[2][0] != '' and ((2,0),(1,1),(2,0)) not in history:
            history.update(((2,0),(1,1),(2,0)))
            return [True,self.nome[2][0]]
        return [False]

    def check_comp(self):
        for y in range(len(self.nome)):
            for x in range(len(self.nome[0])):
                if self.nome[y][x] == '':
                    return False
        return True

    def tipo(self):
        if self.check_node():

            V = self.check_V()
            O = self.check_O()
            D = self.check_D()
            if V[0]:
                return V[1]
            elif O[0]:
                return O[1]
            elif D[0]:
                return D[1]
        else:
            if self.check_comp():
                return '-'
            else:
                return '?'

    def check_t(self,R,H):
    	#print(H)
        if self.check_node():
            V = self.check_V(H)
            O = self.check_O(H)
            D = self.check_D(H)
            if V[0]:
                if V[1] == 'o':
                    R[1] += 1
                else:
                    R[2] += 1
            elif O[0]:
                if O[1] == 'o':
                    R[1] += 1
                else:
                    R[2] += 1
            elif D[0]:
                if D[1] == 'o':
                    R[1] += 1
                else:
                    #print("NODO: ",self.nome," SET: ",H)
                    R[2] += 1
        else:
            if self.check_comp():
                R[0] += 1

        for el in self.lista_figli:
            el.check_t(R,H)

    def esiti(self):
        R = [0,0,0]
        story = set()
        self.check_t(R,story)
        return (R[0],R[1],R[2])

    def control_player(self,count,player,h,hc):
        if self.check_node() and hc[0] == h:
            V = self.check_V()
            O = self.check_O()
            D = self.check_D()

            if V[0] and V[1] == player:
                count[0] += 1
            if O[0] and O[1] == player:
                count[0] += 1
            if D[0] and D[1] == player:
                count[0] += 1

        hc[0] += 1

        for el in self.lista_figli:
            el.control_player(count,player,h,hc)

        hc[0] -= 1


    def vittorie_livello(self, giocatore, h):
        count = [0]
        hc = [0]
        self.control_player(count,giocatore,h,hc)
        return count[0]

    def check_victorius(self,player,f):
        if self.check_node():
            V = self.check_V()
            O = self.check_O()
            D = self.check_D()

            if V[0] and V[1] == player:
                f[0] = True
            elif O[0] and O[1] == player:
                f[0] = True
            elif D[0] and D[1] == player:
                f[0] = True
            else:
                f[0] = False
        else:
            if self.check_comp():
                f[0] = False
            else:
                for el in self.lista_figli:
                    el.check_victorius(player,f)

    def strategia_vincente(self,giocatore):
        F = [False]
        self.check_victorius(giocatore,F)
        return F[0]

def gen_tree(griglia):
   root = NodoTris(griglia)
   root.create_sub_tree()
   return root
