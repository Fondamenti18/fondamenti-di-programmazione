import json
def dizComp(file):
    riga = file.readline()
    diz = {}
    while riga!='':
        numComp = ''
        numSub = ''
        for i in riga:
            if i.isdecimal():
                numComp+=i
        riga = file.readline()
        if 'sub' in riga:
            for i in riga:
                if i.isdecimal():
                    numSub += i
            riga = file.readline()
        diz[numComp] = numSub
    return diz
def inizializzaDiz(insieme,dizComp):
    diz={}
    for i in insieme:
        if i in dizComp.keys():
            diz[i]=[]
    return diz
def listaUscita(chiave, dizComp, lista):
    if chiave in dizComp.keys():
        if dizComp[chiave]!='':
            lista.append(dizComp[chiave])
            listaUscita(dizComp[chiave],dizComp,lista)
        else:
            lista.reverse()
def pianifica(fcompiti,insi,fout):
    fin = open(fcompiti,'r',encoding='UTF-8')
    fwrite = open(fout,'w',encoding='UTF-8')
    dizionario = dizComp(fin)
    dizOut = inizializzaDiz(insi,dizionario)
    for num in insi:
        if num in dizionario.keys():
            listaUscita(num,dizionario,dizOut[num])
    print(json.dumps(dizOut),file=fwrite)
    fin.close()
    fwrite.close()



























