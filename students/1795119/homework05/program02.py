from copy import deepcopy

def horizontal(griglia, myPos, verso):
    buca = None
    if verso:
        for ind, x in enumerate(griglia[myPos[1]][myPos[0]:]):
            if x == "O" and buca == None:
                buca = ind
            elif x == "|":
                buca = [buca, ind+1]
            elif x in "#AB":
                return ind-1, buca
    else:
        rev = reversed(griglia[myPos[1]][:myPos[0]])
        for ind, x in enumerate(rev):
            if x == "O" and buca == None:
                buca = ind
            elif x == "|":
                buca = [buca, ind+1]
            elif x in "#AB":
                return ind, buca

def vertical(griglia, myPos, verso):
    buca = None
    if verso:
        ls = [x[myPos[0]] for x in griglia[:myPos[1]]]
        for ind, x in enumerate(reversed(ls)):
            if x == "O" and buca == None:
                buca = ind
            elif x == "|":
                buca = [buca, ind+1]
            elif x in "#AB":
                return ind, buca
    else:
        ls = [x[myPos[0]] for x in griglia[myPos[1]:]]
        for ind, x in enumerate(ls):
            if x == "O" and buca == None:
                buca = ind
            elif x == "|":
                buca = [buca, ind+1]
            elif x in "#AB":
                return ind-1, buca

def diagonal_one(griglia, myPos, verso):
    count = 0
    buca = None
    x = griglia[myPos[1]][myPos[0]]
    if verso:
        while x not in "#AB":
            if x == "O" and buca == None:
                buca = count-1
            count += 1
            x = griglia[myPos[1]+count][myPos[0]+count]
        return count-1, buca
    else:
        while x not in "#AB":
            if x == "O" and buca == None:
                buca = count-1
            count += 1
            x = griglia[myPos[1]+count][myPos[0]-count]
        return count-1, buca

def diagonal_two(griglia, myPos, verso):
    count = 0
    buca = None
    x = griglia[myPos[1]][myPos[0]]
    if verso:
        while x not in "#AB":
            if x == "O" and buca == None:
                buca = count-1
            count += 1
            x = griglia[myPos[1]-count][myPos[0]+count]
        return count-1, buca
    else:
        while x not in "#AB":
            if x == "O" and buca == None:
                buca = count-1
            count += 1
            x = griglia[myPos[1]-count][myPos[0]-count]
        return count-1, buca

def sensoreAvanti(griglia, myPos, velx, vely):
    if velx == 0 and vely == 0:
        global car_dir
        return sensoreAvanti(griglia, myPos, car_dir[0], car_dir[1])
    elif vely == 0:
        if velx > 0:
            return horizontal(griglia, myPos, True)
        return horizontal(griglia, myPos, False)
    elif velx == 0:
        if vely > 0:
            return vertical(griglia, myPos, False)
        return vertical(griglia, myPos, True)
    elif vely > 0:
        if velx > 0:
            return diagonal_one(griglia, myPos, True)
        return diagonal_one(griglia, myPos, False)
    elif vely < 0:
        if velx > 0:
            return diagonal_two(griglia, myPos, True)
        return diagonal_two(griglia, myPos, False)

def sensoreAv_Destra(griglia, myPos, velx, vely):
    if velx == 0 and vely == 0:
        global car_dir
        return sensoreAv_Destra(griglia, myPos, car_dir[0], car_dir[1])
    elif vely == 0:
        if velx > 0:
            return diagonal_one(griglia, myPos, True)
        return diagonal_two(griglia, myPos, False)
    elif velx == 0:
        if vely > 0:
            return diagonal_one(griglia, myPos, False)
        return diagonal_two(griglia, myPos, True)
    elif vely > 0:
        if velx > 0:
            return vertical(griglia, myPos, False)
        return horizontal(griglia, myPos, False)
    elif vely < 0:
        if velx > 0:
            return horizontal(griglia, myPos, True)
        return vertical(griglia, myPos, True)

def sensoreAv_Sinistra(griglia, myPos, velx, vely):
    if velx == 0 and vely == 0:
        global car_dir
        return sensoreAv_Sinistra(griglia, myPos, car_dir[0], car_dir[1])
    elif vely == 0:
        if velx > 0:
            return diagonal_two(griglia, myPos, True)
        return diagonal_one(griglia, myPos, False)
    elif velx == 0:
        if vely > 0:
            return diagonal_one(griglia, myPos, True)
        return diagonal_two(griglia, myPos, False)
    elif vely > 0:
        if velx > 0:
            return horizontal(griglia, myPos, True)
        return vertical(griglia, myPos, False)
    elif vely < 0:
        if velx > 0:
            return vertical(griglia, myPos, True)
        return horizontal(griglia, myPos, False)

