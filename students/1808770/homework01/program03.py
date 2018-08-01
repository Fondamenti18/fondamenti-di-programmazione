def codifica(chiave,testo):
    global dictionario
    lista=[]
    for c in chiave[::-1]:
        if c.islower() and c not in lista:
            lista.append(c)
        else:
            chiave.replace(c,"")
    disordinata="".join(lista[::-1])
    ordinata="".join(sorted(disordinata))
    dictionario={}
    for i,j in zip(ordinata,disordinata):
            dictionario.update({i:j})
    stringa=""
    for char in testo:
        if dictionario.get(char)!=None:
            stringa+=dictionario.get(char)
        else:
            stringa+=char
    decodifica(chiave,stringa)
    return stringa

def decodifica(chiave,testo):
    global dictionario
    stringa=""
    dictionario2={}
    for k,v in zip(list(dictionario.keys()),list(dictionario.values())):
        dictionario2.update({v:k})
    for char in testo:
        if dictionario2.get(char)!=None:
            stringa+=dictionario2.get(char)
        else:
            stringa+=char
    return stringa