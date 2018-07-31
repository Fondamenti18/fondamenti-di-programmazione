'''
Un documento HTML puo' essere rappresentato sotto forma di albero, come visto a lezione, che si chiama DOM (Document Object Model).

Un qualsiasi nodo di questo albero puo' essere individuato sulla base delle proprie caratteristiche:
    - tag                       un tag del tipo indicato
    - .classe                   una delle parole presenti nel valore dell'attributo "class"
    - #id                       il valore dell'attributo "id"
    - @[attributo="valore"]     valore di un attributo generico
ed in base alla sua relazione con i tag che lo contengono:
    - avo discendente           il tag 'avo' contiene un tag 'discendente' a qualsiasi profondita'
    - padre > figlio            il tag 'padre' contiene il tag 'figlio' nel livello immediatamente sotto

Un selettore CSS e' una successione di selettori di tag separati da spazio che serve ad individuare uno o piu' nodi all'interno del DOM.
Esempio:
    div .class1 > #main_window
        seleziona un qualsiasi tag che ha                                       id="main_window"
        e' il figlio di un tag che ha                                            class="... class1 ..."
        e si trova all'interno (a qualsiasi livello di distanza) di un tag      div
Esempio2:
    p  table > tr > td > a
	seleziona un link (<a ...> </a>)
	figlio di una casella (<td> ... </td>)
	figlia di una riga (<tr> ... </tr>)
	figlia di una tabella (<table> ... </table>)
	contenuta a qualsiasi livello in un paragrafo (<p> .... </p>)

NOTA: questa definizione del CSS e' una versione ridottissima che non segue lo standard completo. 
In particolare, non e' possibile usare piu' relazioni '>' consecutive o costruire selettori alternativi (in OR) e selettori in AND.

Le modifiche da attuare su un DOM possono essere di 3 tipi:
    - conteggio dei nodi che soddisfano il selettore CSS
    - eliminazione di tutti i tag individuati da un selettore CSS
    - modifica degli attributi di tutti i tag individuati da un selettore CSS

Realizzate le funzioni che esplorano e modificano l'albero:
    conta_nodi(       fileIn, selettore)				
    elimina_nodi(       fileIn, selettore, fileOut)				
    cambia_attributo(	fileIn, selettore, chiave, valore, fileOut)

ATTENZIONE: nei test verra' utilizzato un timout globale di 1*N secondi (se il grader fa N test)
'''

from  my_html import HTMLNode, fparse

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    page = fparse(fileIn)
    splittedSelector = selettore.replace(' >', '').split(' ')
    #print(splittedSelector)
    if len(splittedSelector) <= 2:
        numeroTag = 0
        key, value = selector(selettore)
        #print('chiave:' + str(key))
        numeroTag = contaTag(page, cleanSelector(selettore,key), key, value, numeroTag)
        #print(numeroTag)
        return numeroTag
    else:
        listaStep = []
        splittedSelector = selettore.split(' ')
        findStep(splittedSelector, 0, listaStep)
        #print(listaStep)
        
        listaNode = page.content
        for step in range(0, len(listaStep)):
            newListaNode = []
            #print('step:' + str(listaStep[step]) + ' listanode:' + str(len(listaNode)))
            for nodo in listaNode:
                #print('entro con:' + str(len(listaNode)) + ' step:' + str(listaStep[step])) 
                if not nodo.istext():
                    #print('entro not text')
                    if listaStep[step] == '>':
                        newListaNode = listaNode
                        break
                    elif step+1 < len(listaStep) and listaStep[step+1] == '>':
                        tipoSelettore = listaStep[step]
                        key, value = selector(splittedSelector[step])
                        #print('qui' + str(splittedSelector[step]))
                        #print('key:' + str(key) + ' value:' + str(value))
                        if(key == 'id'):
                            tipoSelettore = 'id'
                        elif key == 'class':
                            tipoSelettore = 'class'
                        findNodes(nodo, key, value, tipoSelettore, False, newListaNode, False)
                    else:
                        tipoSelettore = listaStep[step]
                        key, value = selector(splittedSelector[step])
                        #print('key:' + str(key) + ' value:' + str(value))
                        if(key == 'id'):
                            tipoSelettore = 'id'
                        elif key == 'class':
                            tipoSelettore = 'class'
                        findNodes(nodo, key, value, tipoSelettore, True, newListaNode, False)
                    #print(len(newListaNode))
            listaNode = newListaNode
    
        return len(listaNode)
    
