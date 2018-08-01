'''

Definiamo adiacenti di un pixel p di un immagine i pixel adiacenti a p in  orizzontale o in  verticale.
Se un pixel e' sul bordo dell'immagine il suo vicinato non comprende i pixel non contenuti nell'immagine.
Il pixel dell'immagine con coordinate(x,y) ha dunque come adiacenti i pixel   
con coordinate (x-1,y),(x+1,y),(x,y-1),(x,y+1) appartenenti all'immagine. 
 
Definiamo connessi due pixel se e' possibile dall'uno raggiungere l'altro spostandosi solo su   
pixel adiacenti e dello stesso colore (ovviamente perche' cio' sia possobile e' necessario 
che i due pixel abbiano lo stesso colore).

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una funzione ricolora(fname, lista,  fnameout) che presi:
- il percorso di un file che contiene un'immagine in formato PNG
- una lista di quadruple del tipo (x,y,c1,c2) dove  x e y sono coordinate di un pixel dell'immagine e c1 e c2 due triple colore RGB
- il percorso di un file (fnameout) da creare
legge l'immagine in fname, esegue un'operazione di ricolorazione di alcuni pixel dell'immagine e 
registra l'immagine ricolorata nel file fnameout.

L'operazione di ricolorazione e' la seguente. Per ciascuna delle quadruple (x,y,c1,c2) della lista (nell'ordine), 
- tutti i pixel connessi al pixel  di coordinate (x,y) nell'immagine vanno ricolorati col colore c1, 
- tutti i pixel del perimetro (che si trovano sul 'bordo') della zona che si e' appena colorata devono essere ricolorati col colore c2.
Il perimetro della zona colorata è l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro è il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''

from immagini import *

def height(img):
    return len(img)

def width(img):
    return len(img[0])

def trova_coordinata(lista):
    lista_coord = []
    for quadrupla in lista:
        x,y = quadrupla[0],quadrupla[1]
        p = (x,y)
        lista_coord.append(p)
    return lista_coord

def colore_in(lista_coord,img):
    '''lista che tiene traccia dei colori iniziali da modificare'''
    lista_col = []
    for el in lista_coord:
        col = img[el[0]][el[1]]
        lista_col.append(col)
    return lista_col

def adiacenti(lista_coord,img,h,w):
    '''Per ogni pixel ritorna i quattro pixel adiacenti'''
    matr_ad = []
    for el in lista_coord:
        x,y = el[0],el[1]
        while x > 0 and y > 0 and x < h and y < w:
            p_a = (x-1,y)  # adiacente in alto
            p_b = (x+1,y)  # adiacente in basso
            p_d = (x,y+1)  # adiacente a destra
            p_s = (x,y-1)  # adiacente a sinistra
            colore = img[x][y]
            lista_ad = [p_a,p_b,p_d,p_s,colore]
            matr_ad.append(lista_ad)
            break
    return matr_ad

def connessi(matr_ad,img):
    '''Trova i pixel connessi a (x,y)'''
    matr_conn = []
    for lis in matr_ad:
        lista_conn = []
        l = len(lis)
        colore = lis[l-1]
        lis.remove(colore) # lo rimuovo dato che mi serve solo a prendere le coordinate dei pixel con stesso colore
        for el in lis:
            i,j = el[0],el[1]
            if img[i][j] == colore:
                lista_conn.append(el)
            else:
                pass
        matr_conn.append(lista_conn)
    return matr_conn

def conn_indiretti(matr_conn,img,h,w,colori_mod2,lista_col):
    '''Trova e colora tutti i pixel connessi indirettamente a quello di coordinate (x,y)'''
    fin2 = []
    l = len(matr_conn)
    for x in range(l):
        lis = matr_conn[x]
        colore = colori_mod2[x][1] # colore è la tupla RGB per colorare l'interno, e quindi l'area, del quadrato
        fin = []
        el0,el1,el2,el3 = lis[0],lis[1],lis[2],lis[3]
        lis2 = [el0,el1,el2,el3]
        for el in lis2:
            if el == lis2[0]:
                a,b = el[0],el[1]
                while a > 0 and b > 0 and a < h and b < w and img[a][b] == lista_col[x]:
                    img[a][b] = colore
                    a -= 1
                fin.append((a,b))
            elif el == lis2[1]:
                a, b = el[0], el[1]
                while a > 0 and b > 0 and a < h and b < w and img[a][b] == lista_col[x]:
                    img[a][b] = colore
                    a += 1
                fin.append((a, b))
            elif el == lis2[2]:
                a, b = el[0], el[1]
                while a > 0 and b > 0 and a < h and b < w and img[a][b] == lista_col[x]:
                    img[a][b] = colore
                    b += 1
                fin.append((a, b))
            elif el == lis2[3]:
                a, b = el[0], el[1]
                while a > 0 and b > 0 and a < h and b < w and img[a][b] == lista_col[x]:
                    img[a][b] = colore
                    b -= 1
                fin.append((a, b))
        fin2.append(fin)
    return fin2

def colora(fin2,img,colori_mod2):
    '''Colora l'area del quadrato considerato'''
    colorati2 = []
    l = len(fin2)
    for i in range(l):
        fin = fin2[i]
        base = fin[1][0] - fin[0][0]
        altezza = fin[2][1] - fin[3][1]
        colore = colori_mod2[i][0]
        for x in range(len(fin)):
            colorati = []
    # dato che la differenza di righe tra le prime due tuple è uguale alla base e la differenza tra le colonne delle ultime
    # due tuple da l'altezza, mi ricavo questi due parametri da qui
            for x in range(base):
                for y in range(altezza):
                    img[x][y] = colore
                    colorati.append((x,y))
            colorati2.append(colorati)
    return colorati2

