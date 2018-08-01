import copy
def chivince(griglia):   
    if ((griglia[0][0]=='o' and griglia[0][1]=='o' and griglia[0][2]=='o') or (griglia[1][0]=='o' and griglia[1][1]=='o' and griglia[1][2]=='o')  or (griglia[2][0]=='o' and griglia[2][1]=='o' and griglia[2][2]=='o')
    or (griglia[0][0]=='o' and griglia[1][0]=='o' and griglia[2][0]=='o') or (griglia[0][1]=='o' and griglia[1][1]=='o' and griglia[2][1]=='o') or (griglia[0][2]=='o' and griglia[1][2]=='o' and griglia[2][2]=='o')
    or (griglia[0][0]=='o' and griglia[1][1]=='o' and griglia[2][2]=='o') or (griglia[0][2]=='o' and griglia[1][1]=='o' and griglia[2][0]=='o')):
        return 'o'
    elif ((griglia[0][0]=='x' and griglia[0][1]=='x' and griglia[0][2]=='x') or (griglia[1][0]=='x' and griglia[1][1]=='x' and griglia[1][2]=='x')  or (griglia[2][0]=='x' and griglia[2][1]=='x' and griglia[2][2]=='x')
    or (griglia[0][0]=='x' and griglia[1][0]=='x' and griglia[2][0]=='x') or (griglia[0][1]=='x' and griglia[1][1]=='x' and griglia[2][1]=='x') or (griglia[0][2]=='x' and griglia[1][2]=='x' and griglia[2][2]=='x')
    or (griglia[0][0]=='x' and griglia[1][1]=='x' and griglia[2][2]=='x') or (griglia[0][2]=='x' and griglia[1][1]=='x' and griglia[2][0]=='x')):
        return 'x'
    elif (griglia[0][0]=='' or griglia[0][1]=='' or griglia[0][2]=='') or (griglia[1][0]=='' or griglia[1][1]=='' or griglia[1][2]=='')  or (griglia[2][0]=='' or griglia[2][1]=='' or griglia[2][2]==''):
        return '?'
    return '-' 
def chigioca(griglia):
    contax=0
    contao=0
    contaspazi=0
    for riga in range(len(griglia)):
        for colonna in range(len(griglia[0])):
                if(griglia[riga][colonna]=='x'):
                    contax+=1
                elif(griglia[riga][colonna]=='o'):
                    contao+=1 
                else:
                    contaspazi+=1 
    if contaspazi==0:
        return 'stop'
    elif contaspazi==9:
        return 'o'
    elif contao>contax:
        return 'x'
    elif contax>=contao:
        return 'o'
'''def livelli(nodo,giocatore,h,livello,lista):
    if(chivince(nodo.nome)==giocatore and livello==h):
        lista+=[nodo]
    elif(chivince(nodo.nome)=='?'):
        for n in  nodo.lista_figli:
            lista+=livelli(n,giocatore,h,livello+1,lista)
        return lista'''
def calcolalivelli(radice):
    if radice.lista_figli==[]:
        return 1
    for n in  radice.lista_figli:
         return 1+calcolalivelli(n)
    
def livelli(nodo,giocatore,livello,l1,a):
    
    if(chivince(nodo.nome)==giocatore):
        a=+1
        l1[livello]+=a
    else:
        for n in  nodo.lista_figli:
            if(chivince(n.nome)!=giocatore and chivince(n.nome)!='?' and chivince(n.nome)!='-'):
                continue
            elif chivince(n.nome)=='-':
                continue
            l1=livelli(n,giocatore,livello+1,l1,a)
    return l1
def strategia(nodo,giocatore): 
    if(chivince(nodo.nome)==giocatore):
        return True
    elif (chigioca(nodo.nome)=='stop' and chivince(nodo.nome)!=giocatore):
        return False
    else:
        for n in  nodo.lista_figli:
            return strategia(n,giocatore)

