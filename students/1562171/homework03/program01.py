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




def load(fname):
    """ Carica la immagine PNG dal file fname.
        Torna una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    with open(fname, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return img

def save(img, filename):
    """ Salva la immagine img  nel file filename in formato PNG8.
        Img e' una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)

def posizionemassimolato(listalati,mass):
    for i in range(0,len(listalati)):
        if(listalati[i]==mass):
            return i

def cercaquadrato(x,y,colore, matrice):
    lato=1
    if(x+1>=len(matrice)or(y+1>=len(matrice[0]))):
           return lato
    while((matrice[x+1][y]==colore)and(matrice[x][y+1]==colore)):
        x=x+1
        y=y+1
        lato=lato+1
        if(x+1>=len(matrice)or(y+1>=len(matrice[0]))):
           break
    return lato

def quadrato(filename,c):
    imm=load(filename)
    lista=[]
    listaris=[]
    lato=0
    for h in range(0,len(imm)):
        for j in range(0,len(imm[0])):
            
            if(imm[h][j]==c):
                lato=cercaquadrato(h,j,c,imm)
                lista+=[lato]
                listaris+=[(j,h)]
    pos=posizionemassimolato(lista,max(lista))
    return(lista[pos],listaris[pos])
    
  

