def decod(pfile, codice):
    
    stringhe_da_analizzare = formattazione_insieme_parole(pfile, codice)
    codice_no_doppie = elimina_doppie_in_codice(codice)
    parole_struttura = crea_lista(pfile, codice)
    
    return parole_struttura

       
def crea_lista(pfile, codice):
    
    struttura = []
    lista_appoggio = []
    parole_corrette = []
    codice = list(codice)
    parole = formattazione_insieme_parole(pfile, codice)
    codice_elaborato = elimina_doppie_in_codice(codice)
    
    for a in parole:
        
        for b in a:
            
            if b not in lista_appoggio:
                
                lista_appoggio += [b]
         
        relazione = dict(zip(lista_appoggio, codice_elaborato))
            
        for c in a:
            
            if c in relazione:
                
                struttura += relazione[c]
        
        if struttura == codice:
            
            parole_corrette += [a]
            
        lista_appoggio = []
        struttura = []
    
    return set(parole_corrette)

    
def elimina_doppie_in_codice(codice):
    
    codice_appoggio = []
    
    for a in codice:
        
        if a not in codice_appoggio:
            
            codice_appoggio += a

    return codice_appoggio

       
def formattazione_insieme_parole(pfile, codice):
    
    with open(pfile, encoding = 'UTF-8') as testo:
        
        righe_testo = testo.readlines()
        insieme_parole = []
        
        for a in righe_testo:
            
            appoggio_analisi = a.split()
            
            for b in appoggio_analisi:
                
                if len(b) == len(codice):
                    
                    insieme_parole += [b]
            
    return insieme_parole