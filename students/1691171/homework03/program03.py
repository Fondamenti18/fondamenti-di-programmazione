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

from immagini import load, save

rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)

DA_ESAMINARE = -1
VUOTO = 0
COLORE = 1
PERIMETRO = 2
NON_TOCCARE = 3


def conta(mat, n):
    count = 0
    for row in mat:
        for e in row:
            if e == n:
                count += 1
    return count


def apply_changes(image, mat, q):
    righe = len(mat)
    colonne = len(mat[0])
    i = 0
    while i < righe:
        j = 0
        while j < colonne:
            if mat[i][j] == COLORE:
                image[j][i] = q[2]
            elif mat[i][j] == PERIMETRO:
                image[j][i] = q[3]
            j += 1
        i += 1


def segna_connessi(image, mat, orig):
    count = 0
    righe = len(mat)
    cols = len(mat[0])
    # print("righemat=", righe, "\tcolsmat=", cols, "\t\trigheimg=", len(image[0]), "\tcolsimg=", len(image))
    i = 0
    while i < righe:
        j = 0
        while j < cols:
            if mat[i][j] == DA_ESAMINARE:
                vicini = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                utili = [x for x in vicini if x[0] >= 0 and x[0] < righe and x[1] >= 0 and x[1] < cols and mat[x[0]][x[1]] == VUOTO and image[x[1]][x[0]] == orig]
                fuori = [x for x in vicini if x[0] < 0 or x[0] >= righe or x[1] < 0 or x[1] >= cols or image[x[1]][x[0]] != orig]
                if len(fuori) > 0:
                    mat[i][j] = PERIMETRO
                else:
                    mat[i][j] = COLORE
                for u in utili:
                    if mat[u[0]][u[1]] == VUOTO:
                        mat[u[0]][u[1]] = DA_ESAMINARE
                        count += 1
            j += 1
        i += 1
    return count


def ricolora(fname, lista, fnameout):
    ris = []
    image = load(fname)
    for q in lista:
        mat = [[VUOTO for i in range(0, len(image[0]))] for j in range(0, len(image))]
        r = q[0]
        c = q[1]
        orig = image[c][r]
        mat[r][c] = DA_ESAMINARE
        count = segna_connessi(image, mat, orig)
        while count > 0:
            count = segna_connessi(image, mat, orig)
        apply_changes(image, mat, q)
        area, perim = conta(mat, COLORE), conta(mat, PERIMETRO)
        ris.append((area, perim))
    save(image, fnameout)
    return ris

