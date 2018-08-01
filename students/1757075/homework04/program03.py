

from  my_html import HTMLNode, fparse

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    alb = fparse(fileIn)                # leggo file
    sel = operazioni(selettore)         # lavoro su selettore
    # lavoro su tutti i nodi
    for nodo in alb.content:
        if not nodo.istext():
            num = conta_nodi2(nodo,sel,0,0)
    return num
            
def conta_nodi2(alb,sel,i,num):
    ''' alb(nodo attuale), sel(lista selettori da soddisfare), i(indice operazione
        selettore), num(contatore per risultato). Vedo se condizioni selettore
        sono soddisfatte in caso incremento contatore '''
    for nodo in alb.content:
        if type(nodo) != str and not nodo.istext():
            num = conta_nodi2(nodo,sel,i,num)     # ricorsione
    flag = False
    if type(sel[i]) == str:
        if alb.tag == sel[i]:       # confronto tag
            if len(sel) == i+1:     # se sono arrivato alla fine dei selettori
                return num+1
            flag = True
    elif sel[i][0] == '@':        # attributo generico
        # se albero ha attributo con valore richiesto
        if alb.attr.get(sel[i][1]) == sel[i][2]:
            print(2222)
            if len(sel) == i+1:     # se sono arrivato alla fine dei selettori
                return num+1
            flag = True
    elif sel[i][0] == '.':      # parola contenuta in attributo class
        if alb.attr.get('class') != None:   # nodo ha attr class
            if alb.attr.get('class').count(sel[i][1]) > 0:  # verifico se parola contenuta
                if len(sel) == i+1:     # se sono arrivato alla fine dei selettori
                    return num+1
                flag = True
    elif sel[i][0] == '#':      # attributo id
        if alb.attr.get('id') == sel[i][1]:
            if len(sel) == i+1:     # se sono arrivato alla fine dei selettori
                return num+1
            flag = True
    if flag == False:   # se non ho passato test
        return num
    # se ho passato test ma non ho finito selettori
    if sel[i+1] == '>':         # se cerco figlio
        for nodo in alb.content:
            num = conta_nodi3(nodo,sel,i+2,num)
    else:                       # cerco antenati
        for nodo in alb.content:
            num = conta_nodi2(nodo,sel,i+1,num)
    return num

def conta_nodi3(alb,sel,i,num):
    ''' funzione per padre figlio '''
    flag = False
    if type(sel[i]) == str:
        if alb.tag == sel[i]:       # confronto tag
            if len(sel) == i+1:     # se sono arrivato alla fine dei selettori
                return num+1
            flag = True
    
    elif sel[i][0] == '@':        # attributo generico
        # se albero ha attributo con valore richiesto
        if alb.attr.get(sel[i][1]) == sel[i][2]:
            if len(sel) == i+1:     # se sono arrivato alla fine dei selettori
                return num+1
            flag = True
    elif sel[i][0] == '.':      # parola contenuta in attributo class
        if alb.attr.get('class') != None:   # nodo ha attr class
            if alb.attr.get('class').count(sel[i][1]) > 0:  # verifico se parola contenuta
                if len(sel) == i+1:     # se sono arrivato alla fine dei selettori
                    return num+1
                flag = True
    elif sel[i][0] == '#':      # attributo id
        if alb.attr.get('id') == sel[i][1]:
            if len(sel) == i+1:     # se sono arrivato alla fine dei selettori
                return num+1
            flag = True
    if flag == False:   # se non ho passato test
        return num
    # se ho passato test ma non ho finito selettori
    if sel[i+1] == '>':         # se cerco figlio
        for nodo in alb.content:
            num = conta_nodi3(nodo,sel,i+2,num)
    else:                       # cerco antenati
        for nodo in alb.content:
            num = conta_nodi2(nodo,sel,i+1,num)
    return num
    
def operazioni(s):
    ''' metodo che divide tutte le operazioni del selettore e restituisce una
        lista con le operazioni '''
    s2 = []
    for i in s.split():
        if i.count('@') > 0:
            i = i.replace('@','')
            i = i.replace('[','')
            i = i.replace(']','')
            i = i.replace('"','')
            i = i.split('=')
            s2.append(('@',i[0],i[1]))
        elif i.count('.') > 0:
            i = i.replace('.','')
            s2.append(('.',i))
        elif i.count('#') > 0:
            i = i.replace('#','')
            s2.append(('#',i))
        elif i.count('>') > 0:
            s2.append('>')
        else: s2.append(i)
    return s2
        

