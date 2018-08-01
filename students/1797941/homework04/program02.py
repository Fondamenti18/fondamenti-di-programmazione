
diz_strategie = {}

class NodoTris:
    def __init__(self, griglia,simbolo):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.simbolo = simbolo
        self.var_tipo = None
        
    def print_tree(self,livello=0):
        print('-'*livello,self)
        for figlio in self.lista_figli:
            figlio.print_tree(livello+1)
        
    def tipo(self):
        ''''''
        if self.var_tipo != None: return self.var_tipo
        for i in range(3):
            if self.nome[i][0] == self.nome[i][1] == self.nome[i][2] != '':
                self.var_tipo = self.nome[i][0]
                return self.nome[i][0]
            if self.nome[0][i] == self.nome[1][i] == self.nome[2][i] != '':
                self.var_tipo = self.nome[0][i]
                return self.nome[0][i]
        if self.nome[0][0] == self.nome[1][1] == self.nome[2][2] != '':
            self.var_tipo = self.nome[0][0]
            return self.nome[0][0]
        if self.nome[2][0] == self.nome[1][1] == self.nome[0][2] != '':
            self.var_tipo = self.nome[2][0]
            return self.nome[2][0]
        if '' not in self.nome[0]+self.nome[1]+self.nome[2]:
            self.var_tipo = '-'
            return '-'
        self.var_tipo = '?'
        return self.var_tipo

    
    def add_figlio(self,nodo):
        self.lista_figli.append(nodo)
        
    def __str__(self):
        #return str(self.nome[0])+"\n"+str(self.nome[1])+"\n"+str(self.nome[2])
        return str(self.nome[0])+str(self.nome[1])+str(self.nome[2])
    
    def esiti(self):
        '''inserire qui il vostro codice'''
        arr = self.crea_arr_totale([])
#        print(len(arr),"count ?: ",arr.count('?'))
        return(arr.count('-'),arr.count('o'),arr.count('x'))
     
    def crea_arr_totale(self,arr,livello=0):
        '''inserire qui il vostro codice'''
        arr+=[self.tipo()]
#        print("-"*livello,self,",",arr)
        for figlio in self.lista_figli:
            arr = figlio.crea_arr_totale(arr,livello+1) 
        return arr

    def crea_arr_livello(self,arr,giocatore,h,livello=0):
        '''inserire qui il vostro codice'''
        if livello==h:
            if self.tipo()==giocatore:
                arr+=[self.tipo()]
                return arr
            else: return arr
#        print("-"*livello,self,",",arr)
        for figlio in self.lista_figli:
            arr = figlio.crea_arr_livello(arr,giocatore,h,livello+1) 
        return arr
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        return self.crea_arr_livello([],giocatore,h).count(giocatore)


    def crea_arr_livello_n(self,arr,giocatore,h,livello=0):
        '''inserire qui il vostro codice'''
        if livello==h:
            arr+=[self.tipo()]
        for figlio in self.lista_figli:
            arr = figlio.crea_arr_livello_n(arr,giocatore,h,livello+1) 
        
    #        print("-"*livello,self,",",arr)
        return arr
    
    def strategia_vincente(self,giocatore,livello=0,griglia_padre=[]):
        '''inserire qui il vostro codice'''
        global diz_strategie
        if livello==0: 
            griglia_padre = copia_lista(self.nome)
            if self.calcola_inversa() in diz_strategie.keys():
                return not(diz_strategie[self.calcola_inversa()]) 

        arr=[]
        for figlio in self.lista_figli:
            arr=figlio.crea_arr_livello_n(arr,giocatore,livello+1,livello+1)   
#        print("-"*livello,arr,"p: ",self.simbolo,"       f: ",figlio.simbolo)
        if giocatore != self.simbolo in arr:
#            print("Sconfitta",giocatore)
            diz_strategie[str(griglia_padre)]=False
            return False
        elif giocatore == self.simbolo in arr:
#            print("Vittoria",giocatore)
            diz_strategie[str(griglia_padre)]=True
            return True
        else:
            for figlio in self.lista_figli:
                return figlio.strategia_vincente(giocatore,livello+1,griglia_padre)

    def calcola_inversa(self):
        gr = copia_lista(self.nome)
        for y in range(3):
            for x in range(3):
                if gr[y][x]=='x': gr[y][x]='o'
                elif gr[y][x]=='o': gr[y][x]='x'
        return str(gr)
        
                

    def crea_diz_all(self,diz_all={},livello=0):
        if livello not in diz_all.keys(): diz_all[livello]=[]
        diz_all[livello]+=[self.tipo()]
        for figlio in self.lista_figli:
            diz_all = figlio.crea_diz_all(diz_all,livello+1)
        return diz_all


        
def gen_tree(griglia,livello=0):
    '''inserire qui il vostro codice'''
#    if livello == 0: print(griglia)
    arr_griglia = griglia[0]+griglia[1]+griglia[2]
    simbolo = trova_simbolo(arr_griglia)
    nodo = NodoTris(griglia,simbolo)
    if nodo.tipo() in "xo-": return nodo    
#    print("+"*livello,"nodo: \n",nodo)
    if '' not in arr_griglia: return nodo
    for y in range(3):
        for x in range(3): 
            if griglia[y][x] == '':
                new = copia_lista(griglia)
                new[y][x] = simbolo
#                print("-"*livello,new)
                nodo.add_figlio(gen_tree(new,livello+1))
#                if livello == 0: print("-"*70+"\n")
    
    return nodo    

def copia_lista(lista):
    return [l[:] for l in lista]

def trova_simbolo(arr_griglia):
    if arr_griglia.count('') == 0: return 'o'
    if arr_griglia.count('o') == arr_griglia.count('x'): return 'o'
    return 'x'
