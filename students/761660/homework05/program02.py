from random     import randint
def cercabucax(g,a,b,d):
    for r in range(a,b+d,d):
            if g[r]=='o':
                return r
    return -1
def cercaostacolox(g,a,b,d):
    for r in range(a,b+d,d):
            if g[r]=='#':
                return r
    return -1
def cercaostacolo1x(g,a,b,d):
    for r in range(a,b+d,d):
            if g[r]=='#':
                return r
    return -1
def cercabucay(g,r,a,b,d):
    for c in range(a,b+d,d):
            if g[c][r]=='o':
                return c
    return -1
def cercaostacoloy(g,r,a,b,d):
    for c in range(a,b+d,d):
            if g[c][r]=='#':
                return c
    return -1
def inside(griglia_corrente,x,y):
    return 0<=x<len(griglia_corrente[0]) and 0<=y<len(griglia_corrente)


def inizializza(g):
     altezza=len(g)
     larghezza=len(g[0])
     for _ in range(altezza):
        riga=[]
        for _ in range(larghezza):
            riga.append(0)
        griglia.append(riga)
     return griglia
ax=0
ay=0
Dx=0
Dy=0
sx=0
sy=0
px=0
py=0
q=0
t=0
cambio=0
inizio=0
conta=0
direzione=0
griglia=[[]]
diz={}
def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty):
    '''inserite qui il vostro codice'''
    global ax
    global ay
    global Dx
    global Dy
    global sx
    global sy
    global px
    global py
    global q
    global t
    global cambio
    global inizio
    global conta
    global griglia
    global direzione
    global diz
    Dx+=ax
    Dy+=ay
    
    sx=x+vx+verso
    sy=y+vy+verso
    diz[(x,y)]=1
    if(inizio==0) :
        ax=verso
        ay=0
        inizio=1
        direzione=0
    elif direzione==0 and griglia_corrente[y][x-1]!='#' and (x-1,y) not in diz:
        ax=0
        ay=0
    elif direzione==2 and griglia_corrente[y][x+1]!='#' and (x+1,y) not in diz:
        ax=0
        ay=0    
    elif direzione==0 and griglia_corrente[y][x-1]=='o' and (x,y+1) not in diz:
         ax=-verso
         ay=-verso
         direzione=1
    elif direzione==1 and griglia_corrente[y-1][x-1]=='o' and (x-1,y) not in diz:
         ax=verso
         ay=verso
         direzione=0   
    elif direzione==3 and griglia_corrente[y-1][x]=='o' and (x-1,y) not in diz:
         ax=verso
         ay=-verso
         direzione=0  
    elif direzione==0 and griglia_corrente[y][x-1]=='#' and griglia_corrente[y+1][x]=='#' and griglia_corrente[y-1][x]!='#' and (x,y-1) not in diz:
         ax=-verso
         ay=verso
         direzione=3
    elif direzione==0 and griglia_corrente[y][x-1]=='#' and griglia_corrente[y+1][x]!='#' and griglia_corrente[y-1][x]!='#' and (x,y-1) not in diz:
         ax=-verso
         ay=verso
         direzione=3     
    elif direzione==0 and griglia_corrente[y][x-1]=='#' and griglia_corrente[y-1][x]=='#' and griglia_corrente[y+1][x]!='#' and (x,y+1) not in diz:
         ax=-verso
         ay=-verso
         direzione=1
    elif direzione==3 and griglia_corrente[y-1][x]!='#'  and (x,y-1) not in diz:
         ax=0
         ay=0
    elif direzione==3  and griglia_corrente[y-1][x]=='#' and griglia_corrente[y][x-1]=='#' and (x+1,y) not in diz:
         ax=-verso
         ay=-verso
         direzione=2
    elif direzione==3  and griglia_corrente[y-1][x]=='#' and griglia_corrente[y][x+1]=='#' and (x-1,y) not in diz:
         ax=verso
         ay=-verso
         direzione=0  
    elif direzione==3  and griglia_corrente[y-1][x]=='#' and (x-1,y) not in diz:
         ax=verso
         ay=-verso
         direzione=0      
    elif direzione==3  and griglia_corrente[y-1][x]=='#' and (x+1,y) not in diz:
         ax=-verso
         ay=-verso
         direzione=2    
    elif direzione==1 and griglia_corrente[y+1][x]!='#' and (x,y+1) not in diz:
        ax=0
        ay=0    
    elif direzione==1 and griglia_corrente[y+1][x]=='#' and griglia_corrente[y][x+1]=='#' and griglia_corrente[y][x-1]!='#'  and (x-1,y) not in diz:
        ax=verso
        ay=verso
        direzione=0
     
    elif direzione==1 and griglia_corrente[y+1][x]=='#' and griglia_corrente[y][x+1]!='#' and griglia_corrente[y][x-1]!='#'  and (x+1,y) not in diz:
        ax=-verso
        ay=verso
        direzione=2    
    elif direzione==1 and griglia_corrente[y+1][x]=='#' and griglia_corrente[y][x+1]=='#' and griglia_corrente[y][x-1]!='#'  and (x-1,y)  in diz:
        ax=-verso
        ay=verso
        direzione=2   
    elif direzione==1 and griglia_corrente[y+1][x]=='#' and griglia_corrente[y][x-1]=='#' and griglia_corrente[y][x+1]!='#'  and (x+1,y) not in diz:
        ax=-verso
        ay=verso
        direzione=2  
     
    elif direzione==2 and griglia_corrente[y][x+1]=='#' and griglia_corrente[y-1][x]!='#'  and (x,y-1) not in diz:
        ax=verso
        ay=verso
        direzione=3 
   
    elif direzione==1 and griglia_corrente[y-1][x]=='#' and griglia_corrente[y][x-1]=='#'  and (x+1,y) in diz:
        ax=-verso
        ay=verso
        direzione=2 
    elif direzione==2 and griglia_corrente[y-1][x]=='#' and griglia_corrente[y][x+1]=='#'  and (x,y+1) not in diz:
        ax=verso
        ay=-verso
        direzione=1     
    return ax,ay