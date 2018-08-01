import copy
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []
        self.turno=''
        self.type=''
    def tipo(self):
        for y in self.nome:
            if y[0]=='o' or y[0]=='x':
                if y[0]==y[1] and y[1]==y[2]:
                    self.type=y[0]
                    return y[0]
        for x in range(0,3):
            if self.nome[0][x]=='o' or self.nome[0][x]=='x':
                if self.nome[0][x]==self.nome[1][x] and self.nome[1][x]==self.nome[2][x]:
                    self.type=self.nome[0][x]
                    return self.nome[0][x]
        f=0
        f1=0
        for n in range(1,3):
            if self.nome[0][0]=='x' or self.nome[0][0]=='o':
                if self.nome[0+n][0+n]==self.nome[0][0]:
                    f+=1
            if self.nome[2][0]=='x' or self.nome[2][0]=='o':
                if self.nome[2-n][0+n]==self.nome[2][0]:
                    f1+=1
        if f==2:
            self.type=self.nome[0][0]
            return(self.nome[0][0])
        if f1==2:
            self.type=self.nome[2][0]
            return(self.nome[2][0])
        f=0
        for y in self.nome:
            for x in y:
                if x=='':
                    f=1
        if f==1:
            self.type='?'
            return '?'
        else:
            self.type='-'
            return'-'
    def trovaturno(self):
        cx=0
        co=0
        for y in self.nome:
            for x in y:
                if x=='o':
                    co+=1
                elif x=='x':
                    cx+=1
        if cx>co:
            self.turno='x'
        else:
            self.turno='o'
        return self.turno
    def figli(self, t):
        if not self.lista_figli:
            self.tipo()
            c=0
            for y in range(0,3):
                for x in range(0,3):
                    if self.nome[y][x]=='':
                        self.lista_figli.append(copy.deepcopy(self.nome))
                        self.lista_figli[c][y][x]=self.turno
                        self.lista_figli[c]=NodoTris(self.lista_figli[c])
                        c+=1
        if t=='o':
            t='x'
        else:
            t='o'
        return t                
    def esiti(self):
        risp=[0,0,0]
        t= self.trovaturno()
        risp=self.esiti2(risp, t)
        risp=tuple(risp)
        return risp
    
    def esiti2(self, risp, t):
        tipo=self.type
        '''()'''
        if tipo=='x':
            risp[2]=risp[2]+1
            return risp
        elif tipo=='o':
            risp[1]=risp[1]+1
            return risp
        elif tipo=='-':
            risp[0]=risp[0]+1
            return risp
        elif tipo=='?':
            '''turno=self.figli(t)'''
            for e in self.lista_figli:
                '''e=NodoTris(e)'''
                risp=e.esiti2(risp, self.turno)
        return risp

    def vittorie_livello(self, giocatore, h):
        cont=0
        cont=self.winh(giocatore, self.trovaturno(), h, cont)
        return cont

    def winh(self, gioc, t, h, cont):
        tipo=self.type
        if h==0:
            if tipo==gioc:
                cont+=1
                return cont
            return cont
        else:
            if tipo=='?':
                h-=1
                for e in self.lista_figli:
                    cont= e.winh(gioc, self.turno, h, cont)
                return cont
        return cont
    def strategia_vincente(self,giocatore):
        risp=None
        risp, bo=self.vincente(giocatore, risp)
        return risp
    def vincente(self, gioc, flag):
        tipo=self.tipo()
        for e in self.lista_figli:
            flag, ris=e.vincente(gioc, flag)
            if self.turno==gioc:
                if ris==gioc:
                    flag=True
                    tipo='o'
                    break
                elif ris!=gioc and ris!='?':
                    flag=False
                    tipo='x'
            else:
                if ris==gioc:
                    flag=True
                    tipo='o'
                elif ris!=gioc and ris!='?':
                    flag=False
                    tipo='x'
                    break
        return flag, tipo

def gen_tree(griglia, t=''):
    if t=='':
        griglia=NodoTris(griglia)
        t=griglia.trovaturno()
    else:
        griglia.turno=t
    if griglia.tipo() =='?':
        t=griglia.figli(t)
        for e in griglia.lista_figli:
            gen_tree(e, t)
    return griglia
