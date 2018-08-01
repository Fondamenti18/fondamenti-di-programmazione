#smart version ,scanline fill,using checkGrid

from immagini import *

img = []
checkGrid = []
w,h = 0,0

def ricolora(fname, lista, fnameout):
    
    global img,w,h
    
    img = load(fname)
    arealist = []
    
    w = len(img[0])
    h = len(img)
    
    for quad in lista:
        
        current = [quad[0],quad[1]]
        startC = img[quad[1]][quad[0]]        
        
        arealist.append(fill(current,startC,quad[2],quad[3]))
    
    save(img,fnameout)
    return arealist
    
def makeCheckGrid(startCol):
    global checkGrid

    checkGrid = [[1 for y in range(h)] for x in range(w)]
    
    for x in range(w):
        for y in range(h):            
            if getP([x,y]) == startCol:
                checkGrid[x][y] = 0
                
    return checkGrid
    
def visited(pos):

    try:
        if pos[0] < 0 or pos[1] < 0:
            return True
        else:
            return checkGrid[pos[0]][pos[1]] != 0
    except IndexError:
            return True

    
def fill(position,startCol,fillCol,borderCol):
    
    queue = set ([(position[0],position[1])])
    
    ns = [[0,1],[0,-1]]
    nsew = ns + [[1,0],[-1,0]]    
    area,per = 0,0    
    dic = {}    
    keys = set()
    borderDic = {}
    
    global checkGrid
    checkGrid = makeCheckGrid(startCol)
        
    while len(queue) > 0:
        
        n = queue.pop()               
        w,e = [n[0]-1,n[1]],[n[0],n[1]]
        wx,ex = n[0]-1,n[0]
        
        while not visited(e):
            e[0] += 1
            ex += 1
 
        while not visited(w):                    
            w[0] -= 1
            wx -= 1
    
        for x in range(wx+1,ex):
            
            N = [x,n[1]]
             
            if not visited(N):
            
                area += 1
                
                try:
                    dic[ n[1] ].add(x)
                except KeyError:
                    dic [n[1]] = set([x])
                    
                checkGrid[N[0]][N[1]] = 2
                
                setP(N,fillCol)
                
                                
                for dir in nsew:
                
                    next = [N[0] + dir[0],N[1] + dir[1]]
                
                    if not visited(next):
                        queue.add((next[0],next[1]))
                        
                    elif not inGrid(next) or checkGrid[next[0]][next[1]] == 1 :

                        try:
                            borderDic[N[1]].add(N[0])
                        except KeyError:                            
                            borderDic [N[1]] = set([N[0]])

    
    for y in borderDic:
        for x in borderDic[y]:
                per += 1
                area -= 1
                setP([x,y],borderCol)

    return area,per;
    
        
   
def getP(position):
    
    if inGrid(position):
        return img[position[1]][position[0]]
    else:
        return False
       
def setP(pos,c):

    try:
        if pos[0] < 0 or pos[1] < 0:
            return
    
        img[pos[1]][pos[0]] = c

    except IndexError:
        return

   
def inGrid(pos):
   
    try:
        img[pos[1]][pos[0]]

    except IndexError:
        return False
        
    else:
    
        if pos[0] < 0 or pos[1] < 0:
            return False
        else:
            return True










