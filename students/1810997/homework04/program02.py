
from copy import deepcopy
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        
        self.cat=''
    
    
    def tipo(self):
        '''inserire qui il vostro codice'''
        return self.cat
        
    def esiti(self):
        '''inserire qui il vostro codice'''
        ls=[0,0,0]
        ls= es(self,ls)
        return(ls)
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
    
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''

def check(x1,x2,res):
    if x1==x2:
        return res+1

def es(nodo,ls=[0,0,0]):
    
    ls[0]=check(nodo.cat,'-',ls[0])
    ls[1]=check(nodo.cat,'o',ls[1])
    ls[2]=check(nodo.cat,'x',ls[2])
          
    if nodo.lista_figli ==[]:
        return ls
    
    for figlio in nodo.lista_figli:
         es(figlio,ls) 
    return ls


     
        
def checks(combo,s,sign,old):
    if combo in s:
        return sign
    else:
        return old
    
def checkt(turno):
    t=''
    if turno=='o':
        t='x'
    else:
        t='o'
    return t        
    
def gen_tree(griglia,turno='o'):
    '''inserire qui il vostro codice'''
    dt={'o':'x','x':'o'}
    nodo=NodoTris(griglia)
    s=''
    for y in range(3): #orizzontale
        #for x in range(3):
        
        c1=nodo.nome[y][0]
        c2=nodo.nome[y][1]
        c3=nodo.nome[y][2]
        s=c1+c2+c3
        nodo.cat=checks('xxx',s,'x',nodo.cat)
        nodo.cat=checks('ooo',s,'o',nodo.cat)
        s=''
    
    for x in range(3): #verticale
        #for y in range(3):
        #    s+=nodo.nome[y][x]
        
        c1=nodo.nome[0][x]
        c2=nodo.nome[1][x]
        c3=nodo.nome[2][x]
        s=c1+c2+c3
        nodo.cat=checks('xxx',s,'x',nodo.cat)
        nodo.cat=checks('ooo',s,'o',nodo.cat)
        s=''
        
    s=''
    
    s+=nodo.nome[0][0]+nodo.nome[1][1]+nodo.nome[2][2] #diag 1
    nodo.cat=checks('xxx',s,'x',nodo.cat)
    nodo.cat=checks('ooo',s,'o',nodo.cat)
    s+=nodo.nome[0][2]+nodo.nome[1][1]+nodo.nome[2][1] #diag 2
    nodo.cat=checks('xxx',s,'x',nodo.cat)
    nodo.cat=checks('ooo',s,'o',nodo.cat)


        


    
    #controllo per patta----se tutto pieno e cat non e' definito allora e' patta(?)
    
    if nodo.cat=='':
        flagpieno=True
        
        
        for y in range(3):
            for x in range(3):
                if nodo.nome[y][x]=='':
                    flagpieno=False
        if flagpieno==True:
            nodo.cat='-'
        else:
            nodo.cat='?'
        
    if nodo.cat=='?':
        figlio=deepcopy(nodo.nome)
        ls=[]
        
        
        for y in range(3):
            for x in range(3):
                if nodo.nome[y][x]=='':
                    figlio=deepcopy(nodo.nome)
                    figlio[y][x]=turno
                    ls.append(figlio)
        turno=dt[turno]
            
        for x in ls:
            nodo.lista_figli.append(gen_tree(x,turno))
        return nodo
    else:
        return nodo
    
    
    
    