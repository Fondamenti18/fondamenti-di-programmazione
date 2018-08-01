# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:33:11 2018

@author: Admin_2
"""

#prove program02
from mappe import *
from math import sqrt
import collections

#anello=piste['anello']
##anello[40][48]==B
monza=piste['monza']


class Nodo:
    def __init__(self,mappa,x,y):
        self.mappa = mappa
        self.x=x
        self.y=y
        self.value = self.mappa[y][x]
        self.parent = None
        self.H = 0
        self.G = 0 
        self.coord_figli=[]
        for d in [ (x-1, y),(x,y - 1),(x,y + 1),(x+1,y),(x-1,y-1), (x-1,y+1),(x+1,y+1),(x+1,y-1)]:
            if d[0] in range(len(mappa[0])) and d[1] in range(len(mappa)):
                if mappa[d[1]][d[0]]==' ':
                    self.coord_figli.append((d[1],d[0]))
        self.lista_figli=[]
      


'''fuori dalla classe, funzioni generali (non sono metodi specifici per gli oggetti perchè non gli si passa self come parametro)'''

        
def distance(nodoA, nodoB):
    #manhattan distance, o taxi distance
    return abs(nodoA.x-nodoB.x)+abs(nodoA.y-nodoB.y)

#start=Nodo(anello, 48, 40)
#goal= Nodo(anello, 46, 40)
#start=Nodo(provola, 7,6)
#goal=Nodo(provola,9,6)


def aStar(start, goal, mappa):
    opendict = {}
    closeddict={}
    current = start
    opendict[(current.y,current.x)]=current
    while opendict:   
        #Find the item in the open set with the lowest G + H score
        current = min(opendict.values(), key=lambda o:o.G + o.H)
        #belle le lambda! molto molto fighe. le regine delle oneline. 
        # il carattere 'o' e' del tutto arbitrario, puo' essere qualsiasi cosa e fa riferimento a ognuno degli elementi fra i quali si sceglie il minimo
        
        if (current.x,current.y) == (goal.x,goal.y):
            #print('ricostruisco il percorso')
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1] #ordinato da Start a Goal
        
        opendict.pop((current.y,current.x))
        closeddict[(current.y,current.x)]=current
        for tupla in current.coord_figli:
            y,x=tupla
           # print('provo ogni figlio')
            if tupla in closeddict.keys():
                continue
            if tupla in opendict.keys():
                new_g = current.G + 1
                node=opendict[tupla]
                if node.G > new_g:
                    #If so, update the node to have a new parent. ovvero se il 
                    #modo in cui ci sono arrivato prima era piu' lungo della strada che ho preso ora, 
                    #scegli il padre più conveniente!
                    node.G = new_g
                    node.parent = current
            else:
                #If it isn't in the open set, calculate the G and H score for the node
                #print('son tutti figli nuovi')
                node=Nodo(mappa,tupla[1],tupla[0])
                node.G = current.G + 1
                node.H = distance(node, goal)
                node.parent = current
                opendict[tupla]=node
    raise ValueError('No Path Found')
    
def gen_tree_path(path):
    n=0
    nodo_fine=path[-1]
    while path[n]!=nodo_fine:
        path[n].lista_figli=[path[n+1]]
        n+=1
    return

def get_d_a(nodoA, vx, vy):
    nodoB=nodoA.lista_figli[0]
    dx=nodoB.x-nodoA.x  #verso del vettore che e' direzionato lungo l'asse x. ha lunghezza 1
    ax=dx-vx
    dy=nodoB.y-nodoA.y
    ay=dy-vy
    return dx, dy, ax, ay

def find_n(l, spazi): #must be used with l>=4. 
    #returns how many times is possible to accelerate
    diff=[l-el for el in spazi if l-el>=0 ]
    return int(sqrt(l-min(diff)))

def gen_acc(n,ax, ay):
    pross_x=[ax]*(n-1)+[-ax]*(n-1)
    p_x=collections.deque(pross_x)
    pross_y=[ay]*(n-1)+[-ay]*(n-1)
    p_y=collections.deque(pross_y)
    return p_x, p_y
    
#####################

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    mappa=griglia_corrente
    start=Nodo(mappa,startx, starty)
    z=-(verso*2)
    u=-(verso)
    goal= Nodo(mappa, startx+z, starty)
    traguardo=Nodo(mappa,startx+u,starty)
    spazi=[4,9,16,25,36,49,64,81,100]
    lrange=[-1,0,1]
    if traguardo.x==x and traguardo.y==y: #se sono arrivata al traguardo freno (assumendo di essere sulla casella traguardo con vx e vy moduli <=1)
        ax=-vx
        ay=-vy
#        print('arrivata')
        return ax, ay
    elif x==startx and y==starty and laps==0: #se e' la prima mossa che faccio
        global path
        global dict_path
        path=[]
        path=aStar(start, goal, mappa)
        path+=[traguardo] #aggiungo la casella traguardo che avevo scartato in aStar()
        gen_tree_path(path)
        dict_path={}
        for el in path:
            dict_path[(el.y,el.x)]=el
        dx,dy,ax,ay=get_d_a(start, vx, vy)
        m=0
        nodo0=start
        nodo1=nodo0.lista_figli[0]
        while nodo1.x==nodo0.x+dx and nodo1.y==nodo0.y+dy:
            m+=1
            nodo0=nodo1
            nodo1=nodo0.lista_figli[0]
        global p_x
        global p_y
        p_x=collections.deque()
        p_y=collections.deque()
        if m>=4:
            n=find_n(m, spazi)
            p_x, p_y =gen_acc(n, ax, ay)
            Ax=p_x.popleft()
            Ay=p_y.popleft()
            print( p_x, p_y, Ax, Ay)
            return Ax, Ay
        else:
#            print( p_x, p_y, ax, ay)
            return ax, ay
    else: #sono gia' un pezzo avanti, non mi devo ricalcolare il percorso..
        node=dict_path[(y,x)]
        if p_x:
            Ax=p_x.popleft()
            Ay=p_y.popleft()
#            print( p_x, p_y, Ax, Ay, 'ppp')
            return Ax, Ay
        else: 
            dx,dy,ax,ay=get_d_a(node, vx, vy)
            if ax!=0 or ay!=0: #devo girare (non possso accelerare)
#                print( ax, ay, 'ooo')
                if ax in lrange and ay in lrange:
                    return ax, ay
                else: #se sto tornando indietro in una delle 2 direzioni
                    ax=-vx
                    ay=-vy
#                    print( ax, ay, 'aaa')
                    return ax, ay
            else: #sto andando nella direzione giusta (posso accelerare)
                #ho ax==0 e ay==0
                m=0 #quanto è lungo il rettilineo 
                nodo0=node
                nodo1=nodo0.lista_figli[0]
                while nodo1.x==nodo0.x+dx and nodo1.y==nodo0.y+dy:
                    m+=1
                    nodo0=nodo1
                    try:
                        nodo1!=traguardo
                        nodo1=nodo0.lista_figli[0]
                    except: 
                        break
                if m>=4:
                    n=find_n(m, spazi)
                    p_x, p_y =gen_acc(n, vx, vy) #dato che le a=0, prendo in considerazione le v
                    Ax=p_x.popleft()
                    Ay=p_y.popleft()
#                    print( p_x, p_y, Ax, Ay, 'kkk', m, n)
                    return Ax, Ay
                else:
#                    print( p_x, p_y, ax, ay, 'iiii', m)
                    return ax, ay
            

