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
    primi=[]
    divisori=0
    radice=0
    resto = 0
    for ind in range(len(ls)-1,-1,-1):
        divisori = 0
        radice = int((ls[ind])**(1/2))+1
        for numero in range(2,radice):
            resto = ls[ind] % numero
            if resto == 0:  
                divisori+=1
            else:
                pass
        fattore = (divisori*2)
        if divisori == 0:
            primi.append(ls[ind])
        if fattore != k:
            del ls[ind]
    primi.reverse()    
    return(primi)


        
                