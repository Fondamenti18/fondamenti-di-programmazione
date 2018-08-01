from  my_html import HTMLNode, fparse

nnode={}
mem={}

def conta_nodi(fileIn, selettore):
    node=fparse(fileIn)
    scan=scan_selettore(selettore)
    mem['source']='count'
    for el in scan:
        nnode[el]=[]
    res=lconta_nodi(node,scan)
    return len(res)

def lconta_nodi(node, scan):
    verify_scanned(scan,node,node)
    return nnode[scan[len(scan)-1]]

def elimina_nodi(fileIn, selettore, fileOut):
    node=fparse(fileIn)
    scan=scan_selettore(selettore)
    mem['source']='delete'
    verify_scanned(scan,node,node)
    with open(fileOut, mode='w') as f:
        f.write(node.to_string())

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    node=fparse(fileIn)
    scan=scan_selettore(selettore)
    mem['source']='modify'
    mem['modvalues']=(chiave, valore)
    verify_scanned(scan,node,node)
    with open(fileOut, mode='w') as f:
        f.write(node.to_string())

def scan_selettore(selettore):
    k=selettore.split(' ')
    while '>' in k:
        index=k.index('>')
        k[index]=k[index]+k[index+1]
        del k[index+1]
    return k

def verify_scanned(scan,node,parent):
    nxtcond=scan[0]
    if nxtcond[:1]=='>':
        son_search(scan,node,parent)
    else:
        free_search(scan,node,parent)
        
def matchfound(scan,node,parent):
    if len(scan)>1:
        verify_scanned(scan[1:],node,parent)
        
def son_search(scan,node,parent):
    mscan=scan[0][1:].split()
    tf=checktag(mscan,node)
    if tf==True:
        if len(scan)==1 and node not in nnode[scan[0]]:
            performop(scan,node,parent)
        if isinstance(node.content,str)==False:
            for el in node.content:
                matchfound(scan,el,node)
    
def free_search(scan,node,parent):
    tf=checktag(scan,node)
    if tf==True:
        if len(scan)==1:
            performop(scan,node,parent)
        for el in node.content:
            matchfound(scan,el,node)
    if isinstance(node.content, str)==False:
        for el in node.content:
            free_search(scan,el,node)

def performop(scan,node,parent):
    if mem['source']=='count' and node not in nnode[scan[0]]:
        nnode[scan[0]].append(node)
    elif mem['source']=='delete':
        dex=parent.content.index(node)
        del parent.content[dex]
    elif mem['source']=='modify':
        node.attr[mem['modvalues'][0]]=mem['modvalues'][1]
        

def checktag(scan,node):
    char=scan[0][0]
    if char=='.' and 'class' in node.attr:
        return tagdot(scan,node)
    elif char=='#' and 'id' in node.attr:
        return tagsharp(scan,node)
    elif char=='@':
        return tagat(scan,node)
    else:
        return tagreg(scan,node)
    return False
        
def tagdot(scan,node):
    if scan[0][1:] in node.attr['class']:
            return True

def tagsharp(scan,node):
    if scan[0][1:]==node.attr['id']:
            return True
        
def tagat(scan,node):
    vals=scan[0][2:len(scan[0])-1].split('=')
    if vals[0] in node.attr:
        if node.attr[vals[0]]==vals[1][1:len(vals[1])-1]:
            return True

def tagreg(scan,node):
    if scan[0]==node.tag:
            return True