# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:14:48 2017

@author: manuel
"""

from immagini import *
from functools import reduce

class Point():
    def __init__(self, x, y, colore):
        self._x= x
        self._y=y
        self._colore= colore
        

    def get_colore(self):
        return self._colore

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def coords(self):
        return (self._x, self._y)

    def __str__(self):
        return "'(" + str(self.x) + ", " + str(self.y) + ",colore:" + str(self._colore) + ")'"

    def __eq__(self, other):
        return other!= None and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    x = property(get_x, set_x)
    y = property(get_y, set_y)

class Counter():
    def __init__(self):
        self._area = 0
        self._perimeter = 0
        self._S_area = set()
        self._S_perimeter = set()


    def get_area(self):
        return self._area

    def get_perimeter(self):
        return self._perimeter

    def get_S_perimeter(self):
        return self._S_perimeter

    def get_S_area(self):
        return self._S_area

    def increment_perimeter(self):
        self._perimeter += 1

    def decrement_perimeter(self):
        self._perimeter -= 1

    def increment_area(self):
        self._area += 1

    def decrement_area(self):
        self._area -= 1

    def increment_S_perimeter(self, coord):
        self._S_perimeter.add(coord)

    def increment_S_area(self, coord):
        self._S_area.add(coord)

def ricolora(fname, lista, fnameout):
    '''Implementare qui la funzione'''

    img=load(fname)

    x=0
    y=0
    c1=()
    c2=()
    risultato=[]

    for riga in lista:
        counter = Counter()
        x, y = riga[0], riga[1]
        c1 = riga[2]
        c2 = riga[3]
        colore_punto = img[y][x]
        punto_iniziale = Point(x, y, colore_punto)
        traverse_pixels(img, punto_iniziale, colore_punto, c1, c2, counter)
        #risultato.append((counter.get_area(), counter.get_perimeter()))
        risultato.append((len(counter.get_S_area()), len(counter.get_S_perimeter())))

    save(img, fnameout)

    return risultato

def traverse_pixels(img_matrix, point, base_color, area_color, perimeter_color, counter):
    # define a stack to accumulate pixels to be processed
    pixel_stack = []
    # fill the stack with the firs pixel to be processed
    pixel_stack.append(point)

    # define a dictionary to associate points to counters to exclud a point when it has been visited from all of its neighbors
    exclusion_dictionary = {}

    # iterate until the stack is empty
    while pixel_stack:
        current_point = pixel_stack.pop() # take the last appended value from the stack
        
        if current_point in counter.get_S_area() or current_point in counter.get_S_perimeter(): continue # aggiunta
        
        # get all valid adjacent points
        adjacency_list = get_adjacents(img_matrix, current_point, exclusion_dictionary, base_color)

        # get the correct color checking the adjacent points
        color = get_color2(current_point, adjacency_list, base_color, area_color, perimeter_color, counter)

        # paint the current pixel with the given color
        paint2(img_matrix, current_point, color, perimeter_color, area_color, counter)

        # add an entry to the eclusion dicctionary so in the next iterations the current point will be excluded
        exclusion_dictionary[current_point.coords()] = len(adjacency_list)

        # add adjacent points to the processing stack for the next iteration
        [pixel_stack.append(p[0]) for p in adjacency_list if p[1] == 1]


def paint2(img_matrix, current_point, color, perimeter_color, area_color, counter):
    #print("scrivo colore:", color, "a:", current_point.coords())
    img_matrix[current_point.y][current_point.x] = color


def get_color2(current_point, adjacency_list, base_color, area_color, perimeter_color, counter):
    # if there are less than four adjacent pixels it is at the end of the image. return perimeter color.
    if(len(adjacency_list) < 4):
        counter.increment_S_perimeter(current_point)
        return perimeter_color

    # if a point which is not excluded has a different color from base_color return perimeter_color
    for p in adjacency_list:
        if p[1] and p[0].get_colore() != base_color:
            counter.increment_S_perimeter(current_point)
            return perimeter_color

    # if none of the other conditions are tue return area_color
    counter.increment_S_area(current_point)
    return area_color


def get_adjacents(img_matrix, current_point, exclusion_dictionary, base_color):
    pU = extract_point(img_matrix, current_point.x, current_point.y - 1)
    pD = extract_point(img_matrix, current_point.x, current_point.y + 1)
    pL = extract_point(img_matrix, current_point.x - 1, current_point.y)
    pR = extract_point(img_matrix, current_point.x + 1, current_point.y)

    # remove None values
    not_none = [pt for pt in [pU, pD, pL, pR] if pt != None]
    result = []
    for current_point in not_none:
        #check if the current point is marked for exclusion
        if current_point.coords() in exclusion_dictionary:
            exclusion_count = exclusion_dictionary[current_point.coords()] # get the count for the excluded point

            # if the current point has been visited from all neighbors remove it from the list, otherwise decrement the visitors counter
            if(exclusion_count):
                exclusion_count - 1
            else:
                del exclusion_dictionary[current_point.coords()]

            # appent the point to the adjacents list indicating this point does not need to be visited
            result.append((current_point, 0))
        else:
            # here the poont needs to be visited but we signal the fact that this point is different from base color
            if(current_point.get_colore() != base_color):
                result.append((current_point, 2))
            else:
                result.append((current_point, 1))

    return result

def extract_point(img, x, y):
    if inside(img, x, y):
        return Point(x, y, img[y][x])
    else:
        return None

def inside(img, x, y):
    '''Verifica se il pixel di coordinate x,y è contenuto nella immagine'''
    return 0 <= x < width(img) and 0 <= y < height(img)

def width(img):
    return len(img[0]) # è la prima riga mi da le colonne e dunque la larghezza

def height(img):
    return len(img) # numero di righe quindi l'altezza della matrice

if __name__ == '__main__':

    rosso = (255,   0,   0)
    blu   = (  0,   0, 255)
    verde = (  0, 255,   0)
    nero  = (  0,   0,   0)
    bianco= (255, 255, 255)
    giallo= (255, 255,   0)
    cyan  = (  0, 255, 255)
    magenta= (255,  0, 255)


    #args        = ('me.png',[(5,2,bianco,blu)],'test1.png')

    #args        = ('I1.png',[(10,10,rosso,blu)],'test1.png')
    #args        = ('I1.png',[(10,10,rosso,blu),(90,10,nero,verde)],'test2.png')
    #args        = ('I1.png',[(10,10,bianco,blu),(90,10,verde,rosso)],'test3.png')
    #lista=[(i*30+1,j*30+1,bianco,verde) for i in range(10) for j in range (10)if not (i+j)%2]
    #args       = ('I2.png',lista,'test4.png')
    #lista0=[(i*30+1,j*30+1,nero, verde) for i in range(10) for j in range (10)if not (i+j)%2]
    #lista1=[(i*30+1,j*30+1,rosso,bianco) for i in range(10) for j in range (10)if  (i+j)%2]
    #args        = ('I2.png',lista0+lista1,'test5.png')

    #lista=[(25,25,(0,0,0),(0,5*i,5*i)) for i in range(1,25)]
    #args = ('I1.png',lista,'test6.png')
    #lista=[(0,0,(0,0,0),(0,5*i,5*i)) for i in range(1,25)]
    #args        = ('I1.png',lista,'test7.png')
    #lista=[(5*i+2,5*i+2,(0,255-6*i,0),(0,0,255-6*i)) for i in range(40)]
    #args        = ('I3.png',lista,'test8.png')
    #lista=[(100,100,(255-x,255,255),(0,0,255-x)) for x in range(100)]
    #args        = ('I4.png',lista,'test9.png')
    #lista=[(1,1,(255,255,255),(255,255,255)),(1,1,(255,0,0),(255,0,0))]*40
    #args        = ('I5.png',lista,'test10.png')
    #lista=[(200+j,200+j,(255-i,255*j,0),(255*j,255-i,0))for i in range(10) for j in range(2)]
    #args        = ('I6.png',lista,'test11.png')
    lista=[(204,204,(0,250,0),(240,0,250))for i in range(10) ]
    args        = ('I7.png',lista,'test12.png')

    ret=ricolora(*args)
    print(ret)
