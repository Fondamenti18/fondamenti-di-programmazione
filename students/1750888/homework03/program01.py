# -*- coding: cp1252 -*-
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

In caso ci siano piu' quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si puo' assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout e' impostato a 10*N secondi (con N numero di test del grader).
'''




import immagini
def quadrato(filename,c):
    A = immagini.load(filename)
    righe = len(A)
    colonne = len(A[0])
    S = set()
    for i in range(righe):
        for j in range(colonne):
            if A[i][j] == c:
                S.add((i,j))
    
    d = 0 # dimensione iniziale del lato del quadrato 
    a = b = -1  # coordinate del punto in alto a sinistra da cui parte il quadrato da individuare
    for r1 in range(righe):
        for c1 in range(colonne):
            if (r1, c1) in S:
                
                W = set()
                W.add((r1,c1))
                S = S - W
                
                
                dx = lato(S, r1, c1)
                if (dx>d) or (dx==d and r1<a) or (dx==d and r1==a and c1<b):
                    d = dx
                    a = r1
                    b = c1
                    # righe = len(A) - dx
                    # colonne = len(A[0]) - dx
            # c1 = c1 + 1
        # r1 = r1 + 1
                    
    return (d, (b, a))
        
    # return S

def lato(S, rig, col):
    """ determina la lunghezza del quadrato di coordinate rig, col """
    dx = 1
    t = True
    while t:
        r = rig + dx
        for j in range(col, col+dx):
            if (r,j) not in S:
                t = False
                break
        if t:
            c = col + dx
            for i in range(rig, rig+dx):
                if (i, c) not in S:
                    t = False
                    break
        if t:
            if (r,c) not in S:
                t = False
        if t:
            dx = dx + 1
    return dx

def misure():
    A = immagini.load("Ist0.png")
    print("L'immagine Ist0.png e' " + str(len(A)) + " X " + str(len(A[0])))
    A = immagini.load("Ist1.png")
    print("L'immagine Ist1.png e' " + str(len(A)) + " X " + str(len(A[0])))
    A = immagini.load("Ist2.png")
    print("L'immagine Ist2.png e' " + str(len(A)) + " X " + str(len(A[0])))
    A = immagini.load("Ist3.png")
    print("L'immagine Ist3.png e' " + str(len(A)) + " X " + str(len(A[0])))
    A = immagini.load("Ist4.png")
    print("L'immagine Ist4.png e' " + str(len(A)) + " X " + str(len(A[0])))            
                
def creaSet(n):
    S = set()
    for i in range(n):
        for j in range(n):
            S.add((i,j))
    return S
    
def creaDiz(n):
    S = dict()
    for i in range(n):
        for j in range(n):
            S[(i,j)] = "***"
    return S
    
def prova1(filename,c):
    A = immagini.load(filename)
    righe = len(A)
    colonne = len(A[0])
    S = set()
    for i in range(righe):
        for j in range(colonne):
            if A[i][j] == c:
                S.add((i,j))
    return S