def modi(ls,k):
    
    # La lista_primi conterrà i numeri primi contenuti in ls quindi con 0 divisori #
    
    lista_primi = []
    
    # La lista_divisori_k conterrà i numeri contenuti in ls che hanno k divisori #
    
    lista_divisori_k = []
        
    # Eseguo un ciclo for nel quale prendo tutti gli elementi (cioè n) della variabile (lista) #
    
    for n in ls:        
        
        numero_divisori = 0

        # Per ogni elemento della (lista) eseguo un ciclo di calcolo dei possibili divisori #
        
        for d in range ( 2, int ( n ** 0.5 ) + 1 ):
                        
            # Se l'elemento (n) diviso un ipotetico divisore (d) restituisce un resto (%) = 0 #
            
            if n % d == 0:
                
                # Il numero_divisori aumenta di 2 perchè il divisore moltiplica un secondo divisore non contenuto nel range #

                numero_divisori = numero_divisori + 2
                
                # se d è uguale alla radice di n #
                
                if d == ( n ** 0.5 ):
                    
                    # il numero_divisori aumenta di 1 perchè il divisore moltiplica se stesso #
                    
                    numero_divisori = numero_divisori + 1
                
                    # se il numero dei divisori supera k #
                
                    if numero_divisori > k:
                    
                        # il ciclo for finisce #
                    
                        break
                    
        # se il numero_divisori è uguale a k #
                                
        if numero_divisori == k:
            
            # l'elemento n si aggiunge alla lista_divisori_k #
            
            lista_divisori_k = lista_divisori_k + [n]
            
        # se invece il numero_divisori è uguale a 0 l'elemento n sarà un numero primo #
            
        elif numero_divisori == 0:
            
            # quindi aggiungo l'elemento n alla lista_primi
            
            lista_primi = lista_primi + [n]
                
    # pulisco la lista ls #
            
    ls.clear()
    
    # e la sostituisco con la lista_divisori_k #
	
    ls += lista_divisori_k
    
    # con il comando return chiudo la funzione e richiamo la lista_primi #
            
    return lista_primi