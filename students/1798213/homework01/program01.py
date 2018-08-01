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
    
            # creiamo una lista che contiene i numeri primi, e la chiamiami lsP, con nessun divisore #
    
    lsP = []
    
            # creiamo una lista che contiene i numeri della lista con i divisori verificati (k), e la chiamiamo lsK #
    
    lsK = []
    
            # creiamo un cicolo for che andrà ad analizzare ciascun numero contenuto in ls #
    
    for n in ls:
            
        # usiamo Nd per identificare il numero di divisori#
        
        Nd = 0
    
            # creiamo un'altro ciclo for che andrà a trovare i divisori di ciascun numero contenuto in ls utilizzando la radice ( n^0,5) #
    
        for d in range ( 2, int ( n ** 0.5 ) +1 ) :
                
            # se il risultato dell'operazione ci restituisce un rest pari a 0, allora incrementiamo di 2 #       
            
            if n % d == 0 :
                            
                Nd = Nd + 2
    
            # se il rosiultato dell'operazione ci restituisce d=n^0,5 #             
    
            if d == n ** 0.5 :
                    
                    Nd == Nd + 1
            
            # se il numero di divisori supera k, interrompiamo la funzione con il comando break #        
            
                    if Nd > k :
                
                       break
    
            # se il numero di divisorei è contenuto in k, allora aggiungiamo i valori alla lista #
    
        if Nd == k :
        
            # se Nd è uguale a k facciamo aggiungere questo numero a lsK #
            
                lsK = lsK + [n]
                    
            # se invece Nd è uguale a 0, questo sarà un numero primo #    
                
        elif Nd == 0 :
        
            # e quindi lo aggiungiamo alla lista lsP #
            
                lsP = lsP + [n]
     
            # arrivati a questo punto cancelliamo gli elementi presnti nella lista originale e aggiungiamo i valori ottenuti grazie all' programma #    
    
    ls.clear()
    
    ls += lsK
           
            # quindi facciamo eseguire il programma con il comando return #
    
    return lsP
