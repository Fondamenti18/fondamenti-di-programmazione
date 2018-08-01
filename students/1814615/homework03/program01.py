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

#from immagini import *
import png
 
def quadrato(filename,c):
    '''Implementare qui la funzione'''
    with open(filename, mode='rb') as f:
            reader = png.Reader(file=f)
            w, h, png_img, _ = reader.asRGB8()
            img = []
            for line in png_img:
                l = []
                for i in range(0, len(line), 3):
                    l+=[(line[i], line[i+1], line[i+2])]
                img+=[l]

#    img=load(filename)
    massimo=0
    ret=(0,(0,0))
    test=0
    a=0
    for x in range(len(img)):
        #print("X="+str(x)+ " ")
        for y in range(len(img[0])):
            if c==img[x][y]:

                i=1
                test=0
                while (test==0 and x+i<len(img) and y+i<len(img[0]) and y+massimo<len(img[0]) and x+massimo<len(img)):
                    if img[x][y+massimo]!=c or img[x+massimo][y]!=c: break
                    for a in range(i):
                        if img[x+a][y+i]!=c or img[x+i][y+a]!=c: test=1                  
                    if test==1: break
                    i=i+1
                if i>massimo:
                    
                    massimo=i
                    ret=(i,(y,x))
                    

                

    return ret


