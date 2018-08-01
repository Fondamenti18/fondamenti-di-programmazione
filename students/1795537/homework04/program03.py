from  my_html import HTMLNode, fparse

def trovaDaTag(nodo, tag):
    '''conta il numero di nodi aventi il tag cercato'''
    nNodi = 0
    if nodo.tag == tag: nNodi += 1
    if not nodo.istext():
        for el in nodo.content:
            nNodi += trovaDaTag(el, tag)
    return nNodi

def trovaDaID(nodo, id_nodo):
    '''conta il numero di nodi aventi l'ID cercato'''
    nNodi = 0
    try:
        if nodo.attr['id'] == id_nodo: nNodi += 1
    except: pass
    if not nodo.istext():
        for el in nodo.content:
            nNodi += trovaDaID(el, id_nodo)
    return nNodi

def trovaDaClasse(nodo, classe):
    '''conta il numero di nodi aventi l'ID cercato'''
    nNodi = 0
    try:
        if classe in nodo.attr['class']: nNodi += 1
    except: pass
    if not nodo.istext():
        for el in nodo.content:
            nNodi += trovaDaClasse(el, classe)
    return nNodi

def trovaDaAttributo(nodo, attributo):
    '''conta il numero di nodi aventi l'ID cercato'''
    att = attributo.replace('="', ' ')
    att = att[1:-2]
    att = att.split()
    nNodi = 0
    try:
        if nodo.attr[att[0]] == att[1]: nNodi += 1
    except: pass
    if not nodo.istext():
        for el in nodo.content:
            nNodi += trovaDaAttributo(el, attributo)
    return nNodi

def trovaPadreFiglio(nodo, selettore, pos=0):
    '''controllo i vari padri se hanno i figli cercati uno consecutivo agli altri'''
    nNodi = 0
    if nodo.tag == selettore[pos] and pos == len(selettore)-1 : 
        nNodi += 1
    elif nodo.tag == selettore[pos] and pos != len(selettore)-1 : 
        pos = pos+1
    else : pos = 0
    if not nodo.istext():
        for el in nodo.content:
            nNodi += trovaPadreFiglio(el, selettore, pos)
    return nNodi

def trovaAvoDiscendente(nodo, selettore, pos=0):
    '''controllo i vari padri se hanno i figli cercati'''
    nNodi = 0
    if nodo.tag == selettore[pos] and pos == len(selettore)-1 : 
        nNodi += 1
    elif nodo.tag == selettore[pos] and pos != len(selettore)-1 : 
        pos = pos+1
    if not nodo.istext():
        for el in nodo.content:
            nNodi += trovaAvoDiscendente(el, selettore, pos)
    return nNodi
    
def trovaSelettoreT(nodo, selettore):
    '''esamino il selettore dato. in base al selettore richiamo la funzione corretta'''
    sel2 = selettore.split()
    s = []
    if selettore[0] == '.' : return(trovaDaClasse(nodo, selettore[1:]))
    if selettore[0] == '@' : return(trovaDaAttributo(nodo, selettore[1:]))
    if selettore[0] == '#' : return(trovaDaID(nodo, selettore[1:]))
    if len(sel2) == 1 : return(trovaDaTag(nodo, selettore))
    if sel2[1] == '>' : 
        for i in range(0, len(sel2), 2):
            s += [sel2[i]]
        return(trovaPadreFiglio(nodo, s))
    else : return (trovaAvoDiscendente(nodo, sel2))


def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    file = fparse(fileIn)
    return (trovaSelettoreT(file, selettore))
'''-----------------------------------------------------------------------------------------------------------------------------------------------------'''
def eliminaDaTag(nodo, tag):
    '''cerco e cancello il nodo avente il tag cercato'''
    if nodo.istext(): return
    for pos, el in enumerate(nodo.content):
        if el.tag == tag:
            del(nodo.content[pos])
        else: eliminaDaTag(el, tag)
    
def eliminaDaID(nodo, id_nodo):
    '''cerco e cancello il nodo avente l' ID cercato'''
    if nodo.istext(): return
    for pos, el in enumerate(nodo.content):
        try:
            if el.attr['id'] == id_nodo:
                del(nodo.content[pos])  
        except: eliminaDaID(el, id_nodo)
    
def eliminaDaClasse(nodo, classe):
    '''cerco e cancello il nodo avente la classe cercata'''
    if nodo.istext(): return
    for pos, el in enumerate(nodo.content):
        try:
            if classe in el.attr['class']:
                del(nodo.content[pos])  
        except: eliminaDaClasse(el, classe)
        
def eliminaDaAttributo(nodo, attributo):
    '''cerco e cancello il nodo avente l'attributo cercato'''
    att = attributo.replace('="', ' ')
    att = att[1:-2]
    att = att.split()
    if nodo.istext(): return
    for pos, el in enumerate(nodo.content):
        try:
            if el.attr[att[0]] == att[1]:
                del(nodo.content[pos])  
        except: eliminaDaAttributo(el, attributo)
        
def eliminaPadreFiglio(nodo, selettore, pos=0):
    '''cerco e cancello i vari padri che hanno i figli cercati uno consecutivo all'altro'''
    if nodo.tag == selettore[pos] and pos != len(selettore)-1: 
        pos += 1
    elif nodo.tag == selettore[pos] and pos == len(selettore)-1: 
        return (True)
    else : pos=0
    if not nodo.istext():
        for pose, el in enumerate(nodo.content):
            if eliminaPadreFiglio(el, selettore, pos):
                del(nodo.content[pose])
            
