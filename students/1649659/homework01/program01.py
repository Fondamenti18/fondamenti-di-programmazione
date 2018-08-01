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
def fattori(numero):
    x=2
    lista=[]
    numero_or=numero
    while x<numero :
        if numero%x==0 :
            numero=numero//x
            if x not in lista :
                lista.append(x)
            x=x-1
        x+=1
        for i in lista: 
            if numero_or%(i*x)==0 and i*x!=numero_or and (i*x)not in lista:
                lista.append(i*x)
    if x==numero and x!=numero_or and x not in lista : 
        lista.append(x)
    return len(lista)
    
def modi(ls,k):
    lista_ret=[]
    lista_ls=[]
    lista_scar=[]
    for j in ls : 
        if fattori(j)==0:
            lista_ret.append(j)
    for i,valore in enumerate(ls): 
        if fattori(ls[i])!=k:
            lista_scar.append(valore)
    for i in lista_scar:
            ls.remove(i)
    return lista_ret