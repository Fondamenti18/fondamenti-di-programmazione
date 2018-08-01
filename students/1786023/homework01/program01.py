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

#Create list
#Save populate list with user data
#Get divider times , Save K

#Function
#Find prime numbers
import math
def findPrimes(listing):
    primeList=[]
    #Run thouth the list
    for i in range(len(listing)):
        #if the listing [i] is prime , save new number in primelist
        if (IsPrime(listing[i])):
           primeList.append(listing[i])
    print("Questa una lista con i numeri primi", primeList)
    #check if number is prime
def IsPrime(num):
        # Returns True if num is a prime number, otherwise False.
    # all numbers less than 2 are not prime
    if num < 2:
        return False
    # see if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
#end of function
def Divisible(num,factors):
    counter=0
    for i in range(2,num):
        #check if no reminder
        if num%i==0:
            #increase division counter
            counter+=1
            #if counter already bigger then times return false
            if counter>factors:
                return False
    #check if counter equales to times
    if factors==counter:
        return True        
    else:
        return False

def divisibleList(listing,k):
    divisibleLista = []
    #run trough the list
    #decide if divisible
    for i in range(len(listing)):
        if (Divisible(listing[i],k)):
            #if true append to the list
            divisibleLista.append(listing[i])
    #print the list
    #print("Questi sono i numeri divisori di",k,divisibleLista)
    
def modi(lista,k):
    findPrimes(lista)
    divisibleList(lista,k)
    