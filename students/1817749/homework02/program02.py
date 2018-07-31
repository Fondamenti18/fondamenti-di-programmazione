import json


def get(info):
    dic = {}
    for el in filter(None, info.replace(" ", "").split("comp")):
        spl = el.split('\n')
        dic[spl[0]] = spl[1][3:]
    return dic


def combo(comp, compiti):
    next = compiti[comp]
    ret = []
    while next != '':
        ret.insert(0, next)
        next = compiti[next]
    return ret


def pianifica(fcompiti, insi, fout):
    ret = {}
    compiti = get(open(fcompiti, 'r').read())
    for comp in insi:
        if comp in compiti:
            ret[comp] = combo(comp, compiti)
    retle = open(fout, 'w')
    json.dump(ret, retle)
