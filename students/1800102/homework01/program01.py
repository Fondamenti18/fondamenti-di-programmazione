from math import sqrt

def modi(ls, k):
    
    Fattori_primi = Scomposizione_in_fattori_primi(ls, k)
    Numeri_primi = Stampa_numeri_primi(ls, k)
    ls = Elimina_elementi(ls, k)
    
    return Numeri_primi


def Scomposizione_in_fattori_primi(ls, k):

    c = 0
    n = 0
    Fattori_primi = []
    
    for a in range(len(ls)):
        
        if ls[a] % 2 == 0:
            
            for b in range(2, int(sqrt(ls[n])) + 1, 1):
            
                if ls[n] % b == 0: 
                
                    c += 1
                    
        else:
            
            for b in range(3, int(sqrt(ls[n])) + 1, 2):
            
                if ls[n] % b == 0:
                    
                    c += 1
                    
        Fattori_primi += [c * 2]
        c = 0
        n += 1
        
    return Fattori_primi
        
def Stampa_numeri_primi(ls, k):
    
    N_fattori_primi = Scomposizione_in_fattori_primi(ls, k)
    Numeri_primi = []
    
    for a in range(len(ls)):
      
        if N_fattori_primi[a] == 0 or N_fattori_primi == 1: Numeri_primi += [ls[a]]
        
    return Numeri_primi


def Elimina_elementi(ls, k):
    
    N_fattori = Scomposizione_in_fattori_primi(ls, k)
    i = 0
    
    for a in ls[:]:
        
        if N_fattori[i] != k: ls.remove(a)
            
        i += 1
        
    return ls