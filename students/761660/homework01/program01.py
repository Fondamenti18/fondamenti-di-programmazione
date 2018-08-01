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
l1=[]
ls=[]
def primi (a):
    b=2
    if ((b**(a-1))% a)==1:
        return True
    return False

def modi(ls,k):
    lp=[]
    for i in ls:
        b=i
        if primi(b)==True:
            lp+=[b]
            ls.remove(b)    
    l1=ls[:]
    for e in l1:
        conta=0
    
        for d in range(2,e,1):
             if(e%d==0):
                  conta+=1
             if(conta>k):
                  ls.remove(e)
                  break   
        if((e in ls) and (conta<k or conta>k)):
            ls.remove(e)
    return lp     
   


