
from immagini import *
    
def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    img=load(fname)
    misure=[]
    for (colonna,riga,c1,c2) in lista:
        grafo=creaGrafo(img,img[riga][colonna])
        inizio=grafo[riga,colonna]
        visitati=set()
        da_visitare=[inizio]

        while( da_visitare ):     #una visita del grafo 
            u=da_visitare.pop(0)
            if u in visitati:
                continue
            visitati.add(u)
            img[u.riga][u.colonna]=c1
            for v in u.vicini:
                if( v not in visitati):
                    da_visitare.append(v)
        perimetro=0
        
        for v in visitati:
            if(len(v.vicini)<4):
                img[v.riga][v.colonna]=c2
                perimetro+=1
        misure.append((len(visitati)-perimetro,perimetro))
     
    save(img,fnameout)
    return misure
                    
class Nodo:    #classe nodo mi morizza le coordiante di pixel 

    def __init__(self,riga,colonna):
        self.riga=riga
        self.colonna=colonna
        self.vicini=[]   #lista continene i vicini  cioe i nodi 

def  creaGrafo(img,c1):
    grafo={}
    for riga in range(len(img)):
        for colonna in range(len(img[0])):
            if(img[riga][colonna]==c1):
                grafo[(riga,colonna)]=Nodo(riga,colonna)
    for (riga,colonna),nodo in grafo.items():
        if(riga-1,colonna) in grafo:
            nodo.vicini.append(grafo[(riga-1,colonna)])
        if(riga+1,colonna) in grafo:
            nodo.vicini.append(grafo[(riga+1,colonna)])
        if(riga,colonna+1) in grafo:
            nodo.vicini.append(grafo[(riga,colonna+1)])
        if(riga,colonna-1) in grafo:
            nodo.vicini.append(grafo[(riga,colonna-1)])
    return grafo

