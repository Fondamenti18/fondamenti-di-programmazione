from immagini import *


def test_mini_quad(c,i,j,mypixel_list, test_dim, col,row):
    
    test_col = j + test_dim - 1
    test_riga = i + test_dim -1
    
    if test_riga >= row:
        return False
    if test_col >= col:
        return False
    for k in range(0,test_dim):
        current_riga = i + k
        if current_riga >= row:
            return False
        if(mypixel_list[current_riga][test_col] != c):
            return False 
    for h in range(0,test_dim):
        current_colonna = j  + h
        if current_colonna >= col:
            return False
        if(mypixel_list[test_riga][current_colonna] != c):
            return False 
    return True

def quadrato(filename,c):
    
    mypixel_list = load(filename)
    rows = len(mypixel_list)
    cols = len(mypixel_list[0])
    riga = -1
    colonna = -1
    max_lunghezza_quadrato = -1
    for i in range(0, rows):
        for j in range(0,cols):
            if mypixel_list[i][j] == c:
                
                dim_quadrato = 1
                my_dim_is_real = True
                while my_dim_is_real:
                    test_dim = dim_quadrato + 1
                    
                    my_dim_is_real = test_mini_quad(c,i,j,mypixel_list,test_dim,cols,rows)
                    
                    if my_dim_is_real:
                        dim_quadrato = test_dim
                        
                if dim_quadrato > max_lunghezza_quadrato:
                    max_lunghezza_quadrato = dim_quadrato
                    riga = i
                    colonna = j
    return (max_lunghezza_quadrato,(colonna,riga) )    
        
        