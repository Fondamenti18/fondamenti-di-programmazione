# -*- coding: cp1252 -*-
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
Il perimetro della zona colorata e' l'insieme dei pixel che non hanno tutti e 4 i vicini che fanno parte della zona ricolorata 
(ovvero almeno uno è di un colore diverso da quello che si sta ricolorando oppure almeno uno non esiste perchè sarebbe fuori dall'immagine)

Si consideri ad esempio l'immagine 'I1.png', l'invocazione di ricolora('I1.png',[(10,10,(255,0,0), (0,0,255))],’OUT1.png')
produrra' l'immagine 'OUT1.png' identica all'immagine di partenza se non per il fatto che,
 tutti i pixel adiacenti al pixel di coordinate (10,10) (e di colore verde), verranno ricolorati 
 di rosso ((255,0,0)), mentre i pixel sul bordo della zona inizialmente verde vengono ricolorati di blu.

Per ciascuna area ricolorata bisogna inoltre calcolare area interna e perimetro, che sono definite come segue:
- l'area interna e' il numero di pixel ricolorati con il colore c1
- il perimetro e' il numero di pixel ricolorati con il colore c2

La funzone deve tornare la lista di coppie (area interna, perimetro) nello stesso ordine in cui sono state colorate le aree.
 
Per altri  esempi vedere il file grade03.txt 
'''


import immagini    
def ricolora(fname, lista, fnameout):
    A = immagini.load(fname)
    righe = len(A)
    colonne = len(A[0])
    
    L = list()   # Lista delle coppie (superfice, perimetro)
    for tp in lista:   
        y, x, a, b = tp  # a e' il colore interno, b il colore dei pixel perimetrali
        coloreIniziale = A[x][y]
        daEsaminare = set()
        perimetro = set()
        if e_dentro(x-1, y, righe, colonne) and A[x-1][y] == coloreIniziale:
            daEsaminare.add((x-1, y))
            if e_sulPerimetro(A, x-1, y, righe, colonne):  # e_sulPerimetro(A, x, y, righe, colonne)
                perimetro.add((x-1,y))
        if e_dentro(x, y+1, righe, colonne) and A[x][y+1] == coloreIniziale:
            daEsaminare.add((x, y+1))
            if e_sulPerimetro(A, x, y+1, righe, colonne):
                perimetro.add((x,y+1))
        if e_dentro(x+1, y, righe, colonne) and A[x+1][y] == coloreIniziale:
            daEsaminare.add((x+1, y))
            if e_sulPerimetro(A, x+1, y, righe, colonne):  # e_sulPerimetro(A, x, y, righe, colonne)
                perimetro.add((x+1,y))
        if e_dentro(x, y-1, righe, colonne) and A[x][y-1] == coloreIniziale:
            daEsaminare.add((x, y-1)) 
            if e_sulPerimetro(A, x, y-1, righe, colonne):  # e_sulPerimetro(A, x, y, righe, colonne)
                perimetro.add((x,y-1))
            
        esaminati = set()
        while len(daEsaminare)>0:
            (i, j) = daEsaminare.pop()  # pop preleva l'elemento dal set
            if (i,j) not in esaminati: # and A[i][j] == coloreIniziale:
                esaminati.add((i,j))
                if e_dentro(i-1, j, righe, colonne) and A[i-1][j] == coloreIniziale:
                    daEsaminare.add((i-1, j))
                    if e_sulPerimetro(A, i-1, j, righe, colonne):
                        perimetro.add((i-1,j))
                if e_dentro(i, j+1, righe, colonne) and A[i][j+1] == coloreIniziale:
                    daEsaminare.add((i, j+1))
                    if e_sulPerimetro(A, i, j+1, righe, colonne):
                        perimetro.add((i,j+1))
                if e_dentro(i+1, j, righe, colonne) and A[i+1][j] == coloreIniziale:
                    daEsaminare.add((i+1, j))
                    if e_sulPerimetro(A, i+1, j, righe, colonne):
                        perimetro.add((i+1,j))
                if e_dentro(i, j-1, righe, colonne) and A[i][j-1] == coloreIniziale:
                    daEsaminare.add((i, j-1)) 
                    if e_sulPerimetro(A, i, j-1, righe, colonne):
                        perimetro.add((i,j-1))
        
       
        p = s = 0   # p = perimetro (numero di pixel perimetrali), s = superfice (numero di pixel interni)
        for i, j in esaminati:
            if (i,j) in perimetro:
                A[i][j] = b
                p = p + 1
            else:
                A[i][j] = a
                s = s + 1
        L.append((s,p)) 
        
    immagini.save(A, fnameout)
    
    return L
    
def e_dentro(x, y, righe, colonne):
    #Restituisce True se il punto (x,y) e' interno all'immagine, False altrimenti 
    t = (0<=x and x<righe) and (0<=y and y<colonne)
    return t
    
def e_sulPerimetro(A, x, y, righe, colonne):
    if x==0 or x==righe-1 or y==0 or y==colonne-1:  # x = coordinata di riga, y = coordinata di colonna
        t = True
    else:
        t = False
        if A[x][y] != A[x-1][y] or A[x][y] != A[x][y+1] or A[x][y] != A[x+1][y] or A[x][y] != A[x][y-1]:
            t = True
              
    return t   
            
def misure():
    A = immagini.load("I1.png")
    print("L'immagine I1.png e' " + str(len(A)) + " X " + str(len(A[0])))
    A = immagini.load("I2.png")
    print("L'immagine I2.png e' " + str(len(A)) + " X " + str(len(A[0])))

def uguali(F1, F2):
    A = immagini.load(F1)
    B = immagini.load(F2)
    return A==B

