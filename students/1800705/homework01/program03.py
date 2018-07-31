# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:30:27 2017

@author: Ali
"""

import re 

def countnremove(a):
    a = re.sub ('[^a-z]', '', a)
    l = list(a)
    for el in l[:]:
        if l.count(el) > 1:
            l.remove(el)
    b = sorted(l)
    return list (zip(b,l))

def codifica (chiave,testo):
    stringa=""
    for lettera in testo:
        for d in countnremove(chiave):
            if lettera is d[0]:
                lettera=lettera.replace(d[0],d[1])
        stringa += lettera
    return stringa

def decodifica(chiave,testo):
    stringa=""
    for lettera in testo:
        for d in countnremove(chiave):
            if lettera is d[1]:
                lettera=lettera.replace(d[1],d[0])
        stringa += lettera 
    return stringa

