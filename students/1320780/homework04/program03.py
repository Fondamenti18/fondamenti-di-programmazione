from  my_html import HTMLNode, fparse

def findByTag(tag, root):
    lsF = []
    
    if not root.istext():
        for ch in root.content:
            if ch.tag == tag:
                lsF.append(ch)
            else:
                lsF += findByTag(tag, ch)
    
    return lsF
    
def findByAttrAndVal(attr, value, root):
    lsF = []
    
    if not root.istext():
        for ch in root.content:
            if attr in ch.attr and value in ch.attr[attr]:
                lsF.append(ch)
            else:
                lsF += findByAttrAndVal(attr, value, ch)
    
    return lsF
    
def findById(id, root):
    return findByAttrAndVal('id', id[1:], root)
    
def findByClass(clazz, root):
    return findByAttrAndVal('class', clazz[1:], root)
    
def findByExpr(expr, root):
    spl1 = expr.split('[')
    spl2 = spl1[1].split('=')
    attr = spl2[0]
    value = spl2[1].split('"')[1]
    return findByAttrAndVal(attr, value, root)

def findInAllSubs(sel, root):
    lsChs = []

    if '#' in sel:
        lsChs += findById(sel, root)
    elif '.' in sel:
        lsChs += findByClass(sel, root)
    elif '@' in sel:
        lsChs += findByExpr(sel, root)
    else:
        lsChs += findByTag(sel, root)
    
    return lsChs
    
def findInDirectSubs(sel, root):
    lsChs = []
    if '#' in sel:
        if not root.istext():
            for ch in root.content:
                if 'id' in ch.attr and sel[1:] in ch.attr['id']:
                    lsChs += [ch]
    elif '.' in sel:
        if not root.istext():
            for ch in root.content:
                if 'class' in ch.attr and sel[1:] in ch.attr['class']:
                    lsChs += [ch]
    elif '@' in sel:
        spl1 = sel.split('[')
        spl2 = spl1[1].split('=')
        attr = spl2[0]
        value = spl2[1].split('"')[1]
        if not root.istext():
            for ch in root.content:
                if attr in ch.attr and value in ch.attr[attr]:
                    lsChs += [ch]
    else:
        if not root.istext():
            for ch in root.content:
                if ch.tag == sel:
                    lsChs += [ch]
    return lsChs

def findBySel(sel, root):
    splSel = sel.split()
    splSel = [None] + splSel
    selWFlag = []
    
    for i in range(1, len(splSel)):
        if splSel[i - 1] == '>':
            selWFlag.append((splSel[i], True))
        else:
            if splSel[i] != '>':
                selWFlag.append((splSel[i], False))
    
    lsFth = [root]
    
    for s in selWFlag:
        lsChs = []
        if s[1]:
            for fth in lsFth:
                lsChs += findInDirectSubs(s[0], fth)
        else:
            for fth in lsFth:
                lsChs += findInAllSubs(s[0], fth)
        lsFth = lsChs
        
    return lsFth

def conta_nodi(fileIn, selettore):
    root = fparse(fileIn)     
    return len(findBySel(selettore, root))
    
def cleanTree(root, toDelete):
    for i in range(len(root.content) - 1, -1, -1):
        if root.content[i] in toDelete:
            del root.content[i]
    for ch in root.content:
        if not ch.istext():
            cleanTree(ch, toDelete)
        
    
def elimina_nodi(fileIn, selettore, fileOut):
    root = fparse(fileIn)
    toDelete = set(findBySel(selettore, root))
    cleanTree(root, toDelete)
    with open(fileOut, 'w', encoding='utf8') as fo:
        fo.write(root.to_string())
    
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    root = fparse(fileIn)     
    toModify = findBySel(selettore, root)
    for tag in toModify:
        tag.attr[chiave] = valore
    with open(fileOut, 'w', encoding='utf8') as fo:
        fo.write(root.to_string())