import json

def cleanText(fi):
    fText = ''.join(line[:-1] for line in fi) 
    fText = fText.replace(' ','')
    return fText

def getTree(fText):
    bTree = {}
    comps = fText.split('comp')[1:]
    for comp in comps:
        sComp = comp.split('sub')
        sFath = sComp[0]
        sSub = sComp[1:]
        bTree[sFath] = sSub
    return bTree

def fillTreeRec(tree, inKeys):
    
    for key in inKeys:
        child = tree[key]
        while child != []:
            tree[key] = tree[child[0]] + tree[key]
            child = tree[child[0]]       
    
def pianifica(fcompiti,insi,fout):
    with open(fcompiti, encoding="utf-8") as fi:
        fText = cleanText(fi)
    
    tree = getTree(fText)
    exIds = insi & set(tree.keys())
    
    fillTreeRec(tree, exIds)
    
    compToSave = {}
    
    for cId in exIds:
        compToSave[cId] = tree[cId]
        
    with open(fout, 'w', encoding="utf-8") as fo:
        json.dump(compToSave, fo)