def contaTag(root, selettore, key, value, nTag):
    if key == 'tag':
        nTag = numeroTag(root, selettore, key, value, nTag)
        return nTag
    if key == 'child':
            
        selectorSplitted = value.split(' ')
        return numeroChild(root, selettore, selectorSplitted[0], selectorSplitted[2], nTag)
    if key == 'discendente':
        selectorSplitted = value.split(' ')
        return numeroDiscendenti(root, selectorSplitted[0], selectorSplitted[1], nTag)
    else:
        return numeroSelettori(root, selettore, key, value, nTag)


def numeroTag(root, selettore, key, value, ntag):
    #print('entro')
    for nodo in root.content:
        if not nodo.istext():
            if(nodo.tag == selettore):
                ntag += 1
            if len(nodo.content) > 0:
                ntag = contaTag(nodo, selettore, key, value, ntag)
    return ntag

def numeroSelettori(root, selettore, key, value, numeroTag):
    for nodo in root.content:
        if not nodo.istext():
            #print('kkk' + str(nodo.attr))
            if len(nodo.attr) > 0 and key in nodo.attr:
                if value != '' and nodo.attr[key] == value:
                     numeroTag += 1
                elif nodo.attr[key].find(selettore) != -1:
                    numeroTag += 1
            if len(nodo.content) > 0:
                numeroTag = numeroSelettori(nodo, selettore, key, value, numeroTag)
    return numeroTag

def numeroChild(root, selettore, padre, figlio, numeroTag):
    for nodo in root.content:
        #print('searching father...')
        if not nodo.istext():
            if nodo.tag == padre:
                #print('searching child...')
                for child in nodo.content:
                    if child.open_tag():
                        if not child.istext():
                            if child.tag == figlio:
                                numeroTag += 1
            if len(nodo.content) > 0:
                    numeroTag = numeroChild(nodo, selettore, padre, figlio, numeroTag)
    return numeroTag

def numeroDiscendenti(root, padre, figlio, numeroTag):
    for nodo in root.content:
        #print('searching father...')
        if not nodo.istext():
            if nodo.tag == padre:
                #print('searching child...')
                numeroTag = findDiscendente(nodo, figlio, numeroTag)
            if len(nodo.content) > 0:
                    numeroTag = numeroDiscendenti(nodo, padre, figlio, numeroTag)
    return numeroTag

def findDiscendente(root, figlio, numeroTag):
    for nodo in root.content:
        if not nodo.istext():
            if nodo.tag == figlio:
                numeroTag += 1
            numeroTag = findDiscendente(nodo, figlio, numeroTag)
    return numeroTag
    
                        
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    page = fparse(fileIn)
    listaStep = []
    splittedSelector = selettore.split(' ')
    findStep(splittedSelector, 0, listaStep)
    #print(listaStep)
    listaNode = page.content
    for step in range(0, len(listaStep)):
        if step+1 >= len(listaStep):
            delete = True
        else:
            delete = False
        newListaNode = []
        #print('step:' + str(listaStep[step]) + ' listanode:' + str(len(listaNode)))
        for nodo in listaNode:
            #print('entro con:' + str(len(listaNode)) + ' step:' + str(listaStep[step])) 
            if not nodo.istext():
                #print('entro not text')
                if listaStep[step] == '>':
                    newListaNode = listaNode
                    break
                elif step+1 < len(listaStep) and listaStep[step+1] == '>':
                    tipoSelettore = listaStep[step]
                    key, value = selector(splittedSelector[step])
                    #print('qui' + str(splittedSelector[step]))
                    #print('key:' + str(key) + ' value:' + str(value))
                    if(key == 'id'):
                        tipoSelettore = 'id'
                    elif key == 'class':
                        tipoSelettore = 'class'
                    findNodes(nodo, key, value, tipoSelettore, False, newListaNode, delete)
                else:
                    tipoSelettore = listaStep[step]
                    key, value = selector(splittedSelector[step])
                    #print('key:' + str(key) + ' value:' + str(value))
                    if(key == 'id'):
                        tipoSelettore = 'id'
                    elif key == 'class':
                        tipoSelettore = 'class'
                    findNodes(nodo, key, value, tipoSelettore, True, newListaNode, delete)
                #print(len(newListaNode))
        listaNode = newListaNode
