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
    massimo=k
    listaprimi=[]
    lista2=[]
    for i in ls:
        primo= True
        contak=0
        for a in range(2,int(i/2)+2):
            if i%a==0:
                primo= False
                contak=contak+1
            if contak>massimo:
                break
        if contak!=massimo:
            lista2.append(i)
        if primo:
            listaprimi.append(i)
    for i in lista2:
        ls.remove(i)
    return(listaprimi)
            









    
    
    
    
