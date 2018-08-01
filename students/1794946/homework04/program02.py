import copy
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    def __iter__(self):
         for i in self.nome:
             yield i
    
    def tipo(self):
        lista=['o','x']
        line1=self.nome[0]
        line2=self.nome[1]
        line3=self.nome[2]
        for el in lista:
            cont=0
            if all(u==el for u in line1) or all(u==el for u in line2) or all(u==el for u in line3):
                return el
            elif line1[0]==line2[1]==line3[2]==el:
                return el
            elif line1[2]==line2[1]==line3[1]==el:
                return el
            for i in line1:
                if i==el==line2[cont]==line3[cont]:
                    return el
                cont+=1
        if any('' in u for u in self.nome):
            return'?'
        return '-'

    def esiti(self):
        patte=0
        o=0
        x=0
        c=player(self.nome)
        if c%2!=0:
            turn='o'
        else:
            turn='x'
        lista_esiti=crea_esiti(self.nome, [],turn)
        for el in lista_esiti:
            if tipo(el)=='-':
                patte+=1
            elif tipo(el)=='o':
                o+=1
            elif tipo(el)=='x':
                x+=1
        return (patte,o,x)
    

    def vittorie_livello(self, giocatore, h):
        c=player(self.nome)
        if c%2!=0:
            turn='o'
        else:
            turn='x'
        lista=gen_listafigli(self.nome,turn)
        if h==0:
            if tipo(self.nome)==giocatore:
                return 1
            return 0
        lista_figli=conteggio(h,turn,1,lista)
        cont=0
        for el in lista_figli:
            if tipo(el)==giocatore:
                cont+=1
        return cont
            
    
    def strategia_vincente(self,giocatore):
        esiti=self.esiti()
        o=esiti[1]
        x=esiti[2]
        c=player(self.nome)
        if c%2!=0:
            turn='o'
        else:
            turn='x'
        figli=gen_listafigli(self.nome,turn)
        if giocatore==turn:
            for el in figli:
                if tipo(el)==giocatore:
                    return True
        else:
            for el in figli:
                if tipo(el)==turn:
                    return False
        if giocatore=='o':
            if o > x :
                return True
        else:
            if x > o:
                return True
        return False

def player(griglia):
    c=0
    for u in griglia:
        f=u.count('')
        c+=f
    return c

        
def gen_tree(griglia):
    c=player(griglia)
    if c%2!=0:
        turn='o'
    else:
        turn='x'
    figli=gen_listafigli(griglia,turn)
    griglia=NodoTris(griglia)
    griglia.lista_figli=[figli]
    for el in figli:
        if tipo(el)=='?':
            griglia.lista_figli+=gen_tree(el)
    return griglia

def crea_esiti(nodo, lista,turn):
    lista_figli=gen_listafigli(nodo,turn)
    if tipo(nodo)!='?':
        lista=[nodo]
        return lista
    else:
        lista=[]
    for el in lista_figli:
        if turn=='x':
            g='o'
        else:
            g='x'
        lista+=crea_esiti(el,lista,g)
    return lista

def gen_listafigli(griglia,turn):
    lista=[]
    for x in range(0,3):
        for y in range(0,3):
            if griglia[y][x]=='':
                griglia[y][x]=turn
                lista.append(copy.deepcopy(griglia))
                griglia[y][x]=''
    return lista

def tipo(self):
        lista=['x','o']
        line1=self[0]
        line2=self[1]
        line3=self[2]
        for el in lista:
            cont=0
            if all(u==el for u in line1) or all(u==el for u in line2) or all(u==el for u in line3):
                return el
            elif line1[0]==line2[1]==line3[2]==el:
                return el
            elif line1[2]==line2[1]==line3[1]==el:
                return el
            for i in line1:
                if i==el==line2[cont]==line3[cont]:
                    return el
                cont+=1
        if any('' in u for u in self):
            return'?'
        return '-'


def conteggio(h,turn,cont,lista):
    lista_figli=[]
    if cont==h:
        return lista
    for el in lista:
        lista_figli+=gen_listafigli(el,turn)
    if turn=='x':
        g='o'
    else:
        g='x'
    return conteggio(h,g,cont+1,lista_figli)

