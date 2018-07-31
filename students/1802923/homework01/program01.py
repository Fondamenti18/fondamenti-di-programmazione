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

def k_divisori(a, k):
  x = 0
  for i in range(2, a):
    if a % i == 0:
      x += 1
    if x > k:
      return False

  if x == k:
    return True
  else:
    return False

def primo(a):
  x = 0

  for i in range(2, a):
    if a % i == 0:
      return False
  
  return True
  

def modi(ls, k):
  
  out = []

  # TRICK DE DARIO
  p = ls[:]

  for i in p:
    if primo(i):
      # print(i)
      # print('è primo')
      out.append(i)
      ls.remove(i)
    else:
      # print(i)
      # print('NON è PRIMO')
      if not k_divisori(i, k):
        # print('E NON HA k DIVISORI')
        ls.remove(i)

  return out

  
