from immagini import load,save 


def LdiLnpixel(fname):
    tovaglia_quadri = []
    l_pixel_load=load(fname)
    for y in range(0,len(l_pixel_load),40):
        for x in range(0,len(l_pixel_load[0]),40):
            singolo_pixel=l_pixel_load[y][x]
            if (255,0,0)==singolo_pixel:
                tovaglia_quadri.append('o')
            else:
                tovaglia_quadri.append(' ')
    tovaglia_quadri = [tovaglia_quadri[n:n+15] for n in range(0, 225, 15)]    #225 perchè tovaglia_quadri è 15*15
    return tovaglia_quadri, l_pixel_load


def giraMRobot(direzione_MRobot):
    direzione_MRobot+=1
    if direzione_MRobot==4:
        direzione_MRobot=0
    return direzione_MRobot


def verif_dimensioni(tovaglia_quadri,x_y):
    return 0<=x_y[1]<len(tovaglia_quadri) and 0<=x_y[0]<len(tovaglia_quadri[0])


def muoviDX(tovaglia_quadri, posizione_MRobot):
    nuova_posizione_MRobot = (posizione_MRobot[0],posizione_MRobot[1]+1)
    if verif_dimensioni(tovaglia_quadri,nuova_posizione_MRobot):
        if tovaglia_quadri[nuova_posizione_MRobot[0]][nuova_posizione_MRobot[1]]==' ':
            return True
    return False

                    
def muoviSX(tovaglia_quadri, posizione_MRobot):
    nuova_posizione_MRobot = (posizione_MRobot[0],posizione_MRobot[1]-1)
    if verif_dimensioni(tovaglia_quadri,nuova_posizione_MRobot):
        if tovaglia_quadri[nuova_posizione_MRobot[0]][nuova_posizione_MRobot[1]]==' ':
            return True
    return False

    
def muoviUP(tovaglia_quadri, posizione_MRobot): 
    nuova_posizione_MRobot = (posizione_MRobot[0]-1,posizione_MRobot[1])
    if verif_dimensioni(tovaglia_quadri,nuova_posizione_MRobot):
        if tovaglia_quadri[nuova_posizione_MRobot[0]][nuova_posizione_MRobot[1]]==' ':
            return True
    return False

        
def muoviDOWN(tovaglia_quadri, posizione_MRobot):
    nuova_posizione_MRobot = (posizione_MRobot[0]+1,posizione_MRobot[1])
    if verif_dimensioni(tovaglia_quadri,nuova_posizione_MRobot):
        if tovaglia_quadri[nuova_posizione_MRobot[0]][nuova_posizione_MRobot[1]]==' ':
            return True
    return False

        
def muovi(tovaglia_quadri, direzione_MRobot, img):
    tentativo_MRobot=0
    ritorno_MRobot = ""
    posizione_MRobot = [0, 0]  #coordinata
    while tentativo_MRobot<4:
        if direzione_MRobot == 0:
            if muoviDX(tovaglia_quadri, posizione_MRobot):
                tovaglia_quadri[posizione_MRobot[0]][posizione_MRobot[1]] = 'v'
                ritorno_MRobot += str(direzione_MRobot)
                posizione_MRobot = [posizione_MRobot[0], posizione_MRobot[1]+1]
                tentativo_MRobot=0
            else:
                tentativo_MRobot += 1
                direzione_MRobot = giraMRobot(direzione_MRobot)
        elif direzione_MRobot == 1:
            if muoviDOWN(tovaglia_quadri, posizione_MRobot):
                ritorno_MRobot += str(direzione_MRobot)
                tovaglia_quadri[posizione_MRobot[0]][posizione_MRobot[1]] = 'v'
                posizione_MRobot = [posizione_MRobot[0]+1, posizione_MRobot[1]]
                tentativo_MRobot=0
            else:
                tentativo_MRobot += 1
                direzione_MRobot = giraMRobot(direzione_MRobot)
        elif direzione_MRobot == 2:
            if muoviSX(tovaglia_quadri, posizione_MRobot):
                tovaglia_quadri[posizione_MRobot[0]][posizione_MRobot[1]] = 'v'
                posizione_MRobot = [posizione_MRobot[0], posizione_MRobot[1]-1]
                ritorno_MRobot += str(direzione_MRobot)
                tentativo_MRobot=0
            else:
                tentativo_MRobot += 1
                direzione_MRobot = giraMRobot(direzione_MRobot)
        elif direzione_MRobot == 3:
            if muoviUP(tovaglia_quadri, posizione_MRobot):
                ritorno_MRobot += str(direzione_MRobot)
                tovaglia_quadri[posizione_MRobot[0]][posizione_MRobot[1]] = 'v'
                posizione_MRobot = [posizione_MRobot[0]-1, posizione_MRobot[1]]
                tentativo_MRobot=0
            else:
                tentativo_MRobot += 1
                direzione_MRobot = giraMRobot(direzione_MRobot)
    tovaglia_quadri[posizione_MRobot[0]][posizione_MRobot[1]]= 'b'
    return ritorno_MRobot


def modifica_casella(l_pixel_load, posizione_MRobot, colore_quadro):
    for y in range(posizione_MRobot[0]*40, posizione_MRobot[0]*40+40):
        for x in range(posizione_MRobot[1]*40, posizione_MRobot[1]*40+40):
            l_pixel_load[y][x]= colore_quadro
    
    
def cammino(fname,fname1):
    tovaglia_quadri, l_pixel_load = LdiLnpixel(fname)
    ritorno_MRobot = muovi(tovaglia_quadri, 0, l_pixel_load)
    y_c = -1
    for riga in tovaglia_quadri:
        y_c += 1 
        x_c = -1
        for el in riga:
            x_c += 1
            if el== 'v':
                modifica_casella(l_pixel_load, (y_c, x_c), (0, 255, 0))
            elif el == 'b':
                modifica_casella(l_pixel_load, (y_c, x_c), (0, 0, 255))
    save(l_pixel_load,fname1)
    return ritorno_MRobot
