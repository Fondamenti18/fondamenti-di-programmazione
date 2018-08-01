# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 15:32:57 2017

@author: tmald
"""

def decod(pfile, codice):
    ind=open(pfile)
    a=ind.readline()
    risposta=set()
    while a!='':
        a=a.rstrip('\n')
        if len(a)==len(codice):
            conversione=codice
            con=0
            for n in codice:
                conversione=conversione.replace(n,a[con])
                if len(set(conversione))==len(set(codice)) and conversione==a:
                    risposta.add(a)
                con+=1
                    
        a=ind.readline()
    ind.close()
    return risposta
