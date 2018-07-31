'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def modi(ls,k):
    "inserite qui il vostro codice"
   
    l1 = ls[:]
    divisori1 = []
    divisori = divisoriPropri(ls)
          #lista contenente le liste dei divisori propri
       
    for intero, lista in zip(ls,divisori):
        divisori1.append([int(intero/elemento) for elemento in lista if intero % elemento == 0])
    
    
    for lista, lista1 in zip(divisori,divisori1):
        lista += lista1
        
      
     
    indice = estraiIndice(divisori, k) 
        
     
    ls[:] = elimina(ls, indice)
    print(ls)
    return numeriPrimi(l1, divisori)
    
    
    
    

def numeriPrimi(ls, divisori):
    "estrae i numeri primi"
    numeri = []
    
    numeri += [intero for intero, divisore in zip(ls, divisori) if divisore == []]
    return numeri
     



def elimina(ls, indice): 
    "restituisce la lista con gli elementi finali"
   
    return [intero for intero in (ls) if ls.index(intero) in indice ]



def estraiIndice(divisori, k):
    "estrae l'indice di ogni elemento con divisori = k"
    
    return [divisori.index(lista) for lista in divisori if len(lista) == k]
     

def divisoriPropri(ls):
    "restituisce i divisori propri di ogni intero dato"
    from math import sqrt
    return [[divisore for divisore in range(2, int(sqrt(intero)+1)) if intero % divisore == 0] for intero in ls]
    

if __name__ == '__main__' : 
    lista=[340887623,26237927,2491,777923,5311430407,6437635961,82284023]
    print(modi(lista,4))
            

