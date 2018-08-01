
from immagini import *
from IPython.display import Image
   
def quadrato(filename,c):
    img = load(filename)
    h = heigth(img)
    w = width(img)
    ls_all=[]
    ls_all = crea_res_matrix(crea_bin_mat(img,h,w,c),h,w)
    max_lato = max(ls_all)
    pos = ls_all.index(max_lato)
    coordinate = ((pos-(w*(pos//w)))-max_lato+1,(pos//w)-max_lato+1)
    return (max_lato,coordinate)

    
def crea_bin_mat(img,h,w,color):
    matrix = []
    for y in range(h):
        matrix.append([])
        for x in range(w):
            if img[y][x] == color: matrix[y].append(1)
            else: matrix[y].append(0)
    return matrix 


def crea_res_matrix(matrix,h,w):
    ls_all = []
    ls_all = matrix[0]
    res_mat = matrix.copy()
    for y in range(1,h):
        ls_all.append(matrix[y][0])
        for x in range(1,w):
            if matrix[y][x]==0:
                ls_all.append(0)
                res_mat[y][x] = 0
            else:
                ls_all.append(min(res_mat[y][x-1],res_mat[y-1][x-1],res_mat[y-1][x])+1)
                res_mat[y][x] = ls_all[-1]
    return ls_all

        
def heigth(img) : return len(img)
def width(img) : return len(img[0])