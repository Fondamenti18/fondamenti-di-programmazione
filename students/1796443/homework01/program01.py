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
def verifica_primo(a):
    "Dato un intero non negativo a, ritorna True se primo, False altrimenti"
    c=3
    if a<=3:
        return True
    if a>3 and a%2==0:
        return False
    if a>3:
        b=int(a/2)
        while c<=b:
            if a%c==0:
                return False
            c+=2
        return True

def verifica_k_divisori(a,k):
    "Dati 2 interi a k, ritorna True se a ha esattamente k divisori propri, False altrimenti"
    if a<=3 and k!=0:
        return False
    x=[]
    ls1=[]
    c=2
    u=1
    b=a
    p=int(a/2)
    while c<=a:
        if b%(c**u)==0:
            if not c**u in x and (c**u)!=b:
                x+=[c**u]
                a=int(a/c)
            if not a in x and a!=1 and b%a==0:
                x+=[a]
            if u==1:
                y=[]
                y[:]=x
                for i in y:
                    d=i*c
                    if not d in x and d<=p and b%d==0:
                        x+=[d]
            u+=1
        else:
            c+=1
            u=1
        if len(x)>k:
            return False
    ls1[:]=x
    for i in x:
        for t in ls1:
            if not (i*t) in x and (i*t)<=p and b%(i*t)==0:
                x+=[i*t]    
    if len(x)==k:
        return True
    else:
        return False 

def cancella_interi(ls,k):
    "Data una lista di interi ls e un intero k, rimuove da ls tutti gli interi che non hanno k divisori propri e ritorna ls"
    c=0
    while c<len(ls):
        if not (verifica_k_divisori(ls[c],k)):
            ls.pop(c)
        else:
            c+=1

def modi(ls,k):
    "inserite qui il vostro codice"
    ls2=[]
    for i in ls:
        if verifica_primo(i):
            ls2+=[i]
    if k>0:
        c=len(ls)-1
        while c>=0:
            if ls[c] in ls2:
                del ls[c]
            c-=1
    cancella_interi(ls,k)
    return ls2