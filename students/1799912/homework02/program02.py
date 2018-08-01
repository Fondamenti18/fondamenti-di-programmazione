import json

def converti(lsub):
    st = ''
    for i in lsub:
        if i.isdigit() == 1:
            st += i
    return st

def creaDizionario(file):
    ret = {}

    linee = [""]

    for linea in file:
        linee.append(linea)
        if "sub" in linea:
            ret[converti(linee[-2])] = converti(linea)
        if "comp" in linea:
            ret[converti(linea)] = []
    return ret
    

def ricorsiva(lista_fin, x, dizionario):
    if x == []:
        return lista_fin[1:]
    lista_fin.insert(0, dizionario[x])
    return ricorsiva(lista_fin, dizionario[x], dizionario)


def pianifica(fcompiti, insieme, fout):
    dizionario = creaDizionario(open(fcompiti))

    ret = {}
    
    for compito in insieme:
        if compito in dizionario:
            ret[compito] = ricorsiva([], compito, dizionario)

    json.dump(ret,open(fout,'w'))


