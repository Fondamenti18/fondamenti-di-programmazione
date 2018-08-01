def lista (chiave):
    lista = []
    for k in chiave :
        if k < "a" or k > "z":
            chiave = chiave.replace(k,"")
        else:
            lista.extend(k)
    lista = lista[::-1]
    lista=sorted(set(lista), key=lista.index)
    lista = lista[::-1]
    return "".join(lista) 

def lista_ordinata (chiave) :
    a = lista(chiave)
    b = "".join(sorted(a))
    return b

def codifica (chiave,testo):
    a = lista(chiave)
    b = lista_ordinata(chiave)
    traduci = str.maketrans(b,a)
    return (testo.translate(traduci))

def decodifica(chiave,testo):
    a = lista(chiave)
    b = lista_ordinata(chiave)
    traduci = str.maketrans(a,b)
    return (testo.translate(traduci))
