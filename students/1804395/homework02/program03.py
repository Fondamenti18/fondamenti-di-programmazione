def decod(pfile, codice):
    with open(pfile) as f:
        file= (f.read()).splitlines()
    result=set()
    for word in file:
        try :
            transTableWordToCode = str.maketrans(word, codice)
            transTableCodeToWord = str.maketrans(codice, word)
        except ValueError:
            continue
        if (word.translate(transTableWordToCode)== codice and codice.translate(transTableCodeToWord) == word):
            result.add(word)            
    return (result) 
        
