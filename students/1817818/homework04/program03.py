from  my_html import HTMLNode, fparse   
def albero(a):
    if  type(a.content) is not str:
        for e in a.content:
            albero(e)
def conta_nodi(fileIn, selettore):
    f = fparse(fileIn)
    topo,gatto = selCSS(selettore)
    num = [0]
    numNodi(f,topo,gatto,num)
    return num[0]
def selCSS(sel):
    match = None
    if '.' in sel:
        return 1, sel[1:]
    elif '#' in sel:
        return 2,['id','=', sel[1:]]
    elif '@' in sel:
        match = [sel[2:sel.find('=')], '=',
               sel[sel.find('=') + 2:sel.rfind('"')]]
        return 3,match
    elif '>' in sel:
        match = []
        char = 0
        while char<len(sel):
            if sel[char] != ' ':
                i = char
                s = sel[i]
                while i+1 < len(sel) and sel[i + 1] != ' ':
                    s+=sel[i + 1]
                    i+=1
                match.append(s)
                char = i
            char+=1
        return 4,match
    elif ' ' in sel:
        match = []
        for char in sel:
            if char != ' ':
                match.append(char)
                match.append('')
        return 5,match
    else:
        return 6, sel
def elimina_nodi(fileIn, selettore, fileOut):
    f = fparse(fileIn)
    albero(f)
    return 0
def controllo(stringa, thtml, antenato):
    c = None
    i = 0
    l = []
    tS = stringa
    while i < len(tS):
        if tS[i] == '<':
            tS = tS[i:]
            l.append(tS[0:tS.find('>')+1])
            i = tS.find('>')+1
        i+=1
    ap = []
    for e in l[1:]:
        if '<'+thtml[2] in e:
            if antenato:
                c = True if len(ap)!=0 else False
            else:
                c = True if len(ap) == 0 else False
            break
        elif '/' not in e:
            ap.append([e[0:e.find('>') if ' ' not in e else e.find(' ')],True])
    return c
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    f = fparse(fileIn)
    albero(f)
    return 0
def numNodi(albero, cond, par, num):
    if type(par) == list:
        if ('=' in par and par[0] in albero.attr.keys()
           and albero.attr[par[0]] == par[2]):
            num[0]+=1
        elif ((cond == 4 or cond == 5) and albero.tag == par[0]
              and '<' + par[2] in albero.to_string()):
            diz = {5:True,4:False}
            s = albero.to_string()
            if controllo(s, par, diz[cond]):
                num[0]+=1
    elif cond == 6 and albero.tag == par:
        num[0]+=1
    elif cond == 1 and par in albero.attr.keys():
        num[0]+=1
    if  type(albero.content) is not str:
        for e in albero.content:
            numNodi(e, cond, par, num)