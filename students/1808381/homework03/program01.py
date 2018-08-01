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

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    img = load(filename)
   
    matrice = creaMatrice(img, c)
    
    return trova(matrice)
    

    
    
def creaMatrice(img, c):    
    
    matrice = []
    matriceVuota = []
    for i in range(len(img)):
        
        matrice += [[1 if img[i][j] == c else 0 for j in range(len(img[i]))]]
        matriceVuota += [[[] for j in range(len(img[i]))]]
        
        for j in range(len(img[i])):  
            if i == 0 or j == 0:
                matriceVuota[i][j] = matrice[i][j]
            if not matrice[i][j]:
                matriceVuota[i][j] = 0
            else:
                if matriceVuota[i-1][j-1] == []:
                    matriceVuota[i-1][j-1] = 0
                if matriceVuota[i-1][j] == []:
                    matriceVuota[i-1][j] = 0
                if matriceVuota[i][j-1] == []:
                    matriceVuota[i][j-1] = 0
                matriceVuota[i][j] = min(matriceVuota[i-1][j-1], matriceVuota[i-1][j], matriceVuota[i][j-1])+1
    
    return matriceVuota


def trova(matrice):
    lista = []
    listaMassimi = []
    a = []
    listaMassimi += [max(matrice[i]) for i in range(len(matrice))]
    lista += [((matrice[i].index(max(matrice[i]))), i) for i in range(len(matrice))]
    
    for cordinata in lista[listaMassimi.index(max(listaMassimi))] :
        cordinata = cordinata - max(listaMassimi) + 1
        a += [cordinata]
    return max(listaMassimi), tuple(a)      