# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:01:23 2017

@author: User
"""

from copy import *

class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.padre=None
        self.minimax=None
        self.risultato=None
    
    def tipo(self):
        d1=[(self.nome[0])[0],(self.nome[1])[1],(self.nome[2])[2]]
        d2=[(self.nome[0])[2],(self.nome[1])[1],(self.nome[2])[0]]
        r='-'
        for l in self.nome:
            if l.count('x')==2 and '' in l :
                r= '?'
            elif l.count('x')==3:
                return 'x'
            elif l.count('o')==2 and '' in l:
                r= '?'
            elif l.count('o')==3:
                return 'o'
            elif l.count('')==2 or l.count('')==3:
                r= '?'
        colonne=self.colonne()
        for c in colonne:
            if c.count('x')==2 and '' in c :
                r= '?'
            elif c.count('x')==3:
                return 'x'
            elif c.count('o')==2 and '' in c:
                r= '?'
            elif c.count('o')==3:
                return 'o'
            elif c.count('')==2 or c.count('')==3:
                r= '?'
        diagonali=[d1,d2]
        for d in diagonali:
            if d.count('x')==2 and '' in d :
                r= '?'
            elif d.count('x')==3:
                return 'x'
            elif d.count('o')==2 and '' in d:
                r= '?'
            elif d.count('o')==3:
                return 'o'
            elif d.count('')==2 or d.count('')==3:
                r= '?'
        return r
        
    def colonne(self):
        colonna1=[]
        colonna2=[]
        colonna3=[]
        for l in self.nome:
            colonna1.append(l[0])
            colonna2.append(l[1])
            colonna3.append(l[2])
        colonne=[colonna1,colonna2,colonna3]
        return colonne
                
        
    def esiti(self):
        l=self.lista_figli
        if self.tipo()=='-':
           return(1,0,0)
        elif self.tipo()=='o':
           return(0,1,0)
        elif self.tipo()=='x':
           return (0,0,1)
        else: 
           return ris(l,[0,0,0])
        
    
    def vittorie_livello(self, giocatore, h):
        return conta_vittorie(giocatore,h,0,[self])
    
    
   
            
       
            
                
    
    def strategia_vincente(self,giocatore):
        lista=[self]
        assegna_valori(lista,giocatore)
        return check_strategia(self,giocatore)
        
            
        
        
            
            
                    
        
        
        
        
        
        
        
    def prossimo_turno(self):
       contatore=0
       for l in self.nome:
          contatore+= l.count('x')
          contatore+= l.count('o')
       if contatore%2==0:
           return 'o'
       else:
           return 'x'
       
    
     
def check_strategia(nodo,giocatore):
    if nodo.lista_figli==[]:
        return False
    else:
       figli=nodo.lista_figli
       prox_mossa=None
       valore=figli[0].minimax
       if nodo.prossimo_turno()==giocatore:
           for x in figli:
               if x.minimax==None and x.risultato==giocatore:
                   return True
               if x.minimax==None and x.risultato=='-':
                   valore=0
                   prox_mossa=x
               elif valore== None:
                   valore=x.minimax
                   prox_mossa=x
               elif x.minimax < valore:
                   valore=x.minimax
                   prox_mossa=x
               else:
                   l=x.lista_figli
                   best=10
                   for m in l:
                       if m.minimax== None and m.risultato != '-':
                           best=10
                       elif m.minimax== None and m.risultato == '-':
                           best=5
                       elif m.minimax < best:
                           best=m.minimax
                       else:
                           next
                   if best < valore:
                       valore=best
                       prox_mossa=x
       else:
           for x in figli:
               if x.minimax==None and x.risultato!='-':
                   return False
               if x.minimax==None and x.risultato=='-':
                   valore=0
                   prox_mossa=x
               elif valore== None:
                   valore=x.minimax
                   prox_mossa=x
               elif x.minimax > valore:
                   valore=x.minimax
                   prox_mossa=x
               else:
                   l=x.lista_figli
                   best=-10
                   for m in l:
                       if m.minimax== None and m.risultato == giocatore:
                           best=-10
                       elif m.minimax== None and m.risultato == '-':
                           best=-5
                       elif m.minimax > best:
                           best=m.minimax
                       else:
                           next
                   if best> valore:
                       valore=best
                       prox_mossa=x
                       
       return check_strategia(prox_mossa,giocatore)
           
               
       
        
        
    
    
    
    
def assegna_valori(nodi,giocatore):
    if nodi ==[]:
        return
    else:
       lista2=[]
       for n in nodi:
           figli=n.lista_figli
           if n.prossimo_turno()== giocatore:
               for f in figli:
                   if f.risultato==giocatore:
                      n.minimax=-10
                      break
                   elif f.risultato=='-':
                      n.minimax=0
                   else:
                      n.minimax=-5
               lista2+=figli
           else:
               for f in figli:
                  if f.risultato=='-':
                      n.minimax=0
                  elif f.risultato=='?':
                      n.minimax=5
                  else:
                      n.minimax=10
                      break
               lista2+=figli
    return assegna_valori(lista2,giocatore)
            
    
                
                
        
    
        
        
        
    
    
    
                        
    
              
                
def conta_vittorie(giocatore, h,livello,lista):
    if h==livello:
        vittorie=0
        for nodo in lista:
            if nodo.risultato==giocatore:
                vittorie+=1
        return vittorie
    else:
        lista2=[]
        for nodo in lista:
            lista2+=nodo.lista_figli
        return conta_vittorie(giocatore,h,livello+1,lista2)
            
                
        
    
        
def ris(l,r):
    lista2=[]
    if l==[]:
        return tuple(r)
    for x in l:
       if x.risultato=='-':
        r[0]+=1
        lista2+=x.lista_figli
       elif x.risultato=='o':
        r[1]+=1
        lista2+=x.lista_figli
       elif x.risultato=='x':
        r[2]+=1
        lista2+=x.lista_figli
       else:
        lista2+=x.lista_figli    
    return ris(lista2,r)   


    
    
        
        
def gen_tree(griglia):
    radice=NodoTris(griglia)
    lista=[radice]
    gen_figli(lista)
    return radice

def gen_figli(lista):
    lista2=[]
    if lista==[]:
        return  
    else:
        for nodo in lista:
           matrice=nodo.nome
           g=nodo.prossimo_turno()
           for c in range(3):
              for i in range(3):
                   if (matrice[c])[i] == '':
                    (matrice[c])[i] =g
                    copia=deepcopy(nodo.nome)
                    figlio=NodoTris(copia)
                    figlio.padre=nodo
                    if figlio.tipo()=='?':
                        figlio.risultato='?'
                        nodo.lista_figli.append(figlio)
                        lista2.append(figlio)
                        (matrice[c])[i] =''   
                    elif figlio.tipo()=='o':
                        figlio.risultato='o'
                        nodo.lista_figli.append(figlio)
                        (matrice[c])[i] ='' 
                    elif figlio.tipo()=='x':
                        figlio.risultato='x'
                        nodo.lista_figli.append(figlio)
                        (matrice[c])[i] ='' 
                    elif figlio.tipo()=='-':
                        figlio.risultato='-'
                        nodo.lista_figli.append(figlio)
                        (matrice[c])[i] ='' 
                   else:
                    next
    
    return gen_figli(lista2)





        
    
                    
            
        
    
    
    
    


    

    