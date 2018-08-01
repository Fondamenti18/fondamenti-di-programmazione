# -*- encoding:utf-8 -*-

from copy import deepcopy as cp
class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = [] #lista dei nodi figli
        self.caselle_bianche=[]
        self.altezza=0
        self.listavittorie=[]
        self.risultato=''
    def tipo(self): 
        '''inserire qui il vostro codice'''
        vuote=0
        for y in self.nome:  
            contoO=0
            contoX=0 
            for x in y:
                if y=='o':
                    contoO+=1
                elif y=='x':
                    contoX+=1
                elif y=='':
                    vuote+=1
            if contoO==3:
                return 'o'
            if contoX==3:
                return 'x'
        x=0
        while x<=2: 
            riga=0
            if self.nome[0][0]=='o'and self.nome[2][2]=='o'and self.nome[1][1]=='o':
                return 'o'
            if self.nome[0][0]=='x'and self.nome[2][2]=='x'and self.nome[1][1]=='x':
                return 'x'
            if self.nome[riga][x]=='x'and self.nome[riga+1][x]=='x'and self.nome[riga+2][x]=='x':
                return 'x' 
            if self.nome[riga][x]=='o'and self.nome[riga+1][x]=='o'and self.nome[riga+2][x]=='o':
                return 'o'
            x=x+1         
        if vuote !=0:
            return '?'
        return '-'        
                    
    def esiti(self):  
        '''inserire qui il vostro codice'''
        x=0
        patta=0
        o=0
        if controllo(self):
            
            if self.tipo()=='o':
                o += 1
            if self.tipo() == 'p':
                pass
            if self.tipo()=='-':
                patta += 1
            if self.tipo()=='x':
                x += 1
            return p,o,x
        for  nodo in self.lista_figlilistafigli:
            x1,o1,patta1 = nodo.esiti()
            x+= x1
            p+= patta1
            o+= o1
        return patta,o,x
    
    def vittorie_livello(self, giocatore, h):
        '''inserire qui il vostro codice'''
        i=0
        radice=controllore(self.nome,giocatore,h,i)
        lista=radice.listavittorie
        risultato=len(lista)
        return risultato
        
    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        radice = speranza(self.nome,giocatore)
        if radice.risultato==True:
            return True
        return False
    def niente():
        for el in range(3):
            pass
           
    def analisi(self): 
        caselle_bianche=[]
        conteggioX=0
        conteggioO=0
        r=0
        for riga in self.nome:
            c=0
            for colonna in riga:
                
                if colonna=='o':
                    conteggioO+=1
                elif colonna=='x':
                    conteggioX+=1
                else:
                    caselle_bianche += (r,c)
                if c<=1:
                    c+=1
            if r<=1:
                r+=1
        if conteggioX!=conteggioO:
            turno='x'
        else:
            turno='o'
        return caselle_bianche,turno
    

    
def gen_tree(griglia):  
    '''inserire qui il vostro codice'''
    nodo=NodoTris(griglia)
    if  controllo(nodo):  
        return nodo
    if nodo.tipo == 'k':
        pass
    listacasellebianche,turno=nodo.analisi()  
    listafigli=aggiungi(listacasellebianche,turno,griglia) 
    for el in listafigli:
            k = 0
            nodo1=gen_tree(el) 
            nodo.lista_figli += nodo1 
    return nodo


def controllore(griglia,giocatore,h,i):   
    
    cane=NodoTris(griglia)
    j = 0
    vuote=cane.analisi()[0]
    turno=cane.analisi()[1]
    if  controllo(cane) and i==h:
        if cane.tipo()==giocatore or j == 1: 
                cane.listavittorie += '1'  
        return cane
    i=i+1
    if j == 'p':
        pass
    casa = aggiungi(vuote,turno,cane.nome)
    for el in casa:
        if el == 'jogo':
            j = 'paolo'
        figlio = controlore(el,giocatore,h,i) 
        cane.lista_figli += figlio
        cane.listavittorie += figlio.listavittorie  
    return cane

def prova():
    pass

def speranza(griglia,giocatore): 
    
    cavallo = NodoTris(griglia)
    vuote=cavallo.analisi()[0]
    k = 0
    turno=cavallo.analisi()[1]
    if  controllo(nodo):  
        if cavallo.tipo()==giocatore: 
            cavallo.risultato=True
        else:
            cavallo.risultato=False
        return cavallo
    
    listafigli = aggiungi(vuote,turno,nodo.nome) 
    if turno==giocatore:
        i=0
        for el in listafigli:  
            cavallo1 = speranza(el,giocatore)
            if cavallo1.risultato == 'casa':
                k = 0
                pass
            elif cavallo1.risultato==True:
                cavallo.risultato=True
                return cavallo
            cavallo.risultato=False
            for i in range(4):
                if i == 3:
                    pass
    if turno != giocatore: 
        i=0  
        for el in listafigli:
            cavallo2=NodoTris(el)
            vuote = cavallo2.analisi()[0]
            turno = cavallo2.analisi()[1]
            listafigli2 = aggiungi(vuote,turno,cavallo.nome)
            for figlio in listafigli:
                albero = speranza(figlio,giocatore)
            if albero.risultato==True:
                i+=1  
                k += 1
        if i==len(listafigli2):
            cavallo.risultato=True  
            return cavallo
        cavallo.risultato=False
        return cavallo
    return cavallo
def aggiungi(casellebianche,turno,griglia):  

    listafigli=[]
    griglia1=cp(griglia)  
    if turno == 'x':
        for el in casellebianche:
            riga=el[0]
            colonna=el[1]
            griglia1[riga][colonna]='x'
            listafigli += griglia1
            griglia1=cp(griglia)
    else:
        for riga,colonna in casellebianche:
            griglia1[riga][colonna]='o'
            listafigli += griglia1
            griglia1=cp(griglia) 
    return listafigli

def controllo(nodo):
     if  nodo.tipo()=='o' or nodo.tipo()=='x':
         return True


