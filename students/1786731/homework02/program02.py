import json


# stiamo assumendo che una definizione di un compID non appaia due volte 
# Inoltre, nessun comp ha 2 subcomp
def appendcomp(linea, compiti): 
    compid = linea[linea.find("p") + 1 :].strip()
    compiti[ compid ] = ''

    return compid

def appendsubcomp(linea, compiti, currentcompid): 
    compiti[currentcompid] = linea[linea.find("b") + 1 :].strip()

def appendirisultato(compid, risultato, compiti):
    if compid not in compiti:
        return
    
    dependencies = []
    startid = compid

    currid = compiti[startid] # get the child
    while(True):
        if currid == '':
            break
        else:
            dependencies.append(currid)
            currid = compiti[currid]

    risultato[startid] = dependencies[::-1]

def evalFile(f, compiti):
    currentcompid = -1

    for linea in f:
        if( "comp" in linea ):
            currentcompid = appendcomp(linea, compiti)
        else:
            appendsubcomp(linea, compiti, currentcompid)  # appendi subcomp nel current comp

def pianifica(fcompiti,insi,fout):
    compiti = { }     # id, [dependencies]

    with open(fcompiti) as f:
        evalFile(f, compiti)

    risultato = { }
    for compid in insi:
        appendirisultato(compid, risultato, compiti)

    outfile = open(fout, 'w')
    json.dump(risultato, outfile)
    outfile.close()