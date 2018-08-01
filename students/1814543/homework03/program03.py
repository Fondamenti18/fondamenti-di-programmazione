from immagini import *

rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)



def get_coord_pixel_adiacenti(immagine,i,j,l,h,col_perimetro,col_interno):
    risultato = []
    my_colore = immagine[i][j]
    if (i+1) < h:
        if (immagine[i+1][j] == my_colore and immagine[i+1][j] != col_perimetro and immagine[i+1][j] != col_interno):
            risultato.append((i+1,j))
    if (j+1) < l:
        if (immagine[i][j+1] == my_colore and immagine[i][j+1] != col_perimetro and immagine[i][j+1] != col_interno):
            risultato.append((i,j+1))
    if (i-1) >= 0:
        if (immagine[i-1][j] == my_colore and immagine[i-1][j] != col_perimetro and immagine[i-1][j] != col_interno):
            risultato.append((i-1,j))
    if (j-1) < l:
        if (immagine[i][j-1] == my_colore and immagine[i][j-1] != col_perimetro and immagine[i][j-1] != col_interno):
            risultato.append((i,j-1))
    return risultato

def is_perimetro(immagine,i,j,l,h, col_interno,col_perimetro):
    
    my_colore = immagine[i][j]
    
    risultato = False
    
    if (i+1) < h:
        if (immagine[i+1][j] != my_colore and  immagine[i+1][j] != col_interno and immagine[i+1][j] != col_perimetro):
            risultato = True
    else:
        return True
    
    
    if (j+1) < l:
        if (immagine[i][j+1] != my_colore and  immagine[i][j+1] != col_interno and immagine[i][j+1] != col_perimetro):
            risultato = True
    else:
        return True
    
    if (i-1) >= 0:
        if (immagine[i-1][j] != my_colore and  immagine[i-1][j] != col_interno and immagine[i-1][j] != col_perimetro):
            risultato = True
    else:
        return True
    
    if (j-1) < l:
        if (immagine[i][j-1] != my_colore and  immagine[i][j-1] != col_interno and immagine[i][j-1] != col_perimetro):
            risultato = True
    else:
        return True
    return risultato

def ricolora(fname, lista, fnameout):
    
    my_img = load(fname)
    
    l = len(my_img[0])
    h = len(my_img)
    
    lista_risultato = []
    
    for item in lista:
        j = (item[0])
        i = (item[1])
        colore_pixel_connessi = item[2]
        colore_pixel_perimetro = item[3]
        
        lista_adiacenze = []
        lista_adiacenze.append((i,j))
        
        num_adiacenze = 1
        
        area = 0
        perimetro = 0
        
        while num_adiacenze > 0:
            my_coordinate = lista_adiacenze.pop()
            num_adiacenze = num_adiacenze - 1
            
            my_i = my_coordinate[0]
            my_j = my_coordinate[1]
            
            my_lista_adiacenze = get_coord_pixel_adiacenti(my_img,my_i,my_j,l,h,colore_pixel_perimetro,colore_pixel_connessi)
            
            
            my_num_adiacenze = len(my_lista_adiacenze)
            
            my_is_perimetro = is_perimetro(my_img,my_i,my_j,l,h,colore_pixel_connessi,colore_pixel_perimetro)
            
            if my_is_perimetro:
                if my_img[my_i][my_j] != colore_pixel_perimetro:
                    my_img[my_i][my_j] = colore_pixel_perimetro             
                    perimetro += 1
            else:
                if my_img[my_i][my_j] != colore_pixel_connessi:
                    my_img[my_i][my_j] = colore_pixel_connessi 
                    area += 1
            num_adiacenze = num_adiacenze + my_num_adiacenze
            lista_adiacenze = lista_adiacenze +  my_lista_adiacenze
        lista_risultato.append((area,perimetro))
    save(my_img,fnameout)
    return lista_risultato
    
    
    