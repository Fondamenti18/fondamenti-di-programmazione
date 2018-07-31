'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra (x crescente). 
Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o verticale. 
Le regole di movimento del robottino sono le seguenti: 
- al generico step, si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci e' gia transitato in passato. 
- se invece la cella risulta occupata o e' una cella su cui ha gia transitato, ruota di 90 gradi in senso orario ed aspetta lo step successivo. 
- dopo aver ruotato  di 360 gradi senza essere riuscito a spostarsi si ferma. 

Progettare la funzione  percorso(fname, fname1) che presi in input:
- il percorso di un file (fname) contenente l'immagine in formato .png di una scacchiera con ostacoli
- il percorso di un file di tipo .png (fname1) da creare
legge l'immagine della scacchiera in fname, colora di verde le celle della scacchiera percorse dal robottino prima di fermarsi, 
colora di blu la cella in cui il robottino si ferma e registra l'immagine ricolorata nel file fname1. 
Inoltre restituisce una stringa dove in sequanza sono codificati i passi effettuati dal robottino prima di fermarsi. 
La codifica e' a seguente: 
    '0' per un passo verso destra (x crescenti)
    '1' per un passo verso il basso (y crescenti)
    '2' per un passo verso sinistra (x decrescenti)
    '3' per un passo verso l'alto (y decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt 

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
'''

from immagini import *

def height(img):
    '''Ritorna l'altezza'''
    return len(img)

def width(img):
    '''Ritorn ala larghezza'''
    return len(img[0])

def controlla_ostacolo(img2,rob,h,w):
    '''Ritorna True o False in base alla presenza o meno di un ostacolo. Si controlla la presenza (o assenza) di un ostacolo
    considerando il colore della determinata casella'''
    bianco = (255,255,255)
    nero = (0,0,0)
    rosso = (255,0,0)
    verde = (0,255,0)
    i,j = rob[0],rob[1]
    if i < h and j < w:
        if img2[i][j] == bianco or img2[i][j] == nero:
            ostacolo = False
            tupla = ((i,j),ostacolo)
        elif img2[i][j] == rosso or img2[i][j] == verde:
            ostacolo = True
            tupla = ((i,j),ostacolo)
    elif i < 0 or j < 0: # caso: prima riga
        ostacolo = True
        tupla = ((i,j),ostacolo)
    elif i == h or j == w:
        ostacolo = True
        tupla = ((i,j),ostacolo)
    return tupla

def verso(rob,b,a,s,d):
    '''In base all'ultima rotazione e la predisposizione degli ostacoli decido dove andare a
    controllare la casella successiva'''
    i,j = rob[0],rob[1]
    lista_c = []
    basso = (i+40,j)
    alto = (i-40,j)
    destra = (i,j+40)
    sinistra = (i,j-40)
    if b == True: # se l'ultimo spostamento è stato verso il basso allora inizio a controllare la casella in basso
    # per poi continuare in senso orario
        lista_c = [basso,sinistra,alto,destra]
    elif s == True:
        lista_c = [sinistra,alto,destra,basso]
    elif a == True:
        lista_c = [alto,destra,basso,sinistra]
    elif d == True:
        lista_c = [destra,basso,sinistra,alto]
    return lista_c

def step(img2,h,w,rob,lista_spostamenti):
    i,j = rob[0],rob[1]
    d,b,s,a = False,False,False,False
    if i == 0 and j == 0: # in questo caso faccio partire il controllo da destra dato che èil primo spostamento che il
    # robottino fa di default
        d = True
        lista_c = verso(rob,b,a,s,d)
        rob = controllo(lista_c,img2,h,w)
    elif i == 0 and j != 0: # in questo caso il controllo può partire da una qualsiasi posizione che non sia alto
        d = True
        lista_c = verso(rob,b,a,s,d)
        rob = controllo(lista_c, img2, h, w)
    elif i != 0 and j == 0: # in questo caso il controllo può partire da una qualsiasi posizione che non sia sinistra
        a = True
        lista_c = verso(rob, b, a, s, d)
        rob = controllo(lista_c, img2, h, w)
    elif i != 0 and j != 0:
        l = len(lista_spostamenti)
        penultimo,ultimo = lista_spostamenti[l-2],lista_spostamenti[l-1]
        if penultimo[1] == ultimo[1] and penultimo[0] == ultimo[0] - 40:
        # significa che prima c'è stato uno spostamento verso il BASSO
            b = True
            lista_c = verso(rob, b, a, s, d)
            rob = controllo(lista_c, img2, h, w)
        elif penultimo[0] == ultimo[0] and penultimo[1] == ultimo[1] - 40:
        # prima c'è stato uno spostamento verso DESTRA
            d = True
            lista_c = verso(rob, b, a, s, d)
            rob = controllo(lista_c, img2, h, w)
        elif penultimo[1] == ultimo[1] and penultimo[0] == ultimo[0] + 40:
        # prima c'è stato uno spostamento verso l'ALTO
            a = True
            lista_c = verso(rob, b, a, s, d)
            rob = controllo(lista_c, img2, h, w)
        elif penultimo[0] == ultimo[0] and penultimo[1] == ultimo[1] + 40:
        # prima c'è stato uno spostamento verso SINISTRA
            s = True
            lista_c = verso(rob, b, a, s, d)
            rob = controllo(lista_c, img2, h, w)
    lista_spostamenti.append(rob)
    return rob

