from  my_html import HTMLNode, fparse


def conta_nodi(fileIn, selettore):
    global root
    global trovati
    trovati=[]
    root=fparse(fileIn)
    lista_nodi=[root]
    sel=dividi_selettore(selettore)
    cont=0
    lista=cerca_selettore(sel, lista_nodi)
    return len(trovati)

def dividi_selettore(selettore):
    return selettore.split()

def cerca_selettore(sel, lista_nodi, rec=True):
    global trovati
    prossimo=1
    diz=dict()
    lista=[]
    lista_ricerca=lista_nodi
    if sel[0].isalnum():
        for i in lista_ricerca:
            lista+=ricerca_per_tag(i, sel[0],rec)
    if sel[0].startswith('.'):
        for i in lista_ricerca:
            testo=sel[0][1:]
            lista+=ricerca_per_class(i, testo,rec)
    if sel[0].startswith('#'):
        for i in lista_ricerca:
            value=sel[0][1:]
            lista+=ricerca_per_attr(i, 'id', value, rec)
    if sel[0].startswith('@'):
        for i in lista_ricerca:
            attr, val =separa_attr_val(sel[0])
            lista+=ricerca_per_attr(i,attr,val, rec)
    if sel[0]=='>':
        lista=lista_ricerca
        rec=False
    else:
        rec=True
    if len(sel)>1:
        lista+=cerca_selettore(sel[1:], lista, rec)
    else:
        trovati+=lista
    return lista

def ricerca_per_class(node, value, rec):
    ret=[]
    if rec==False:
        for child in node.content:
            if 'class' in child.attr.keys():
                a=child.attr['class']
                if value in a:
                    ret+=[node]
        return ret
    if 'class' in node.attr.keys():
        a=node.attr['class']
        if value in a:
            ret+=[node]
    if not node.istext():
        for child in node.content:
            ret+= ricerca_per_class(child,value,rec)       
    return ret  

def separa_attr_val(stringa):
        stringa=stringa[2:-1]
        coppia=stringa.split('=')
        coppia[1]=coppia[1][1:-1]
        return coppia[0],coppia[1]
    
def ricerca_per_attr(node,key, value, rec):
    ret=[]
    if rec==False:
        for child in node.content:
            if key in child.attr.keys():
                if child.attr[key]==value: 
                    ret+=[child]
        return ret
    if key in node.attr.keys():
        if node.attr[key]==value: 
            ret+=[node]
    if not node.istext():
            for child in node.content:
                ret+= ricerca_per_attr(child,key,value,rec)
    return ret  

def rimuovi(padre,figli):
    for i in figli:
        padre.content.remove(i)
                                           
def ricerca_per_tag(node, tag, rec):
    ret=[]
    if rec==False:
        for child in node.content:
            if child.tag==tag:
                ret+=[child]
        return ret
                    
    if node.tag==tag: 
        ret+=[node]
    if not node.istext():
        for child in node.content:
            ret+=ricerca_per_tag(child,tag,rec)
    return ret

def elimina_nodi(fileIn, selettore, fileOut):
    global root
    global trovati
    global figli_padri
    figli_padri=dict()
    trovati=[]
    root=fparse(fileIn)
    lista_nodi=[root]
    sel=dividi_selettore(selettore)
    lista=cerca_selettore(sel, lista_nodi)
    for i in trovati:
        elimina(root, i)
    stringa=root.to_string()
    with open(fileOut,'w') as f:
        f.write(stringa)
        
def elimina(node, figlio):
    if not node.istext():
        for child in node.content:
            if figlio in node.content:
                node.content.remove(figlio)
            else:
                if not child.istext():
                    elimina(child, figlio)
    return 
            
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    global root
    global trovati
    trovati=[]
    root=fparse(fileIn)
    lista_nodi=[root]
    sel=dividi_selettore(selettore)
    cont=0
    lista=cerca_selettore(sel, lista_nodi)
    for i in trovati:
            i.attr[chiave]=valore
    stringa=root.to_string()
    with open(fileOut,'w') as f:
        f.write(stringa)