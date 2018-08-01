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
import math
def num_divisori(x):
    num = 0;
    i = 2;
    d = math.sqrt(x)
    while i<d:
        if x%i == 0:
            num += 2;
        i += 1;
    if d % 1 == 0:
        num +=1;
    return num;
    
def modi(ls,k):
    i = 0;
    primi = [];
    while i < len(ls):
        app = num_divisori(ls[i]);
        if app == 0:
            primi.append(ls[i]);
        
        if app != k:
            ls.pop(i);
        else:
            i += 1;
    return primi;