def chiave(parola):
    disordinata=[]
    for i in range(0,len(parola)):
        if parola[i]>='a' and parola[i]<='z':
            disordinata.append(parola[i])
    copia=[]
    copia=disordinata[:]
    for i in copia:
        if disordinata.count(i)>1:
            disordinata.remove(i)
    ordinata=[]
    ordinata=sorted(disordinata)
    return(ordinata,disordinata)

def codifica(key, testo):
    txt=testo
    (list_o,list_d) = chiave(key)
    testocod=[]
    lung=len(testo)
    for i in range(0,lung):
        if txt[i] in list_o:
            var= list_o.index(txt[i])
            txt=txt[0:i] + txt[i:].replace(txt[i],list_d[var].upper())
            del list_d[var]
            del list_o[var]
        if list_o == []:
            break
    for i in range(0,lung):
        if txt[i].isupper() and testo[i].islower():
            testocod.append(txt[i].lower())
        else:
            testocod.append(txt[i])
    test_cod=''
    for j in testocod:
        test_cod+=j
    return (test_cod)

def decodifica(key, testo):
    txt=testo
    (list_o,list_d)= chiave(key)
    testodecod=[]
    lung=len(testo)
    for i in range(0,lung):
        if txt[i] in list_d:
            var= list_d.index(txt[i])
            txt=txt[0:i] + txt[i:].replace(txt[i],list_o[var].upper())
            del list_o[var]
            del list_d[var]
        if list_d ==[]:
            break
    for i in range(0,lung):
        if txt[i].isupper() and testo[i].islower():
            testodecod.append(txt[i].lower())
        else:
            testodecod.append(txt[i])
    test_decod=''
    for j in testodecod:
        test_decod+=j
    return (test_decod)
        

    
