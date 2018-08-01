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

def isPrime(n):
    #Verifica se il numero in input è primo
    if n%2==0:
        return False
    else:
        for number in range(3,int(n**0.5)+1,2):
            if n%number==0:
                return False
        return True

def divideNumber(num,k):
    #Dato un intero pari ed un intero k, verifica che il numero num abbia
    #esattamente k divisori ritornando un valore booleano
    DividerList=[]
    for number in range(2,int(num**0.5)+1):
        if num%number==0:
            DividerList.append(number)
            DividerList.append(num//number)
    if len(DividerList)==k:
        return True
    else:
        return False
            
def modi(ls,k):
    ListOfPrimes=[]
    if k<0:
        return "Inserisci un numero k>=0" 
    else:
        Counter=0
        MyLength=len(ls)
        while Counter<MyLength:
            if isPrime(ls[Counter])==True:
                ListOfPrimes.append(ls[Counter])
                ls.remove(ls[Counter])
                MyLength=MyLength-1
            else:
                if divideNumber(ls[Counter],k)==False:
                    ls.remove(ls[Counter])
                    MyLength=MyLength-1
                else:
                    Counter=Counter+1
        return ListOfPrimes
    