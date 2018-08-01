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

# creo una funzione per sapere se un numero è primo oppure no 

def primo(num):
    for n in range(2,num):
        if num % n == 0:
          return False
    return True 

#creo una funzione per trovare i divisori di un numero

def divisori(num, k):
    acc =0
    equals = False
    for n in range(2,num):
        if num % n == 0:
            acc+=1
        if (acc==k):
            equals = True
        if (acc>k):
            return False
    return equals

# applico le funzioni che ho creato alla funzione modi 
           
def modi(ls,k):
    to_delete=[]
    prime_list=[]
    for el in ls:
        if primo(el):
            prime_list.append(el)
            to_delete.append(el)
        elif not divisori(el,k):
            to_delete.append(el)
    for temp in to_delete:
        ls.remove(temp)
    return prime_list

  
