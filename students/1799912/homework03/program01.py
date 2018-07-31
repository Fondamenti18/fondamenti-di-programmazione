'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolor_pixel rettangoli 
di vari coordinateslori i cui assi sono sempre parallei agli assi dell'image.

Vedi ad esempio l'image Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percoordinatesrso di un file (filename) che coordinatesntine un image in formato png della  tipologia appena descritta.
- una tupla C che rappresenta un color_pixel in formato RGB (3 valori interi tra 0 e 255 coordinatesmpresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e color_pixel C interamente visibile nell'image. 
- le points  (x,y)  del pixel dell'image che coordinatesrrisponde alla posizione 
all'interno dell'image del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va coordinatesnsiderato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la coordinateslonna minima) all'interno dell' image. 

Si può assumere che nell'image e' sempre  presente almeno un pixel del color_pixel cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secoordinatesndi (coordinatesn N numero di test del grader).
'''

from immagini import *


def quadrato(filename,c):
    image=load(filename)
    points=()
    x=0
    y=0
    big=0
    new_points=()
    spigolo_quad,points,x=Draw_square(image,y,c,x)
    y=y+1
    big,new_points =ctr(big,image,x,y,spigolo_quad,points,c,new_points)
    return big,new_points






def ctr(big,image,x,y,spigolo_quad,points,c,new_points):
     while y<len(image):
        if x>=len(image):
            x=0
        while x<len(image):
            x=x+1
            spigolo_quad,points,x=Draw_square(image,y,c,x)
            if spigolo_quad>big:
                big=spigolo_quad
                new_points=points
            y=y+1
     return big,new_points



def Draw_square(picture,ax,color_pixel,by):
    lato_quad_1=0
    lato_quad_2=0
    center=ax
    square=0
    big=0
    coordinates=()
    while interno(picture,by,ax)==True and picture[ax][by]!=color_pixel :
        by=by+1
    if interno(picture,by,ax)==True and picture[ax][by]==color_pixel:
        coordinates=(by,ax)
        while picture[ax][by]==color_pixel:
            lato_quad_1+=1
            by=by+1
        by=by-1
        while picture[ax][by]==color_pixel and lato_quad_2<lato_quad_1:
            lato_quad_2+=1
            ax+=1
            if lato_quad_1==lato_quad_2:
                square=lato_quad_1
    return square,coordinates,by
                
            
                
def interno (img,ix,jy):
    iw,ih=len(img[0]),len(img)
    return 0<=ix<iw and 0<=jy<ih                    
                                    
                





            

                
                

                
                
 
                
                

            