def eliminaAvoDiscendente(nodo, selettore, pos=0):
    '''cerco e cancello i vari padri che hanno i figli cercati'''
    if nodo.tag == selettore[pos] and pos != len(selettore)-1: 
        pos += 1
    elif nodo.tag == selettore[pos] and pos == len(selettore)-1: 
        return (True)
    if not nodo.istext():
        for pose, el in enumerate(nodo.content):
            if eliminaAvoDiscendente(el, selettore, pos):
                del(nodo.content[pose])

def trovaSelettoreC(nodo, selettore):
    '''esamino il selettore dato. in base al selettore richiamo la funzione corretta'''
    sel2 = selettore.split()
    s = []
    if selettore[0] == '.' : return(eliminaDaClasse(nodo, selettore[1:]))
    if selettore[0] == '@' : return(eliminaDaAttributo(nodo, selettore[1:]))
    if selettore[0] == '#' : return(eliminaDaID(nodo, selettore[1:]))
    if len(sel2) == 1 : return(eliminaDaTag(nodo, selettore))
    if sel2[1] == '>' : 
        for i in range(0, len(sel2), 2):
            s += [sel2[i]]
        return(eliminaPadreFiglio(nodo, s))
    else : return (eliminaAvoDiscendente(nodo, sel2))
       
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    file = fparse(fileIn)
    trovaSelettoreC(file, selettore)
    f = open(fileOut, mode='w')
    f.write(file.to_string())
    f.close()
#'''-----------------------------------------------------------------------------------------------------------------------------------------------------'''
def modificaDaTag(nodo, tag, chiave, valore):
    '''cerco e cancello il nodo avente il tag cercato'''
    if nodo.istext(): return
    for pos, el in enumerate(nodo.content):
        if el.tag == tag:
            el.attr[chiave] = valore
        else: modificaDaTag(el, tag, chiave, valore)

def modificaDaID(nodo, id_nodo, chiave, valore):
    '''cerco e cancello il nodo avente l' ID cercato'''
    if not nodo.istext():
        for el in nodo.content:
            if 'id' in el.attr:
                if el.attr['id'] == id_nodo:
                    el.attr[chiave] = valore
            modificaDaID(el, id_nodo, chiave, valore)
        
def modificaDaClasse(nodo, classe, chiave, valore):
    '''cerco e cancello il nodo avente la classe cercata'''
    if nodo.istext(): return
    for pos, el in enumerate(nodo.content):
        try:
            if classe in el.attr['class']:
                el.attr[chiave] = valore  
        except: modificaDaClasse(el, classe, chiave, valore)
        
def modificaDaAttributo(nodo, attributo, chiave, valore):
    '''cerco e cancello il nodo avente l'attributo cercato'''
    att = attributo.replace('="', ' ')
    att = att[1:]
    att = att.split()
    if nodo.istext(): return
    for pos, el in enumerate(nodo.content):
        try:
            if el.attr[att[0]] == att[1]:
                el.attr[chiave] = valore
        except: modificaDaAttributo(el, attributo, chiave, valore)
        
def modificaPadreFiglio(nodo, selettore, chiave, valore, pos=0):
    '''cerco e cancello i vari padri che hanno i figli cercati uno consecutivo all'altro'''
    if nodo.tag == selettore[pos] and pos != len(selettore)-1: 
        pos += 1
    elif nodo.tag == selettore[pos] and pos == len(selettore)-1: 
        return (True)
    else : pos=0
    if not nodo.istext():
        for pose, el in enumerate(nodo.content):
            if modificaPadreFiglio(el, selettore, chiave, valore, pos):
                el.attr[chiave] = valore
        
def modificaAvoDiscendente(nodo, selettore, chiave, valore, pos=0):
    '''cerco e cancello i vari padri che hanno i figli cercati'''
    if nodo.tag == selettore[pos] and pos != len(selettore)-1: 
        pos += 1
    elif nodo.tag == selettore[pos] and pos == len(selettore)-1: 
        return (True)
    if not nodo.istext():
        for pose, el in enumerate(nodo.content):
            if modificaAvoDiscendente(el, selettore, chiave, valore, pos):
                el.attr[chiave] = valore
        
def trovaSelettoreM(nodo, selettore, chiave, valore):
    '''esamino il selettore dato. in base al selettore richiamo la funzione corretta'''
    sel2 = selettore.split()
    s = []
    if selettore[0] == '.' : return(modificaDaClasse(nodo, selettore[1:], chiave, valore))
    if selettore[0] == '@' : return(modificaDaAttributo(nodo, selettore[1:], chiave, valore))
    if selettore[0] == '#' : return(modificaDaID(nodo, selettore[1:], chiave, valore))
    if len(sel2) == 1 : return(modificaDaTag(nodo, selettore, chiave, valore))
    if sel2[1] == '>' : 
        for i in range(0, len(sel2), 2):
            s += [sel2[i]]
        return(modificaPadreFiglio(nodo, s, chiave, valore))
    else : return (modificaAvoDiscendente(nodo, sel2, chiave, valore))
        
        
        
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    file = fparse(fileIn)
    trovaSelettoreM(file, selettore, chiave, valore)
    f = open(fileOut, mode='w')
    f.write(file.to_string())
    f.close()
#'''-----------------------------------------------------------------------------------------------------------------------------------------------------'''