# =============================================================================
#     key, value = selector(selettore)
#     print('selettore:' + str(selettore) + 'chiave:' + str(key))
#     eliminaTag(page, cleanSelector(selettore,key), key, value)
#     print('saving file...')
    # print(page.to_string())
    with open(fileOut,'w', encoding="utf-8") as file:
        file.write(page.to_string())
# =============================================================================

def eliminaTag(root, selettore, key, value):
    if key == 'tag':
        return numeroTag(root, selettore, key, value)
    if key == 'child':
            
        selectorSplitted = value.split(' ')
        return numeroChild(root, selettore, selectorSplitted[0], selectorSplitted[2])
    if key == 'discendente':
        selectorSplitted = value.split(' ')
        eliminaDiscendenti(root, selectorSplitted[0], selectorSplitted[1])
    else:
        eliminaSelettori(root, selettore, key, value)

def eliminaDiscendenti(root, padre, figlio):
    #print('starting eleminaDiscendenti...')
    for nodo in root.content:
        #print('searching father...')
        if not nodo.istext():
            if nodo.tag == padre:
                #print('searching child...')
                eliminaDiscendente(nodo, figlio)
            if len(nodo.content) > 0:
                    eliminaDiscendenti(nodo, padre, figlio)

def eliminaDiscendente(root, figlio):
    #print('starting elimina disc...')
    for nodo in root.content:
        if not nodo.istext():
            if nodo.tag == figlio:
                root.content.remove(nodo)
            else:
                eliminaDiscendente(nodo, figlio)

def eliminaSelettori(root, selettore, key, value):
    for nodo in root.content:
        if not nodo.istext():
            #print('kkk' + str(nodo.attr))
            if len(nodo.attr) > 0 and key in nodo.attr:
                if value != '' and nodo.attr[key] == value:
                     root.content.remove(nodo)
                elif nodo.attr[key].find(selettore) != -1:
                    root.content.remove(nodo)
            if len(nodo.content) > 0:
                 eliminaSelettori(nodo, selettore, key, value)

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    page = fparse(fileIn)
    key, value = selector(selettore)
    #print('chiave:' + str(key))
    addAttribute(page, cleanSelector(selettore,key), key, value, chiave, valore)
    #print('saving file...')
    #print(page.to_string())
    with open(fileOut, 'w', encoding="utf-8") as file:
        file.write(page.to_string())

def addAttribute(root, selettore, key, value, chiave, valore):
    if key == 'tag':
        return numeroTag(root, selettore, key, value)
    if key == 'child':
            
        selectorSplitted = value.split(' ')
        return numeroChild(root, selettore, selectorSplitted[0], selectorSplitted[2])
    if key == 'discendente':
        selectorSplitted = value.split(' ')
        addAttributeDiscendenti(root, selectorSplitted[0], selectorSplitted[1], chiave, valore)
    else:
        addAttributeSelettori(root, key, selettore, chiave, valore)

        
def addAttributeDiscendenti(root, padre, figlio, chiave, valore):
    #print('starting addDiscendenti...')
    for nodo in root.content:
        #print('searching father...')
        if not nodo.istext():
            if nodo.tag == padre:
                #print('searching child...')
                addAttributeDiscendente(nodo, figlio, chiave, valore)
            if len(nodo.content) > 0:
                    addAttributeDiscendenti(nodo, padre, figlio, chiave, valore)

def addAttributeDiscendente(root, figlio, chiave, valore):
    #print('starting add disc...')
    for nodo in root.content:
        if not nodo.istext():
            if nodo.tag == figlio:
                nodo.attr[chiave] = valore
           
            addAttributeDiscendente(nodo, figlio, chiave, valore)

