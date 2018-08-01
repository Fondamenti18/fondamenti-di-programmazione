#you're a bunch of stinking cunts,fuck you


from random import randint,getrandbits

w,h = 0,0
grid,visited = None,None
targetLine =[]
maxSpeed,topSpeed = 0,15
lineTop,lineBottom,lineX,startDir = 0,0,0,0
pointers = {}
badPointers = set ()
toAvoid = []
lastLapCount = 0

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty,laps):

   # print('cunt')

    global grid,startDir,maxSpeed,yourCar,lastLapCount,pointers,topSpeed,visited,toAvoid
    
    reset = False
    
    if (x == startx and y == starty or grid == None):
    
        #print('\n','\n','    RESET','\n','\n')
        startDir = verso
        visited = None
        
        GenerateGrid(startx,starty,verso,griglia_corrente)
        UpdateField()
        DebugGrid()
        reset = True
         
    yourCar = car

    if yourCar != 'X':
        FindPlayers(griglia_precedente,griglia_corrente)
    #else:
    #    toAvoid = []
            
    avoid = (x + vx,y + vy) in toAvoid
    
    test = 15
        
    while (x,y,vx,vy) not in pointers or laps != lastLapCount or avoid or reset:
    
        maxSpeed = topSpeed
        lastLapCount = laps
        
        if laps == 0:
            CalculatePath(x,y,100,vx,vy,avoid)
        else:
            if abs(vx) + abs(vy) != 0:
                CalculatePath(x,y,100,vx,vy,True)
            else:
                #print ('\n','RETURNING 0 0','\n',)
                return 0,0
                
        avoid = False
        reset = False
        
        test -= 1
        if test == 0:
            break
    
    #if pointers != None:
        #print ('\n','POINTERS:',len(pointers),'\n',)
    
    try:
        return pointers[(x,y,vx,vy)]
    except (KeyError):
        #print ('\n','RETURNING 0 0','\n',)
        return 0,0
    
def FindPlayers(oldGrid,newGrid):
    
    global yourCar,toAvoid,w,h
    
    toAvoid = []
    otherPlayers = {}
    
    for x in range (w):
        for y in range (h):
            char = oldGrid[y][x]
            if char.isalpha() and char not in [yourCar,'O']:
                otherPlayers[char] = [(x,y)]
                
    for x in range (w):
        for y in range (h):
            char = newGrid[y][x]
            if char.isalpha() and char not in [yourCar,'O']:
                otherPlayers[char] += [(x,y)]
                
    for key in otherPlayers:
        list = otherPlayers[key]

        vx = list[1][0] - list[0][0]
        vy = list[1][1] - list[0][1]
        
        X,Y = list[1][0] + vx,list[1][1] + vy
        
        toAvoid += AvoidAround(X,Y,yourCar)
        
            
def AvoidAround(x,y,car):
    
    avoid = []
    
    for xx in range(-1,2):
        for yy in range(-1,2):
            if InGrid(x+xx,y+yy):
                avoid.append((x+xx, y+yy, grid[x+xx][y+yy].value,car))
    
    avoid.sort(key = lambda x: x[2])
    
    for i in range(len(avoid)):
        avoid[i] = (avoid[i][0],avoid[i][1])
    
    return avoid
    
def CalculatePath(x,y,startDepth,vx,vy,slowdown):
    
    global maxSpeed,toAvoid,badPointers,pointers
    
    startVx,startVy,startX,startY = vx,vy,x,y
    depth = 0
    fails = 0
    badPointers = set()
    lastinfo = None
    lastVarX,lastVary = 0,0
    
    maxSpeed = topSpeed
    
    while depth != startDepth:
        
        avoid = False
        
        dir = []
        foundEnd = False
        
        for xx in range(-1,2):
            for yy in range(-1,2):
                
                X = x + vx + xx
                Y = y + vy + yy
                
                avoid = ((X,Y) in toAvoid) and (depth <= 0)
                
                if (InGrid(X,Y)) and (x,y,vx,vy,xx,yy) not in badPointers and not avoid:
                    
                    vec = (vx + xx)** 2 + (vy + yy)** 2
                    
                    if slowdown and vec != 0 and vec > vx ** 2 + vy ** 2:
                        continue
                    
                    if LegitEnd(x,y,X,Y) and grid[X][Y].char == ' ' and vec <= maxSpeed ** 2 :
                        
                        newPointer = (grid[X][Y].value,xx,yy)
                        dir.append(newPointer)
        
        if len(dir) != 0:
            
          #  if not avoid:
            if not slowdown:
                dir.sort( key = lambda x: x[0] )
            
            pointers[(x,y,vx,vy)] = (dir[0][1],dir[0][2])
            
            if foundEnd:
                break
            
            lastinfo = (x,y,vx,vy,dir[0][1],dir[0][2])
            
            vx += dir[0][1]
            vy += dir[0][2]
            
            x += vx
            y += vy
            
            depth += 1
            
            if CrossedEnd(x,y,x+vx,y+vy) or slowdown and vx == 0 and vy == 0:
                break
            
            if maxSpeed < topSpeed:
               maxSpeed += 1

        else:
            
            fails += 1
            
            if not fails % 5 and maxSpeed > 0:
                maxSpeed -= 1
                
            if avoid:
                slowdown = True
                
            if avoid and not fails % 10 and len(toAvoid) > 2:
               # print('AVOID',yourCar)
                #slowdown = True
                toAvoid.pop()


            if fails > 20000:
                pointers[(startX,startY,startVx,startVy)] = (0,0)
                return 
            
            pointers = {}
            badPointers.add( lastinfo )
            
            x,y,vx,vy = startX,startY,startVx,startVy
            depth = 0
            
 

