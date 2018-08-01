from  my_html import HTMLNode, fparse
import copy

def classe(res, nodo, c):
    for el in nodo.content:
        if not el.istext():
            d = el.attr
            if "class" in d.keys():
                if c in d["class"]:
                    res.append(el)
            classe(res, el, c)

def id(res, nodo, i):
    for el in nodo.content:
        if not el.istext():
            d = el.attr
            if "id" in d.keys():
                if i == d["id"]:
                    res.append(el)
            id(res, el, i)

def attributo(res, nodo, attr, val):
    for el in nodo.content:
        if not el.istext():
            d = el.attr
            if attr in d.keys():
                if d[attr] == val:
                    res.append(el)
            attributo(res, el, attr, val)

def tag(res, nodo, t):
    for el in nodo.content:
        if not el.istext():
            if el.tag == t:
                res.append(el)
            tag(res, el, t)

def figlio(res, nodo, b):
    for el in nodo.content:
        if not el.istext():
            res += base(el, b, False)

def discendente(res, nodo, b):
    for el in nodo.content:
        if not el.istext():
            res += base(el, b)

def base(html, padre, ric=True):
    r = list()
    if padre[0] == ".":
        # .class
        d = html.attr
        if "class" in d.keys():
            if padre[1:] in d["class"]:
                r.append(html)
        if ric:
            classe(r, html, padre[1:])
    elif padre[0] == "#":
        # #id
        d = html.attr
        if "id" in d.keys():
            if padre[1:] == d["id"]:
                r.append(html)
        if ric:
            id(r, html, padre[1:])
    elif padre[0] == "@":
        # @[attr="val"]
        attr = padre[2:padre.find("=")]
        val = padre[padre.find("=")+2:-2]
        d = html.attr
        if attr in d.keys():
            if d[attr] == val:
                r.append(html)
        if ric:
            attributo(r, html, attr, val)
    elif padre[0].isalpha():
        # tag
        if html.tag == padre:
            r.append(html)
        if ric:
            tag(r, html, padre)
    else:
        return False
    return r

def nodi(html, selettore):
    s = selettore.split()
    nodi = base(html, s[0])
    if len(s) > 1 and nodi != []:
        ind = 1
        while ind < len(s):
            sel = s[ind]
            r = list()
            if sel == ">":
                for el in nodi:
                    figlio(r, el, s[ind+1])
                ind += 1
            else:
                for el in nodi:
                    discendente(r, el, s[ind])
            nodi = r
            ind += 1
    return nodi

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    html = fparse(fileIn)
    n = nodi(html, selettore)
    return len(n)

def delete(nodo, el):
    for child in nodo.content:
        if not child.istext():
            if child == el:
                nodo.content.remove(child)
            delete(child, el)

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    html = fparse(fileIn)
    n = nodi(html, selettore)
    for el in n:
        delete(html, el)
    with open(fileOut, "w", encoding='utf8') as file:
        file.write(html.to_string())

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    html = fparse(fileIn)
    n = nodi(html, selettore)
    for el in n:
        el.attr[chiave] = valore
    with open(fileOut, "w", encoding='utf8') as file:
        file.write(html.to_string())
