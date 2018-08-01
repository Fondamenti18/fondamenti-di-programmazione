def decod(pfile,codice):
    lista,ssx=[],sorted(set(codice),key=codice.index)
    with open(pfile,"r") as infile:
        lines=infile.read()
        for line in lines.split("\n"):
            if len(line)==len(codice) and len(ssx)==len(sorted(set(line),key=line.index)):
                dictionario={}
                [dictionario.update({y:x}) for y,x in zip(sorted(set(line),key=line.index),ssx)]
                get(codice,line,dictionario,lista)
    return set(lista)

def get(codice,line,dictionario,lista):
    for x,y in zip(codice,line):
        if dictionario.get(y)!=x and dictionario.get(y)!=None:
            return
    lista.append(line)
    return lista
