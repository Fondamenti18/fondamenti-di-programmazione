from immagini import *
 
directions = [[1,0],[0,1],[-1,0],[0,-1]]
currentDir = 0
grid = []

 
def cammino(fname,  fname1):
    global grid
    path = ""
    imgGrid = load(fname)
    pos=[0,0]
   
    grid = [[0 for y in range(15)]for x in range(15)]
   
    for x in range(15):
        for y in range(15):
           
            c = imgGrid[x*40][y*40]
           
            if c == (255,0,0):
                grid[y][x] = 1
    
    loop = True
    
    i = 0
    count = 0
    
    while count != 4:
    
        dir = directions[i]
        found = False
        
        if isFree(pos[0] + dir[0],pos[1] + dir[1]):
            found = True
            grid[pos[0]][pos[1]] = 2
            pos[0] += dir[0]
            pos[1] += dir[1]
            count = 0
            path += str(i)
        else:
            count += 1
            i += 1
            if i > 3:
                i = 0
            
    grid[pos[0]][pos[1]] = 3
            
    #for y in range(15):
    #    for x in range(15):
    #        print(grid[x][y],end = "")
    #    print()
           
    #print(path)
    
    dic = { 2 : (0,255,0), 3 : (0,0,255) }
    
    for y in range(15):
        for x in range(15):
            if grid[x][y] > 1:
                for xx in range(40):
                    for yy in range(40):
                        imgGrid[y * 40 + yy][x * 40 + xx] = dic[grid[x][y]]
                        
                        
    save(imgGrid,fname1)
    return path
    
    
def isFree(x,y):
    if x >= 0 and y >=0 and x < 15 and y < 15:
        if grid[x][y] != 0:
            return False
        else:
            return True
    return False
    
    
#cammino("I2.png","test2.png")
    