# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:20:05 2017

@author: miki1
"""

from  my_html import HTMLNode, fparse

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    albero = fparse(fileIn)
    if len(selettore.split()) == 1:
        lista=[]
        return contaFacile(albero,selettore,lista)
    elif len(selettore.split()) == 3:
        lista = []
        return contaMedio(albero,selettore,lista)
    elif len(selettore.split()) == 2:
        lista=[]
        avo=False
        return contaFastidioso(albero,selettore,lista,avo)
    else:
        lista = []
        avo = False
        return contaFastidiosissimo(albero,selettore,lista,avo)
        
    

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    nodo = fparse(fileIn)
    if len(selettore.split()) == 1:
        return cancellaFacile(nodo,selettore,fileOut)
    if len(selettore.split()) == 2:
        return cancellaFastidioso(nodo,selettore,False,fileOut)
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    nodo = fparse(fileIn)
    if len(selettore.split()) == 1:
        return(cambiaFacile(nodo,selettore,chiave,valore,fileOut))
    else:
        avo = False
        return(cambiaFastidioso(nodo,selettore,avo,chiave,valore,fileOut))

  
            
def lista_attributi(nodo):
    diz = nodo.attr
    lista = []
    lista.append(nodo.tag)
    for chiave in diz:
        risultato = ''
        if chiave == 'class':
            risultato+='.'
            risultato+=diz[chiave]
            lista.append(risultato)
        elif chiave == 'id':
            risultato1 = risultato
            risultato+='#'
            risultato1 = risultato1 + "@["+chiave+"=\""+diz[chiave]+"\"]"
            risultato+=diz[chiave]
            lista.append(risultato)
            lista.append(risultato1)
        elif chiave == 'title':
            risultato+='.title'
            lista.append(risultato)
        else:
            risultato = risultato + "@["+chiave+"=\""+diz[chiave]+"\"]"
            lista.append(risultato)
    return lista
        
def contaFastidioso(nodo,selettore,lista,avo):
    sel = selettore.split()
    if sel[0] in lista_attributi(nodo):
        avo = True
    for figlio in nodo.content:
        #print(figlio)
        if type(figlio.content) == list:
            #print('cacca')
            #print(sel[1],lista_attributi(figlio))
            #print(avo)
            if sel[1] in lista_attributi(figlio) and avo == True:
                #print('entrooooooooooooooo')
                lista.append('a')
                #print(contatore)
            else:
                contaFastidioso(figlio,selettore,lista,avo)
    return len(lista)

def contaMedio(nodo,selettore,lista):
    sel = selettore.split()
    if sel[0] in lista_attributi(nodo):
        for figlio in nodo.content:
            #print(figlio)
            if type(figlio.content) == list:
                if sel[2] in lista_attributi(figlio):
                    lista.append('a')
    for x in nodo.content:
        if type(x.content) == list:
            contaMedio(x,selettore,lista)
    return len(lista)



def contaFastidiosissimo(nodo,selettore,lista,avo):
    sel = selettore.split()
    if sel[0] in lista_attributi(nodo):
        for figlio in nodo.content:
            if not figlio.istext():
                if sel[2] in lista_attributi(figlio):
                    avo = True
    if sel[3] in lista_attributi(nodo):
        for figlio in nodo.content:
            if not figlio.istext():
                if sel[5] in lista_attributi(figlio) and avo == True:
                    lista.append('c')
    for figlio in nodo.content:
            if not figlio.istext():
                contaFastidiosissimo(figlio,selettore,lista,avo)
    return len(lista)

def contaFacile(nodo,selettore,lista):
    if selettore in lista_attributi(nodo):
        #print(lista)
        lista.append('a')
    for x in nodo.content:
        #print(nodo.attr)
        #print(lista_attributi(nodo))
        if type(x.content) == list:
            contaFacile(x,selettore,lista)
    return len(lista)

def cancellaFacile(nodo,selettore,fileOut):
    if selettore in lista_attributi(nodo):
        #print(lista)
        del(nodo)
    for x in nodo.content:
        #print(nodo.attr)
        #print(lista_attributi(nodo))
        if type(x.content) == list:
            cancellaFacile(x,selettore,fileOut)
    stringa = nodo.to_string()         
    with open(fileOut,'w',encode='utf-8') as f:
        f.write(stringa)


def cancellaFastidioso(nodo,selettore,avo,fileOut):
    sel = selettore.split()
    if sel[0] in lista_attributi(nodo):
        avo = True
    for figlio in nodo.content:
        #print(figlio)
        if type(figlio.content) == list:
            #print('cacca')
            #print(sel[1],lista_attributi(figlio),figlio.tag)
            #print(avo)
            if sel[1] in lista_attributi(figlio) and avo == True:
                #print(figlio.tag,lista_attributi(figlio))
                (nodo.content).remove(figlio)
                #print(contatore)
            else:
                cancellaFastidioso(figlio,selettore,avo,fileOut)
    for figlio in nodo.content:
        if type(figlio.content) == list:
            cancellaFastidioso(figlio,selettore,avo,fileOut)
    stringa = nodo.to_string()         
    with open(fileOut,'w',encoding='utf-8') as f:
        f.write(stringa)
        
def cancellaFastidiosissimo(nodo,selettore,avo,fileOut):
    sel = selettore.split()
    if sel[0] in lista_attributi(nodo):
        for figlio in nodo.content:
            if not figlio.istext():
                if sel[2] in lista_attributi(figlio):
                    avo = True
    if sel[3] in lista_attributi(nodo):
        for figlio in nodo.content:
            if not figlio.istext():
                if sel[5] in lista_attributi(figlio) and avo == True:
                    (nodo.content).remove(figlio)
    for figlio in nodo.content:
            if not figlio.istext():
                contaFastidiosissimo(figlio,selettore,avo,fileOut)
    stringa = nodo.to_string()         
    with open(fileOut,'w',encoding='utf-8') as f:
        f.write(stringa)
        
def cambiaFacile(nodo,selettore,chiave,valore,fileOut):
    if selettore in lista_attributi(nodo):
        #print(lista)
        nodo.attr[chiave] = valore
    for x in nodo.content:
        #print(nodo.attr)
        #print(lista_attributi(nodo))
        if type(x.content) == list:
            cambiaFacile(x,selettore,chiave,valore,fileOut)
    stringa = nodo.to_string()
    with open(fileOut,'w',encoding='utf-8') as f:
        f.write(stringa)
        
def cambiaFastidioso(nodo,selettore,avo,chiave,valore,fileOut):
    sel = selettore.split()
    if sel[0] in lista_attributi(nodo):
        avo = True
    for figlio in nodo.content:
        #print(figlio)
        if type(figlio.content) == list:
            #print('cacca')
            #print(sel[1],lista_attributi(figlio))
            #print(avo)
            if sel[1] in lista_attributi(figlio) and avo == True:
                #print('entrooooooooooooooo')
                figlio.attr[chiave] = valore
                #print(contatore)
            else:
                cambiaFastidioso(figlio,selettore,avo,chiave,valore,fileOut)
    stringa = nodo.to_string()
    with open(fileOut,'w',encoding='utf-8') as f:
        f.write(stringa)
        
  