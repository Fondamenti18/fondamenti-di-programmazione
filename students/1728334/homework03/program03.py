# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:05:35 2017

@author: Edoardo
"""
from immagini import *
from PIL import Image


def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''
    return main(fname, lista, fnameout)[1]

# Con l'algoritmo floodfill coloro a "macchia" a partire dalla mia coordinata.
def floodfill(coords, image, c1):
    '''
        coords: punto iniziale
        image: nome della mia immagine
        c1: colore da sostituire
    '''
    img = Image.open(image) # carico la mia immagine
    pixels = img.load() # carico tutti i pixel all'interno di questa
    w, h = img.size # width e height per controllare dopo i bordi
    my_set = set(((coords[0], coords[1]), )) # il mio set deve essere pieno per poter ciclare.
    # salvo il colore principale da andare a cambiare
    main_color = pixels[coords[0], coords[1]]
    # controllo che il main colore sia diverso da c1.
    if c1 == main_color:
        raise ValueError("Errore: questo pixel è già con questo colore!")  
    lista_pixels = [(coords[0], coords[1])] # in questa lista salverò tutti i pixel ricolorati
    # se ho qualcosa nel mio set, ciclo    
    while my_set:
        # prendo le mie coordinate (metodo LIFO, last in, first out)
        new_coords = my_set.pop() 
        if pixels[new_coords[0], new_coords[1]] == main_color: # se è il mio colore 
            lista_pixels.append(new_coords) # appendo alla lista dei pixel ricolorati
            pixels[new_coords[0], new_coords[1]] = c1 # setto il nuovo colore
            # adesso devo riempire di nuovo il mio set.
            if new_coords[0] > 0:
                my_set.add((new_coords[0] - 1, new_coords[1])) # vado verso sinistra
            if new_coords[0] < (w - 1):
                my_set.add((new_coords[0] + 1, new_coords[1]))
            if new_coords[1] > 0:
                my_set.add((new_coords[0], new_coords[1] - 1))
            if new_coords[1] < (h - 1):
                my_set.add((new_coords[0], new_coords[1] + 1))
    
    return lista_pixels
        
def recolor_area(lista, img, c1):
    for el in lista:
        img[el[1]][el[0]] = c1
    return img

def ricolora_bordi(img, minimo, massimo, c2):
    #print(minimo, massimo)
    xMax, xMin, yMax, yMin = massimo[0], minimo[0], massimo[1], minimo[1]
    for x in range(xMin, xMax+1):
        img[yMin][x] = c2
        img[yMax][x] = c2
    for y in range(yMin, yMax+1):
        img[y][xMin] = c2
        img[y][xMax] = c2
    return img
        
def main(image, lista, nome):
    img = load(image)
    nc = []
    for el in lista:
        coords = el[0], el[1]
        c1 = el[2]
        c2 = el[3]
        lista_pixel_area = floodfill(coords, image, c1)
        recolor_area(lista_pixel_area, img, c1)
        img = ricolora_bordi(img, min(lista_pixel_area), max(lista_pixel_area), c2)
        lato = int(((len(lista_pixel_area)-1)**0.5)-1)
        perimetro = int(lato*4)
        area = int((lato-1)**2)
        nc.append((area, perimetro))
    return save(img, nome), nc
    