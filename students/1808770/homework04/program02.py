import copy

class NodoTris:

    def __init__(self,griglia):
        self.griglia=griglia
        self.lista_figli=[]

    def tipo(self):
        c=parser(self.griglia)
        if c[0]==c[1]==c[2]!="" or c[0]==c[4]==c[8]!="" or c[0]==c[3]==c[6]!="":
            return trythat(c[0])
        elif c[6]==c[7]==c[8]!="" or c[2]==c[5]==c[8]!="":
            return trythat(c[8])
        elif c[3]==c[4]==c[5]!="" or c[2]==c[4]==c[6]!="":
            return trythat(c[4])
        else:
            if counter("",self.griglia)>0:
                return "?"
            else:
                return "-"

    def esiti(self):
        cp,co,cx=0,0,0
        if NodoTris.tipo(self)!="?":
            self.lista_figli=[self.griglia]
        for y in self.lista_figli:
            c=parser(y)
            if c[0]==c[1]==c[2]!="" or c[3]==c[4]==c[5]!="" or c[6]==c[7]==c[8]!="":
                co,cx=trythat2(y,co,cx)
            elif c[2]==c[5]==c[8]!="" or c[0]==c[4]==c[8]!="":
                co,cx=trythat2(y,co,cx)
                for x in self.lista_figli:
                    if x[2][2]==c[8] and x[2][1]=="" and x!=y:
                        del self.lista_figli[self.lista_figli.index(x)]
            elif c[0]==c[3]==c[6]!="" or c[2]==c[4]==c[6]!="":
                co,cx=trythat2(y,co,cx)
                for x in self.lista_figli:
                    if x[2][0]==c[6] and x!=y:
                        del self.lista_figli[self.lista_figli.index(x)]
            else:
                if counter("",self.griglia)==0:
                    cp+=1
        return cp,co,cx

    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''

    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''

def gen_tree(griglia):
    if istipo(griglia)!="?":
        return NodoTris(griglia)
    else:
        g=NodoTris(griglia)
        copia1,copia2=copy.deepcopy(griglia),copy.deepcopy(griglia)
        g.lista_figli=rec(copia1,copia2,0,[])
        return g

def rec(griglia,dpcp,count,lista):
    if count==0:
        count=counter("",griglia)
    if count==3:
        lista.append(putting(0,1,"o",griglia))
        lista.append(putting(1,2,"o",copy.deepcopy(dpcp)))
        lista.append(putting(2,3,"o",copy.deepcopy(dpcp)))
    elif count==2:
        griglia=putting(0,1,"o",griglia)
        lista.append(putting(1,2,"x",griglia))
        griglia=putting(0,1,"o",copy.deepcopy(dpcp))
        lista.append(putting(2,3,"x",griglia))
        griglia=putting(1,2,"o",copy.deepcopy(dpcp))
        lista.append(putting(0,1,"x",griglia))
        griglia=putting(1,2,"o",copy.deepcopy(dpcp))
        lista.append(putting(2,3,"x",griglia))
        griglia=putting(2,3,"o",copy.deepcopy(dpcp))
        lista.append(putting(0,1,"x",griglia))
        griglia=putting(2,3,"o",copy.deepcopy(dpcp))
        lista.append(putting(1,2,"x",griglia))
    elif count==1:
        griglia=putting(0,1,"o",griglia)
        griglia=putting(2,3,"o",griglia)
        lista.append(putting(1,2,"x",griglia))
        griglia=putting(0,1,"o",copy.deepcopy(dpcp))
        griglia=putting(1,2,"o",griglia)
        lista.append(putting(2,3,"x",griglia))
        griglia=putting(1,2,"o",copy.deepcopy(dpcp))
        griglia=putting(2,3,"o",griglia)
        lista.append(putting(0,1,"x",griglia))
    if count-1==0:
        return lista
    else:
        return rec(copy.deepcopy(dpcp),dpcp,count-1,lista)


def counter(char,griglia):
    return [x for y in griglia for x in y].count(char)
def parser(griglia):
    return [x for y in griglia for x in y]
def trythat(xxx):
    if xxx=="x":
        return "x"
    else:
        return "o"
def trythat2(y,co,cx):
    if counter("",y)%2==0!=1:
        co+=1
    else:
        cx+=1
    return co,cx
def putting(a,b,char,griglia):
    for y in range(0,3):
        for x in range(a,b):
            if griglia[y][x]=="":
                griglia[y][x]=char
                break
    return griglia
def istipo(griglia):
    return NodoTris.tipo(NodoTris(griglia))