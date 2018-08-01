import ast
#g1=[['', '', ''], ['', '', ''], ['', '', '']]
#g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
#g1=[['', 'x', 'o'], ['', '', ''], ['', '', '']]


class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli

    def add_nodo(self,new):
        self.lista_figli.append(new)
        
    def __str__(self):
        return str(self.nome)
    
    def __repr__(self):
        return self.__str__()

    def tipo(self):
        es=centro(self)
        if es=='o':
            return 'o'
        elif es=='x':
            return 'x'
        elif es=='-':
            return '-'
        else:
            return '?'
        
    def esiti(self):
        lista_nuova=[]
        griglia=self.nome
        h=NodoTris(griglia)
        l=possibil(griglia,h,lista_nuova)
        if l==None:
            tripla=vincente2(griglia)
        else:
            tripla=vincente(l)
        return tripla
    
    
    def strategia_vincente(self,giocatore):
        griglia=self.nome
        n1=NodoTris(griglia)
        lista=[]
        lista=possibil(griglia,n1,lista)
        
        
def vittorie_livello(self, giocatore, h):
        '''griglia=self.nome
        n1=NodoTris(griglia)
        albero(griglia,n1)
        g1=ast.literal_eval(str(n1.nome))
        c=0
        if vincente4(g1,giocatore)==True:
            return 1
        for x in g1:
            num=n1.lista_figli[c]
            c+=1
            if vincente4(num,giocatore)==True:
                k+=1
            h=0
            for y in num.lista_figli:
                al=num.lista_figli[h]
                h+=1
                if vincente4(num,giocatore)==True:
                    ka+=1
        print(k,ka)


def vincente4(a,giocatore):
    cc=centro2(a)
    if cc==giocatore:
        return True
    return False'''
    
'''def possibil(griglia,n1,lista,lista_nuova):
    g1=ast.literal_eval(str(n1.nome))
    check=vi(g1)
    check2=n_space(g1)
    if check==True or check2==False:
        return lista_nuova.append(g1)
    val = mossa(g1)
    for x in range(0,3):
        for y in range(0,3):
            if n1.nome[x][y]=='':
                g1=ast.literal_eval(str(n1.nome))
                new_nodo=NodoTris(g1)
                n1.add_nodo(new_nodo)
                g1=aggiungi(g1,x,y,val)
                lista.append(g1)
                b=n1.lista_figli[-1]
                possibil(griglia,b,lista,lista_nuova)
    return lista_nuova'''


def gen_tree(griglia):
    h=NodoTris(griglia)
    albero(griglia,h)
    return h
 
def possibil(griglia,h,lista_nuova):
    gri=ast.literal_eval(str(h.nome))
    contr=vi(gri)
    control=n_space(gri)
    if contr==True or control==False:
        #lista_nuova.append(g1)
        return lista_nuova.append(gri)
    valore = mossa(gri)
    for x in range(0,3):
        for y in range(0,3):
            if h.nome[x][y]=='':
                new=NodoTris(gri)
                h.add_nodo(new)
                gri=aggiungi(gri,x,y,valore)
                elemento=h.lista_figli[-1]
                possibil(griglia,elemento,lista_nuova)
    return lista_nuova
 
    


def vincente(lista):
    vince_o=0
    vince_x=0
    pari=0
    for a in lista:
        cc=centro2(a)
        if cc=='o':
            vince_o+=1
        elif cc=='x':
            vince_x+=1
        elif cc=='-':
            pari+=1
        else:
            continue
    tripla=(pari,vince_o,vince_x)
    return tripla

def vincente2(a):
    vince_o=0
    vince_x=0
    pari=0
    cc=centro2(a)
    if cc=='o':
        vince_o+=1
    elif cc=='x':
        vince_x+=1
    elif cc=='-':
        pari+=1
    tripla=(pari,vince_o,vince_x)
    return tripla
    
    
    
    
def centro2(st):
    if st==0:
        return None
    if st[1][1]==st[0][0]==st[2][2]:
        return st[1][1]
    if st[1][1]==st[0][1]==st[2][1]:
        return st[1][1]
    if st[1][1]==st[1][0]==st[1][2]:
        return st[1][1]
    if st[1][1]==st[2][0]==st[0][2]:
        return st[1][1]
    if st[0][0]==st[1][0]==st[2][0]:
        return st[0][0]
    if st[0][0]==st[0][1]==st[0][2]:
        return st[0][0]
    if st[2][0]==st[2][1]==st[2][2]:
        return st[2][0]
    if st[0][2]==st[1][2]==st[2][2]:
        return st[0][2]
    if n_space(st)==False:
        return '-'
    else:
        return '?'     
        
def centro(self):
    st=self.nome
    if st[1][1]==st[0][0]==st[2][2]:
        return st[1][1]
    if st[1][1]==st[0][1]==st[2][1]:
        return st[1][1]
    if st[1][1]==st[1][0]==st[1][2]:
        return st[1][1]
    if st[1][1]==st[2][0]==st[0][2]:
        return st[1][1]
    if st[0][0]==st[1][0]==st[2][0]:
        return st[0][0]
    if st[0][0]==st[0][1]==st[0][2]:
        return st[0][0]
    if st[2][0]==st[2][1]==st[2][2]:
        return st[2][0]
    if st[0][2]==st[1][2]==st[2][2]:
        return st[0][2]
    if n_space(st)==False:
        return '-'
    else:
        return '?'
    
                            
def mossa(stato):
    c=0
    for x in range(0,3):
        for y in range(0,3):
            if stato[x][y]=='x':
                c+=1
            if stato[x][y]=='o':
                c+=1
    if c%2==0:
        return 'o'
    elif c%2!=0:
        return 'x'
    elif c==0:
        return 'o'

       
def n_space(griglia):
    for x in range(len(griglia)):
        for y in range(len(griglia[0])):
            if griglia[x][y] == '':
                return True
            else:
                continue
    return False
            

def aggiungi(griglia,x,y,valore):
    griglia[x][y]=valore
    return griglia

def vi(st):
    if st[1][1]==st[0][0]==st[2][2]:
        if st[1][1]=='':
            return False
        else:
            return True
    if st[1][1]==st[0][1]==st[2][1]:
        if st[1][1]=='':
            return False
        else:
            return True
    if st[1][1]==st[1][0]==st[1][2]:
        if st[1][1]=='':
            return False
        else:
            return True
    if st[1][1]==st[2][0]==st[0][2]:
        if st[1][1]=='':
            return False
        else:
            return True
    if st[0][0]==st[1][0]==st[2][0]:
        if st[0][0]=='':
            return False
        else:
            return True
    if st[0][0]==st[0][1]==st[0][2]:
        if st[0][0]=='':
            return False
        else:
            return True
    if st[2][0]==st[2][1]==st[2][2]:
        if st[2][0]=='':
            return False
        else:
            return True
    if st[0][2]==st[1][2]==st[2][2]:
        if st[0][2]=='':
            return False
        else:
            return True
    else:
        return False
    
def albero(griglia,h):
    gri=ast.literal_eval(str(h.nome))
    contr=vi(gri)
    control=n_space(gri)
    if contr==True:
        return None
    if control==False:
        return None
    valore = mossa(gri)
    for x in range(0,3):
        for y in range(0,3):
            if h.nome[x][y]=='':
                new=NodoTris(gri)
                h.add_nodo(new)
                gri=aggiungi(gri,x,y,valore)
                elemento=h.lista_figli[-1]
                albero(griglia,elemento)    



  