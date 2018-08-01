def post(fposts,insieme):
    ID = set()
    doc = open(fposts)
    text = doc.read()
    #il testo va in rifinitura con l'eliminazione del POST e dello spazio
    stringa =' '.join(text.split())
    lst = stringa.split('<POST>')
    for i in lst:
        strpost = i.split()
        for stringa in strpost:
            parola = list(stringa)
            #elimino i caratteri fastidiosi
            for char in parola:
                if char == '!' or char == '*' or char=='[' or char==']':
                    char == 'char'
                    #elimino tutto ciò che non appartiene ad isalpha
                elif not char.isalpha() == True:
                    parola.remove(char)
                clean = ''.join(parola) 
                minclean = clean.lower()
                #equivalgo le maiuscole con le minuscole
                for x in insieme:
                    nuova= x.lower()
                    if minclean == nuova:
                        ID.add(strpost[0])
    return ID