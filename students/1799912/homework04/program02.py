class NodoTris:
    def __init__(self, griglia):
        self.name = griglia
        self.issue, self.next_one, self.free_one = self.obtain_infos()
        self.sons = self.find_sons()

    def tipo(self):
        return self.issue
    
    def vittorie_livello(self, giocatore, h):
        numb = 0
        ls_numb = [0]
        finale = self.lvl_winning(giocatore, numb, h, ls_numb)
        return finale
    
    def find_issues(self, ls_num):
        if self.issue is '-':
            ls_num[0] += 1
        if self.issue is 'o':
            ls_num[1] += 1
        if self.issue is 'x':
            ls_num[2] += 1
        for schema in self.sons:
            schema.find_issues(ls_num)
        return ls_num
    
    def find_right_strategy(self, plr):
        if self.issue != '?':
            s = self.issue != plr
            return s
        if self.next_one != plr:
            return self.wrong_strategy(plr)
        else:
            return self.right_strategy(plr)
        
    def right_strategy(self,ply):
        for crux in self.sons:
                if crux.find_right_strategy(ply) == True:
                    return True
        return False

    def wrong_strategy(self,ply):
        for crux in self.sons:
                if crux.find_right_strategy(ply) == False:
                    return False
        return True
    
    def esiti(self):
        tupla_list_num = [0, 0, 0]
        self.find_issues(tupla_list_num)
        return tuple(tupla_list_num)

    def obtain_infos(self):
        x_symbol = 0
        o_symbol = 0
        prox_str=""
        advice=""
        col_tic_toe = ['', '', '']
        rig_tic_toe = ['', '', '']
        free_one = []
        rig_tic_toe,col_tic_toe,free_one,x_symbol,o_symbol = self.get_info(col_tic_toe,rig_tic_toe,x_symbol,o_symbol,free_one)
        rig_tic_toe,col_tic_toe=self.get_info_sup(col_tic_toe,rig_tic_toe)
        advice,prox_str=self.get_inf_sup2(x_symbol,o_symbol,rig_tic_toe,col_tic_toe,prox_str,advice,free_one)
        return advice, prox_str, free_one        
        
    def strategia_vincente(self, giocatore):
        return self.find_right_strategy(giocatore)

    def lvl_winning(self, player, lvl, finished, s):
        if lvl == finished:
            if self.issue is player:
                s[0] += 1
        else:
            for crux in self.sons:
                lvl = lvl + 1
                crux.lvl_winning(player, lvl, finished, s)
       
        return s[0]

    def find_sons_sup(self,ls_ret):
        for box in self.free_one:
                winter_scheme = []
                winter_scheme.append(self.name[0][:])
                winter_scheme.append(self.name[1][:])
                winter_scheme.append(self.name[2][:])
                winter_scheme[box[0]][box[1]] = self.next_one
                ls_ret.append(NodoTris(winter_scheme))
        return ls_ret
        

    def find_sons(self):
        return_list = []
        if self.issue == "?":
            return_list=self.find_sons_sup(return_list)
        return return_list
    
    def get_inf_sup2(self,X,O,rig,col,prox,adc,free):
        if X == O:
            prox = "o"
        else:
            prox = "x"
        if "ooo" in col or "ooo" in rig:
            adc = "o"
        elif "xxx" in col or "xxx" in rig:
            adc = "x"
        elif len(free) != 0:
            adc = "?"
        else:
            adc = "-"
        return adc,prox

    def get_info1(self,rig,col,V,val,x,y):
        rig[y] += val
        col[x] += val
        V += 1
        return rig,col,V

    def get_info(self,col,rig,X,O,free):
        xx='x'
        oo='o'
        for y in range(3):
            for x in range(3):
                if self.name[y][x] is xx:
                    rig,col,X=self.get_info1(rig,col,X,xx,x,y)
                if self.name[y][x] is oo:
                    rig,col,O=self.get_info1(rig,col,O,oo,x,y)
                if self.name[y][x] is '':
                    free.append((y, x))
        return rig,col,free,X,O
    def get_info_sup(self,col,rig):
        rig.append("")
        col.append("")
        col[3] += self.name[0][0]
        col[3] += self.name[1][1]
        col[3] += self.name[2][2]
        rig[3] += self.name[0][2]
        rig[3] += self.name[1][1]
        rig[3] += self.name[2][0]
        return rig,col
    
        
    


def gen_tree(griglia):
    return NodoTris(griglia)
