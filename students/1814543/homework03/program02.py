from immagini import*

NUMERO_CASELLE = 15
LATO = 40
GIA_PASSATO = (0,255,0)
FERMATO = (0,0,255)
OSTACOLO = (255,0,0)

def ricrea_matrice(vecchia_matrice):
    
    h = 0
    k = 0
    scacchiera_finale = [[0 for x in range(NUMERO_CASELLE*LATO)]for y in range(NUMERO_CASELLE*LATO)]
    for h in range(NUMERO_CASELLE*LATO):
        for k in range(NUMERO_CASELLE * LATO):
            my_x = int (h / LATO)
            m_y = int ( k / LATO )
            scacchiera_finale[h][k] = vecchia_matrice[my_x][m_y]
        
    return scacchiera_finale

def get_next_direction (direzione):
    new_dir = direzione+1
    if new_dir == 4:
        new_dir= 0  
    return new_dir

def nuova_matrice(scacchiera,i,j):
    new_scacchiera = [[0 for x in range(NUMERO_CASELLE)]for y in range(NUMERO_CASELLE)]
    h = 0
    k = 0 
    while (i<=NUMERO_CASELLE*LATO and j<=NUMERO_CASELLE*LATO):
        new_scacchiera[h][k] = scacchiera[i][j]
        i = i+40
        h = h+1
        if (i >= NUMERO_CASELLE*LATO):
            i = 0 
            j = j+40
            h = 0
            k = k+1
        if (j >= NUMERO_CASELLE*LATO):
            break
    return new_scacchiera


def direzioni_possibili(new_scacchiera,i,j):
    
    lista_risultato = []
    if( i+1< NUMERO_CASELLE ):
        if(new_scacchiera[i+1][j] != OSTACOLO and new_scacchiera[i+1][j] != GIA_PASSATO ):
            lista_risultato.append(1)
    if( j+1< NUMERO_CASELLE ):
        if(new_scacchiera[i][j+1] != OSTACOLO and new_scacchiera[i][j+1] != GIA_PASSATO ):
            lista_risultato.append(0)
    
    if( i-1>=0 ):
        if(new_scacchiera[i-1][j] != OSTACOLO and new_scacchiera[i-1][j] != GIA_PASSATO ):
            lista_risultato.append(3)
    if( j-1>=0 ):
        if(new_scacchiera[i][j-1] != OSTACOLO and new_scacchiera[i][j-1] != GIA_PASSATO ):
            lista_risultato.append(2)
    return lista_risultato

def movimento_robot (new_scacchiera,i,j,direzione):
    
    new_scacchiera[i][j] = GIA_PASSATO
    
    if(direzione == 1):
        i = i+1
    if(direzione == 0):
        j = j+1
    if(direzione == 3):
        i = i-1
    if(direzione == 2):
        j = j-1
    return i,j

def cammino (fname, fname1):
    scacchiera = load(fname)
    i = 0
    j = 0
    passi_svolti = ""
    direzione_attuale = 0
    new_scacchiera = nuova_matrice(scacchiera,i,j)
    
    while(0<= i <NUMERO_CASELLE and 0<= j <NUMERO_CASELLE):
        direzioni = direzioni_possibili(new_scacchiera,i,j)
        if(len(direzioni) == 0):
            break
        direzione_da_testare = direzione_attuale
        conta_direzioni = 0
        while(conta_direzioni<4):
            if(direzione_da_testare in direzioni):
                i,j = movimento_robot(new_scacchiera,i,j,direzione_da_testare)
                direzione_attuale = direzione_da_testare
                passi_svolti = passi_svolti+str(direzione_attuale)
                break
            else:
                direzione_da_testare = get_next_direction (direzione_da_testare)
                conta_direzioni += 1
            
    new_scacchiera[i][j] = FERMATO
    scacchiera_finale = ricrea_matrice(new_scacchiera)
    save(scacchiera_finale, fname1)
    return passi_svolti
