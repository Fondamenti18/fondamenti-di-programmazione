from copy import deepcopy

memo = {}
v_memo = {}
s_memo = {}

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []
        self.result = 'lorem ipsum'
        
    def tipo(self):
        return self.result
                
    def esiti(self):
        tn=tuple(self.nome[0]+self.nome[1]+self.nome[2])
        if tn not in memo:
            cp=0
            co=0
            cx=0
            if self.result=='?':
                for el in self.lista_figli:
                    k=el.esiti()
                    cp+=k[0]
                    co+=k[1]
                    cx+=k[2]
            else:
                if self.result=='-':
                    cp+=1
                elif self.result=='o':
                    co+=1
                else:
                    cx+=1
            memo[tn]=(cp,co,cx)
        else:
            val=memo[tn]
            cp=val[0]
            co=val[1]
            cx=val[2]
        return (cp,co,cx)
                
        
    
    def vittorie_livello(self, giocatore, h):
        b=self.nome
        m=b[0]+b[1]+b[2]
        if 9-m.count('')+h<5:
            return 0
        if giocatore=='x' and 9-m.count('')+h==5:
            return 0
        if m.count('o')>m.count('x'):
            turno='x'
        else:
            turno='o'
        if turno==giocatore and h%2==0:
            return 0
        elif turno!=giocatore and h%2==1:
            return 0
        th=[h]
        tnh=tuple(m+th+list(giocatore))
        if tnh not in v_memo:
            numvittorie=0
            if h>0:
                for el in self.lista_figli:
                    numvittorie+=el.vittorie_livello(giocatore,h-1)
            else:
                if self.result==giocatore:
                    numvittorie=1
                else:
                    numvittorie=0
            v_memo[tnh]=numvittorie
        else:
            numvittorie=v_memo[tnh]
        return numvittorie
        
    
    def strategia_vincente(self,giocatore):
        b=self.nome
        m=b[0]+b[1]+b[2]
        tng=tuple(m+list(giocatore))
        if tng not in s_memo:
            if len(self.lista_figli)==0:
                if self.result==giocatore:
                    s_memo[tng]=True
                else:
                    s_memo[tng]=False
            else:
                if m.count('o')>m.count('x'):
                    turno='x'
                else:
                    turno='o'
                numvincenti=0
                for figlio in self.lista_figli:
                    q=figlio.strategia_vincente(giocatore)
                    if q==True:
                        numvincenti+=1
                if turno!=giocatore and numvincenti==len(self.lista_figli):
                    s_memo[tng]=True
                elif turno==giocatore and numvincenti>0:
                    s_memo[tng]=True
                else:
                    s_memo[tng]=False
        return s_memo[tng]
        
def gen_tree(griglia):
    radice=NodoTris(griglia)
    k=findtipo(griglia)
    radice.result=k
    if k=='?':
        m=griglia[0]+griglia[1]+griglia[2]
        listavuoti=[]
        oc=0
        xc=0
        n=-1
        for el in m:
            n+=1
            if el=='':
                listavuoti.append((n//3,n%3))
            elif el=='o':
                oc+=1
            else:
                xc+=1
        if oc>xc:
            for el in listavuoti:
                newgriglia=deepcopy(griglia)
                newgriglia[el[0]][el[1]]='x'
                radice.lista_figli.append(gen_tree(newgriglia))
        else:
            for el in listavuoti:
                newgriglia=deepcopy(griglia)
                newgriglia[el[0]][el[1]]='o'
                radice.lista_figli.append(gen_tree(newgriglia))
    return radice

def findtipo(griglia):
        a=griglia
        m=a[0]+a[1]+a[2]
        if m.count('')>4:
            return '?'
        s4=m[4]
        s0=m[0]
        s8=m[8]
        if s4!='':
            if m[1]==s4 and m[7]==s4:
                return m[4]
            if m[3]==s4 and m[5]==s4:
                return m[4]
            if s0==s4 and s8==s4:
                return m[4]
            if m[2]==s4 and m[6]==s4:
                return s4
        if s0!='':
            if m[1]==s0 and m[2]==s0:
                return s0
            if m[3]==s0 and m[6]==s0:
                return s0
        if s8!='':
            if m[6]==s8 and m[7]==s8:
                return m[8]
            if m[2]==s8 and m[5]==s8:
                return s8
        if m.count('')==0:
            return '-'
        return '?'