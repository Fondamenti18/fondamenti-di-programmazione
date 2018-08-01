def codifica(chiave, testo):
    Lchiave=[]
    LchiaveOrd=[]
    Ltesto=[]
    pos=0
    for x in chiave:
         if ord(x) >= ord('a') and ord(x) <= ord('z'):
             Lchiave+=x
    for x in testo:
         Ltesto+=x
    for x in Lchiave:
        while Lchiave.count(x) != 1:
            if Lchiave.count(x) > 1:
                Lchiave.remove(x)
    for x in Lchiave:
        while Lchiave.count(x) != 1:
            if Lchiave.count(x) > 1:
                Lchiave.remove(x)    
    LchiaveOrd = sorted(Lchiave)
    for x in Ltesto:
        for c in range(len(Lchiave)):
            if x == LchiaveOrd[c]:
                Ltesto[pos] = Lchiave[c]
        pos+=1
    testo = ''.join(Ltesto)
    chiave = ''.join(Lchiave)
    return testo

def decodifica(chiave, testo):
    Lchiave = []
    LchiaveOrd = []
    Ltesto = []
    pos = 0
    for x in chiave:
         if ord(x) >= ord('a') and ord(x) <= ord('z'):
             Lchiave+=x
    for x in testo:
         Ltesto+=x
    for x in Lchiave:
        while Lchiave.count(x) != 1:
            if Lchiave.count(x) > 1:
                Lchiave.remove(x)
    for x in Lchiave:
        while Lchiave.count(x) != 1:
            if Lchiave.count(x) > 1:
                Lchiave.remove(x)
    LchiaveOrd = sorted(Lchiave)
    for x in Ltesto:
        for c in range(len(Lchiave)):
            if x == Lchiave[c]:
                Ltesto[pos] = LchiaveOrd[c]
        pos+=1
    testo = ''.join(Ltesto)
    chiave = ''.join(Lchiave)
    return testo