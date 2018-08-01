# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:58:08 2017

@author: Alessio
"""
from collections import Counter

def fattori_primi(num):
    x = 2
    lista_fattori = []
    while x * x <= num:
        if num % x:
            x += 1
        else:
            num //= x
            lista_fattori.append(x)
    if num > 1:
        lista_fattori.append(num)
    return (lista_fattori)

def contatore(lista_fattori):
    d={}
    lista_occorrenze=[]
    d=Counter(lista_fattori)
    lista_occorrenze=d.values()
    return (list(lista_occorrenze))
    
def numero_divisori(lista_occorrenze):
    prodotto=1
    for x in list(lista_occorrenze):
        x+=1
        prodotto*=x
        prodotto_finale=int(prodotto)-2
    return (prodotto_finale)
    
def finale(lista_iniziale,k):
    lista_finale=[]
    for i in lista_iniziale:
        n=numero_divisori(contatore(fattori_primi(i)))
    if n==k:
        lista_finale.append(i)
    return (lista_finale)