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

def calcolaNumeroDivisori(numero, divisoriMassimi):
    k = 2
    numeroDivisori = 0
    divisoriPrimi = {}
    
    radiceNumero=numero**0.5
    while (numero > 1):
       if (k > radiceNumero):
           k = numero
       if ((numero % k)==0):
            if (k in divisoriPrimi):
                divisoriPrimi[k] += 1
            else:
                divisoriPrimi[k] = 1
            numeroDivisori += 1
            numero /= k
            radiceNumero = numero**0.5
            k = 1
            if (calcolaDivisoriTotali(divisoriPrimi)>divisoriMassimi):
                break
       k += 1
        
    return divisoriPrimi
        
def calcolaDivisoriTotali(listaDivisori):
    numeroTotale = 1
    for d in listaDivisori:
        numeroTotale *= (listaDivisori[d] + 1)
    return numeroTotale - 2 


def modi(ls,k):
    listaBocciati=[]
    listaPrimi=[]
    for numero in ls:
        numeroDiDivisori = calcolaDivisoriTotali(calcolaNumeroDivisori(numero, k))
        if (numeroDiDivisori==0):
            listaPrimi+=[numero]
        if (numeroDiDivisori!=k):
            listaBocciati+=[numero]
            
    for numero in listaBocciati:
        ls.remove(numero)

    return listaPrimi
    
