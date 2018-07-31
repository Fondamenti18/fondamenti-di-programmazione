import sys
sys.setrecursionlimit(500000)

def leggi(f):
	f = open(f, "r")
	return f.read()

import re
def splitCompiti(testo):
    listTesto = re.split("\s*comp\s*", re.sub("\s*\n\s*", "", testo))
    return listTesto[1:]

def formatta(lista, insieme):
    dict = {}
    for x in lista:
        if x.isdigit():
            dict[x] = []
        else:
            x = re.split("\s*sub\s*", x)
            dict[x[0]] = x[1]
    res = {}
    d = {}
    for x in insieme:
        if x in dict.keys():
            res[x] = csub(x, d, dict)
    return res

def csub(comp, d, dict):
    sub = dict[comp]
    if sub == []:
        d[comp] = []
        return []
    if sub in d:
        d[comp] = d[sub] + [sub]
    else:
        d[comp] = csub(sub, d, dict) + [sub]
    return d[comp]

import json
def scrivi(fout, d):
    f = open(fout, "w")
    json.dump(d, f)
    f.close()

def pianifica(fcompiti,insi,fout):
    '''Implementare qui la funzione'''
    compiti = leggi(fcompiti)
    comp = splitCompiti(compiti)
    d = formatta(comp, insi)
    scrivi(fout, d)
