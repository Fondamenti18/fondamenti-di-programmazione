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

from  my_html import HTMLNode, fparse

def check_node(node, regola):
    return (node.tag == regola) or (regola[0] == '.' and 'class' in node.attr and regola[1:] in node.attr["class"]) or (regola[0] == '#' and "id" in node.attr and node.attr["id"] == regola[1:]) or(regola[0] == '@' and regola[2:regola.index("=")] in node.attr and node.attr[regola[2:regola.index("=")]] == regola[regola.index("=")+2:-2])

def _conta_nodi(node,regole,indice_regola):
    res = []
    regola = regole[indice_regola]
    direct_child=False
    if regola == '>':
        direct_child=True
        indice_regola +=1
        regola = regole[indice_regola]

    for child in node.content:
        if child.istext():
            continue
        elif check_node(child, regola) and (not direct_child or (direct_child and check_node(node, regole[indice_regola - 2]))):
            if len(regole) - 1 == indice_regola:
                res.append(child)
            else:
                res.extend(_conta_nodi(child,regole,indice_regola+1))
        else:
            if direct_child:
                res.extend(_conta_nodi(child, regole, 0))
            else:
                res.extend(_conta_nodi(child, regole, indice_regola))

    return res

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    dom = fparse(fileIn)
    regole = selettore.split(" ")
    res = _conta_nodi(dom,regole,0)
    return len(res)

def _elimina_nodi(node,regole,indice_regola):
    res = []
    regola = regole[indice_regola]
    direct_child =False
    if regola == '>':
        direct_child=True
        indice_regola +=1
        regola = regole[indice_regola]

    for child in node.content:
        if child.istext():
            continue
        elif check_node(child, regola) and (not direct_child or (direct_child and check_node(node, regole[indice_regola - 2]))):
            if len(regole) - 1 == indice_regola:
                node.content.remove(child)
            else:
                _elimina_nodi(child, regole, indice_regola+1)
        else:
            if direct_child:
                _elimina_nodi(child, regole, 0)
            else:
                _elimina_nodi(child, regole, indice_regola)

    return res

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    dom = fparse(fileIn)
    regole = selettore.split(" ")
    _elimina_nodi(dom, regole, 0)
    with open(fileOut, "w",encoding='utf8' ) as file:
        file.write(dom.to_string())

def _cambia_attributo(node,regole,indice_regola, chiave,valore):
    res = []
    regola = regole[indice_regola]
    direct_child=False
    if regola == '>':
        direct_child=True
        indice_regola +=1
        regola = regole[indice_regola]

    for child in node.content:
        if child.istext():
            continue
        elif check_node(child, regola) and (not direct_child or (direct_child and check_node(node, regole[indice_regola - 2]))):
            if len(regole) - 1 == indice_regola:
                child.attr[chiave] = valore
            else:
                _cambia_attributo(child,regole,indice_regola+1,chiave,valore)
        else:
            if direct_child:
                _cambia_attributo(child,regole,0,chiave,valore)
            else:
                _cambia_attributo(child, regole, indice_regola, chiave, valore)

    return res

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    dom = fparse(fileIn)
    regole = selettore.split(" ")
    _cambia_attributo(dom, regole, 0,chiave,valore)
    with open(fileOut, "w",encoding='utf8' ) as file:
        file.write(dom.to_string())

if __name__ == "__main__":
    fileIn = 'slashdot.html'
    selettore = '@[id="slashboxes"] > article h2 > a'
    conta_nodi((fileIn, selettore))
