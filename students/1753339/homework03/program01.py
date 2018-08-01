'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contine un immagine in formato png della  tipologia appena descritta.
- una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0 e 255 compresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e colore C interamente visibile nell'immagine. 
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
all'interno dell'immagine del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''


from immagini import *

def height(img):
    '''Ritorna l'altezza dell'immagine'''
    h = len(img)
    return h

def width(img):
    '''Ritorna la larghezza dell'immagine'''
    w = len(img[0])
    return w

def trova_quad(img,h,w,c):
    '''Per ogni riga in img ritorna una lista contenente le coordinate dei pixel di colore c su quella riga'''
    matr = []
    for i in range(h):
        lista = []
        for j in range(w):
            if img[i][j] == c:
                lista.append((i,j))
                continue
            if lista != []:
                matr.append(lista)
            lista = []
            continue
    return matr

def controlla_larghezza(matr):
    '''Per ogni lista in m_quad ritorno una lista contenente le coordinate in cui inizia una forma geometrica (non so se è un quad)
    e la lunghezza del lato (per quante colonne si ripetono pixel dello stesso colore)'''
    matr3 = []
    for lista in matr:
        lato = len(lista)
        lista.append(lato)
    for lista in matr:
        l = len(lista)
        tupla3 = lista[0],lista[l-1]
        matr3.append(tupla3)
    return matr3

def controlla_altezza(matr_l,img,c):
    '''Presa in input matr_l calcolo l'altezza di ogni quadrato/rettangolo, partendo delle coordinate di " inizio" '''
    matr = []
    matr_l2 = matr_l
    for el in matr_l:
        app = []
        lato = el[1]
        colonna = el[0][1]
        for el2 in matr_l2:
            if el2[1] == lato and el2[0][1] == colonna:
                app.append(el2)
        if app not in matr:
            matr.append(app)
        else:
            pass
    return matr

def controlla_quad(matr_l2):

    matr = []
    for lista in matr_l2:
        altezza = len(lista)
        lista.append(altezza)
        matr.append(lista)
    return matr

def dati(matr_quad):
    '''Ritorna per ogni inizio quadrato la lunghezza di altezza e base'''
    matrice = []
    for lista in matr_quad:
        lista_m = []
        l = len(lista)
        lista_m.append(lista[0])
        lista_m.append(lista[l-1])
        matrice.append(lista_m)
    matrice2 = []
    for lista_m in matrice:
        lista_m2 = []
        lista_m2.append(lista_m[0][0])  # pixel alto sx
        lista_m2.append(lista_m[0][1])  # base
        lista_m2.append(lista_m[1])     # altezza
        matrice2.append(lista_m2)
    return matrice2

def controllo(matrice):
    '''Modifica i valori definendo il rettangolo trovato come effettivo quadrato'''
    for lista in matrice:
        if lista[1] == lista[2]:
            pass
        else:
            if lista[1] < lista[2]:
                lista[2] = lista[1]
            else:
                lista[1] = lista[2]
    return matrice

def finale(matrice2):
    '''Scelgo il quadrato con lato maggiore'''
    max = matrice2[0][1]
    l_max = (max,(matrice2[0][0][1],matrice2[0][0][0]))
    for lista in matrice2:
        if len(lista) == 1:
            break
        elif lista[1] > max:
            max  = lista[1]
            tupla = (lista[0][1],lista[0][0]) # inverto i valori dato che inizialmente avevo colorra,riga
            l_max = (max,tupla)
    return l_max

def quadrato(filename, c):
    img = load(filename)
    h = height(img)
    w = width(img)
    m_quad = trova_quad(img,h,w,c)
    matr_l = controlla_larghezza(m_quad)
    matr_l2 = controlla_altezza(matr_l,img,c)
    matr_quad = controlla_quad(matr_l2)
    matrice = dati(matr_quad)
    matrice2 = controllo(matrice)
    l_max = finale(matrice2)

    return l_max
