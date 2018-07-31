
from copy import *
import json
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
    
    def tipo(self):
        d1 = [self.nome[0][0],self.nome[1][1],self.nome[2][2]]
        d2 = [self.nome[0][2],self.nome[1][1],self.nome[2][0]]
        r1 = [self.nome[0][0],self.nome[0][1],self.nome[0][2]]
        r2 = [self.nome[1][0],self.nome[1][1],self.nome[1][2]]
        r3 = [self.nome[2][0],self.nome[2][1],self.nome[2][2]]
        v1 = [self.nome[0][0],self.nome[1][0],self.nome[2][0]]
        v2 = [self.nome[0][1],self.nome[1][1],self.nome[2][1]]
        v3 = [self.nome[0][2],self.nome[1][2],self.nome[2][2]]

        lista_vittorie = [d1,d2,r1,r2,r3,v1,v2,v3]
        t = 0
        for x in lista_vittorie :
            if x.count("x") == 3 :
                return "x"
            if x.count("o") == 3 :
                return "o"
            if "" in x :
                t = 1
        if t == 1:
            return "?"
        else :
            return "-"
    def esiti(self):
        return (self.inizio())[0]
    def inizio(self):
        m = self.nome
        vlx = 0
        vlo = 0
        d = {}
        vo = []
        vx = []
        pt = []
        l = []
        c = 0
        a = NodoTris(m)
        if a.tipo() == "x" :
            d = {0:[0,1]}
            return (0,0,1),d
        elif a.tipo() == "o" :
            d = {0:[1,0]}
            return (0,1,0),d
        elif a.tipo() == "-" :
            return (1,0,0),d
        else :
            d[0] = [0,0]
            return figli(m,vo,vx,pt,l,c,vlx,vlo,d)
    def vittorie_livello(self, giocatore, h):

        """ """
                
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''      
def gen_tree(griglia):
    griglia = NodoTris(griglia)
    return griglia
def figli(m,vo,vx,pt,l,c,vlx,vlo,d):
    l = []
    c = c + 1
    vlx = 0
    vlo = 0
    for i in range (len(m)):
        for j in range(len(m[0])):
            if m[i][j] == "":
                m[i][j] = controllo(m)
                r = deepcopy(m)
                r = NodoTris(r)
                if r.tipo() == "x":
                    vx.append(1)
                    vlx = len(vx)
                elif r.tipo() == "o":
                    vo.append(1)
                    vlo = len(vo)
                elif r.tipo() == "-":
                    pt.append(1)
                elif r.tipo() == "?" :
                    a = deepcopy(m)
                    l.append(a)
                m[i][j] = ""
    d[c] = [vlo,vlx]
    for x in l :
        figli(x,vo,vx,pt,l,c,vlx,vlo,d)
    return (len(pt),len(vo),len(vx)),d

def controllo(m):
    co=0
    cx=0
    for i in range(len(m)):
            for j in range(len(m[0])):
                    if m[i][j]=="x":
                            co+=1
                    if m[i][j]=="o":
                            cx+=1
    if (co==0 and cx==0) or co<cx:
            return "x"
    else:
            return "o"
