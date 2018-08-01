
import numpy as np
import sys
sys.setrecursionlimit(25000)


import copy
def cerca_orizontale(lista,stringa="",x=0,y=0):
   
    while x<3:
        stringa+=lista[y][x]
        x+=1
    return stringa  
def cerca_verticale(lista,stringa="",x=0,y=0):
     while y<3:
        stringa+=lista[y][x]
        y+=1
     return stringa
def diagonale(lista,stringa="",x=0,y=0):
     while x < 3 and y<3 :
        stringa+=lista[y][x]
        y+=1
        x+=1
     return stringa
def diagonale2(lista,stringa="",x=2,y=0):
     while x >= 0 and y<=2 :
        stringa+=lista[y][x]
        y=y+ 1
        x=x-1
     return stringa
def controllo_turno(griglia):
    cont=0
    for y in griglia:
        for q in y:
            if q=="":
                cont+=1
                
    if cont%2==0:
        return "x"
    else:
        return "o"

def coordinate(griglia):
    k=[]
    for y in range(3):
        for x in range(3):
            if griglia[y][x]=="":
                k.append([y,x])
    return k 


contatore=0
def scorri(nodo,giocatore,h,livello):
    global contatore
    if livello != h:
         for i in nodo.lista_figli:
             scorri(i,giocatore,h,livello+1)    
    if livello == h-1: 
        for child in nodo.lista_figli:
            
            if child.tipo()==giocatore:
                contatore+=1            
    return contatore

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] 
        self.foglie=[]
        self.rx=[]
        self.ro=[]
        self.rp=[]
    def tipo(self):
       
        pareggio=False    
        vittoria = False
        in_corso=False
        risultato=""
        for n in range(3):
    
            h=cerca_orizontale(self.nome,"",0,n)
            o=cerca_verticale(self.nome,"",n,0)
    
            if h == "ooo" or h=="xxx":
                vittoria=True
                risultato=h[0]
                break
            if o=="ooo" or o=="xxx":
                vittoria=True
                risultato=o[0]
                break
    
    
        if vittoria ==False:
            t=diagonale2(self.nome,"",2,0)
            b=diagonale(self.nome,"",0,0)
            if t=="ooo" or t=="xxx":
                vittoria=True
                risultato=t[0]
            if b=="ooo" or b=="xxx":
                vittoria=True
                risultato=b[0]     
    
        if vittoria ==False:
            for a in self.nome:
                for _ in a:
                    if _ =="":
                        in_corso=True
                        risultato="?"
                        break
            if in_corso==False:
                risultato="-"
                pareggio=True
        
        return risultato
               
    def esiti(self):
        g=Tupla_Ricorsiva(self.rp,self.rx,self.ro,0,0,0,0)
        return g

  
            
        
             
    def vittorie_livello(self, giocatore, h):
        global contatore
        contatore=0
        t=scorri(self,giocatore,h,livello=0)
  
        return t
        
        
        
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
       
xu=[]
ou=[]
pu=[]
def albero(griglia):    
    global x
    global o
    global p
    c=NodoTris(griglia)
    if c.tipo()=="?":
        a=controllo_turno(c.nome)
        lis=coordinate(c.nome)
        for co in lis:
           
            cop=[]
            for el in c.nome:
                sli=el[:]
                cop.append(sli)
            y=co[0]
            x=co[1]
            cop[y][x]=a
        
            c.lista_figli.append(albero(cop))
        
    else:
        
        if c.tipo()=="x":
            xu.append(c.nome)
        elif c.tipo()=="o":
            ou.append(c.nome)
        elif c.tipo()=="-":
            pu.append(c.nome)
            
        
    return c      
def gen_tree(griglia):
    
    del xu[:]
    del ou[:]
    del pu[:]
    weed=albero(griglia)
  
    weed.ro=copy.copy(ou)
    weed.rx=copy.copy(xu)
    weed.rp=copy.copy(pu)
    return weed            
def stampa(nodo,livello):
 
    for child in nodo.lista_figli:
       stampa(child,livello+1)
 

def Tupla_Ricorsiva(listap,listax,listao,n=0,p=0,o=0,x=0):
    if n==0:
        p=len(listap)
        return Tupla_Ricorsiva(listap,listax,listao,n+1,p,o,x)
    elif n==1:
        o=len(listao)
        return Tupla_Ricorsiva(listap,listax,listao,n+1,p,o,x)
    elif n==2:
        x=len(listax)
        return Tupla_Ricorsiva(listap,listax,listao,n+1,p,o,x) 

    return ((p,o,x))
