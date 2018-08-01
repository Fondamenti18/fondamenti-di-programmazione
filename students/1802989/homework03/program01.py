from immagini import *

def load(fname, c):
    'Funzione load modificata affinché il programma lavori su una ricerca binaria'
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                # Modifica: se la tupla è il colore cercato allora appende 1, altrimenti 0
                if (line[i], line[i+1], line[i+2]) == c:
                    l+=[1]
                else:
                    l+=[0]
            img+=[l]
        return img

def quadrato(filename,c):
    '''Il programma scandisce l'immagine e forma la matrice del risultato'''
    img = load(filename, c)
    h = len(img)
    w = len(img[0])
    lato = 0
    coord = 0,0
    matrice = []
    matrice.append([0] * (w+1))
    #A questo punto creiamo una prima fila di 0 per evitare IndexError
    for j in range(1,h+1):
        # Ho traslato il range di +1 perché altrimenti sarebbe fallito il controllo
        riga = []
        riga.append(0)
        # All'inizio di ogni riga appendiamo uno 0 per lo stesso motivo
        for i in range(1,w+1):
            if img[j-1][i-1]:
                num = min(matrice[j-1][i-1], riga[i-1], matrice[j-1][i] ) +1
                # Questo controllo, che guarda l'elemento precedente
                riga.append( num )
                if num > lato:
                    lato = num
                    coord = (i-lato,j-lato)
            else:
                riga.append(0)
        matrice.append(riga)
    
    return lato, coord