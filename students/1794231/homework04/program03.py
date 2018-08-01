# -*- coding: utf-8 -*-
from  my_html import HTMLNode, fparse

def conta_nodi(fileIn, selettore):
    trad, rel=traduci(selettore)
    c=fparse(fileIn)
    val=''
    risp=trovaelemento(c, trad, trad[0][1], trad[0][0], rel, val)
    return risp
def trovaelemento(c, trad, tipo, par, rel, val, cont=0, cr=0):
    if c.istext():
        return cont
    temp=0
    if tipo=='t':
        if c.tag==par:
            if len(val)==len(rel): cont+=1
            elif rel[cr]=='a':
                val=val+'a'
                temp=1
            elif rel[cr]=='p':
                val=val+'p'
                temp=1
    else:
        for key in c.attr:
            if tipo=='classi':
                if key==par:
                    if len(val)==len(rel): cont+=1
                    elif rel[cr]=='a':
                        val= val+'a'
                        temp=1
                    elif rel[cr]=='p':
                        val= val+'p'
                        temp=1
                    break
            if key==tipo:
                if c.attr[key]==par:
                    if len(val)==len(rel): cont+=1
                    elif rel[cr]=='a':
                        val= val+'a'
                        temp=1
                        break
                    elif rel[cr]=='p':
                        val= val+'p'
                        temp=1
                        break
    if rel:
        if temp==1: cr+=1
        elif temp==0 and rel[cr-1]=='p' and cr!=0:
            val=val[:-1]
            cr-=1
    for child in c.content:
        cont=trovaelemento(child, trad, trad[cr][1], trad[cr][0] , rel, val, cont, cr)
    return cont
def traduci(selettore):
    rel=[]
    trad=[]
    selettore=selettore.split()
    pf=2
    for parola in selettore:
        if parola[0]=='@':
            temp=parola[2:-1].split('=')
            trad.append([temp[1][1:-1], temp[0]])
        elif parola[0]=='#': trad.append([parola[1:], 'id'])
        elif parola[0]=='.': trad.append([parola[1:], 'classi'])
        elif parola!='>': trad.append([parola, 't'])
        if parola=='>': pf=1
        else:
            if pf==1: rel.append('p')
            elif pf==0: rel.append('a')
            pf=0
    return trad, rel

def elimina_nodi(fileIn, selettore, fileOut):
    trad, rel=traduci(selettore)
    c=fparse(fileIn)
    val=''
    individuaelimina(c, trad, trad[0][1], trad[0][0], rel, val)
    c=c.to_string()
    with open(fileOut, 'w', encoding='utf-8') as salv: salv.write(c)
    return
def individuaelimina(c, trad, tipo, par, rel, val, cr=0):
    listarimoz=[]
    cont=0
    if c.istext():
        return cont
    temp=0
    if tipo=='t':
        if c.tag==par:
            if len(val)==len(rel): cont+=1
            elif rel[cr]=='a':
                val=val+'a'
                temp=1
            elif rel[cr]=='p':
                val=val+'p'
                temp=1
    else:
        for key in c.attr:
            if tipo=='classi':
                if key==par:
                    if len(val)==len(rel): cont+=1
                    elif rel[cr]=='a':
                        val=val+'a'
                        temp=1
                    elif rel[cr]=='p':
                        val=val+'p'
                        temp=1
                    break
            if key==tipo:
                if c.attr[key]==par:
                    if len(val)==len(rel): cont+=1
                    elif rel[cr]=='a':
                        val=val+'a'
                        temp=1
                        break
                    elif rel[cr]=='p':
                        val=val+'p'
                        temp=1
                        break
    if rel:
        if temp==1: cr+=1
        elif temp==0 and rel[cr-1]=='p' and cr!=0:
            val=val[:-1]
            cr-=1
    if cont==0:
        for child in c.content:
            if individuaelimina(child, trad, trad[cr][1], trad[cr][0] , rel, val, cr)==1:
                listarimoz.append(child)
    for e in listarimoz:
        c.content.remove(e)
    return cont

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    trad, rel=traduci(selettore)
    c=fparse(fileIn)
    val=''
    change(c, trad, trad[0][1], trad[0][0], rel, val,chiave ,valore)
    c=c.to_string()
    with open(fileOut, 'w', encoding='utf-8') as salv:
        salv.write(c)
    return
def change(c, trad, tipo, par, rel, val,chiave ,valore, cr=0, cont=0):
    if c.istext():
        return cont
    temp=0
    if tipo=='t':
        if c.tag==par:
            if len(val)==len(rel): cont+=1
            elif rel[0]=='a':
                val=val+'a'
                temp=1
            elif rel[0]=='p':
                val=val+'p'
                temp=1
    else:
        for key in c.attr:
            if tipo=='classi':
                if key==par:
                    if len(val)==len(rel): cont+=1
                    elif rel[0]=='a':
                        val=val+'a'
                        temp=1
                    elif rel[0]=='p':
                        val=val+'p'
                        temp=1
                    break
            if key==tipo:
                if c.attr[key]==par:
                    if len(val)==len(rel): cont+=1
                    elif rel[0]=='a':
                        val=val+'a'
                        temp=1
                        break
                    elif rel[0]=='p':
                        val=val+'p'
                        temp=1
                        break
    if rel:
        if temp==1: cr+=1
        elif temp==0 and rel[cr-1]=='p' and cr!=0:
            val=val[:-1]
            cr-=1
    for child in c.content:
        if change(child, trad, trad[cr][1], trad[cr][0] , rel, val,chiave ,valore, cr)==1:
                child.attr[chiave]=valore
    return cont
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

