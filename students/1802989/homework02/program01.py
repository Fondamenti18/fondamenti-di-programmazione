# -*- coding: utf-8 -*-
import re
alfabeto = 'abcdefghijklmnopqrrstuvwzyzàéèìòù '

def post(fposts,insieme):
    ''' implementare qui la funzione'''
    with open(fposts, 'r', encoding="utf-8") as f:
        diz = elabora(f)
    out = check(insieme, diz)
    return out

def elabora(f):
    diz = {}
    k = ''
    for line in f:
        if "<POST>" in line:
            k = ''.join(re.findall(r'\d+', line))
            diz[k] = ''
        else:
            diz[k] += pulisci_testo(line.lower())
    return diz

def pulisci_testo(txt):
    "Funzione che pulisce tutto ciò che non è nell'alfabeto"
    for char in txt:
        if char not in alfabeto:
            txt = txt.replace(char, ' ')
    return txt

def check(insieme, dizio):
    'Funzione che controlla se gli elementi sono presenti nei valori del dizionario'
    ris = set()
    for item in insieme:
        item = item.lower()
        for k,v in dizio.items():
            if ' '+item+' ' in v:
                ris.add(k)
    return ris