def colora_perimetro(img,h,w,fin2,colori_mod2):
    lista2 = []
    l = len(fin2)
    for i in range(l):
        fin = fin2[i]
        colore2 = colori_mod2[i][1]
        base = fin[1][0] - fin[0][0]
        altezza = fin[2][1] - fin[3][1] - 1
        lato_a = fin[0][0]
        lato_b = fin[1][0] - 1
        lista = []
        for x in range(base):
            img[lato_a][x] = colore2
            lista.append((lato_a,x))
        for y in range(altezza):
            img[y][lato_b] = colore2
            lista.append((y,lato_b))
        for y in range(base):
            img[lato_b][y] = colore2
            lista.append((lato_b,y))
        for x in range(altezza):
            img[x][lato_a] = colore2
            lista.append((x,lato_a))
        lista2.append(lista)
    return lista2

def area(colorati2,l_perimetri):
    l_aree = []
    for el,el2 in zip(colorati2,l_perimetri):
        area = len(el) - el2
        l_aree.append(area)
    return l_aree

def perimetro(perimetro_a):
    l_perimetri = []
    for el in perimetro_a:
        el = set(el)
        perim = len(el)
        l_perimetri.append(perim)
    return l_perimetri

def trova_colori(lista):
    '''Salva su una lista i colori che serviranno per colorare, rispettivamente, area e perimetro'''
    colori_mod2 = []
    l = len(lista)
    for x in range(l):
        lis = lista[x]
        colore_a = lis[2]
        colore_p = lis[3]
        colori_mod = [colore_a,colore_p]
        colori_mod2.append(colori_mod)
    return colori_mod2

def ris(l_aree,l_perimetri):
    risultato = []
    for area,perim in zip(l_aree,l_perimetri):
        risultato.append((area,perim))
    return risultato

def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''

    img = load(fname)
    h = height(img)
    w = width(img)
    colori_mod2 = trova_colori(lista)  # colori della modifica
    #print(colori_mod2)
    lista_coord = trova_coordinata(lista)  # colori iniziali dei pixel di partenza
    lista_col = colore_in(lista_coord, img)
    #print(lista_col)
    matr_ad = adiacenti(lista_coord,img,h,w)
    #print(matr_ad)
    matr_conn = connessi(matr_ad,img)
    #print(matr_conn)
    fin2 = conn_indiretti(matr_conn,img,h,w,colori_mod2,lista_col)
    #print(fin)
    colorati2 = colora(fin2,img,colori_mod2)
    #print(colorati2)
    perimetro_a = colora_perimetro(img,h,w,fin2,colori_mod2)
    #print(perimetro_a)
    l_perimetri = perimetro(perimetro_a)
    #print(l_perimetri)
    l_aree = area(colorati2,l_perimetri)
    #print(area_a)
    risultato = ris(l_aree,l_perimetri)
    img = save(img,fnameout)

    return risultato

