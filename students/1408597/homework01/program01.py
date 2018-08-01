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

def modi(ls,k):#circa 50 secondi
    lista_primi=[]
    lista=[]
    k_uguali=[]
    for numero in ls:
        if primo(numero):
            lista_primi.append(numero)
        else:
            lista.append(numero)
        conteggio=0
        for div in range(2,(numero+4)//2):
            if numero%div==0:
                conteggio+=1
                if conteggio>k:break
            if div>=20 and conteggio==0:
                break
        if conteggio==k:
            k_uguali.append(numero)
    ls[:]=k_uguali
    return lista_primi
def primo(n):
    k=2
    while k<n and (n%k)!=0:
        k+=1
    return k==n
            

#cd C:\Users\matte\Desktop\homework01
#lista=[70,330,293,154,128,113,178]

#modi(lista,6)
#([293, 113], [70, 154, 128])

#lista=[858659,8640829,777923,178433279,148035889,3125]

#modi(lista,4)
#([], [3125])

#lista=[340887623,26237927,2491,777923,5311430407,6437635961,82284023]

#modi(lista,4)
#([26237927], [])