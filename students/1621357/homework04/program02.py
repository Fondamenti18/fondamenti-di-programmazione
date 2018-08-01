import copy

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli

    def spaziVuoti(self):
        for row in range(0,3):
            for col in range(0,3):      
                if(self.nome[row][col] == ''):
                    return True 
    
    def tipo(self):
        if(self.nome[0][0] == self.nome[0][1] == self.nome[0][2] == 'x' or 
            self.nome[1][0] == self.nome[1][1] == self.nome[1][2] == 'x' or 
            self.nome[2][0] == self.nome[2][1] == self.nome[2][2] == 'x' or 
            self.nome[0][0] == self.nome[1][0] == self.nome[2][0] == 'x' or 
            self.nome[0][1] == self.nome[1][1] == self.nome[2][1] == 'x' or 
            self.nome[0][2] == self.nome[1][2] == self.nome[2][2] == 'x' or 
            self.nome[0][0] == self.nome[1][1] == self.nome[2][2] == 'x' or 
            self.nome[0][2] == self.nome[1][1] == self.nome[2][0] == 'x' ):
            return 'x'
        elif(self.nome[0][0] == self.nome[0][1] == self.nome[0][2] == 'o' or 
            self.nome[1][0] == self.nome[1][1] == self.nome[1][2] == 'o' or 
            self.nome[2][0] == self.nome[2][1] == self.nome[2][2] == 'o' or 
            self.nome[0][0] == self.nome[1][0] == self.nome[2][0] == 'o' or 
            self.nome[0][1] == self.nome[1][1] == self.nome[2][1] == 'o' or 
            self.nome[0][2] == self.nome[1][2] == self.nome[2][2] == 'o' or 
            self.nome[0][0] == self.nome[1][1] == self.nome[2][2] == 'o' or 
            self.nome[0][2] == self.nome[1][1] == self.nome[2][0] == 'o' ):
            return 'o'
        elif(self.spaziVuoti()):
            return '?'
        else:
            return '-'

    def check_num_x(self):
        num_x = 0
        for row in range(0,3):
            for col in range(0,3):
                if self.nome[row][col] == 'x':
                    num_x = num_x + 1
        return num_x

    def check_num_y(self):
        num_y = 0
        for row in range(0,3):
            for col in range(0,3):
                if self.nome[row][col] == 'o':
                    num_y = num_y + 1
        return num_y


    def check_turno(self):
        turno = None
        num_x = self.check_num_x()
        num_y = self.check_num_y()
        if( num_x >= num_y):
            turno = 'o'
        else:
            turno = 'x'
        return turno


    def esiti(self):
        # for x in self.lista_figli:
        #     print(x.nome)
        #     print(x.tipo())
        diz = {}
        diz = self.esitiricorsivo(self.lista_figli,diz)
        tupla = (diz.get('-'),diz.get('x'),diz.get('o'))
        return tupla

    def esitiricorsivo(self ,lista,diz,parity = 0,num_x = 0,num_o = 0):

        diz.setdefault('x',num_x)
        diz.setdefault('o',num_o)
        diz.setdefault('-',parity)

        for x in lista:

            listaa = x.lista_figli
            nodo = x

            if(x.tipo() == 'x'):
                num_x = diz.get('x')
                num_x +=1
                diz['x'] = num_x
            elif(x.tipo() == 'o'):
                num_o = diz.get('o')
                num_o = num_o + 1
                diz['o'] = num_o
            elif(x.tipo() == '-'):
                parity +=1
                diz['-'] = parity
            else:
                self.esitiricorsivo(listaa,diz,parity,num_x,num_o)
        return diz
                


    def esitiricorsivo2(self ,lista,diz,nodo,parity = 0,num_x = 0,num_o = 0):

        diz.setdefault('x',num_x)
        diz.setdefault('o',num_o)
        diz.setdefault('-',parity)

        if(nodo.tipo() == 'x'):
            num_x +=1
            diz['x'] = num_x
        elif nodo.tipo() == 'o':
            num_o += 1
            diz['o'] = num_o
        elif nodo.tipo() == '-':
            parity += 1
            diz['-'] = parity
        else:
            for x in lista:
                listaa = x.lista_figli
            diz.update(self.esitiricorsivo2(listaa,diz,x))
        return diz


    # def check_esiti_ricorsivo(self,griglia,nodo,tupla):
    #     turno = nodo.check_turno()
    #     if(nodo.tipo() == 'x'):
    #         print('x')
    #     elif(nodo.tipo() == 'o'):
    #         print('o')
    #     elif(nodo.tipo() == '-'):
    #         print('-')
    #     else:
    #         for row in range(0,3):
    #             for col in range(0,3):
    #                 if griglia[row][col] == '':
    #                     new_griglia = copy.deepcopy(griglia)
    #                     nodo = NodoTris(new_griglia)
    #                     print("--",nodo.nome, "**", nodo.lista_figli)
    #                     new_griglia[row][col] = turno
    #                     nodo.lista_figli.append(new_griglia)
    #                     print(nodo.lista_figli)
    #                     self.check_esiti_ricorsivo(new_griglia,nodo,tupla)

    
    def vittorie_livello(self, giocatore, h):
        listasoluzioni = []
        return self.vittorie_ricorsivo(self.lista_figli,giocatore,h)
        
    def vittorie_ricorsivo(self,lista,giocatore,h,altezza = 1):            
        vittorie = 0
        for x in lista:
            if(x.tipo() == giocatore and h == altezza):
                vittorie = vittorie + 1
            vittorie += self.vittorie_ricorsivo(x.lista_figli,giocatore,h,altezza+1)
        return vittorie
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''




def gen_tree(griglia):
    radice = NodoTris(griglia)
    return gen_tree2(griglia,radice)


   
def gen_tree2(griglia,radice):

    turno = radice.check_turno()

    for row in range(0,3):
        for col in range(0,3):

            if griglia[row][col] == '':

                new_griglia = copy.deepcopy(griglia)

                new_griglia[row][col] = turno
                new_nodo = NodoTris(new_griglia)

                radice.lista_figli.append(new_nodo)
                new_nodo = gen_tree2(new_griglia,new_nodo)

    return radice


# g1=[['x', 'o', 'o'], 
#     ['x', 'x', 'o'], 
#     ['', '', '']]


# x = gen_tree(g1)


# # k = j = l = 0
# # y = (k,j+1,l)

# # print(y)


# print("esito = ", x.esiti())
# # print("esito finale",x.vittorie_livello('o',3))
# # print("ricorsione = ", nodo.ricorsione(g1,'x',nodo))


