#

from  my_html import HTMLNode, fparse


def find_by_attr_value(nodo, attributo, valore):

    ret = []
    if attributo in nodo.attr.keys():
        if valore == nodo.attr[attributo]: ret += [nodo]

    if nodo.tag != '_text_':
        for figlio in nodo.content:
            ret += find_by_attr_value(figlio, attributo, valore)
    return ret

def find_by_attr_value_dir(nodo, attributo, valore):

    ret = []
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            if attributo in figlio.attr.keys():
                if valore in figlio.attr[attributo]: ret += [figlio]
    return ret

def find_by_class_value(nodo, classVal):

    ret = []
    if 'class' in nodo.attr.keys():
        if classVal in nodo.attr['class']: ret += [nodo]

    if nodo.tag != '_text_':
        for figlio in nodo.content:
            ret += find_by_class_value(figlio, classVal)

    return ret 

def find_by_class_value_dir(nodo, classVal):

    ret = []
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            if 'class' in figlio.attr.keys():
                if classVal in figlio.attr['class']: ret += [figlio]

    return ret

def find_by_id(nodo, id):

    ret = []
    if 'id' in nodo.attr.keys():
        if nodo.attr['id'] == id: ret += [nodo]

    if nodo.tag != '_text_':
        for figlio in nodo.content:
            ret += find_by_id(figlio, id)

    return ret

def find_by_id_dir(nodo, id):

    ret = []

    if nodo.tag != '_text_':
        for figlio in nodo.content:
            if 'id' in figlio.attr.keys():
                if figlio.attr['id'] == id: ret += [figlio]

    return ret

def find_by_tag(nodo, tag):

    ret = []
    if nodo.tag == tag: ret += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret += find_by_tag(figlio, tag)
    return ret

def elimina(nodo, tag):

    i = -1
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            i+=1
            if tag == str(repr(nodo.content[i])):
                del nodo.content[i]
            elimina(nodo.content[i], tag)
    return nodo

def cambia(nodo, tag, chiave, valore):

    i = -1
    
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            i+=1
            #print(tag, str(repr(nodo.content[i])))
            if tag == str(repr(nodo.content[i])):
                nodo.content[i].attr[chiave] = valore
                #print(nodo.content[i].attr)
            cambia(nodo.content[i], tag, chiave, valore)
    return nodo

def find_by_tag_dir(nodo, tag):

    ret = []
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            if figlio.tag == tag: ret += [figlio]
    
    return ret

def estrai_attributo(nodo, selettore):

    attributo = ''
    tot = 2
    for x in selettore:
        if not x.isalnum():
            break
        tot += 1
        attributo += ''.join(x)
    
    valore = selettore[tot:-2]
    return attributo, valore

def interpreta_selettore(selettore, nodo, id):

    if '.' in selettore[0]:
        if id == 1:
            return find_by_class_value_dir(nodo, selettore[1:])
        return find_by_class_value(nodo, selettore[1:]) 

    elif '#' in selettore[0]: 
        if id == 1:
            return find_by_id_dir(nodo, selettore[1:])
        else: return find_by_id(nodo, selettore[1:])

    elif '@' in selettore[0]:
        combo = estrai_attributo(nodo, selettore[2:])
        if id == 1:
            return find_by_attr_value_dir(nodo, combo[0], combo[1])
        else: return find_by_attr_value(nodo, combo[0], combo[1])           

    else:
        if id == 1:
            return find_by_tag_dir(nodo, selettore)
        else: return find_by_tag(nodo, selettore)

def genera_selettore(selettore):

    i = 0
    while i != len(selettore)-1:
        if selettore[i+1] != '>':
            selettore.insert(i+1, '$')
        i+= 2
    
    return selettore

def trova_concatenato(selettore, nodo, i = 0):

    switch = 0
    j = 0
    b = []
    if selettore[i+1] == '>': switch = 1
    
    while j != len(nodo):
        
        b += interpreta_selettore(selettore[i+2], nodo[j], switch)
        
        j += 1

    if i+2 == len(selettore)-1: return b
    
    b = trova_concatenato(selettore, b, i+2)
    
    return b

def selettoreCompl(selettore, nodo):

    selettore = genera_selettore(selettore)

    listaTrovati = interpreta_selettore(selettore[0], nodo, 0)
    listaNodi = trova_concatenato(selettore, listaTrovati)

    return listaNodi


def conta_nodi(fileIn, selettore):

    nodo = fparse(fileIn)
    if len(selettore.split()) == 1: return len(interpreta_selettore(str(selettore), nodo, 0))

    return len(selettoreCompl(selettore.split(), nodo))
       
def elimina_nodi(fileIn, selettore, fileOut):
    
    nodo = fparse(fileIn)
    if len(selettore.split()) == 1: listaNodi = interpreta_selettore(str(selettore), nodo, 0)
    else: listaNodi = selettoreCompl(selettore.split(), nodo)
    for x in range(len(listaNodi)):
        
        nodo = elimina(nodo, repr(listaNodi[x]))
    if selettore == nodo.tag:
        file = open(fileOut, "w", encoding="utf-8")
        file.write('')
        return
    file = open(fileOut,"w", encoding="utf-8")
    file.write(nodo.to_string())
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut, i= 0):
    
    nodo = fparse(fileIn)
    if len(selettore.split()) == 1: listaNodi = interpreta_selettore(str(selettore), nodo, 0)
    else: listaNodi = selettoreCompl(selettore.split(), nodo)
    #print(listaNodi)
    for x in range(len(listaNodi)):

        nodo = cambia(nodo, repr(listaNodi[x]), chiave, valore)
    file = open(fileOut,"w", encoding="utf-8")
    file.write(nodo.to_string())
    