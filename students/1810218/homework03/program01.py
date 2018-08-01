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


def f(R,C,M,S):
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1 :
                S[i][j] = min(S[i][j-1],min(S[i-1][j], S[i-1][j-1])) + 1
            else:
                S[i][j] = 0	 	

                

def trova(img,colore):
    lista=[]
    
    for i in img:
        temp=[]
        for j in i:        
            if j != colore:
                temp.append(0)
            else:
                temp.append(1)
        lista.append(temp)
    return lista

def quadrmax(M):
    i=0
    j=0
    R = len(M)
    C = len(M[0])
    S = M
    max_of_s = 0
    max_i = 0
    max_j = 0 		
    
    f(R,C,M,S)

    
    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    for i in range(R):
        for j in range(C):
            if max_of_s < S[i][j]:
                max_of_s = S[i][j]
                max_i = i
                max_j = j
    coord = max_j-max_of_s+1,max_i-max_of_s+1
    lato = max_of_s
    return (lato,coord)

def quadrato(filename,C):
	img_ = load(filename)
	tem= trova(img_,C)
	return quadrmax(tem)

