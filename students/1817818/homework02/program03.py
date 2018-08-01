def corrisponde(s,codice):
    corrispondenze = {}
    corrispondenze[codice[0]] = s[0]
    corr = True
    for i in range(1,len(s)):
        if codice[i] in corrispondenze.keys():
            if corrispondenze[codice[i]] != s[i]:
                corr = False
        else:
            if s[i] in corrispondenze.values():
                corr = False
            else:
                corrispondenze[codice[i]] = s[i]
    return corr
def decod(pfile, codice):
    insieme = set()
    fileTesto = open(pfile,'r',encoding='UTF-8')
    riga = fileTesto.readline()
    while riga!='':
        riga = riga.strip()
        if (len(riga)==len(codice)):
            corr = corrisponde(riga,codice)
            if corr:
                insieme.add(riga)
        riga = fileTesto.readline()
    fileTesto.close()
    return insieme



