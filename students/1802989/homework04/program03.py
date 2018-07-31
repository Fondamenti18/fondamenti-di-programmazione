from  my_html import HTMLNode, fparse

def conta_nodi(fileIn, selettore):
    'Funzione per contare i nodi di un albero'
    file, lista_nodi = finder(fileIn, selettore)
    return len(lista_nodi)

def finder(fileIn, selettore):
    'Funzione main-hub che è in grado di cercare nella pagina HTML'
    specials = {'#': 'id', '.': 'class'}
    file_ris = fparse(fileIn)
    lista_nodi = [file_ris]
    selectors = selettore.split()
    index = 0
    while index < len(selectors):
        ris = []
        prefix = selectors[index][0]
        if prefix in specials:
            lista_nodi = iter_find_by_attr(lista_nodi, specials[prefix], selectors[index][1:], ris)
            index += 1
        elif prefix == '@':
            prop,value = (selectors[index][2:-1]).split('=')
            lista_nodi = iter_find_by_at(lista_nodi, prop, value[1:-1], ris)
            index += 1
        elif prefix == '>':
            index += 1
            prefix = selectors[index][0]
            if prefix in specials:
                lista_nodi =  iter_quick_find_by_attr(lista_nodi, specials[prefix], selectors[index][1:], ris)
                index += 1
            else:
                lista_nodi = iter_quick_find_by_tag(lista_nodi, selectors[index], ris)
                index += 1
        else:
            for nodo in lista_nodi:
                ris += deep_find_by_tag(nodo, selectors[index])
            lista_nodi = ris
            index += 1
    return file_ris, lista_nodi
    
def deep_find_by_tag(nodo, tag):
    'Funzione ricorsiva che cerca in profondita per tag'
    lista = []
    if nodo.tag == tag: lista += [nodo]
    if not nodo.istext():
        for figlio in nodo.content:
            lista += deep_find_by_tag(figlio, tag)
    return lista

def quick_find_by_tag(nodo, tag):
    'Funzione che cerca i diretti discedenti di un nodo'
    lista = []
    if nodo.tag == tag: lista += [nodo]
    if not nodo.istext():
        for figlio in nodo.content:
            if figlio.tag == tag:
                lista += [figlio]
    return lista

def find_by_attr(nodo, key , attr):
    'Funzione che cerca per id o classi'
    lista = []
    if key in nodo.attr and (attr == nodo.attr[key] or (attr in nodo.attr[key] and ' ' in nodo.attr[key])):
        lista += [nodo]
    if not nodo.istext():
        for figlio in nodo.content:
            lista += find_by_attr(figlio, key ,attr)
    return lista

def quick_find_by_attr(nodo, key, attr):
    lista = []
    if key in nodo.attr and attr in nodo.attr[key]: lista += [nodo]
    if not nodo.istext():
        for figlio in nodo.content:
            if key in figlio.attr and attr in figlio.attr[key]:
                lista += [figlio]
    return lista

def find_by_at(nodo, prop, value):
    'Funzione che cerca per generici attributi'
    lista = []
    if nodo.attr and prop in nodo.attr and nodo.attr[prop] == value:
        lista += [nodo]
    if not nodo.istext():
        for figlio in nodo.content:
            lista += find_by_at(figlio, prop, value)
    return lista

def elimina_nodi(fileIn, selettore, fileOut):
    file, lista_nodi = finder(fileIn, selettore)
    for nodo in lista_nodi:
        nodo.tag = '_text_'
        nodo.content = ''
    with open(fileOut, 'w') as file_out:
        file_out.write(file.to_string())

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    'Funzione che riconosce gli attributi e li modifica'
    file, lista_nodi = finder(fileIn, selettore)
    for nodo in lista_nodi:
        nodo.attr[chiave] = valore
    with open(fileOut, 'w') as file_out:
        file_out.write(file.to_string())
        
def iter_find_by_attr(lista_nodi, chiave, elemento, ris):
    'Funzione iteratrice sul finder_attr'
    for nodo in lista_nodi:
        ris += find_by_attr(nodo, chiave, elemento)
    return ris

def iter_find_by_at(lista_nodi, prop, value, ris):
    'Funzione iteratrice sul finder_at'
    for nodo in lista_nodi:
        ris += find_by_at(nodo, prop, value)
    return ris

def iter_quick_find_by_tag(lista_nodi, elemento, ris):
    'Funzione iteratrice sul finder_tag'
    for nodo in lista_nodi:
        ris += quick_find_by_tag(nodo, elemento)
    return ris

def iter_quick_find_by_attr(lista_nodi, chiave, elemento, ris):
    'Funzione iteratrice sugli attributi'
    for nodo in lista_nodi:
        ris += quick_find_by_attr(nodo, chiave, elemento)
    return ris