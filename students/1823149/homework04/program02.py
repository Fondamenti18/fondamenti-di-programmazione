

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.r0=(griglia[0].count('o'),griglia[0].count('x'),griglia[0].count(''))
        self.r1=(griglia[1].count('o'),griglia[1].count('x'),griglia[1].count(''))
        self.r2=(griglia[2].count('o'),griglia[2].count('x'),griglia[2].count(''))
        self.col0=[griglia[y][0] for y in range(0,3)]
        self.col1=[griglia[y][1] for y in range(0,3)]
        self.col2=[griglia[y][2] for y in range(0,3)]
        self.c0=(self.col0.count('o'),self.col0.count('x'),self.col0.count(' '))
        self.c1=(self.col1.count('o'),self.col1.count('x'),self.col1.count(' '))
        self.c2=(self.col2.count('o'),self.col2.count('x'),self.col2.count(' '))
        self.diag1=[griglia[0][0],griglia[1][1],griglia[2][2]]
        self.diag2=[griglia[0][2],griglia[1][1],griglia[2][0]]
        self.d1=(self.diag1.count('o'), self.diag1.count('x'))
        self.d2=(self.diag2.count('o'), self.diag2.count('x'))
        self.vuote=[(x,y) for x in range(0,3) for y in range(0,3) if griglia[y][x]=='']
        self.o=self.r0[0]+self.r1[0]+self.r2[0]
        self.x=self.r0[1]+self.r1[1]+self.r2[1]
        self.mossa_succ=self.prossima_mossa()
        self.vincente=self.tipo()
        self.livello=-1
        self.strategia=-10
    
    def prossima_mossa(self):
        if len(self.vuote)==0:  return "-"
        if self.o>self.x:
            return 'x'
        return 'o'
            
    def tipo(self):
        for d in [self.d1,self.d2]:
            if d[0]==3:    return 'o'
            if d[1]==3:    return 'x'
        for i in [self.r0,self.r1,self.r2]:
            if i[0]==3: return 'o'
            if i[1]==3: return 'x'
        for i in [self.c0, self.c1,self.c2]:
            if i[0]==3: return 'o'
            if i[1]==3: return 'x'
        if len(self.vuote)==0:  return "-"
        return "?"
    
    def esiti(self):
        ret=[0,0,0]
        if len(self.vuote)>0:
            for i in self.lista_figli:
                b=list(i.esiti())
                for j in range(0,3):
                    ret[j]+=b[j]
        if self.vincente=='-':  ret[0]+=1
        if self.vincente=='o':  ret[1]+=1
        if self.vincente=='x':   ret[2]+=1
        return tuple(ret)

    def vittorie_livello(self, giocatore, h):
        ret=0
        if h==0:
            if self.vincente==giocatore:
                ret+=1
        else:
            for i in self.lista_figli:
                ret+=i.vittorie_livello(giocatore,h-1)
        return ret
    
    def strategia_vincente(self,giocatore):
        self.valori_strategia(giocatore)
        if(self.strategia==1):
            return True
        else:
            return False
        
        
    def valori_strategia(self,giocatore):    
        if self.vincente==giocatore:
            self.strategia=1
        elif self.vincente=='-':
            self.strategia=0
        elif self.vincente in {'o','x'}:
            self.strategia=-1
        if self.vincente=='?':
            lista=set()
            for i in self.lista_figli:
                lista.add(i.valori_strategia(giocatore))
            if self.mossa_succ==giocatore:
                self.strategia=max(lista)
            else:
                self.strategia=min(lista)
        return self.strategia 
                
        
      
                        
def gen_tree(griglia):
    lista=griglia
    root=NodoTris(lista)
    if root.vincente=='?':
        for i in root.vuote:
            griglia2=copia_griglia(griglia)
            griglia2[i[1]][i[0]]=root.mossa_succ
            figlio=gen_tree(griglia2)
            root.lista_figli.append(figlio)
    return root
    
def copia_griglia(griglia):
    new_griglia=[]
    for y in range(0,3):
        row=['','','']
        for x in range(0,3):
                row[x]=griglia[y][x]
        new_griglia+=[row]
    return new_griglia