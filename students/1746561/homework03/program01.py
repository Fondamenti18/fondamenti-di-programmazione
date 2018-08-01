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

import time
from immagini import *

def width(img): return len(img[0]) #ampiezza/n.colonne
def height(img): return len(img) #altezza/n.righe 
def inside(img,i,j):
    w, h=width(img),height(img)
    return 0<=i<w and 0<=j<h


def process(img, c): #crea lista con x e lista con y
    lj = []
    li = []
    for j in range(height(img)):
        for i in range(width(img)):
            if img[j][i] == c:
                lj.append(str(j))
                li.append(str(i))
                if img[j][i+1] != c: li.append('|')
                if img[j+1][i] != c: lj.append('|')
    il = [l.split(',') for l in ','.join(li).split('|')]
    jl = [l.split(',') for l in ','.join(lj).split('|')]
    return jl,il

def clean(ls): #alleregisce lista e organizza subliste uguali
    l_ext = []
    for i in ls:
        l_int = []
        for j in range(len(i)-1,-1,-1):
                try: l_int.append(int(i[j]))
                except ValueError: pass
        l_ext.append(tuple(l_int))
    return list(reversed(sorted(set(filter(None,tuple(l_ext))))))

def create_dic(st):
    dic ={}
    for i in st:
        try: dic.update({len(i):i})
        except ValueError: pass
    return dic
        
def quadrato(filename,c):
    img = load(filename)
    lj, li = process(img, c)
    lj ,li = clean(lj), clean(li)

    kx, vx = tuple(create_dic(clean(li)).keys()), tuple(create_dic(clean(li)).values())
    ky, vy = tuple(create_dic(clean(lj)).keys()), tuple(create_dic(clean(lj)).values())
    #x_left = vx[kx.index(min(kx))]
    x_right = vx[kx.index(max(kx))] #lunghezza lato quadrato più grande
    #y_top = vy[ky.index(min(ky))]
    #y_bottom = vy[ky.index(max(ky))]
    left = min(vx[kx.index(max(kx))])  #punto più a sinistra
    up = min(vy[ky.index(max(ky))]) #punto più in alto
    
    return (len(x_right), (left,up))
if __name__ == '__main__':
    start = time.time()
    print(quadrato('Ist2.png',(255,0,0)))
    print('---- %s seconds ---' %(time.time() - start))
    