def controllo(lista_c,img2,h,w):
    for el in lista_c:
        prox = controlla_ostacolo(img2,el,h,w)
        if prox [1] == False:
            break
        else:
            continue
    return prox[0]

def adiacenti(lista_spostamenti,rob,img2,h,w):
    '''La funzione adiacenti crea una lista di caselle adiacenti a quella con coordinate = rob.
    Se tutte e 4 le caselle sono già state attraversate (e quindi si trovano in lista_spostamenti) allora il robottino
    si ferma.'''
    rosso = (255,0,0)
    verde = (0,255,0)
    l_adiacenti = []
    fine = False
    i,j = rob[0],rob[1]
    sopra = (i-40,j)
    l_adiacenti.append(sopra)
    sotto = (i+40,j)
    l_adiacenti.append(sotto)
    destra = (i,j+40)
    l_adiacenti.append(destra)
    sinistra = (i,j-40)
    l_adiacenti.append(sinistra)
    gradi = 0
    for el in l_adiacenti:
        x,y = el[0],el[1]
        if x < h and y < w:
            if img2[x][y] == rosso or img2[x][y] == verde:
                gradi += 90
            else:
                break
    for el in l_adiacenti:
        x,y = el[0],el[1]
        if el in lista_spostamenti or x < 0 or x > 600 or y < 0 or y > 600:
            fine = True
        elif gradi == 360: # se il robottino ha compiuto un giro di 360 gradi allora deve fermarsi
            fine = True
            break
        else:
            fine = False
            break
    return fine

def codice(lista_spostamenti,copia_spostamenti):
    '''In base allo spostamento aggiunge una cifra a cod_cammino.
    Dato che per come passo le liste mi considera spostamento anche l'ultimo, in cui non avviene però, lo elimino.'''
    cod_cammino = []
    for pos,pos2 in zip(lista_spostamenti,copia_spostamenti):
        if pos[0] == pos2[0]:
            if pos[1] == pos2[1] + 40:
                cod_cammino.append('2')
            elif pos[1] == pos2[1] - 40:
                cod_cammino.append('0')
        elif pos[1] == pos2[1]:
            if pos[0] == pos2[0] - 40:
                cod_cammino.append('1')
            elif pos[0] == pos2[0] + 40:
                cod_cammino.append('3')
    l = len(cod_cammino)
    l1,l2 = len(lista_spostamenti),len(copia_spostamenti)
    fine1,fine2 = lista_spostamenti[l1-1],copia_spostamenti[l2-1]
    if fine1[0] - fine2[0] in [40,-40] or fine1[1] - fine2[1] in [40,-40]:
        cod_cammino = cod_cammino[0:l-1]
    else:
        pass
    cod_cammino = ''.join(cod_cammino)
    return cod_cammino

def modifica_img(img2,rob):
    '''Colora di verde tutte le casella che sono state attraversate dal robottino'''
    i,j = rob[0],rob[1]
    for x in range(i,i+40):
        for y in range(j,j+40):
            img2[x][y] = (0,255,0)
    return img2

def casella_finale(img2,lista_spostamenti):
    '''Stabilisce qual è la casella finale e la colora di blu'''
    l = len(lista_spostamenti)
    el = lista_spostamenti[l-1]
    if el[0] < 0 or el[0] > 600 or el[1] < 0 or el[1] > 600:
        el = lista_spostamenti[l-2]
    else:
        el = lista_spostamenti[l-1]
    i,j = el[0],el[1]
    for x in range(i,i+40):
        for y in range(j,j+40):
            img2[x][y] = (0,0,255)
    return img2

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    img = load(fname)
    h = height(img)
    w = width(img)

    lista_spostamenti = []
    rob = (0,0) # rob indica la posizione attuale del robottino
    i,j = rob[0],rob[1]
    lista_spostamenti.append(rob)
    img2 = img
    while i < h and j < w:
        img2 = modifica_img(img2, rob)
        rob = step(img2,h,w,rob,lista_spostamenti)
        fine = adiacenti(lista_spostamenti,rob,img2,h,w)
        if fine == False:
            continue
        elif fine == True:
            break

    copia_spostamenti = lista_spostamenti[1:] + lista_spostamenti[:1]
    cod_cammino = codice(lista_spostamenti,copia_spostamenti)
    img2 = casella_finale(img2, lista_spostamenti)
    img2 = save(img2,fname1)
    #print(lista_spostamenti)
    return cod_cammino

#print(cammino('I1.png','t1.png'))
#print(cammino('I3.png','t3.png'))

