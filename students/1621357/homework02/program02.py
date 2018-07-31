
import json

def pianifica(fcompiti,insi,fout):
    dictionary = {}
    dictionary2 = {}
    diz = {}
    comp = ''
    sub = ''
    file = open(fcompiti,"r")
    for line in file:
        if 'comp' in line:
            comp = line.split('comp',1)[1]
            comp = comp.strip()
            # if not(comp in dictionary):
            #     dictionary[comp] = []
            dictionary[comp] = []
        if  'sub' in line:
            sub = line.split('sub',1)[1]
            sub = sub.strip()
            if sub in dictionary:
                dictionary[comp] = dictionary.get(sub) + [sub]
            else:
                dictionary[comp] = [sub]

    for x in insi:
        if x in dictionary:
            dictionary2[x] = dictionary.get(x)
    js = json.dumps(dictionary2)
    fp = open(fout, 'w')
    fp.write(js)
    fp.close()
    file.close()
    return None
