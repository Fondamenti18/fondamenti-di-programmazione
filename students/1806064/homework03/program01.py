from immagini import *
def quadrato(file,c):
    matrice=load(file)
    altezza=len(matrice)
    larghezza=len(matrice[0])
    a=cercapx(matrice,altezza,larghezza,c)
    matrice_con_indice=indice_c(matrice,altezza,larghezza,c)
    output=cerca_quadrato(altezza,larghezza,matrice_con_indice,a)
    return output

def indice_c(matrice,altezza,larghezza,c):
    matrice_indici=[]
    for j in range(altezza):
        intervalli=set()
        for i in range(larghezza):
            if matrice[j][i]==c:
                intervalli.add(i)
        matrice_indici.append(intervalli)
    return matrice_indici

def verifica_intervallo(intervallo,dimensione_quadrato):
    c=0
    i=0
    intervallo=sorted(intervallo)
    coordinate_quadrato=[]
    lista_intervallo=[]
    intervallo=list(intervallo)
    while i<len(intervallo)-1:
        if intervallo[i]==intervallo[i+1]-1:
            c=c+1
            lista_intervallo.append(intervallo[i])
        else:
            c=0
            lista_intervallo=[]
        if c==dimensione_quadrato-1:
            lista_intervallo.append(intervallo[i+1])
            return lista_intervallo[0]
        i=i+1
    return "x"
            
            
def cerca_quadrato(altezza,larghezza,matrice,a):
    dimensione_quadrato=2
    maxx=()
    j=0
    while j+dimensione_quadrato<=altezza:
        intersezione=matrice[j]
        for i in range(dimensione_quadrato):
            intersezione=intersezione&matrice[j+i]
        x=verifica_intervallo(intersezione,dimensione_quadrato)
        if x!="x":
            dimensione_quadrato+=1
            maxx=(dimensione_quadrato-1,(x,j))
            j=0
        j=j+1
    if maxx==():
        return (1,a)
    return maxx

def cercapx(matrice,altezza,larghezza,c):
    for i in range(altezza):
        for j in range(larghezza):
            if matrice[i][j]==c:
                return (j,i)



        
        
            
            
        
    
    
        
        
            
            
        
        
        
        
        
        
        
    
    
            


                
                
                
                
                
                        
                
                
                
        
            
            
            
                
                
    
                

    
    




        
        
            
            
        
    
    
        
        
            
            
        
        
        
        
        
        
        
    
    
            


                
                
                
                
                
                        
                
                
                
        
            
            
            
                
                
    
                

    
    