def strategia1(nodo,giocatore):
    
    if(nodo.nome[1][1]=='o' and (nodo.nome[0][0]=='x' or nodo.nome[0][2]=='x' or nodo.nome[2][0]=='x' or nodo.nome[2][2]=='x') and giocatore=='o'):
        return False
    elif(nodo.nome[1][1]=='o' and (nodo.nome[0][0]=='x' or nodo.nome[0][2]=='x' or nodo.nome[2][0]=='x' or nodo.nome[2][2]=='x') and giocatore=='x'):
        return False
    elif(nodo.nome[1][1]=='o' and nodo.nome[0][0]!='x' and nodo.nome[0][2]!='x' and nodo.nome[2][0]!='x' and nodo.nome[2][2]!='x' and giocatore=='o'):
        return True
    elif(nodo.nome[1][1]=='o' and nodo.nome[0][0]!='x' and nodo.nome[0][2]!='x' and nodo.nome[2][0]!='x' and nodo.nome[2][2]!='x' and giocatore=='x'):
        return False
    elif(nodo.nome[1][1]=='x' and (nodo.nome[0][0]=='o' or nodo.nome[0][2]=='o' or nodo.nome[2][0]=='o' or nodo.nome[2][2]=='o') and giocatore=='x'):
        return False
    elif(nodo.nome[1][1]=='x' and (nodo.nome[0][0]=='o' or nodo.nome[0][2]=='o' or nodo.nome[2][0]=='o' or nodo.nome[2][2]=='o') and giocatore=='o'):
        return False
    elif (nodo.nome[1][1]=='x' and nodo.nome[0][0]!='o' and nodo.nome[0][2]!='o' and nodo.nome[2][0]!='o' and nodo.nome[2][2]!='o'and giocatore=='x'):
        return True
    elif (nodo.nome[1][1]=='x' and nodo.nome[0][0]!='o' and nodo.nome[0][2]!='o' and nodo.nome[2][0]!='o' and nodo.nome[2][2]!='o'and giocatore=='o'):
        return False
    else: 
        for n in  nodo.lista_figli:
            return strategia1(n,giocatore)
       
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli    
    def getnome(self):
        return self.nome                       
    def tipo(self):
        if ((self.nome[0][0]=='o' and self.nome[0][1]=='o' and self.nome[0][2]=='o') or (self.nome[1][0]=='o' and self.nome[1][1]=='o' and self.nome[1][2]=='o')  or (self.nome[2][0]=='o' and self.nome[2][1]=='o' and self.nome[2][2]=='o')
         or (self.nome[0][0]=='o' and self.nome[1][0]=='o' and self.nome[2][0]=='o') or (self.nome[0][1]=='o' and self.nome[1][1]=='o' and self.nome[2][1]=='o') or (self.nome[0][2]=='o' and self.nome[1][2]=='o' and self.nome[2][2]=='o')
         or (self.nome[0][0]=='o' and self.nome[1][1]=='o' and self.nome[2][2]=='o') or (self.nome[0][2]=='o' and self.nome[1][1]=='o' and self.nome[2][0]=='o')):
            return 'o'
        elif ((self.nome[0][0]=='x' and self.nome[0][1]=='x' and self.nome[0][2]=='x') or (self.nome[1][0]=='x' and self.nome[1][1]=='x' and self.nome[1][2]=='x')  or (self.nome[2][0]=='x' and self.nome[2][1]=='x' and self.nome[2][2]=='x')
        or (self.nome[0][0]=='x' and self.nome[1][0]=='x' and self.nome[2][0]=='x') or (self.nome[0][1]=='x' and self.nome[1][1]=='x' and self.nome[2][1]=='x') or (self.nome[0][2]=='x' and self.nome[1][2]=='x' and self.nome[2][2]=='x')
        or (self.nome[0][0]=='x' and self.nome[1][1]=='x' and self.nome[2][2]=='x') or (self.nome[0][2]=='x' and self.nome[1][1]=='x' and self.nome[2][0]=='x')):
             return 'x'
        elif (self.nome[0][0]=='') or (self.nome[0][1]=='') or (self.nome[0][2]=='') or (self.nome[1][0]=='') or (self.nome[1][1]=='' ) or (self.nome[1][2]=='') or (self.nome[2][0]=='') or (self.nome[2][1]=='') or (self.nome[2][2]==''):
            return '?'
        return '-'   
    def esiti(self):
        lista=[]
        lista,radice=gen_tree1(lista,self.nome)
        contapari=0
        contao=0
        contax=0
        for a in lista:
            if a=='-':
                contapari+=1
            elif a=='o':
                contao+=1 
            elif a=='x':
                contax+=1     
        return (contapari,contao,contax)
    def vittorie_livello(self,giocatore,h):
        l={}        
        radice=gen_tree(self.nome)
        q=calcolalivelli(radice)
        c=0
        for k in range(0,q):
            l[k]=0
        a=livelli(radice,giocatore,0,l,c)
        b=a[h]
        return b
    def strategia_vincente(self,giocatore):
        radice=gen_tree(self.nome)
        return strategia1(radice,giocatore)  
        
def cerca(nodo,s):
        conta=1
        for g in nodo.lista_figli:
            if(chivince(g.nome)==s):
                conta=cerca(g,s)+1
        return conta    
def gen_tree(griglia):
    radice=NodoTris(griglia)
    for riga in range(0,3):
        for colonna in range(0,3): 
            if(griglia[riga][colonna]==''):
                griglia1=copy.deepcopy(griglia)
                griglia1[riga][colonna]=chigioca(griglia)
                radice.lista_figli+=[gen_tree(griglia1)]
    return radice
def gen_tree1(lista,griglia):
    radice=NodoTris(griglia)
    lista+=[chivince(griglia)]
    if(chivince(griglia)=='x' or chivince(griglia)=='o' or chivince(griglia)=='-'):
        return lista,radice
    for riga in range(0,3):
        for colonna in range(0,3): 
            if(griglia[riga][colonna]=='') :
                griglia1=copy.deepcopy(griglia)
                griglia1[riga][colonna]=chigioca(griglia)
                if(chivince(griglia1)=='x' or chivince(griglia1)=='o' or chivince(griglia1)=='-'):
                    lista+=[chivince(griglia1)]
                else:
                    radice.lista_figli+=[gen_tree1(lista,griglia1)]
    return lista,radice

def gen_tree2(griglia):
    radice=NodoTris(griglia)
    if(chivince(griglia)=='x' or chivince(griglia)=='o' or chivince(griglia)=='-'):
        return radice
    for riga in range(0,3):
        for colonna in range(0,3): 
            if(griglia[riga][colonna]=='') :
                griglia1=copy.deepcopy(griglia)
                griglia1[riga][colonna]=chigioca(griglia)
                radice.lista_figli+=[gen_tree2(griglia1)]
    return radice
               