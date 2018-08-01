class NodoTris:
    def creategrid(self, griglia):
        l = []
        for a in griglia:
            l.append(a[:])
        return l

    def __init__(self, griglia):
        self.nome = self.creategrid(griglia)
        self.lista_figli = [] 
        
    def check1(self, cc, n):
        if cc >= n:
            a = 'o'
        elif n > cc:
            a = 'x'
        return cc, n

    def findc1(self):
        cc = n = 0
        for el in self.nome:
            for b in el:
                if b == 'o':
                    n += 1
                elif b == 'x':
                    cc += 1
        return self.check1(cc, n)
         
    def tipocheck1(self):
            if self.nome[0][0] == self.nome[2][2] and self.nome[0][0] == self.nome[1][1]:
                self.ok = self.nome[1][1]
                return self.ok
            elif self.nome[0][2] == self.nome[2][0] and self.nome[0][2] == self.nome[1][1]:
                self.ok = self.nome[1][1]
                return self.ok

    def tipocheck2_1(self, x):
        if self.nome[1][x] == self.nome[0][x]:
            if self.nome[2][x] == self.nome[0][x]:
                self.ok = self.nome[0][x]
                return self.ok

    def tipocheck2_2(self, x):
        if self.nome[x][0] == self.nome[x][1]: 
                if self.nome[x][0]==self.nome[x][2]:  
                    self.ok = self.nome[x][0]
                    return self.ok

    def tipocheck2(self):
        x = 0
        while x < len(self.nome):
            if self.nome[0][x] != '':
                 if self.tipocheck2_1(x) != None:
                    return self.tipocheck2_1(x)
            if self.nome[x][0] != '':
                if self.tipocheck2_2(x) != None:
                    return self.tipocheck2_2(x)
            x += 1

    def tipocheck3(self):
        x, o = self.findc1()
        if o != 5:
            self.ok = "?"
        else:
            self.ok = "-"

    def tipo(self):
        if self.nome[1][1] != '':
            if self.tipocheck1() != None:
                return self.tipocheck1()
        if self.tipocheck2() != None:
            return self.tipocheck2()
        self.tipocheck3()
        return self.ok 
       
    def check2(self):
        if self.ok == 'x':
            NodoTris.y += 1
        elif self.ok == '-':
            NodoTris.nn += 1
        elif self.ok == 'o':
            NodoTris.o += 1
        for x in self.lista_figli:
            x.check2()

    def esiti(self):
        NodoTris.y = NodoTris.nn = NodoTris.o = 0
        self.check2()
        return NodoTris.nn, NodoTris.o, NodoTris.y
    
    def vittorie_livello(self, giocatore, h):
        NodoTris.c = 0
        self.livello(giocatore, h)
        return NodoTris.c

    def checklvl1(self, bb, aa):
        if bb == aa:
            NodoTris.c += 1

    def livello(self, giocatore, h, aa=0):
        for n in self.lista_figli:
            aa += 1
            if n.ok == giocatore:
                self.checklvl1(h, aa)
            ac = aa
            aa = 0
            n.livello(giocatore, h, ac)

    def strategia_vincente(self, giocatore):
        victory = False
        for node in self.lista_figli:
            victory = node.strategia_vincente(giocatore)
        if self.tipo() == giocatore:
            victory = True
        return victory

    nn = y = o = c = 0

def grl(x, y, el1, griglia, a):
    while len(griglia) > x:      
        y = 0
        while len(griglia) > y:
            if griglia[x][y] != '': 
                pass
            else:
                griglia[x][y] = a          
                el1.lista_figli.append(gen_tree(griglia))
                griglia[x][y] = ''
            y += 1
        x += 1

def gencheck1(cc, n):
    if  n > cc:
        a = 'x'
    else:
        a = 'o'
    return a

def gencheck2(el1, x, y, griglia, a):
    if el1.ok == '?':
        grl(x, y, el1, griglia, a)
    elif el1.ok == '-':
        grl(x, y, el1, griglia, a)

def gen_tree(griglia):
    x = y = 0
    el1 = NodoTris(griglia)
    el1.tipo()
    cc = n = 0
    for v in griglia:
        for b in v:
            if b == 'x':
                cc += 1
            elif b == 'o':
                n += 1
    a = gencheck1(cc, n)
    gencheck2(el1, x, y, griglia, a)
    return el1







    
    
