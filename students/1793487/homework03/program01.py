from immagini import load,save


def estrattore_LInversa(img):
    LInversa, y_cntt = [], 0
    for riga in img:
        cntt = 1  #contatore
        C_precedente= (-1,-1,-1)     #valori che un colore non avrà mai ma che servono a creare la variabile
        LInversa.append([])
        for C in reversed(riga):
            C
            if C==C_precedente:
                cntt +=1
            else:
                cntt = 1
            C_precedente=C
            LInversa[y_cntt].insert(0, cntt)
        y_cntt+=1
    return LInversa
    


def essere_quadrato(y,x,L_inv,A_dimensione,C,img):
    if (y+A_dimensione)>=len(L_inv):
        return False
    for y_q in range(y,y+A_dimensione):
        if L_inv[y_q][x] < A_dimensione or img[y_q][x] != C:    #deve essere più grande altrimenti 
            #non ho abbastanza pixel per creare il quadrato di lato A_dimensione
            return False
    return True


def quadrato(filename,C):
    img=load(filename)
    L_inv = estrattore_LInversa(img)
    A_dimensione = 1
    for y in range(len(img)):
        for x in range(len(img[0])):
            if img[y][x]==C:
                while essere_quadrato(y,x,L_inv,A_dimensione,C,img):
                    primo_pixel=(x,y)
                    A_dimensione += 1
    return A_dimensione-1, primo_pixel