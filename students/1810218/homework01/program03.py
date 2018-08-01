def a_z(chiave):
    from copy import copy
    chiave=list(chiave)
    chiave1=copy(chiave)
    for c in chiave1:
        if ord(c)<ord('a') or ord(c)>ord('z'):
            chiave.remove(c)
    return chiave

def canc(chiave):
    chiave=''.join(chiave)
    for c in chiave:
        if c in chiave[chiave.find(c)+1:]:
            chiave=list(chiave)
            chiave.remove(c)
            chiave=''.join(chiave)
    return chiave

def diz1(chiave):
    chiave_ord=sorted(chiave)
    d1={}
    for c in chiave_ord:
        d1[c]=chiave[chiave_ord.index(c)]
    return d1

def diz2(chiave):
    chiave_ord=sorted(chiave)
    d2={}
    for c in chiave:
        d2[c]=chiave_ord[chiave.index(c)]
    return d2
    
def codifica(chiave, testo):
    chiave=a_z(chiave)
    chiave=canc(chiave)
    d1=diz1(chiave)
    testo=list(testo)
    pos=0
    while pos<len(testo):
        if testo[pos] in d1.keys():
            testo[pos]=d1[testo[pos]]
        pos+=1
    testo=''.join(testo)
    return testo
    
def decodifica(chiave, testo):
    chiave=a_z(chiave)
    chiave=canc(chiave)
    d2=diz2(chiave)
    testo=list(testo)
    pos=0
    while pos<len(testo):
        if testo[pos] in d2.keys():
            testo[pos]=d2[testo[pos]]
        pos+=1
    testo=''.join(testo)
    return testo
    
    
    
