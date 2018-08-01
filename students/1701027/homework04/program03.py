
from  my_html import HTMLNode, fparse


def conta_nodi(fileIn, selettore):
    rad = fparse(fileIn)
    selettore = selettore.split()
    padri,c = selet(selettore,rad)
    return c
    

def elimina_nodi(fileIn, selettore, fileOut):
    rad = fparse(fileIn)
    selettore = selettore.split()
    padri,c = selet(selettore,rad)
    delete(rad,padri)
    ris = rad.to_string()
    salva(fileOut,ris)
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    rad = fparse(fileIn)
    selettore = selettore.split()
    padri,c = selet(selettore,rad)
    modifica(rad,padri,chiave,valore)
    ris = rad.to_string()
    salva(fileOut,ris)
    
def modifica(nodo,lst,chiave,valore):
    if not nodo.istext():
        for figlio in nodo.content:
            if figlio in lst: figlio.attr[chiave] = valore
            modifica(figlio,lst,chiave,valore)
    
def delete(nodo,lst):
    if not nodo.istext():
        for figlio in nodo.content:
            if figlio in lst: nodo.content.remove(figlio)
            delete(figlio,lst)
            
def salva(fout,ris):
    with open(fout, "w",encoding='utf8') as f:
        f.write(ris)

def counttag(h1,h,nodo,selettore,padri):
    c = 0
    if h == h1:
        return c
    if not nodo.istext():
        h1 += 1
        for figlio in nodo.content:
            if str(figlio) == str('<'+selettore+'>'):
                c+=1
                padri.append(figlio)
            c += counttag(h1,h,figlio,selettore,padri)
    return c

def countattr(h1,h,nodo,selettore,padri):
    c = 0
    if h == h1:
        return c
    if not nodo.istext():
        h1 += 1
        for figlio in nodo.content:
            k = [k for k in figlio.attr if k == selettore[0] and figlio.attr[k] == selettore[1][1:-1]]
            if len(k) != 0:padri.append(figlio)
            c += countattr(h1,h,figlio,selettore,padri) +len(k)
    return c

def countclass(h1,h,nodo,selettore,padri):
    c = 0
    if h == h1:
        return c
    if not nodo.istext():
        h1 += 1
    if not nodo.istext():
        for figlio in nodo.content:
            k = [k for k in figlio.attr if k == 'class' and selettore in figlio.attr[k]]
            if len(k) != 0: padri.append(figlio)
            c += countclass(h1,h,figlio,selettore,padri) +len(k)
    return c

def selet(selettore,rad):
    c = 0
    h = 99999999999
    padri = [rad]
    for i in selettore:
        if i[0] == '#':
            c = 0
            lst = []
            i = ['id','"'+i[1:]+'"']
            for r in padri:
                h1 = 0
                c = countattr(h1,h,r,i,lst)
            padri = lst[:]
            h = 99999999999
            
        elif i == '>':
            h = 1
            
        elif i[0] == '@':
            i = i[2:-1].split('=')
            c = 0
            lst = []
            for r in padri:
                h1 = 0
                c += countattr(h1,h,r,i,lst)
            padri = lst[:]
            h = 99999999999
    
        elif i[0] == '.':
            c = 0
            lst = []
            for r in padri:
                h1 = 0
                c = countclass(h1,h,r,i[1:],lst)
            padri = lst[:]
            h = 99999999999
        else:
            c = 0
            lst = []
            for r in padri:
                h1 = 0
                c += counttag(h1,h,r,i,lst)
            padri = lst[:]
            h = 99999999999
    return padri,c