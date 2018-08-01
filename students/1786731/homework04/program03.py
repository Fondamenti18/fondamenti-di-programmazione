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
    cambia_attributo(	fileIn, selettore, chiave, valore, fileOut)

ATTENZIONE: nei test verrà utilizzato un timout globale di 1*N secondi (se il grader fa N test)
'''

from my_html import HTMLNode, fparse

def contatore(node, selectorlist):
    # this node respects given selector, since we ended every possible selector combination
    if len(selectorlist) == 0:
        return 1

    res = 0

    directchild = False
    if selectorlist[0] == ">":
        directchild = True
        selectorlist = selectorlist[1:]




    # tag selector type   e.g.   p, em, a, body
    if selectorlist[0][0].isalpha():
        for child in node.content:
            # skip text nodes
            if child.tag == '_text_':
                continue

            if child.tag == selectorlist[0]:
                result = contatore(child, selectorlist[1:])
                res += result
            elif not directchild: # if this was not a 'p' tag, let's look it's children for one
                result = contatore(child, selectorlist)
                res += result
                

    # class selector type  e.g    .class .title .whatever
    if selectorlist[0][0] == ".":
        className = selectorlist[0][1:]
        for child in node.content:
            # skip text nodes
            if child.tag == '_text_':
                continue

            childclass = "" if "class" not in child.attr else child.attr["class"]
            
            if className in childclass:
                result = contatore(child, selectorlist[1:])
                res += result
            elif not directchild: # let's look it's children for one
                result = contatore(child, selectorlist)
                res += result


    # search by id
    if selectorlist[0][0] == "#":
        selectorid = selectorlist[0][1:]
        for child in node.content:
            # skip text nodes
            if child.tag == '_text_':
                continue

            childid = "" if "id" not in child.attr else child.attr["id"]

            if childid == selectorid:
                result = contatore(child, selectorlist[1:])
                res += result
            elif not directchild: # let's look it's children for one
                result = contatore(child, selectorlist)
                res += result


    # search by attribute
    if selectorlist[0][0] == '@':
        eqindex = selectorlist[0].find('=')
        attrib = selectorlist[0][2:eqindex]
        value  = selectorlist[0][eqindex + 2:  selectorlist[0].rfind('"')]

        for child in node.content:
            # skip text nodes
            if child.tag == '_text_':
                continue

            childattribvalue = "" if attrib not in child.attr else child.attr[attrib]

            if childattribvalue == value:
                result = contatore(child, selectorlist[1:])
                res += result
            elif not directchild: # let's look it's children for one
                result = contatore(child, selectorlist)
                res += result

    return res



def delete_nodes(node, selectorlist):
    if len(selectorlist) == 0:
        return None

    newchildren = []

    directchild = False
    if selectorlist[0] == ">":
        directchild = True
        selectorlist = selectorlist[1:]


    # tag selector type   e.g.   p, em, a, body
    if selectorlist[0][0].isalpha():
        for child in node.content:
            # skip text nodes
            if child.tag == '_text_':
                newchildren.append(child)
                continue

            if child.tag == selectorlist[0]:
                result = delete_nodes(child, selectorlist[1:])
                if result != None:
                    newchildren.append(result)
            elif not directchild: # if this was not a 'p' tag, let's look it's children for one
                result = delete_nodes(child, selectorlist)
                if result != None:
                    newchildren.append(result)
            else:
                # append those children
                newchildren.append(child)

    # class selector type  e.g    .class .title .whatever
    if selectorlist[0][0] == ".":
        className = selectorlist[0][1:]
        for child in node.content:
            # skip text nodes
            if child.tag == '_text_':
                newchildren.append(child)
                continue

            childclass = "" if "class" not in child.attr else child.attr["class"]
            
            if className in childclass:
                result = delete_nodes(child, selectorlist[1:])
                if result != None:
                    newchildren.append(result)
            elif not directchild: # let's look it's children for one
                result = delete_nodes(child, selectorlist)
                if result != None:
                    newchildren.append(result)
            else:
                # append those children
                newchildren.append(child)

    # search by id
    if selectorlist[0][0] == "#":
        selectorid = selectorlist[0][1:]
        for child in node.content:
            # skip text nodes
            if child.tag == '_text_':
                newchildren.append(child)
                continue

            childid = "" if "id" not in child.attr else child.attr["id"]

            if childid == selectorid:
                result = delete_nodes(child, selectorlist[1:])
                if result != None:
                    newchildren.append(result)
            elif not directchild: # let's look it's children for one
                result = delete_nodes(child, selectorlist)
                if result != None:
                    newchildren.append(result)
            else:
                # append those children
                newchildren.append(child)

    # search by attribute
    if selectorlist[0][0] == '@':
        eqindex = selectorlist[0].find('=')
        attrib = selectorlist[0][2:eqindex]
        value  = selectorlist[0][eqindex + 2:  selectorlist[0].rfind('"')]

        for child in node.content:
            # skip text nodes
            if child.tag == '_text_':
                newchildren.append(child)
                continue

            childattribvalue = "" if attrib not in child.attr else child.attr[attrib]

            if childattribvalue == value:
                result = delete_nodes(child, selectorlist[1:])
                if result != None:
                    newchildren.append(result)
            elif not directchild: # let's look it's children for one
                result = delete_nodes(child, selectorlist)
                if result != None:
                    newchildren.append(result)
            else:
                # append those children
                newchildren.append(child)

    node.content = newchildren

    return node




def change_attrib(node, selectorlist, key, value):
    
    if len(selectorlist) == 0:
        node.attr[key] = value
        return


    directchild = False
    if selectorlist[0] == ">":
        directchild = True
        selectorlist = selectorlist[1:]


    # tag selector type   e.g.   p, em, a, body
    if selectorlist[0][0].isalpha():
        for child in node.content:
            # skip text nodes
            if child.tag == '_text_':
                continue

            if child.tag == selectorlist[0]:
                change_attrib(child, selectorlist[1:], key, value)
            elif not directchild: # if this was not a 'p' tag, let's look it's children for one
                change_attrib(child, selectorlist, key, value)
                

    # class selector type  e.g    .class .title .whatever
    if selectorlist[0][0] == ".":
        className = selectorlist[0][1:]
        for child in node.content:
            # skip text nodes
            if child.tag == '_text_':
                continue

            childclass = "" if "class" not in child.attr else child.attr["class"]
            
            if className in childclass:
                change_attrib(child, selectorlist[1:], key, value)
            elif not directchild: # let's look it's children for one
                change_attrib(child, selectorlist, key, value)
                


    # search by id
    if selectorlist[0][0] == "#":
        selectorid = selectorlist[0][1:]
        for child in node.content:
            # skip text nodes
            if child.tag == '_text_':
                continue

            childid = "" if "id" not in child.attr else child.attr["id"]

            if childid == selectorid:
                change_attrib(child, selectorlist[1:], key, value)
            elif not directchild: # let's look it's children for one
                change_attrib(child, selectorlist, key, value)


    # search by attribute
    if selectorlist[0][0] == '@':
        eqindex = selectorlist[0].find('=')
        attrib = selectorlist[0][2:eqindex]
        value  = selectorlist[0][eqindex + 2:  selectorlist[0].rfind('"')]

        for child in node.content:
            # skip text nodes
            if child.tag == '_text_':
                continue

            childattribvalue = "" if attrib not in child.attr else child.attr[attrib]

            if childattribvalue == value:
                change_attrib(child, selectorlist[1:], key, value)
            elif not directchild: # let's look it's children for one
                change_attrib(child, selectorlist, key, value)

    return






def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    root = fparse(fileIn)
    

    # suddividiamo il selettore per tipo
    selectorlist = selettore.split()
    count = contatore(root, selectorlist)

    return count



def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    root = fparse(fileIn)
    selectorlist = selettore.split()
    
    newroot = delete_nodes(root, selectorlist)

    file = open(fileOut, "w", encoding='utf8')
    file.write(newroot.to_string())
    file.close() 

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    root = fparse(fileIn)
    selectorlist = selettore.split()

    change_attrib(root, selectorlist, chiave, valore)

    # strs = root.to_string()

    file = open(fileOut, "w", encoding='utf8')
    file.write(root.to_string())
    file.close()


# cambia_attributo("python.org.html", "p a", "style", "background-color:red", "test11.html")
# fileIn    = 'slashdot.html'
# fileOut   = 'test12.html'
# selettore = '@[class="container"] > .main-wrap #firehose > .row strong'
# elimina_nodi(fileIn, selettore, fileOut)