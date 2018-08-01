from my_html import HTMLNode, fparse

def conta_nodi(fileIn,selettore):
    listafile=fparse(fileIn)
    listanodi=[listafile]
    selet=mod_sel(selettore)
    for y in range(len(selet)):
        listaconti=[]
        for z in range(len(listanodi)):
            listaconti+=conto(listanodi[z], selet[y][0])
        if len(selet[y])>1:
            listanodi=listaconti[:]
            listaconti=[]
            for x in range(1, len(selet[y])):
                for z in range(len(listanodi)):
                    listaconti+=figli(listanodi[z].content,selet[y][x])
        listanodi=listaconti[:] 
    return len(listanodi)
                                        
def elimina(listafile,i):
    if not listafile.istext():
        if i in listafile.content:
            del listafile.content[listafile.content.index(i)]
            return
        else:
            for x in listafile.content:
                elimina(x,i)
    return


def elimina_nodi(fileIn, selettore, fileOut):
    listafile=fparse(fileIn)
    listanodi=[listafile]
    
    selet=mod_sel(selettore)
    for y in range(len(selet)):
        listaconti=[]
        for z in range(len(listanodi)):
            listaconti+=conto(listanodi[z], selet[y][0])
        if len(selet[y])>1:
            listanodi=listaconti[:]
            listaconti=[]
            for x in range(1, len(selet[y])):
                for z in range(len(listanodi)):
                    listaconti+=figli(listanodi[z].content,selet[y][x])
        listanodi=listaconti[:]
    for i in listanodi:
        elimina(listafile,i)
    with open (fileOut,'w',encoding='utf_8') as t:
        t.write(listafile.to_string())

def cambia_attributo(fileIn,selettore,chiave,valore,fileOut):        
    listafile=fparse(fileIn)
    listanodi=[listafile]
    selet=mod_sel(selettore)
    for y in range(len(selet)):
        listaconti=[]
        for z in range(len(listanodi)):
            listaconti+=conto(listanodi[z], selet[y][0])
        if len(selet[y])>1:
            listanodi=listaconti[:]
            listaconti=[]
            for x in range(1, len(selet[y])):
                for z in range(len(listanodi)):
                    listaconti+=figli(listanodi[z].content,selet[y][x])
        listanodi=listaconti[:]
    for i in listanodi:
        cambia(i,chiave,valore)
    with open (fileOut,'w',encoding='utf_8') as t:
        t.write(listafile.to_string())   
                        

def sel_tr(selettore):
    n=selettore[0]
    if n == '#':
        return 'id', selettore[1:]
    elif n == '.':
        return 'class', selettore[1:]
    elif n=='@':
        selettore=selettore[2:len(selettore)-1].replace('\"','').split('=')
        return selettore[0],selettore[1]
    else:
        return 'tag',selettore
    		
def mod_sel(selettore):
    sel=[]
    while True:
        n=selettore.find(" ")
        if n!=-1:
            if '>' not in [selettore[n-1],selettore[n+1]]:
                sel.append(selettore[:n])
                selettore=selettore[n+1:]
            else:
                selettore=selettore.replace(" ","",1)
        else:
            break
    sel.append(selettore)
    for i in range(len(sel)):
        sel[i]=sel[i].split('>')
    for y in range(len(sel)):
        for x in range(len(sel[y])):
            sel[y][x]=sel_tr(sel[y][x])
    return sel
						


def conto(nodo,selettore):
    listaprov=[]
    if not nodo.istext():
        if selettore[0] == 'tag' and selettore[1] == nodo.tag:
            return[nodo]
        elif selettore[0] in list(nodo.attr.keys()) and selettore[1] in nodo.attr[selettore[0]]:
            return [nodo]
        for i in nodo.content:
            listaprov+=conto(i,selettore)
    return listaprov

def figli(listanodi,selettore):
    listaprov=[]
    for y in listanodi:
        if not y.istext():
            if selettore[0]=='tag' and selettore[1]== y.tag:
                listaprov+=[y]
            elif selettore[0] in list(y.attr.keys()) and selettore[1] in y.attr[selettore[0]]: 
                listaprov+=[y]
    return listaprov                                                  	

def cambia(i,chiave,valore):
    if not i.istext():
        i.attr[chiave]=valore
    return i