def sensoreDestra(griglia, myPos, velx, vely):
    if velx == 0 and vely == 0:
        global car_dir
        return sensoreDestra(griglia, myPos, car_dir[0], car_dir[1])
    elif vely == 0:
        if velx > 0:
            return vertical(griglia, myPos, False)
        return vertical(griglia, myPos, True)
    elif velx == 0:
        if vely > 0:
            return horizontal(griglia, myPos, False)
        return horizontal(griglia, myPos, True)
    elif vely > 0:
        if velx > 0:
            return diagonal_one(griglia, myPos, False)
        return diagonal_two(griglia, myPos, False)
    elif vely < 0:
        if velx > 0:
            return diagonal_one(griglia, myPos, True)
        return diagonal_two(griglia, myPos, True)

def sensoreSinistra(griglia, myPos, velx, vely):
    if velx == 0 and vely == 0:
        global car_dir
        return sensoreSinistra(griglia, myPos, car_dir[0], car_dir[1])
    elif vely == 0:
        if velx > 0:
            return vertical(griglia, myPos, True)
        return vertical(griglia, myPos, False)
    elif velx == 0:
        if vely > 0:
            return horizontal(griglia, myPos, True)
        return horizontal(griglia, myPos, False)
    elif vely > 0:
        if velx > 0:
            return diagonal_two(griglia, myPos, True)
        return diagonal_one(griglia, myPos, True)
    elif vely < 0:
        if velx > 0:
            return diagonal_two(griglia, myPos, False)
        return diagonal_one(griglia, myPos, False)

def goAv_Destra(velx, vely):
    if velx == 0 and vely == 0:
        global car_dir
        return goAv_Destra(car_dir[0], car_dir[1])
    elif vely == 0:
        if velx > 0:
            return 1, 1
        return -1, -1
    elif velx == 0:
        if vely > 0:
            return -1, 1
        return 1, -1
    elif vely > 0:
        if velx > 0:
            return 0, 1
        return -1, 0
    elif vely < 0:
        if velx > 0:
            return 1, 0
        return 0, -1

def goAv_Sinistra(velx, vely):
    if velx == 0 and vely == 0:
        global car_dir
        return goAv_Sinistra(car_dir[0], car_dir[1])
    elif vely == 0:
        if velx > 0:
            return 1, -1
        return -1, 1
    elif velx == 0:
        if vely > 0:
            return 1, 1
        return -1, -1
    elif vely > 0:
        if velx > 0:
            return 1, 0
        return 0, 1
    elif vely < 0:
        if velx > 0:
            return 0, -1
        return -1, 0

def goDestra(velx, vely):
    if velx == 0 and vely == 0:
        global car_dir
        return goDestra(car_dir[0], car_dir[1])
    elif vely == 0:
        if velx > 0:
            return 0, 1
        return 0, -1
    elif velx == 0:
        if vely > 0:
            return -1, 0
        return 1, 0
    elif vely > 0:
        if velx > 0:
            return 1, -1
        return -1, -1
    elif vely < 0:
        if velx > 0:
            return 1, 1
        return 1, -1

def goSinistra(velx, vely):
    if velx == 0 and vely == 0:
        global car_dir
        return goSinistra(car_dir[0], car_dir[1])
    elif vely == 0:
        if velx > 0:
            return 0, -1
        return 0, 1
    elif velx == 0:
        if vely > 0:
            return 1, 0
        return -1, 0
    elif vely > 0:
        if velx > 0:
            return -1, 1
        return 1, 1
    elif vely < 0:
        if velx > 0:
            return -1, -1
        return -1, 1

def frena(velx, vely):
    if velx == 0 and vely == 0:
        return 0, 0
    elif vely == 0:
        if velx > 0:
            return -1, 0
        return 1, 0
    elif velx == 0:
        if vely > 0:
            return 0, -1
        return 0, 1
    elif vely > 0:
        if velx > 0:
            return -1, -1
        return 1, -1
    elif vely < 0:
        if velx > 0:
            return -1, 1
        return 1, 1

