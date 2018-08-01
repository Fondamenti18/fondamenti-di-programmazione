# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:22:36 2017

@author: VALERIO
"""

def codifica(chiave, testo):
    n=0
    text=''
    key=[]
    diz={}
    for i in range (len(chiave)):
        if chiave[i]<='z' and chiave[i]>='a':
            if chiave[i] not in chiave[i+1:len(chiave)]:
                key.append(chiave[i])
    keyo=key[:]
    list.sort(keyo)
    for i in range(len(key)):
        k=keyo[i]
        v=key[i]
        diz[k]= v
    
    for c in testo:
        if c in key:
            text=text+diz[c]
        else:
            text=text+testo[n]
        n+=1
    return text

def decodifica(chiave, testo):
    n=0
    text=''
    key=[]
    diz={}
    for i in range (len(chiave)):
        if chiave[i]<='z' and chiave[i]>='a':
            if chiave[i] not in chiave[i+1:len(chiave)]:
                key.append(chiave[i])
    keyo=key[:]
    list.sort(keyo)
    for i in range(len(key)):
        k=key[i]
        v=keyo[i]
        diz[k]= v
    for c in testo:
        if c in key:
            text=text+diz[c]
        else:
            text=text+testo[n]
        n+=1
    return text


































