# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:09:53 2017

@author: User
"""
from itertools import product
from copy import *


def decodificatore(configurazione):
    if len(configurazione)==1:
        global cifre
        global lista1
        global lista2
        global soluzione
        global combinazioni
        global l_codice
        combinazioni=[]
        cifre=[1,2,3,4,5,6,7,8,9]
        lista1=[]
        lista2=[0,1,2,3,4,5,6,7,8,9]
        soluzione=None
        l_codice=configurazione[0]
        return trova_cifre(l_codice,configurazione)
    else:
        if combinazioni==[]:
            if type(soluzione)!= list:
               return trova_cifre(l_codice,configurazione)
            else:
               combinazioni= lista_combinazioni(soluzione,l_codice)
               return combinazioni[0]
        else:
            combinazioni.remove(combinazioni[0])
            return indovina_codice(configurazione)

def lista_combinazioni(lista,l):
    if l==8:
       combo=product(lista,lista,lista,lista,lista,lista,lista,lista)
    elif l==7:
        combo=product(lista,lista,lista,lista,lista,lista,lista)
    else:
        combo=product(lista,lista,lista,lista,lista,lista)
    risposta=[]
    for x in combo:
        insieme=set(x)
        if len(insieme)==l:
            risposta.append(list(x))
        else:
            next
    return risposta

def trova_cifre(l,c):
    if len(c)==1:
        risposta=[]
        while l != 0:
            risposta+=[0]
            l=l-1
        global ultima
        ultima=0
        return risposta
    else:
        tupla=(c[-1])[-1]
        if tupla==(0,0):
            lista2.remove(ultima)
            if len(lista2)==l:
                global soluzione
                soluzione=lista2
                return decodificatore(soluzione)
            else:
                risposta=[]
                while l != 0:
                   risposta+=[cifre[0]]
                   l=l-1
                ultima=cifre[0]
                cifre.remove(cifre[0])
                return risposta
        else:
            lista1.append(ultima)
            if len(lista1)== l:
                soluzione=lista1
                return decodificatore(soluzione)
            else:
                risposta=[]
                while l != 0:
                   risposta+=[cifre[0]]
                   l=l-1
                ultima=cifre[0]
                cifre.remove(cifre[0])
                return risposta
        
def indovina_codice(c):   
        lista=(c[-1])[0]
        tupla=(c[-1])[-1]
        global combinazioni
        if tupla[0]<tupla[1]:
            minore=tupla[0]
        else:
            minore=tupla[1]
        lista2=[]
        if minore==1 or minore==0:
           for x in combinazioni:
               uguali=confronto(lista,x)
               if uguali == minore:
                   lista2.append(x)
               else:
                   next
           combinazioni=lista2
           return combinazioni[0]
        else:
            for x in combinazioni:
               uguali=confronto(lista,x)
               if uguali == tupla[0] or uguali== tupla[1]:
                   lista2.append(x)
               else:
                   next
            combinazioni=lista2
            return combinazioni[0]
            
           


def confronto(codice, proposta):
    c=0
    for i in range(len(codice)):
        if codice[i]==proposta[i]:
            c+=1
        else:
            next  
    return c