def div_propri(n):
    rad = (n ** 0.5)
    indice = 2
    numero = 0
     
    while indice < rad:
        
        if n % indice == 0:
            print('valori indice, rad, n', indice, rad, n)
            numero += 2
            
        indice += 1
        
    if rad % 1 == 0:
                print('valori numero, rad', numero, rad)
                numero += 1
    return numero

def modi(ls, k):
    lista_primi = []
    indice = 0 
    
    while indice < len(ls):
        
        richiamo = div_propri(ls[indice])
        
        if richiamo == 0:
            lista_primi.append(ls[indice])
            print('lista primi', lista_primi)
            
        if richiamo != k:
                del ls[indice]
        else:
            indice += 1
    return lista_primi