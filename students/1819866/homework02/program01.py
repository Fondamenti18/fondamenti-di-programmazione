# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 22:59:10 2017

@author: Andrea
"""

def post(fposts,insieme):
    risultato = set()
    insiemeLower = set()
    for el in insieme:
        insiemeLower.add(el.lower())
    with open(fposts) as f:
        splitFile = f.read().lower().split("<post>")
    for string in splitFile:
        wordsSet = words(string)
        if wordsSet & insiemeLower != set():
            iD = string.splitlines()[0].strip()
            risultato.add(iD)
    return risultato

def words(testo):
    for c in testo:
        if not c.isalpha():
            testo = testo.replace(c, ' ')
    return set(testo.split())