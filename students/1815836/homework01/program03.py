
def codifica(chiave,testo):
    kdis,kord=chiavek(chiave)
    key=[]
    lung=len(kdis)
    for i in testo:
        if i not in kord:
            key.append(i)
        else:
            c=0
            while c < lung:
                if kord[c]==i:
                   key.append(kdis[c])
                   break
                c+=1
    ret=''.join(key)
    return (ret)
def decodifica(chiave, testo):
    kdis,kord=chiavek(chiave)
    key=[]
    lung=len(kdis)
    for i in testo:
        if i in kord:
            c=0
            while c < lung:
                if i==kdis[c]:
                   key.append(kord[c])
                   break
                c+=1
        else:
            key.append(i)
    ret=''.join(key)
    return (ret)
def chiavek(chiave):
    keydis=[]
    keyord=[]
    ch=list(chiave)
    ch.reverse()
    for i in ch:
        if(i in keydis)==False and ord('a')<=ord(i)<=ord('z'):
            keydis+=[i]
    keydis.reverse()
    keyord=list(keydis)
    keyord.sort()
    return(keydis,keyord)