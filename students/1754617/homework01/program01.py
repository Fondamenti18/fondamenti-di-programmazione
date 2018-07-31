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
    listaconprimi=[]
    elementiConK=[]
    for numero in ls:     #scorro
        race=calcolaDivisore(numero)
        if(race[1]==True):
            listaconprimi.append(numero)
        elif(race[0]==k):
            elementiConK.append(numero)   #controllo
    ls[:]=elementiConK
    return listaconprimi

     
def calcolaDivisore(n):
    contatore=0 # contatore per il calolco
    i=2
    flag=True    #bandiera
    while(i**2 < n):    
        if(n%i==0):
            contatore=contatore+2  
            flag=False
        i=i+1
    contatore +=(1 if i**2==n else 0)
    return contatore,flag   #ritorno il contatore e il flag
