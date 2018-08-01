def struttura(parola,numero):
    l_parola=len(parola)
    l_numero=len(numero)
    if l_parola != l_numero:
        return False
    numeri = ["0","1","2","3","4","5","6","7","8","9"]
    for i in range(0,l_parola):
        if numeri == []:
            continue
        elif parola[i].isnumeric():
            continue
        elif numero[i] not in numeri:
            continue
        else:
            parola = parola.replace(parola[i],numero[i])
            numeri.remove(numero[i])
    return parola == numero

def decod(pfile,codice):
    f=open(pfile,"r", encoding = "utf-8")
    insieme= set()
    for line in f.readlines():
        if struttura(line[:-1],codice):
            insieme.add(line[:-1])
    f.close()
    return(insieme)

            
