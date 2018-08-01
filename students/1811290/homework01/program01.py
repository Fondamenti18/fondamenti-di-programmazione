'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno
e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero 
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori
    propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16] 
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine
della funzione si avra' che la lista ls=[16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio
e' zero.
'''

def modi(ls,k):
    listapri=[]
    import copy
    ls1=copy.copy(ls)
    i=0
    for x in ls1:
        if divprop(x)!=k:
            ls[i:i+1]=[]
            i-=1
        i+=1
        if verifica(k,x)==True:
            if primo(x)==True:
                listapri+=[x]
            listapri+=[]
    return listapri

def verifica(k,x):
    if k<=1 or k==x:
        return False
    return True


def divprop(x):
    import copy 
    z=copy.copy(x)
    lista2=[]
    lista3=[]
    for y in range(2,z):
        if y<z:
            if x%y==0:
                lista2+=[y]
                if y!=x/y:
                    lista3+=[x/y]
                    z=x/y
        else:
            break
    lista2+=lista3
    return len(lista2)


def primo(x):
    i=2
    while i<x and x%i!=0:
        i+=1
    return i==x