def UpdateField():
    
    global targetLine,grid,visited
   
    if visited == None:
        visited = [[False for y in range(len(grid[0]))] for x in range (len(grid))]
    else:
        for row in visited:
            for cell in row:
                cell = False
        
    frontier = targetLine[:]
    newFrontier = []
    
    for cell in frontier:
        visited[cell.x][cell.y] = True
    
    while True:
        
        if len(frontier) > 0:
            current = frontier.pop()

            for n in current.neighbours:
                if n != None:
                    if not visited[n.x][n.y]:
                        
                        if n.char == 'O':
                            n.value += 1
                                
                        n.value += current.value + 2
                        
                        newFrontier.append(n)
                    visited[n.x][n.y] = True
                
        else:
            if len(newFrontier) == 0:
                break
            frontier = newFrontier[:]
            newFrontier = []

def GenerateGrid(x,y,dir,currentGrid):
    
    global w,h,grid,targetCell,startFrontier,lineBottom,lineTop,lineX,targetLine
    
    
    targetLine = []
    w = len(currentGrid[0])
    h = len(currentGrid)
    grid = [[Node(x,y,currentGrid[y][x]) for y in range(h)] for x in range(w)]
    
    for row in grid:
        for cell in row:
            if cell.char != '#':
                cell.GetNeighbours()
                
                if cell.char == '|':
                    cell.neighbours[dir + 1] = None
                    targetLine.append(cell)

    targetLine.sort(key = lambda x: x.y)
    
    lineTop = targetLine[0].y
    lineBottom = targetLine[-1].y
    lineX = targetLine[0].x
    
def DebugGrid():
    
    global grid,w,h
    debugPrint = []
    vectorRange = ['0','1','2','3','4','5','6','7','8','9']
    
    for y in range (h):
        debugLine = ""
        
        for x in range (w):
            if grid[x][y].value != 0:
                debugLine += str(grid[x][y].value).ljust(5)
            else:
                debugLine += ' ' * 5

        debugLine += '\n'
        debugPrint.append(debugLine)
        
    with open("debug.txt",'w') as f:
        for line in debugPrint:
            f.write(line)
            
def InGrid(x,y):
    
    if( x < 0 or y < 0 or x >= w or y >= h):
        return False
    if grid[x][y].char != '#':
        return True
    return False
    
def LegitEnd(startX,startY,endX,endY):
    
    if Between(lineTop,endY,lineBottom) and Between(startX,lineX,endX):
        dx = endX - startX
        
        if dx > 0 and startDir > 0 or dx < 0 and startDir < 0:
            return True
        return False
    return True
    
def CrossedEnd(startX,startY,endX,endY):
        
    #print(Between(lineTop,endY,lineBottom),lineTop,endY,lineBottom)
    if Between(lineTop,endY,lineBottom) and Between(startX,lineX,endX):
        dx = endX - startX
        
        if dx > 0 and startDir > 0 or dx < 0 and startDir < 0:
            crossedEnd = True
            return True
            
    return False
    
def Between(a,c,b):
    return abs(a - c) + abs(b - c) == abs( a - b )

class Node:
    
    neighbourCoord = [ [-1,0],[0,1],[1,0],[0,-1]]
    
    def __init__(self,x,y,char):
    
        self.x = x ;
        self.y = y ;
        self.neighbours = [None for i in range(4)]
        self.value = 0;
        self.char = char
        
    def GetNeighbours(self):
        
        global grid
        
        for i in range(4):
            n = self.neighbourCoord[i]
            
            if (InGrid(self.x + n[0],self.y + n[1])):
            
                neighbour = grid[self.x + n[0]][self.y + n[1]]
                
                if (neighbour.char != '|'):
                    n = grid[self.x + n[0]][self.y + n[1]]
                    self.neighbours[i] = n

