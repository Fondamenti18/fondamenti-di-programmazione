#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:13:05 2017

@author: fabio
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:08:26 2017

@author: fabio
"""

import numpy as np
from mappe import piste
from collections import deque
control=0
road=[]
holes=[]
finish=[]
path={}
direction=0
bestpath=[]
v=0

class panda750:
    def __init__(self,x,y,vx,vy,step):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.ax=0
        self.ay=0
        self.step=step 
        self.whereigo=[]
        self.position=(self.x,self.y)
        
    def node_value(self):
        if (self.x+v,self.y) in finish and self.vx==v: return 10
        elif abs(self.vx)+abs(self.vy)==0:return -10                                
        elif self.position in finish and self.vx*direction<0:return -10             
        elif self.position in holes:return -10
        elif self.position in road:return 5                                     
        else:return 0
start=panda750(0,0,0,0,0)

def fill_roads(x,y):
    global road
    for i in range(len(x)):road.append((x[i],y[i]))
    return

def fill_holes(x,y):
    global holes
    for i in range(len(x)):holes.append((x[i],y[i]))
    return

def fill_finish(x,y):
    global finish
    for i in range(len(x)):finish.append((x[i],y[i]))
    return

    
def find_neighbors(track):
    neighbors={}
    for el in track:neighbors[el]=directions(el,track)
    return neighbors

def directions(el,track):
    ls=[]
    for i in [-1,0,1]:
        for j in [0,1,-1]: 
            if (el[0]+i,el[1]+j) in track and abs(i)!=abs(j):
                ls.append(((el[0]+i,el[1]+j),[(i,j)]))
    return ls

def shortestpath(neig,start,chessflag):
    pos=deque([(start,[])])
    seen=[]
    while pos:
        lookat=pos.popleft()
        if lookat[0]==chessflag:return lookat[1]
        if lookat[0] in seen:continue
        seen.append(lookat[0])
        for el,path in neig[lookat[0]]:pos.append((el,lookat[1]+path))
    return

def brumbrum(ls,step):
    global start
    global control
    if ls==[]:return 
    ls1=[]
    for el in ls:
        if el.node_value()==10:control=1
        if abs(el.node_value())!=10 or step==1:
            temp=jumps(el.x,el.y,el.vx,el.vy,el.step)
            el.whereigo=temp
            ls1+=temp
            if not control:brumbrum(ls1,el.step)
    return 

def jumps(x,y,vx,vy,step):
    global path
    ls=[]
    tx=x
    ty=y
    tvx=vx
    tvy=vy
    s=np.sign(vx) or 1
    s1=np.sign(vy) or 1
    a=1*s
    b=-2*s
    c=-1*s
    d=1*s1
    e=-2*s1
    f=-1*s1
    for i in range(a,b,c):
        for j in range(d,e,f):
            tvx+=i
            tvy+=j
            tx+=tvx
            ty+=tvy
            if (tx,ty) in set(path.keys())-set(holes) and path[(tx,ty)]>step:
                node=panda750(tx,ty,tvx,tvy,path[(tx,ty)])
                node.ax=i
                node.ay=j
                ls.append(node)
            tx=x
            ty=y
            tvx=vx
            tvy=vy
    return ls

def ayrton_senna(node,alpha):
    global bestpath
    if node.whereigo==[]:return node.node_value(),(node.ax,node.ay)
    for el in node.whereigo:
        score,acc=ayrton_senna(el,alpha)
        if score>alpha:
            bestpath.append(acc)
            alpha=score
    return alpha,(node.ax,node.ay)
 
def fill_shorttrack(track):
    for el in track[:]:
        for i in range(2):
            if (el[0]+i,el[1]) not in track and (el[0]+i,el[1]) in road:
                track.insert(track.index(el)+1,(el[0]+i,el[1]))
        for i in range(2):
            if (el[0],el[1]+i) not in track and (el[0],el[1]+i) in road:
                track.insert(track.index(el)+1,(el[0],el[1]+i))
    return track

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty,laps):
    '''inserite qui il vostro codice'''
    if (startx,starty)==(x,y):
        global road,holes,finish,path,direction,start,v,noholes,control,bestpath
        control=0
        road=[]
        holes=[]
        finish=[]
        path={}
        direction=0
        bestpath=[]
        v=0
        direction=verso
        p=np.matrix(griglia_corrente)
        r=np.where(p==' ')
        h=np.where(p=='O')
        f=np.where(p=='|')
        fill_roads(r[1],r[0]) 
        fill_holes(h[1],h[0]) 
        fill_finish(f[1],f[0])
        road+=[(x,y)]
        dic=find_neighbors(road+holes)
        v=verso
        while (finish[0][0]-v,finish[0][1]) not in road:v+=verso
        short=shortestpath(dic,(x,y),(finish[0][0]-v,finish[0][1]))
        a=x
        b=y
        k=0
        count=0
        cleanpath=[]
        for el in short:
            a+=el[0]
            b+=el[1]
            cleanpath.append((a,b))  
        for el in cleanpath:
            if el in holes:count+=1
        if count>=10:
            cleanpath=fill_shorttrack(cleanpath)
        for el in cleanpath:
            k+=1
            path[(el[0],el[1])]=k
        start=panda750(x,y,vx,vy,0) 
        brumbrum([start],1)
        ayrton_senna(start,-10)
        return bestpath.pop() 
    elif (x+v,y) in finish:return (0,1)
    elif (x,y) in finish or laps:return(-np.sign(vx),-np.sign(vy))
    else:return bestpath.pop()
    
if __name__=='__main__':    
    l=[]
    for el in piste['roma']:
            l.append(list(el))
    ai(l,0,48,35,0,0,0,1,48,35,0)

#    for el in piste['monza']:
#            l.append(list(el))
#    ai(l,0,65,33,0,0,0,-1,65,33,0)
    
#    for el in piste['anello']:
#            l.append(list(el))
#    ai(l,0,48,39,0,0,0,1,48,39,0)
