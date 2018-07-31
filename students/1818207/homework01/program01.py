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
def modi(lista,k) :
    lista2 = []
    
    for i in range(len(lista)-1,-1,-1) :  #iterando al contrario non incappo in problemi di indice sottraendo elementi
        ki = 0 #dichiaro un contatore
        
        for j in range(1,int(lista[i]**(1/2))+1):  #utilizzando la radice risparmio sulle iterazioni
            
            if lista[i] % j == 0 :
                ki = ki +2  #aggiungiamo 2 ogni volta che troviamo un divisore per via della compressione
                
            if j == int(lista[i]**(1/2)) : #il for ha finito di cliclare
                if lista[i]**(1/2)-int(lista[i]**(1/2)) == 0 :
                    ki = ki-3 # nel caso si presenti un numero con dispari divisori devo sottrare 3 al contatore
                else :
                    ki = ki -2
                
                if ki == 0 :
                    lista2.append(lista[i]) #nell'eventualità di numero primo lo metto da parte
                    lista.remove(lista[i])
                    
                if ki != k and ki != 0 : #scarto il numero che non mi serve
                    lista.remove(lista[i])
    print (lista)               
    lista2.reverse()# avendo iterato al contrario devo invertire il risultato per riportarlo all'originale
    
    return lista2
