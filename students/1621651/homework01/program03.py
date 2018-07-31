def codifica(chiave, testo):
    for C in chiave:
        if C<'a' or C>'z':
            chiave=chiave.replace(C, '')
    lettere='abcdefghiljkmnopqrstuvwxyz'
    for L in lettere:
        count=0
        for C in chiave:
            if L==C:
                count+=1
                if count>1:
                    chiave=chiave.replace(C, '', 1)
    vals=list(chiave)
    ordvals=''.join(sorted(vals))
    keys=list(ordvals)
    lesto=list(testo)
    for x in range(len(lesto)):
        for y in range(len(keys)):
            if keys[y]==lesto[x]:
                lesto[x]=vals[y]
                break
    testo=''.join(lesto)
    return(testo)
    print(testo)

def decodifica(chiave, testo):
    for C in chiave:
        if C<'a' or C>'z':
            chiave=chiave.replace(C, '')
    lettere='abcdefghiljkmnopqrstuvwxyz'
    for L in lettere:
        count=0
        for C in chiave:
            if L==C:
                count+=1
                if count>1:
                    chiave=chiave.replace(C, '', 1)
    vals=list(chiave)
    ordvals=''.join(sorted(vals))
    keys=list(ordvals)
    lesto=list(testo)
    for x in range(len(lesto)):
        for y in range(len(vals)):
            if vals[y]==lesto[x]:
                lesto[x]=keys[y]
                break
    testo=''.join(lesto)
    return(testo)
    print(testo)