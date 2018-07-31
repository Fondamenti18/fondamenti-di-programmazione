#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 16:27:40 2017

@author: patriziogermani
"""
def diverso(chiave):
    for el in range(len(chiave)-1,-1,-1):
        if not chiave[el].islower():
            del(chiave[el])
    return chiave
def conta(chiave):
    for el in chiave:
        if chiave.count(el)>1:
            chiave.remove(el)
    return chiave
def codifica (chiave,testo):
    par=""
    chiave=list(chiave)
    chiave=diverso(chiave)
    chiave=conta(chiave)
    chiave1=sorted(chiave)
    chiave1.append(' ')
    chiave.append(' ')
    testo=list(testo)
    print(testo)
    print(chiave,"chiave")
    print(chiave1,"chiave1")
    for el in range(0, len(testo)):
        for x in range(0,len(chiave1)):
            if testo[el]== chiave1[x]:
                par=chiave[x]
            elif not testo[el]in chiave1:
                par=testo[el]
        testo[el]=par
    return ''.join(testo)
def decodifica(chiave,testo):
    return testo
