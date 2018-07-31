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

def controllo_pixel(pixel,colore):
    vero = False
    if pixel == colore:
        vero = True
    return vero

def controllo_quad(img,colore,lun,r_quad,c_quad,part_r,part_c):
    vero = False
    range_r=r_quad
    range_c=c_quad  
    restart=part_c
    while part_r<=range_r:
        part_c=restart
        while part_c<=range_c:     
            if img[r_quad][c_quad]==colore :
                vero = True
            else:
                vero = False
                break
            r_quad+=1
            part_c+=1
        c_quad+=1
        part_r+=1
    return vero

def quadrato(filename,C):
    '''Implementare qui la funzione'''
    img = load(filename)
    r = 0
    c = 0
    lun = 0
    part=0 #partenza
    part_r=0
    part_c=0
    lun_max = 0
    rig = -1
    col = -1
    primo = True
    print(len(img))
    print(len(img[0]))
    while r < len(img):
        c = 0
        while c < len(img[0]):
            
            app = controllo_pixel(img[r][c],C)
            
            if app == True:
                lun += 1
                part+=1
                if part==1:
                    part_r=r
                    part_c=c
                    rig = r
                    col = c
                if primo == True:
                    lun_max = lun
                    rig = r
                    col = c
                    col_max=col
                    rig_max=rig
                    primo = False
                
                if lun > 1:
                    c_quad=c
                    r_quad=r
                    if controllo_quad(img,C,lun,r_quad,c_quad,part_r,part_c) == True:
                        if lun_max < lun:
                            lun_max = lun
                            col_max=col
                            rig_max=rig
                    else:
                        lun = 0
                        part=0
                        rig = 0
                        col = 0
            else:
                lun = 0
                part=0
            c += 1
        r += 1
    return lun_max,(col_max,rig_max)

                                
    





 



