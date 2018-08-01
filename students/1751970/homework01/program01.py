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
    "inserite qui il vostro codice"
    
    
    import math
    appoggio=ls[:]
    appoggio2=appoggio[:]
    
    #CONTROLLO SE È UN NUMERO PRIMO
    for x in appoggio:
        if x%2==0 and x>2 and x !=2:
            appoggio2.remove(x)
        
        
            
            
            
    appoggio=appoggio2[:]       
    
    for x in appoggio: 
        for y in range (3,int(math.sqrt(x))+1,2):  
            if y>100000:
                appoggio2.append(x)
                break
            if x%y==0:
                appoggio2.remove(x)
                break
    lista=appoggio2[:]       
    
    
    
    
    
    #CONTROLLO I DIVISORI PROPRI
    
    fattore = []
    rimuovere=[]

    for x in ls:
        c=x
    
    
        d = 2                      # Assegnamento del valore 2 alla variabile d
        while x >= d:              # Inizio del ciclo while
            if x % d == 0:         # Se il numero n è divisibile per d: la lista fattore viene incrementata
                fattore += d,'*'
                x /= d             # Il valore di n viene diviso per d
            else:
                d = d + 1          # Se n non è divisibile per d, il valore di d viene incrementato di 1       

        cont=[]
        occ=[]
        for x in fattore:
            if x not in occ:
                if type(x) == int:
                    occ.append(x)
                    i=fattore.count(x)
                    cont.append(i) #conto il numero di quante volte ogni fattore è ripetuto e lo metto in cont
                
        z=[]            
        for x in cont:
            z.append(x+1)

        prodotto = 1  
        for x in z:
            prodotto *= x                  
            numerodivisori = prodotto-2
        
        
    
        if numerodivisori != k:                     #se x è uguale a k
            rimuovere.append(c)     #rimuovo 
        fattore.clear()   
    for x in rimuovere:
        for y in ls:
            if x==y:
                ls.remove(y)
                
    return lista
    
    