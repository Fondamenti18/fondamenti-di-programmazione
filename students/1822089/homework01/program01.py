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

def modi(ls,k):
    list_primi=[]
    index = 0 #Conterrà l'indice esatto, anche se l'elemento viene rimosso

	#Scorre la lista
    for i in range(0,len(ls),1):
        num=ls[index]#All'inizio entrambi gli indici saranno 0
        index+=1 #Incrementa l'indice esatto ad ogni ciclo
        countK=0
        
        #Scorre i possibili divisori del numero
        for j in range(2,round(math.sqrt(num))+1, 1):
            if (num%j)==0:
                if math.sqrt(num)==j:#sqrt(121)==11 : 11 si ripeterà solo 1 volta
                    countK+=1
                else:
                    countK+=2
                    
        #Controlli per modifiche liste
        if(countK==0):
            list_primi.append(num)
            ls.remove(num)
            index-=1 #Se un elemento viene rimosso, la grandezza della lista diminuisce, quindi anche l'indice corrente
        elif(countK!=k):
            ls.remove(num)
            index-=1
            
    return list_primi