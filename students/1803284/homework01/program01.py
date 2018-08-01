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
  "creo due liste a partire da ls, una con tutti numeri primi e l'altra con tutti i numeri non aventi 'k' divisori"
  l_nkdev=[]
  l_out=[]
  e=0
  for i in ls: 
    appo=divisori(i,k)
    if appo!=k:
      l_nkdev=l_nkdev+[e] 
    if appo==0:
      l_out=l_out+[i] 
    e+=1
  
  j=0
  for i in l_nkdev:
    del ls[i-j] 	 
    j+=1
  return l_out
def divisori(i,k):
  c=0 
  n=int(i**0.5)
  for j in range(2,n+1):
    if i%j==0:
      if j==n:
        c+=1
      else:
        c+=2
    if c>k:
      break
  return c				 










