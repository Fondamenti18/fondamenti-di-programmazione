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
    la=[] 
    primi=[]
    for numero in ls:
        conteggio=calcola(numero)
        if conteggio==k: #se iil conteggio è uguale a k appende il numero ad la
            la.append(numero)
        elif conteggio==0:#se il conteggio è uguale a 0 appende il numero a primi
            primi.append(numero)
    ls=modifica(ls,la)
    return primi

def calcola(numero):
    '''ritorna il numero dei divisori'''
    lista=[]
    n=2
    while n<int(numero/2)+1 and n<=numero//n: #per tutti gli n da 2 fino al numero/2 se n<=numero/n 
        if numero%n==0 : #se n è un divisore appende alla lista sia n sia numero/n
            lista.append(n)
            lista.append(numero//n)
        n+=1
    return len(lista) #ritorna il numero degli elementi della lista ossia il numero dei divisori

def modifica(l1,l2):
    '''modifica l'originale l1'''
    i=0
    while i<len(l1):
        if l1[i] not in l2:
            l1.remove(l1[i]) #elimina tutti gli elementi di l1 che non sono in l2
        else:
            i+=1
    return l1 #ritorna la nuova l1 che viene sostituita all'originale