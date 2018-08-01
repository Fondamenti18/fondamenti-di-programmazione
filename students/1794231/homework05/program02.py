from random     import randint
from math       import fabs
def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, giri):
    accx=0
    accy=0
    if x==startx and y==starty and griglia_corrente==griglia_precedente and vx==0 and vy==0:
        global dati
        dati=[[0,0],[y,x], 0, 0]
        if starty>(len(griglia_corrente)/2): dati[0][0]=-1
        else: dati[0][0]=1
        dati[0][1]=verso
    griglia_corrente=collis(griglia_corrente, griglia_precedente, car)
    flag=0
    if dati[1][1]>startx and x<startx:
        dati[0][0]=dati[0][0]*-1
    if dati[1][1]<startx and x>startx:
        dati[0][0]=dati[0][0]*-1
    if y>=(len(griglia_corrente)/2)+2 and dati[1][0]<(len(griglia_corrente)/2)+2: dati[0][1]=dati[0][1]*-1
    elif y<=(len(griglia_corrente)/2)+2 and dati[1][0]>(len(griglia_corrente)/2)+2: dati[0][1]=dati[0][1]*-1
    frenatax=0
    if vx>0:
        frenatax+=((vx*2)+1)
        for frenate in range(vx): frenatax+=(frenate)
    else:
        for frenate in range(0, vx, -1): frenatax+=(frenate)
        frenatax=(frenatax+(vx*2)-1)*-1
    spaziox=0
    f=0
    if dati[0][1]==-1:
        for xfuture in range(x, -1, -1):
            if griglia_corrente[y][xfuture]=='#': break
            elif griglia_corrente[y][xfuture]=='O':
                spaziox+=1
                if f!=-1: f+=1
            elif griglia_corrente[y][xfuture]=='|':
                dati[2]=1
                flag=1
                if f>0:
                    dati[3]=f
                spaziox+=6
                break
            else:
                if f!=0: f=-1
                spaziox+=1
    else:
        for xfuture in range(x, len(griglia_corrente[0]), 1):
            if griglia_corrente[y][xfuture]=='#': break
            elif griglia_corrente[y][xfuture]=='O':
                if f!=-1: f+=1
                spaziox+=1
            elif griglia_corrente[y][xfuture]=='|':
                dati[2]=1
                flag=1
                if f>0:
                    dati[3]=f
                spaziox+=6
                break
            else:
                if f!=0: f=-1
                spaziox+=1
    if dati[2]==1 and flag==0:
        accx=dati[0][1]*-1
    elif dati[3]!=0:
        if int(fabs(vx))>dati[3]+1:
            accx=dati[0][1]*-1
        if int(fabs(vx))<dati[3]+1:
            accx=dati[0][1]
        if int(fabs(vx))==dati[3]+1:
            if spaziox%(dati[3]+1)!=0:
                accx=dati[0][1]
            else:
                accx=0
    else:
        if spaziox>frenatax:
            accx=dati[0][1]
            if griglia_corrente[y+vy][x+vx+accx]=='O':
                accx=0
            if griglia_corrente[y+vy][x+vx+accx]=='O':
                accx=dati[0][1]*-1
            if griglia_corrente[y+vy][x+vx+accx]=='O':
                accx=dati[0][1]
        elif spaziox==frenatax:
            accx=0
            if griglia_corrente[y+vy][x+vx+accx]=='O':
                accx=dati[0][1]*-1
            if griglia_corrente[y+vy][x+vx+accx]=='O':
                accx=0
        else:
            accx=dati[0][1]*-1
    frenatay=0
    if vy>0:
        if dati[0][0]>0:
            frenatay+=((vy*2)+1)
            for frenate in range(vy): frenatay+=(frenate)
    else:
        for frenate in range(0, vy, -1): frenatay+=(frenate)
        frenatay=(frenatay+(vy*2)-1)*-1
    spazioy=0
    if dati[0][0]==-1:
        for yfuture in range(y, -1, -1):
            if griglia_corrente[yfuture][vx+x+accx]=='#': break
            else: spazioy+=1
    else:
        for yfuture in range(y, len(griglia_corrente), 1):
            if griglia_corrente[yfuture][vx+x+accx]=='#': break
            else: spazioy+=1
    if spazioy>frenatay:
        accy=dati[0][0]
        try:
            if griglia_corrente[y+vy+accy][x+vx+accx]=='O' or griglia_corrente[y+(vy+accy)*2-dati[0][0]][x+(vx+accx)*2-dati[0][1]]=='O' or griglia_corrente[y+(vy+accy)*2-dati[0][0]][x+(vx+accx)*2-dati[0][1]]=='#':
                accy=0
        except: pass
        if griglia_corrente[y+vy+accy][x+vx+accx]=='O':
            accy=dati[0][0]*-1
        if griglia_corrente[y+vy+accy][x+vx+accx]=='O':
            accy=dati[0][0]
    elif spazioy==frenatay:
        accy=0
        if griglia_corrente[y+vy+accy][x+vx+accx]=='O':
            accy=dati[0][0]*-1
        if griglia_corrente[y+vy+accy][x+vx+accx]=='O':
            accy=0
    else:
        accy=dati[0][0]*-1
        if griglia_corrente[y+vy+accy][x+vx+accx]=='O':
            accy=0
        if griglia_corrente[y+vy+accy][x+vx+accx]=='O':
            accy=dati[0][0]
        if griglia_corrente[y+vy+accy][x+vx+accx]=='O':
            accy=dati[0][0]*-1
    dati[1]=[y,x]
    try:
        if griglia_corrente[(vy+accy)*2+y-dati[0][0]][(vx+accx)*2+x-dati[0][1]]=='#' and dati[0]==[1,1]:
            if accx==0:
                accx= 1
    except: pass
    return(accx, accy)
def collis(griglia_corrente, griglia_precedente, car):
    if car!='X':
        encor=[0,0]
        enpre=[0,0]
        en=[0,0]
        for ny in range(len(griglia_corrente)):
            for nx in range(len(griglia_corrente[ny])):
                if car=='A':
                    if griglia_corrente[ny][nx]=='B':
                        encor=[ny, nx]
                    if griglia_precedente[ny][nx]=='B':
                        enpre=[ny, nx]
                else:
                    if griglia_corrente[ny][nx]=='A':
                        encor=[ny, nx]
                    if griglia_precedente[ny][nx]=='A':
                        enpre=[ny, nx]
        en[0]=enpre[0]-encor[0]
        en[1]=enpre[1]-encor[1]
        for cy in range(-1,2):
            for cx in range(-1,2):
                griglia_corrente[encor[0]+en[0]+cy][encor[1]+en[1]+cx]='O'
    return griglia_corrente