from random     import randint

nAcc = 0
dec0 = False

def getDirV(vx, vy):
    dx = 0
    dy = 0
    
    if vx > 0: dx = 1
    if vx < 0: dx = -1
    if vy > 0: dy = 1
    if vy < 0: dy = -1
    
    return dx, dy
    

def decellera(vx, vy):
    ax = 0
    ay = 0
    if vx > 1:
        ax = -1
    if vy > 1:
        ay = -1
    if vx < -1:
        ax = 1
    if vy < -1:
        ay = 1
    return ax, ay
    
def skipBuche(griglia_corrente, x, y, vx, vy):
    global nAcc
    dvx, dvy = getDirV(vx, vy)
    
    toAcc = False
    
    if griglia_corrente[y+dvy][x+dvx] == 'O' or (griglia_corrente[y+3*dvy][x+3*dvx] == 'O' and griglia_corrente[y+4*dvy][x+4*dvx] == 'O'):
        toAcc = True
    
    if toAcc:
        if nAcc < 2:
            nAcc += 1
            return dvx, dvy
    else:
        if nAcc > 0:
            nAcc -= 1
            dex, dey = decellera(vx, vy)
            
            if griglia_corrente[y+vy+dey][x+vx+dex] == 'O':
                dec0 = True
                return 0,0
            dec0 = False
            return dex, dey 
    return 0, 0

def countFreeSpaces(griglia_corrente, x, y, dx, dy, seBuche = True):
    fSpaces = 0
    
    posC = ' |'
    
    if seBuche:
        posC = ' O|'
    
    while griglia_corrente[y+dy][x+dx] in posC:
        fSpaces += 1
        y += dy
        x += dx
        
    return fSpaces

def getBestDir(griglia_corrente, x, y, vx, vy, verso):
    dispDirs = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    
    dirV = getDirV(vx, vy)
    
    indexV = dispDirs.index(dirV)
    if verso == 1:
        dispDirs = [dispDirs[indexV]]+[dispDirs[indexV-1]]+[dispDirs[(indexV+1)%8]]+[dispDirs[indexV-2]]
    else:
        dispDirs = [dispDirs[indexV]]+[dispDirs[indexV-1]]+[dispDirs[(indexV+1)%8]]+[dispDirs[(indexV+2)%8]]
    
    freeDirs = []
    freeSpaces = []
    for dx, dy in dispDirs:
        spaces = countFreeSpaces(griglia_corrente, x, y, dx, dy)
        if spaces > 0:
            freeDirs += [(dx, dy)]
            freeSpaces += [spaces]
            
    maxSp = max(freeSpaces)
    
    maxFreeDirs = []
    for i in range(len(freeDirs)):
        if maxSp == freeSpaces[i]:
            maxFreeDirs += [freeDirs[i]]
    
    return maxFreeDirs[0]
    
def resetV(vx, vy):
    if vx > 1:
        if vy > 0:
            return -1,-1
        else:
            return -1,0
    if vy > 1:
        if vx > 0:
            return -1,-1
        else:
            return 0,-1
    if vx < -1:
        if vy < 0:
            return 1,1
        else:
            return 1,0
    if vy < -1:
        if vx < 0:
            return 1,1
        else:
            return 0,1
    return 0,0

def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    if (vx, vy) == (0,0):
        return verso, 0
    
    global nAcc, dec0
    
    if laps > 0:
        dec0 = False
        nAcc = 0
        dex, dey = decellera(vx, vy)
        if (0,0) != (dex, dey):
            return dex, dey
        return -vx, -vy
    
    ax, ay = skipBuche(griglia_corrente, x, y, vx, vy)
    cChar = griglia_corrente[y + 3*ay][x + 3*ax]
    ccChar = griglia_corrente[y + 4*ay][x + 4*ax]
    if ((ax, ay) == (0, 0) or (cChar not in ' |' and ccChar != 'O')) and not dec0:
        dx, dy = getBestDir(griglia_corrente, x, y, vx, vy, verso)
        rvx, rvy = resetV(vx, vy)
        if (0,0) != (rvx, rvy):
            return rvx, rvy
        return dx - vx, dy - vy
    
    return ax, ay