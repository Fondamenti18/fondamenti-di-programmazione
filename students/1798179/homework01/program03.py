# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 21:53:37 2017

@author: Gionitoo
"""

def disordinamento(s):
    a=len(s)-1
    dis=[]
    s_dis=""
    while a>=0:
        if "a"<=s[a]<="z":
            dis=[s[a]]+dis
            if s[a] in dis[1: ]:
                dis.remove(s[a])
        a=a-1
    return s_dis.join(dis)

def ordinamento(s):
    s_ord=""
    a=disordinamento(s)
    return s_ord.join(sorted(a))
def coppie(s1):
    d={}
    i=0
    s=disordinamento(s1)
    ss=ordinamento(s1)
    while i<len(s):
        d[s[i]]=ss[i]
        i=i+1
    return d

def codifica(chiave, testo):
    d=coppie(chiave)
    t_mod=""
    for x in testo:
        if x not in d.keys():
            t_mod+=x
        else:
            t_mod+=d[x]
    return t_mod

def coppie_reverse(s1):
    d={}
    i=0
    s=disordinamento(s1)
    ss=ordinamento(s1)
    while i<len(s):
        d[s[i]]=ss[i]
        i=i+1
    return d

def decodifica(chiave, testo):
    d=coppie_reverse(chiave)
    t_mod=""
    for x in testo:
        if x not in d.keys():
            t_mod+=d[x]
    return t_mod
    
