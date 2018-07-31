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

def dismountAttribute(selector):
    tokens = ["", "", 0]
    parsingStatus = 0
    for cnt in range(0,len(selector)):
        character = selector[cnt]
        if (character == "\""):
            continue
        if (character == "]"):
            tokens[2] = cnt
            return tokens
        if (character == "="):
            parsingStatus += 1
            continue
        tokens[parsingStatus] = tokens[parsingStatus] + character
        
    return (["","", 0])
                    
def charToType(c):
    nextTagType = 0
    if (c == "."):
        nextTagType = 1
    elif (c == "#"):
        nextTagType = 2
    elif (c == "@"):
        nextTagType = 3
    return nextTagType
 

def tokenize(rule):
    '''
    0=tag
    1=class .
    2=id #
    3=attribute @[attr="value"]
    '''
    selector = rule[0]
    nextTagType = 0
    string = ""
    attribute = ""
    nextRelIsStrict = False
    for cnt in range(0,len(selector)):
        character = selector[cnt]
        t = charToType(character)
        if (character == " "):
            if (len(string) == 0):
                continue
            else:
                break
        elif (t > 0):
            nextTagType = t
            if (nextTagType == 3):
                cnt += 2
                tokens = dismountAttribute(selector[cnt:])
                string = tokens[0]
                attribute = tokens[1]
                cnt += tokens[2]
                break
        elif (character == ">"):
            nextRelIsStrict = True
        else:
            string = string + character
        
    if (len(string) > 0):
        cnt += 1
        return (selector[cnt:], nextTagType, string, attribute, nextRelIsStrict)
        
    return ("",-1)
    
def nodeRespectsRule(node,rule):
    if (rule[1] == 0):
        return node.tag == rule[2]
    elif (rule[1] == 2):
        if ("id" in node.attr):
            return (node.attr["id"] == rule[2])
    elif (rule[1] == 1):
        if ("class" in node.attr):
            return (node.attr["class"].find(rule[2]) > -1)
    elif (rule[1] == 3):
        if (rule[2] in node.attr):
            return (node.attr[rule[2]] == rule[3])

    
def changeAttribute(node, rule, ruleIsMet, key, value):
    if (nodeRespectsRule(node,rule)):
        rule = tokenize(rule)
        if (rule[1] < 0):
            node.attr[key] = value
            return            
    if (not node.istext()):
        for child in node.content:
            changeAttribute(child, rule, ruleIsMet, key, value)
                

def eraseNode(node, rule, selector):
    if (nodeRespectsRule(node,rule)):
        rule = tokenize(rule)
        if (rule[1] < 0):
            return True
    if (not node.istext()):
        for child in node.content:
            if (eraseNode(child, rule, selector)):
                node.content.remove(child)
    return False


def countNodes(node, rule, selector):
    count = 0
    if (nodeRespectsRule(node, rule)):
        rule = tokenize(rule)
        if (rule[1] < 0):
            count += 1
            rule = tokenize((selector,-1))
    elif (rule[4] == True):
        return 0
    if (not node.istext()):
        for child in node.content:
            count += countNodes(child, rule, selector)
    return count

def conta_nodi(fileIn, selettore):
    root = fparse(fileIn)
    firstRule = tokenize((selettore,-1))
    return countNodes(root, firstRule, selettore)

    

def elimina_nodi(fileIn, selettore, fileOut):
    root = fparse(fileIn)
    firstRule = tokenize((selettore,-1))
    
    if (eraseNode(root, firstRule, selettore)):
        textToPrint = ""
    else:
        textToPrint = root.to_string()
    with open(fileOut,"w") as f:
        f.write(textToPrint)
    
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    root = fparse(fileIn)
    firstRule = tokenize((selettore, -1))
    changeAttribute(root, firstRule, False, chiave, valore)
    with open(fileOut,"w",encoding="utf8") as f:
        f.write(root.to_string())
    


