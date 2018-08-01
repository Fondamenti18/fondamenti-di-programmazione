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

def modi(ls, k):
    lista_primi=ls.copy()
    lista=ls.copy()
    for n in lista:     # Ciclo per scorre la lista.
        divi=cerca_divisori(n) #eseguo funzione cerca divisori
        num_div=len(divi)
        if num_div!=k: # lo tolgo dalla lista
            ls.remove(n)
        if num_div!=0: #ha almeno un divisore, non è un numero primo 
            lista_primi.remove(n)
            
    return lista_primi

# Funzione cerca divisori
def cerca_divisori(n):
    lista_divisori=[]
    divisore=1
    quoziente=n
    resto=0
    while divisore  < quoziente:
        if resto==0: lista_divisori+=[divisore, quoziente]
        divisore+=1
        quoziente, resto = divmod(n, divisore)
        if divisore==quoziente and resto==0: lista_divisori+=[divisore]
    lista_divisori.sort() # in modo da avere primo e ultimo
    return lista_divisori[1:-1] #elimino primo e ultimo cioè 1 e n

if __name__ == '__main__': # eseguo il test solo se lancio lo script direttamente
    """
    ls=[70,330,293,154,128,113,178]
    ret= modi(ls,6)
    ls=[858659,8640829,777923,178433279,148035889,3125]
    ret= modi(ls,4)
    """
    ls=[10000000116, 10000000431, 10000000469, 10000000548, 10000000697, 10000000711, 10000000768, 10000000924]    
    ret= modi(ls,16)
    print(ls)
    print(ret)            
