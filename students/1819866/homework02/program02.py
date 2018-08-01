# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:14:28 2017

@author: Andrea
"""

def pianifica(fcompiti,insi,fout):
    utili = set()
    risultato = {}
    stringa = ''
    dic, compSet = corrispondenze(fcompiti)
    utili = insi & compSet
    for el in utili:
        risultato[el] = dic[el]
        control = dic[el][-1]
        while control != '0':
            risultato[el] += dic[control]
            control = dic[el][-1]
    for chiave in risultato:
        risultato[chiave].pop()
        risultato[chiave].reverse()
    stringa = str(risultato)
    stringa = stringa.replace("'", '"')
    with open(fout, 'w') as f:
        f.write(stringa)

def corrispondenze(file):
    dic = {}
    compSet = set()
    with open(file) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('p', ' ').replace('b', ' ').split()
        if 'com' in lines[i]:
            comp = lines[i][1]
            dic[comp] = ['0']
            compSet.add(comp)
        else:
            sub = lines[i][1]
            dic[comp][-1] = sub
    return dic, compSet