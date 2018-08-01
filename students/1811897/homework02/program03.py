def decod(pfile, codice):
    with open (pfile, encoding='utf-8') as f:
        testo= f.read()
        diz=[]
        for riga in testo.split("\n"):
            stringa= str(riga)
            if cerca(stringa,codice)== True:
                diz.append(stringa)
            else:
                continue
        diz_n=set(diz)
        return diz_n

def cerca(stringa,codice):            
    if len(stringa)==len(codice):
        lista_stringa=list(stringa)  
        lista_codice=list(codice)              
        for st,cod in zip(lista_stringa,lista_codice):
            for i,c in zip(lista_stringa,lista_codice):
                if st==i:
                    if cod==c:
                        continue
                    else:
                        return False
                else:
                    if cod!=c:
                       continue
                    else:
                       return False
        return True
    else:
        return False
        
        
        





