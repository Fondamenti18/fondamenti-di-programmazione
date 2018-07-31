numeri = ['0','1','2','3','4','5','6','7','8','9']

def numeriordinati(x):
    ls = list(x)
    if '\n' in ls:
        ls.remove('\n')
    caratteri = ['\n']
    dizio={}
    for i in range(0,len(ls)):
        if ls[i] not in caratteri:
            caratteri.append(ls[i])
    caratteri.remove('\n')
    if len(caratteri)<11:
        for n in range(0,len(caratteri)):
            dizio[caratteri[n]]=numeri[n]
        for p in range(0,len(ls)):
            ls[p]=dizio[ls[p]]
        stringa=''.join(ls)
        return stringa
    else:
        return 'fuck'

def decod(pfile, codice):
    key=numeriordinati(codice)
    result=set()
    file = open(pfile, 'r')
    for f in file:
        if len(key)==(len(f)-1):
            if numeriordinati(f)==key:
                q = f[:-1]
                result.add(q)
    return result
