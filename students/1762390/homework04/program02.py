
from copy import deepcopy
 
class NodoTris:
    def __init__(self, griglia):
        self.griglia = griglia
        self.lista_figli = []
        self.lista_figli.extend(self.generaFigli(griglia))
                    
        
        
        
    def generaFigli(self,g):
        figli=[]
        
        vincitore=self.tipo()
        if(vincitore=='-'=='o'=='x'):
            return figli
            
        m=prossimaMossa(self.griglia)
        for riga in range(0,3):
            for colonna in range(0,3):
                if(g[riga][colonna]==''):
                    f=deepcopy(g)
                    f[riga][colonna]=m
                    figli+=[NodoTris(f)]
                    
        return figli
            
    def tipo(self):
        if('o' == self.griglia[0][2] and 'o'== self.griglia[1][2] and 'o' == self.griglia[2][2]):
            return 'o'
        if('x' == self.griglia[0][2] and 'x'== self.griglia[1][2] and 'x' == self.griglia[2][2]):
            return 'x'
         
        if('o' == self.griglia[0][0] and 'o'== self.griglia[1][0] and 'o' == self.griglia[2][0]):
            return 'o'
        if('x' == self.griglia[0][0] and 'x'== self.griglia[1][0] and 'x' == self.griglia[2][0]):
            return 'x'
        if('o' == self.griglia[1][0] and 'o'== self.griglia[1][1] and 'o' == self.griglia[1][2]):
            return 'o'
        if('x' == self.griglia[1][0] and 'x'== self.griglia[1][1] and 'x' == self.griglia[1][2]):
            return 'x'
        
        if('o' == self.griglia[0][0] and 'o'== self.griglia[0][1] and 'o' == self.griglia[0][2]):
            return 'o'
        if('x' == self.griglia[0][0] and 'x'== self.griglia[0][1] and 'x' == self.griglia[0][2]):
            return 'x'
        
        if('o' == self.griglia[2][0] and 'o'== self.griglia[2][1] and 'o' == self.griglia[2][2]):
            return 'o'
        if('x' == self.griglia[2][0] and 'x'== self.griglia[2][1] and 'x' == self.griglia[2][2]):
            return 'x'
        
        if('o' == self.griglia[0][0] and 'o'== self.griglia[1][1] and 'o' == self.griglia[2][2]):
            return 'o'
        if('x' == self.griglia[0][0] and 'x'== self.griglia[1][1] and 'x' == self.griglia[2][2]):
            return 'x'
        
        if('o' == self.griglia[0][2] and 'o'== self.griglia[1][1] and 'o' == self.griglia[2][0]):
            return 'o'
            
        if('x' == self.griglia[0][2] and 'x'== self.griglia[1][1] and 'x' == self.griglia[2][0]):
            return 'x'
        
        if('o' == self.griglia[0][1] and 'o'== self.griglia[1][1] and 'o' == self.griglia[2][1]):
            return 'o'
        if('x' == self.griglia[0][1] and 'x'== self.griglia[1][1] and 'x' == self.griglia[2][1]):
            return 'x'
        
        for riga in self.griglia:
            for colonna in riga:
                if(colonna==''):
                    return '?'
        
        return '-'
           
    def esiti(self):
        
        t=(0,0,0)
        r=self.tipo()
        if(r=='-'):
            return tuple(map(sum, zip(t, (1,0,0))))
        elif(r=='o'):
            return tuple(map(sum, zip(t, (0,1,0))))
        elif(r=='x'):
            return tuple(map(sum, zip(t, (0,0,1))))
                 
        for baby in self.lista_figli:
            t=tuple(map(sum, zip(t, baby.esiti())))
        
        return tuple(t)
        
    
    def vittorie_livello(self, giocatore, h):
        
        v=0
        if(h<0):
           return v
        
        r=self.tipo()
        if(r==giocatore and h==0):
            return v+1
        
        if(r=='-' or r=='o' or r=='x'):
            return v
        for baby in self.lista_figli:
            v+=baby.vittorie_livello(giocatore,h-1)
        
        return v
        
    def strategia_vincente(self,giocatore):
        return False    
                    
    def __str__(self):
        return str(self.griglia)             
                    
                    
                    
def prossimaMossa(griglia):
    O=X=0
    O=griglia[0].count('o')+griglia[1].count('o')+griglia[2].count('o')
    X=griglia[0].count('x')+griglia[1].count('x')+griglia[2].count('x')
    if(O>X):
        return 'x'
    return 'o'
        
        
    
def gen_tree(griglia):
    nodoTris=NodoTris(griglia)            
    return nodoTris    
