def controllo_corrispondenza(codice,parola):
    dizionario = {}
    lung_parola = len(parola)
    mycodice = list(codice)
    verita = True

    for i in range(0,lung_parola):
        carattere = parola[i]
        
        if(carattere not in dizionario.keys()): 
            if (mycodice[i] in dizionario.values()):
                verita=False
            else: 
                dizionario[carattere] = mycodice[i]
        else:
            if(dizionario[carattere] != mycodice[i]):
                verita=False
                break
    return (verita)

def decod(pfile, codice):
    result = set()
    myfile = open(pfile,'r',encoding = 'utf-8')
    lista_parole = myfile.readlines()
    
    for parola in lista_parole:
        parola = parola.strip('\n')
        lung_parola=len(parola)
        lung_codice=len(codice)
        
        if(lung_parola != lung_codice):
            continue
        else:
            possibile_parola_trovata = controllo_corrispondenza(codice,parola)
    
            if(possibile_parola_trovata==True):
                result.add(parola)
            else:
                continue
    return(result)
    
    