def addAttributeSelettori(root, key, selettore, chiave, valore):
    #print('key:' + str(key) + ' value:' + str(value))
    for nodo in root.content:
            if not nodo.istext():
                #print('kkk' + str(nodo.attr))
                if len(nodo.attr) > 0 and key in nodo.attr and nodo.attr[key] == selettore:
                    #print('modifico')
                    nodo.attr[chiave] = valore
                if len(nodo.content) > 0:
                     addAttributeSelettori(nodo, key, selettore, chiave, valore)

def selector(selettore):
    if selettore.find('#') != -1:
        return 'id', selettore.replace('#','')
    elif selettore.find('.') != -1:
        return 'class', selettore.replace('.','')
    elif selettore.find('@') != -1:
        if 'class=' in selettore:
            value = selettore[selettore.index('=')+2:-2]
            return 'class', value
        elif 'id=' in selettore:
            value = selettore[selettore.index('=')+2:-2]
            return 'id', value
        else:
            start = selettore.index('[')+1
            end = selettore.index('=')-2
            key = selettore[start:]
            key = key[:end]
            valore = selettore[selettore.index('=')+2:]
            valore = valore[:-2]
            return key, valore
    elif '>' in selettore:
        return 'child', selettore
    elif ' ' in selettore:
        return 'discendente', selettore
    else:
        return 'tag', selettore


def findNodes(root, selettore, valore, tipoSelettore, discendenti, listaNodi, delete):
    #print(tipoSelettore)
    for node in root.content:
        if not node.istext():
            if tipoSelettore == 'tag':
                if node.tag == valore:
                    #print('entro')
                    if delete:
                        root.content.remove(node)
                    else:
                        listaNodi.append(node)
                    if discendenti:
                        findNodes(node, selettore, valore, tipoSelettore, discendenti, listaNodi, delete)
            elif tipoSelettore == 'class':
                #print('entro in class')
                #print(node.attr)
                if 'class' in node.attr and node.attr['class'].find(valore) != -1:
                    #print('entro2')
                    if delete:
                        root.content.remove(node)
                    else:
                        listaNodi.append(node)
                    if discendenti:
                        findNodes(node, selettore, valore, tipoSelettore, discendenti, listaNodi, delete)
            elif tipoSelettore == 'id':
                if 'id' in node.attr and node.attr['id'] == valore:
                    #print('entro3')
                    if delete:
                        root.content.remove(node)
                    else:
                        listaNodi.append(node)
                    if discendenti:
                        findNodes(node, selettore, valore, tipoSelettore, discendenti, listaNodi, delete)
            elif tipoSelettore == 'attribute':
                #print('entro4')
                if listaNodi in node.attr and node.attr[selettore] == valore:
                    if delete:
                        root.content.remove(node)
                    else:
                        listaNodi.append(node)
                    if discendenti:
                        findNodes(node, selettore, valore, tipoSelettore, discendenti, listaNodi, delete)
                        
            findNodes(node, selettore, valore, tipoSelettore, discendenti, listaNodi, delete)

def findStep(splittedSelector, elemNum, listaStep):
    selettore = splittedSelector[elemNum]
    if selettore.find('#') != -1:
        listaStep.append('id')
    elif selettore.find('.') != -1:
        listaStep.append('class')
    elif selettore.find('@') != -1:
        listaStep.append('@')
    elif '>' in selettore:
        listaStep.append('>')
    elif ' ' in selettore:
        listaStep.append('discendente')
    else:
        listaStep.append('tag')
        
    elemNum += 1
    if len(splittedSelector) > elemNum:
        findStep(splittedSelector, elemNum, listaStep)
    else:
        return listaStep

def cleanSelector(selettore, key):
    if key == 'id':
        selettore = selettore.replace('#', '')
    elif key == 'class':
        selettore = selettore.replace('.', '')
    return selettore

# =============================================================================
# page = fparse('page1-3.html')
# page.print_tree()
# for cont in page.content:
#     print(cont.tag)
#     print('')
#     print('tag:' + str(cont.attr))
#     for cont2 in cont.content:
#         print('cont2:' + str(cont2))
#         if(cont.istext()):
#             print('testo')
#         else:
#             print('tag:' + str(cont2.attr))
#     
# =============================================================================