def goAvanti(verso, velx, vely):
    if velx == 0 and vely == 0:
        global car_dir
        if car_dir == (0, 0):
            return verso, 0
        return goAvanti(verso, car_dir[0], car_dir[1])
    elif vely == 0:
        if velx > 0:
            return 1, 0
        return -1, 0
    elif velx == 0:
        if vely > 0:
            return 0, 1
        return 0, -1
    elif vely > 0:
        if velx > 0:
            return 1, 1
        return -1, 1
    elif vely < 0:
        if velx > 0:
            return 1, -1
        return -1, -1

def distanzaFrenata(n):
    count = 0
    if n < 0:
        n *= -1
    for x in range(n+1):
        count += x
    return count

def maggiore(x, y):
    if x < 0:
        x *= -1
    if y < 0:
        y *= -1
    if x > y:
        return x
    return y

def sensoreFrenata(velx, vely, prox, k=1):
    if velx == 0 and vely == 0:
        return -1
    elif vely == 0:
        if velx > 0:
            fren_fut = distanzaFrenata(velx+k)
            prox_fut = prox - (velx+k)
        else:
            fren_fut = distanzaFrenata(velx-k)
            prox_fut = prox + (velx-k)
    elif velx == 0:
        if vely > 0:
            fren_fut = distanzaFrenata(vely+k)
            prox_fut = prox - (vely+k)
        else:
            fren_fut = distanzaFrenata(vely-k)
            prox_fut = prox + (vely-k)
    elif vely > 0:
        vel = maggiore(velx, vely)
        fren_fut = distanzaFrenata(vel+k)
        prox_fut = prox - (vel+k)
    elif vely < 0:
        vel = maggiore(velx, vely)
        fren_fut = distanzaFrenata(vel+k)
        prox_fut = prox - (vel+k)
    if prox_fut - fren_fut < 0:
        return frena(velx, vely)
    return -1

def limit_vel(velx, vely):
    if velx<1 and velx>-1 and vely<1 and vely>-1:
        return True
    return False

def isTrack(griglia, pos):
    if griglia[pos[1]][pos[0]] not in "#OAB":
        return True
    return False

def saltaBuca(griglia, velx, vely, myPos):
    if velx == 0 and vely == 0:
        return False
        global car_dir
        return saltaBuca(griglia, car_dir[0], car_dir[1], myPos)
    elif vely == 0:
        if velx > 0:
            if isTrack(griglia, (myPos[0]+velx+1, myPos[1]+vely)):
                return 1, 0
            elif isTrack(griglia, (myPos[0]+velx, myPos[1]+vely)):
                return 0, 0
            return False
        if isTrack(griglia, (myPos[0]+velx-1, myPos[1]+vely)):
            return -1, 0
        elif isTrack(griglia, (myPos[0]+velx, myPos[1]+vely)):
            return 0, 0
        return False
    elif velx == 0:
        if vely > 0:
            if isTrack(griglia, (myPos[0]+velx, myPos[1]+vely+1)):
                return 0, 1
            elif isTrack(griglia, (myPos[0]+velx, myPos[1]+vely)):
                return 0, 0
            return False
        if isTrack(griglia, (myPos[0]+velx, myPos[1]+vely-1)):
            return 0, -1
        elif isTrack(griglia, (myPos[0]+velx, myPos[1]+vely)):
            return 0, 0
        return False
    elif vely > 0:
        if velx > 0:
            if isTrack(griglia, (myPos[0]+velx+1, myPos[1]+vely+1)):
                return 1, 1
            elif isTrack(griglia, (myPos[0]+velx, myPos[1]+vely)):
                return 0, 0
            return False
        if isTrack(griglia, (myPos[0]+velx-1, myPos[1]+vely+1)):
            return -1, 1
        elif isTrack(griglia, (myPos[0]+velx, myPos[1]+vely)):
            return 0, 0
        return False
    elif vely < 0:
        if velx > 0:
            if isTrack(griglia, (myPos[0]+velx+1, myPos[1]+vely-1)):
                return 1, -1
            elif isTrack(griglia, (myPos[0]+velx, myPos[1]+vely)):
                return 0, 0
            return False
        if isTrack(griglia, (myPos[0]+velx-1, myPos[1]+vely-1)):
            return -1, -1
        elif isTrack(griglia, (myPos[0]+velx, myPos[1]+vely)):
            return 0, 0
        return False

