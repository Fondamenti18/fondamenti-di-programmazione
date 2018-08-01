def post(fposts, insieme):
    
    with open(fposts, encoding = 'UTF-8') as testo:
        
        righe_testo = testo.readlines()
        numero_post = []
        id_post = []
        
        for a in righe_testo:
            
            appoggio = a.replace('>', " ").lower().split()
            
            for b in range(len(appoggio)):
                
                controllo = str(appoggio[b])
                appoggio[b] = controllo.strip(",.;'?!:^")
                
                if appoggio[b] == '<post':
                    
                    numero_post += [appoggio[b + 1]]
                
                for elemento in insieme:
                    
                    elemento = elemento.lower()
                    
                    if elemento == appoggio[b]:
                        
                        id_post += [numero_post[-1]]
                        
    return set(id_post)