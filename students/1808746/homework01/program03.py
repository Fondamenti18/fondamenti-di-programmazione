def codifica(chiave, testoChiaro):
    for c in chiave:
        if c<'a' or c>'z':
            chiave=chiave.replace(c,'')
    for c in chiave:
        numLett=chiave.count(c)
        if numLett>1:
            chiave=chiave.replace(c,'',numLett-1)
    chiaveOrd=''.join(sorted(chiave))
    corrispondenze={}
    acc=0
    for i in chiaveOrd:
        corrispondenze[i]=chiave[acc]
        acc+=1
    encoding=''
    for car in testoChiaro:
        if car in corrispondenze:
            encoding+=corrispondenze[car]
        else:
            encoding+=car
    return encoding

def decodifica(chiave, testoCritto):
    for c in chiave:
        if c<'a' or c>'z':
            chiave=chiave.replace(c,'')
    for c in chiave:
        numLett=chiave.count(c)
        if numLett>1:
            chiave=chiave.replace(c,'',numLett-1)
    chiaveOrd=''.join(sorted(chiave))
    decorrispondenze={}
    acc=0
    for i in chiave:
        decorrispondenze[i]=chiaveOrd[acc]
        acc+=1
    decoding=''
    for car in testoCritto:
        if car in decorrispondenze:
            decoding+=decorrispondenze[car]
        else:
            decoding+=car
    return decoding