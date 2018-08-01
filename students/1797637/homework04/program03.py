from  my_html import HTMLNode, fparse

occ_count = 0

def recogn_sel(doc, sel, sel_count):
    if doc.tag == sel:
        return True
    elif sel[0] == '.':
        return sel_class(doc, sel)    
    elif sel[0] == '#':
        return sel_id(doc, sel)    
    elif sel[0] == '@':
        return sel_attr(doc, sel)
    return False

def sel_class(doc, sel):
    if 'class' in doc.attr:
        if sel[1:] in doc.attr['class'] :
            return True
        else: return False
    else: return False

def sel_id(doc, sel):
    if 'id' in doc.attr:
        if sel[1:] in doc.attr['id'] :
            return True
        else: return False
    else: return False

def sel_attr(doc, sel):
    attribute = sel[2:-1]
    attribute = attribute.split('=')
    if attribute[0] in doc.attr:
        if attribute[1][2:-2] in doc.attr[attribute[0]] :
            return True
        else: return False
    else: return False
    

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    doc = fparse(fileIn)
    list_sel = selettore.split(' ') 
    search_tree(doc, list_sel[0], list_sel)
    global occ_count
    result = occ_count
    occ_count=0
    return result

def search_tree(doc, sel, list_sel, sel_count = 0):
    if doc.istext():
        return
    if count_one(doc, sel, list_sel, sel_count):
        return
    if sel == '>':
        sel_count += 1
        sel = list_sel[sel_count]
        if recogn_sel(doc, sel, sel_count):
            search_tree(doc, sel, list_sel, sel_count)   
        return
    sel, sel_count = increase_sel(doc, sel, list_sel, sel_count)
    for child_doc in doc.content:
        search_tree(child_doc, sel, list_sel, sel_count)  

def count_one(doc, sel, list_sel, sel_count):
    global occ_count  
    if sel_count == len(list_sel)-1:
        if recogn_sel(doc, sel, sel_count):
            occ_count += 1
        for child_doc in doc.content:
            search_tree(child_doc, sel, list_sel, sel_count)
        return True

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    doc = fparse(fileIn)
    list_sel = selettore.split(' ')
    delete_node(doc, doc, list_sel[0], list_sel)
    f = open(fileOut, mode='w', encoding='utf-8')
    f.write(doc.to_string())
    f.close

def delete_node(doc, prev_doc, sel, list_sel, sel_count = 0):
    if doc.istext():
        return
    if apply_delete(doc, prev_doc, sel, list_sel, sel_count):
        return
    if sel == '>':
        sel_count += 1
        sel = list_sel[sel_count]
        if recogn_sel(doc, sel, sel_count):
            delete_node(doc, prev_doc, sel, list_sel, sel_count)
        return
    sel, sel_count = increase_sel(doc, sel, list_sel, sel_count)
    for child_doc in doc.content:
        delete_node(child_doc, doc, sel, list_sel, sel_count) 

def apply_delete(doc, prev_doc, sel, list_sel, sel_count):
    if sel_count == len(list_sel)-1:
        if recogn_sel(doc, sel, sel_count):
            prev_doc.content.remove(doc)
        for child_doc in doc.content:
            delete_node(child_doc, doc, sel, list_sel, sel_count)
        return True

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    doc = fparse(fileIn)
    list_sel = selettore.split(' ')
    change_attr(doc, list_sel[0], list_sel, chiave, valore)
    f = open(fileOut, mode='w', encoding='utf-8')
    f.write(doc.to_string())
    f.close

def change_attr(doc, sel, list_sel, chiave, valore, sel_count = 0):
    if doc.istext():
        return
    if apply_change(doc, sel, list_sel, chiave, valore, sel_count):
        return
    if sel == '>':
        sel_count += 1
        sel = list_sel[sel_count]
        if recogn_sel(doc, sel, sel_count):
            change_attr(doc, sel, list_sel, chiave, valore, sel_count)
        return
    sel, sel_count = increase_sel(doc, sel, list_sel, sel_count)
    for child_doc in doc.content:
        change_attr(child_doc, sel, list_sel, chiave, valore, sel_count)

def apply_change(doc, sel, list_sel, chiave, valore, sel_count):
    if sel_count == len(list_sel)-1:
        if recogn_sel(doc, sel, sel_count):
            doc.attr[chiave] = valore
        for child_doc in doc.content:
            change_attr(child_doc, sel, list_sel, chiave, valore, sel_count)
        return True

def increase_sel(doc, sel, list_sel, sel_count):
    if recogn_sel(doc, sel, sel_count):
        sel_count += 1
        sel = list_sel[sel_count]
    return sel, sel_count