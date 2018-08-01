def decod(pfile, codice):
    
    file_input = open(pfile, 'r')
    
    lista_parole_giuste = []

    for line in file_input:    
        contenitore = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        parola = str (line)
        len_parola = len (parola)-1
        buona = 'S'
        
        if len_parola == len (codice): 
                  
            for progressivo in range(len(codice)):
                posizione= int(codice[progressivo])
               
                #nuova lettera su nuova posizione: OK
                if contenitore[posizione] == parola[progressivo]:
                    pass

                # per nuova lettera su vecchia posizione #
                elif (contenitore[posizione]!= 0) and \
                     (contenitore[posizione]!= 1) and \
                     (contenitore[posizione]!= 2) and \
                     (contenitore[posizione]!= 3) and \
                     (contenitore[posizione]!= 4) and \
                     (contenitore[posizione]!= 5) and \
                     (contenitore[posizione]!= 6) and \
                     (contenitore[posizione]!= 7) and \
                     (contenitore[posizione]!= 8) and \
                     (contenitore[posizione]!= 9):
                         
                    # porto al massimo il progressivo per uscire immediatamente dal ciclo #
                    progressivo = len(codice)
                    # la parola è sbagliata #
                    buona = 'N'

                # nuova lettera su nuova posizione: OK #
                elif contenitore[posizione] == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
                    contenitore[posizione] = parola[progressivo]

                else:
                    print('ERRORE non prevedibile')
                    pass
            # ho caricato le lettere della parola nel giusto elemento del contenitore #
            # ora controllo che non ci siano doppioni (il che vuol dire che
            # lettere uguali corrispondono a numeri differenti, cioè parole errate) #
            for i in range ( len (contenitore) ):
                # ci sono lettere doppioni cioè per differenti posizioni
                if (contenitore.count (contenitore [i])) > 1:
                    buona = 'N'

            if buona == 'S':
                lista_parole_giuste = lista_parole_giuste + [line.strip('\n')]                              

            
    return set(lista_parole_giuste)
