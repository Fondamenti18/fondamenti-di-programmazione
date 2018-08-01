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
   primi=list(ls)
   i=0
   while i < len(ls):
      if dis(ls[i]) != k:
         ls.remove(ls[i])
      else:
         i+=1
         
   i=0
   while i < len(primi):
      if dis(primi[i])!= 0:
         primi.remove(primi[i])
      else:
         i+=1
   return primi

from math import sqrt
def dis(x):
    i=2
    numpropri=0
    while i <= round(sqrt(x)):
       if x%i == 0:
          numpropri += 2
       i+=1
    return numpropri
   
   
