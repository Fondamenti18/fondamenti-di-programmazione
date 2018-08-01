import json
def convertiriga(lsan):
    stringhetta = ''
    for y in lsan:
        if y.isdigit() == 1:
            stringhetta += y
    return stringhetta
def ricochef(listafindus, x, dizionario):
    if x == []:
        return listafindus[1:]
    listafindus.insert(0, dizionario[x])
    return ricochef(listafindus, dizionario[x], dizionario)
def pianifica(fcompiti, insieme, fout):
    file=open(fcompiti)
    rettile = {}
    righee = [""]
    for riga in file:
        righee.append(riga)
        if "sub" in riga:
            rettile[convertiriga(righee[-2])] = convertiriga(riga)
        if "comp" in riga:
            rettile[convertiriga(riga)] = []
    d=rettile
    rettile = {}
    for c in insieme:
        if c in d:
            rettile[c] = ricochef([], c, d)
    json.dump(rettile,open(fout,'w'))