def stopTraguardo(tr, vx, vy, verso, ric=True):
    global traguardo
    if vx == 0 and vy == 0:
        return -1
    if vy == 0:
        if vx > 0:
            f = distanzaFrenata(vx+1)
            tr -= vx+1
        else:
            f = distanzaFrenata(vx-1)
            tr += vx-1
    elif vx == 0:
        if vy > 0:
            f = distanzaFrenata(vy+1)
            tr -= vy+1
        else:
            f = distanzaFrenata(vy-1)
            tr += vy-1
    if f == tr:
        return 0, 0
    elif f > tr:
        return frena(vx, vy)
    else:
        if vy == 0:
            tr -= abs(vx)
            if vx > 0:
                vx +=1
            else:
                vx -=1
        else:
            tr -= abs(vy)
            if vy > 0:
                vy += 1
            else:
                vy -= 1
        if ric:
            stop = stopTraguardo(tr, vx, vy, verso, False)
            if stop == (0, 0):
                return goAvanti(verso, vx, vy)
        return -1

def proxGriglia(griglia, vx, vy, myPos, velx, vely):
    griglia_fut = deepcopy(griglia)
    griglia_fut[myPos[1]][myPos[0]] = " "
    vx += velx
    vy += vely
    newPos = (myPos[0]+vx, myPos[1]+vy)
    griglia_fut[newPos[1]][newPos[0]] = "X"
    return griglia_fut

car_dir = (0, 0)

#def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty): # vecchia versione
def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    '''inserite qui il vostro codice'''
    if x == startx-verso:
        return verso*-1, 0
    myPos = (x, y)  # mia posizione
    global car_dir
    if x == startx and y == starty:
        return goAvanti(verso, vx, vy)
    if vx == 0 and vy == 0:
        if car_dir == (0, 0):
            vx = verso
    else:
        car_dir = (vx, vy)
    prox, buca = sensoreAvanti(griglia_corrente, myPos, vx, vy) # prossimo ostacolo nella griglia e sua distanza
    prox_av_dx, buca_adx = sensoreAv_Destra(griglia_corrente, myPos, vx, vy)
    prox_av_sx, buca_asx = sensoreAv_Sinistra(griglia_corrente, myPos, vx, vy)
    prox_sx, buca_sx = sensoreSinistra(griglia_corrente, myPos, vx, vy)
    prox_dx, buca_dx = sensoreDestra(griglia_corrente, myPos, vx, vy)
    # FRENATA
    sf = sensoreFrenata(vx, vy, prox)
    if sf != -1:
        gr_fut = proxGriglia(griglia_corrente, vx, vy, myPos, sf[0], sf[1])
        prox2, buca2 = sensoreAvanti(gr_fut, myPos, vx, vy)
        if buca2 != None:
            sb = saltaBuca(griglia_corrente, vx+sf[0], vy+sf[1], myPos)
            if vx+sf[0] != 0 or vy+sf[1] != 0:
                if sb == (0, 0) or sb == False:
                    sf1 = sensoreFrenata(vx, vy, prox, k=0)
                    if sf1 == -1:
                        return sf
            else:
                return 0, 0
        return sf
    # BUCA
    if type(buca) is list:
        tr = buca[1]
        buca = buca[0]
        stop = stopTraguardo(tr, vx, vy, verso)
        if stop != -1:
            return stop
    if buca != None:
        sb = saltaBuca(griglia_corrente, vx, vy, myPos)
        if sb != False:
            return sb
    # CURVA
    if prox > 2:
        return goAvanti(verso, vx, vy)
    if prox_av_dx >= prox_av_sx and prox_av_dx > prox:
        if limit_vel(vx, vy):
            return goAv_Destra(vx, vy)
    if prox_av_sx >= prox_av_dx and prox_av_sx > prox:
        if limit_vel(vx, vy):
            return goAv_Sinistra(vx, vy)
    if prox_dx > prox and prox_dx >= prox_sx: #and prox_dx >= prox_av_dx and prox_dx >= prox_av_sx:
        if limit_vel(vx, vy):
            return goDestra(vx, vy)
    if prox_sx > prox and prox_sx >= prox_dx: #and prox_sx >= prox_av_dx and prox_sx >= prox_av_sx:
        if limit_vel(vx, vy):
            return goSinistra(vx, vy)
    # AVANTI
    return goAvanti(verso, vx, vy)
