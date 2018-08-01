import copy
def gen_tree(griglia):
    tb = NodoTris(griglia)
    lp = [griglia]
    d = {}
    m,i = move(griglia)
    newAl(tb, d, lp, i)
    return tb
def cV(tris):
    co = []
    for r in range(len(tris)):
        for c in range(len(tris[0])):
            if tris[r][c] == '':
                co.append((c,r))
    return co
def newAl(p, d, lm, tM):
    m = ['o','x']
    if p.tipo()== '?':
        co = cV(p.nome)
        for c in co:
            tP = copy.deepcopy(p.nome)
            tP[c[1]][c[0]] = m[tM]
            if tP not in lm:
                lm.append(tP)
                match = NodoTris(tP)
                d[str(tP)] = match
                p.lista_figli.append(match)
                if tM+1!=2:
                    newAl(match, d, lm, tM + 1)
                else:
                    newAl(match, d, lm, 0)
            else:
                p.lista_figli.append(d[str(tP)])
def move(tris):
    s = ''
    m = '-'
    iM = -1
    for r in tris:
        for e in r:
            s+=e
    nX = s.count('x')
    nO = s.count('o')
    if nX == nO:
        m = 'o'
        iM = 0
    elif nX != nO and nX+nO!=9:
        m = 'x'
        iM = 1
    return m, iM

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []
        self.al = {}
    def Vv(self, tb):
        t1 = self.Or(tb)
        t2 = self.Vr(tb)
        t3 = self.Vi(tb)
        t = [t1,t2,t3]
        w = '-'
        for e in t:
            if e != '-':
                w = e
        return w
    def tipo(self):
        t = ''
        gr = self.nome
        term = self.Vt(gr)
        ver = self.Vv(gr)
        if term == '?' and ver == '-':
            t = '?'
        else:
            t = ver
        return t
    def Vt(self, tb):
        m = '-'
        for e in tb:
            if '' in e:
                m = '?'
        return m
    def esiti(self):
        l = [0,0,0]
        t = self.tipo()
        if t != '?':
            if t == '-':
                l[0]+=1
            if t == 'o':
                l[1]+=1
            if t == 'x':
                l[2]+=1
        self.ris(l, self.lista_figli)
        ris = (l[0],l[1],l[2])
        return ris
    def Vi(self, tb):
        m = '-'
        if ((tb[0][0] == tb[1][1] and tb[1][1] == tb[2][2] and tb[0][0] != '') or
            (tb[0][2] == tb[1][1] and tb[1][1] == tb[2][0] and tb[0][2] != '')):
            m = tb[1][1]
        return m
    def vittorie_livello(self, giocatore, h):
        v = 0
        if self.tipo() == giocatore and h == 0:
            v = 1
        else:
            l = []
            self.nWin(l, self.lista_figli, giocatore, h, 1)
            v = len(l)
        return v
    def Vr(self, tb):
        m = '-'
        for c in range(3):
            if tb[0][c] == tb[1][c] and tb[1][c] == tb[2][c] and tb[0][c]!= '':
                m = tb[0][c]
        return m
    def strategia_vincente(self,giocatore):  
        v = [-1]
        if giocatore == 'o' and self.lv1(self.lista_figli):
            v.append(True)
        else:    
            d = {}
            self.levels(d, self.lista_figli, 1)
            v.append(self.win(d, giocatore))
        return v[1]
    def Or(self, tb):
        m = '-'
        for r in tb:
            if r[0]==r[1] and r[1]==r[2] and r[0]!='':
                m = r[0]
        return m
    def win(self, d, g):
        player = {'x':'o','o':'x'}
        keys = list(d.keys())[1:]
        m = None
        for k in keys:
            l = 0
            cV = 0
            for n in d[k]:
                if n.tipo() == player[g]:
                    m = False
                    break
                elif n.tipo() == g:
                    cV+=1
                l+=1
            if l != 0 and l == cV:
                m = True
                break
            elif m == False:
                break
        return m
    def ris(self, t, ns):
        if ns != []:
            for n in ns:
                ty = n.tipo()
                if ty != '?':
                    if ty == '-':
                        t[0]+=1
                    if ty == 'o':
                        t[1]+=1
                    if ty == 'x':
                        t[2]+=1
                self.ris(t, n.lista_figli)
    def levels(self, d, n, lv):
        if n != []:
            if lv not in d.keys():
                d[lv] = []
            for i in n:
                d[lv].append(i)
                self.levels(d, i.lista_figli, lv + 1)
    def nWin(self, v, ns, p, lv, tLv):
        if tLv == lv:
            for n in ns:
                if n.tipo() == p:
                    v.append('c')
        else:
            for n in ns:
                self.nWin(v, n.lista_figli, p, lv, tLv + 1)
    def lv1(self, ns):
        m = False
        for n in ns:
            if n.tipo() == 'o':
                m = True
        return m

        








