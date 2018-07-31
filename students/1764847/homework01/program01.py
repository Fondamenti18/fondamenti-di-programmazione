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
    '''Modifica la lista passata in input, cancellando tutti gli interi
    che non hanno esattamente k divisori propri e restituisce una seconda lista
    che contiene i soli numeri primi della lista in input'''
    listaDivisori = []                                          
    lst = []                                                    
    for i in range(len(ls)):                                               
        listaDivisori.append(calcolaDivisori(fattorizza(ls[i])))                                                     
        if listaDivisori[i] == 0:                              
            lst.append(ls[i])                                   
    index = 0
    for j in range(len(ls)):                                   
        if listaDivisori[j] != k:                               
            ls.remove(ls[index])                                
            index -= 1
        index += 1
    return lst




def fattorizza(n):
    '''Preso in input un numero, restituisce una lista contenente il numero 
    fattorizzato'''
    import math
    lst = []
    c = 2
    esponente = 0
    m = n
    while n > 1:
        if c > math.sqrt(m) and n != 1:
            lst.append(1)
            break
        if n%c == 0:
            esponente += 1
            n = n/ c
        else:
            if esponente > 0:
                lst.append(esponente)
                esponente = 0
            c += 1
    lst.append(esponente)
    return lst


def calcolaDivisori(lst):
    '''Presa in input una lista contenente il numero fattorizzato dalla funzione 
    fattorizza(), restituisce il numero di divisori del numero'''                                             
    risultato = 1                                                                               
    for j in lst:                                             
        risultato *= j+1                                        
    return risultato - 2                                        
