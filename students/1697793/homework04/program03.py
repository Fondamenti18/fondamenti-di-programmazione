'''
Un documento HTML può essere rappresentato sotto forma di albero, come visto a lezione, che si chiama DOM (Document Object Model).

Un qualsiasi nodo di questo albero può essere individuato sulla base delle proprie caratteristiche:
    - tag                       un tag del tipo indicato
    - .classe                   una delle parole presenti nel valore dell'attributo "class"
    - #id                       il valore dell'attributo "id"
    - @[attributo="valore"]     valore di un attributo generico
ed in base alla sua relazione con i tag che lo contengono:
    - avo discendente           il tag 'avo' contiene un tag 'discendente' a qualsiasi profondità
    - padre > figlio            il tag 'padre' contiene il tag 'figlio' nel livello immediatamente sotto

Un selettore CSS è una successione di selettori di tag separati da spazio che serve ad individuare uno o più nodi all'interno del DOM.
Esempio:
    div .class1 > #main_window
        seleziona un qualsiasi tag che ha                                       id="main_window"
        è il figlio di un tag che ha                                            class="... class1 ..."
        e si trova all'interno (a qualsiasi livello di distanza) di un tag      div
Esempio2:
    p  table > tr > td > a
    seleziona un link (<a ...> </a>)
    figlio di una casella (<td> ... </td>)
    figlia di una riga (<tr> ... </tr>)
    figlia di una tabella (<table> ... </table>)
    contenuta a qualsiasi livello in un paragrafo (<p> .... </p>)

NOTA: questa definizione del CSS è una versione ridottissima che non segue lo standard completo. 
In particolare, non è possibile usare più relazioni '>' consecutive o costruire selettori alternativi (in OR) e selettori in AND.

Le modifiche da attuare su un DOM possono essere di 3 tipi:
    - conteggio dei nodi che soddisfano il selettore CSS
    - eliminazione di tutti i tag individuati da un selettore CSS
    - modifica degli attributi di tutti i tag individuati da un selettore CSS

Realizzate le funzioni che esplorano e modificano l'albero:
    conta_nodi(       fileIn, selettore)                
    elimina_nodi(       fileIn, selettore, fileOut)             
    cambia_attributo(   fileIn, selettore, chiave, valore, fileOut)

ATTENZIONE: nei test verrà utilizzato un timout globale di 1*N secondi (se il grader fa N test)
'''

from  my_html import HTMLNode, fparse 

# MANAGE_SELECTOR

def checkSelectorType (selector, currentObj):
            
    if selector[0] == '@':
        text = selector[2:len(selector)-2]
        currentObj['type'] = text.split('=')[0]
        currentObj['name'] = text.split('=')[1].split('"')[1]
    elif len(selector.split('.')) > 1:
        currentObj['type'] = 'class'
        currentObj['name'] = selector.split('.')[1]
    elif len(selector.split('#')) > 1:
        currentObj['type'] = 'id'
        currentObj['name'] = selector.split('#')[1]
    else:
        currentObj['type'] = 'tag'
        currentObj['name'] = selector

def checkSelectorRelation(i, end, selectorArr, currentObj):
                
    if i+1 <= end:
        if i+1 == end:
            currentObj['last'] = True
        else:
            currentObj['last'] = False
            if selectorArr[i+1] == '>':
                currentObj['nextRelation'] = 'son'
            else:
                currentObj['nextRelation'] = 'desc'

def genereteSelectors (selector):
    
    selectorArr = selector.split()
    
    arrObjs = []
    
    end = len(selectorArr)
    
    for i in range(end):
        
        if selectorArr[i] != '>':
        
            currentObj = { 'type': None, 'name': None, 'last': None, 'nextRelation': None, 'prevRelation': None  }

            checkSelectorType(selectorArr[i], currentObj)
                
            checkSelectorRelation(i, end, selectorArr, currentObj)
                        
            arrObjs.append(currentObj)
    
    for y in range(len(arrObjs)):
        if y > 0:
            arrObjs[y]['prevRelation'] = arrObjs[y-1].get('nextRelation')

    return arrObjs

def checkSelectorFound(selector, node):
        
    found = False
    
    if selector['type'] == 'tag':
        if node.tag == selector['name']:
            found = True
    
    elif selector['type'] == 'class':
        if node.attr.get('class', None) != None:
            if selector['name'] in node.attr.get('class').split():
                found = True
    
    elif selector['type'] == 'id':
        if selector['name'] == node.attr.get('id'):
            found = True

    else: #generic attribute
        if node.attr.get(selector['type'], None) != None:
            if node.attr.get(selector['type']) == selector['name']:
                found = True
    
    return found

# COUNT_NODES

def countSelector(node, info, index):
    
    if not node.istext():
        
        currentSelector = info['selectorArr'][index]
        found = checkSelectorFound(currentSelector, node)
                
        if info['selectorArr'][index]['last'] and found:
            info['totalNodes']+=1
        else:
            if found:
                index+=1
            if currentSelector['prevRelation'] == 'son':
                if found:
                    for i in range(len(node.content)):
                        countSelector(node.content[i], info, index)
            else:
                for i in range(len(node.content)):
                    countSelector(node.content[i], info, index)

# DELETE_NODES

def deleteNodes(node, info, index, func):
    elsToRemove = []
    for i in range(len(node.content)):
        if func(node.content[i], info, index):
            elsToRemove.append(i)

    while len(elsToRemove) > 0:
        node.content.remove(node.content[elsToRemove[-1]])
        elsToRemove.remove(elsToRemove[-1])

def deleteSelector(node, info, index):
    
    if not node.istext():
        
        currentSelector = info['selectorArr'][index]
        found = checkSelectorFound(currentSelector, node)
                
        if info['selectorArr'][index]['last'] and found:
            return True
        else:
            if found:
                index+=1
            if currentSelector['prevRelation'] == 'son':
                if found:
                    deleteNodes(node, info, index, deleteSelector)
            else:
                deleteNodes(node, info, index, deleteSelector)

# EDIT_NODES

def editSelector(node, info, index):
    
    if not node.istext():
        
        currentSelector = info['selectorArr'][index]
        found = checkSelectorFound(currentSelector, node)
                
        if info['selectorArr'][index]['last'] and found:
            node.attr[info['key']] = info['value']
        else:
            if found:
                index+=1
            if currentSelector['prevRelation'] == 'son':
                if found:
                    for i in range(len(node.content)):
                        editSelector(node.content[i], info, index)
            else:
                for i in range(len(node.content)):
                    editSelector(node.content[i], info, index)

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    htmlTree = fparse(fileIn)
    
    info = { 'selectorArr': genereteSelectors(selettore), 'totalNodes': 0 }
    
    countSelector(htmlTree, info, 0)
    
    return info['totalNodes']

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    htmlTree = fparse(fileIn)

    info = { 'selectorArr': genereteSelectors(selettore) }
    
    deleteSelector(htmlTree, info, 0)

    file = open(fileOut,'w', encoding='utf8')
    file.write(htmlTree.to_string())

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    htmlTree = fparse(fileIn)

    info = { 'selectorArr': genereteSelectors(selettore), 'key': chiave, 'value': valore }
    
    editSelector(htmlTree, info, 0)

    file = open(fileOut,'w', encoding='utf8')
    file.write(htmlTree.to_string())