def elimina_nodi(fileIn, selettore, fileOut):
    ''' Elimina dall'albero tutti i nodi che soddisfano il selettore CSS 
        (compreso il loro contenuto)'''
    alb = fparse(fileIn)                # leggo file
    sel = operazioni(selettore)         # lavoro su selettore
    ls = []
    # lavoro su tutti i nodi
    for nodo in alb.content:
        if not nodo.istext():
            elimina_nodi2(alb,sel,0,ls)
    for n in ls:
        for nodo in alb.content:
            if not nodo.istext():
                elimina(nodo,n)
    s = alb.to_string()
    with open(fileOut,'w') as f:
        f.write(s)
                
def elimina(alb,n):
    for nodo in alb.content:
        if type(nodo) != str and not nodo.istext():
            if nodo == n:
                alb.content.remove(n)
                return None
            elimina(nodo,n)
            
def elimina_nodi2(alb,sel,i,ls):
    ''' alb(nodo attuale), sel(selettore), i(indice per selettore),ls(lista nodi
        da eliminare) cerco nodo che soddisfa requisiti selettore e lo inserisco
        nella lista ls '''
    for nodo in alb.content:
        if type(nodo) != str and not nodo.istext(): # se nodo non e' stringa e testo
            elimina_nodi2(nodo,sel,i,ls)     # ricorsione
    
    flag = False
    if type(sel[i]) == str:
        if alb.tag == sel[i]:       # confronto tag
            if len(sel) == i+1:     # se tutti requisiti sono soddisfatti
                ls.append(alb)
                return None
            flag = True
    elif sel[i][0] == '@':          # attributo generico
        if alb.attr.get(sel[i][1]) == sel[i][2]: # se alb ha attr richiesto
            if len(sel) == i+1:     # selettore completato
                ls.append(alb)
                return None
            flag = True
    elif sel[i][0] == '.':          # parola in attributo class
        if alb.attr.get('class') != None: # nodo ha attr class
            if alb.attr.get('class').count(sel[i][1]) > 0: # parola effettivamente contenuta
                if len(sel) == i+1: # fine selettore
                    ls.append(alb)
                    return None
                flag = True
    elif sel[i][0] == '#':          # attributo id
        if alb.attr.get('id') == sel[i][1]: # id giusto
            if len(sel) == i+1:     # fine selettore
                ls.append(alb)
                return None
            flag = True
    if flag == False:               # non ho passato nessuno test
        return None
    # se passo test ma non ho finito controllo su selettori
    if sel[i+1] == '>':             # cerco figlio
        for nodo in alb.content:
            elimina_nodi3(nodo,sel,i+2,ls)
    else:                           # cerco antenati
        for nodo in alb.content:
            elimina_nodi2(nodo,sel,i+1,ls)
            
def elimina_nodi3(alb,sel,i,ls):
    ''' metodo creato per caso figlio '''
    flag = False
    if type(sel[i]) == str:
        if alb.tag == sel[i]:       # confronto tag
            if len(sel) == i+1:     # se tutti requisiti sono soddisfatti
                ls.append(alb)
                return None
            flag = True
    elif sel[i][0] == '@':          # attributo generico
        if alb.attr.get(sel[i][1]) == sel[i][2]: # se alb ha attr richiesto
            if len(sel) == i+1:     # selettore completato
                ls.append(alb)
                return None
            flag = True
    elif sel[i][0] == '.':          # parola in attributo class
        if alb.attr.get('class') != None: # nodo ha attr class
            if alb.attr.get('class').count(sel[i][1]) > 0: # parola effettivamente contenuta
                if len(sel) == i+1: # fine selettore
                    ls.append(alb)
                    return None
                flag = True
    elif sel[i][0] == '#':          # attributo id
        if alb.attr.get('id') == sel[i][1]: # id giusto
            if len(sel) == i+1:     # fine selettore
                ls.append(alb)
                return None
            flag = True
    if flag == False:               # non ho passato nessuno test
        return None
    # se passo test ma non ho finito controllo su selettori
    if sel[i+1] == '>':             # cerco figlio
        for nodo in alb.content:
            elimina_nodi3(nodo,sel,i+2,ls)
    else:                           # cerco antenati
        for nodo in alb.content:
            elimina_nodi2(nodo,sel,i+1,ls)
            
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    alb = fparse(fileIn)                # leggo file
    sel = operazioni(selettore)         # lavoro su selettore
    ls = []
    # lavoro su tutti i nodi
    for nodo in alb.content:
        if not nodo.istext():
            elimina_nodi2(alb,sel,0,ls)
    for n in ls:
        for nodo in alb.content:
            if not nodo.istext():
                cambia(nodo,n,chiave,valore)
    s = alb.to_string()
    with open(fileOut,'w') as f:
        f.write(s)

def cambia(alb,n,chiave,valore):
    for nodo in alb.content:
        if type(nodo) != str and not nodo.istext():
            if nodo == n:
                nodo.attr[chiave]=valore
                return None
            cambia(nodo,n,chiave,valore)
