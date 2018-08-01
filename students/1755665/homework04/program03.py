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




def tipo_selettore(s):
    '''torna il tipo di selettore'''
    if s.startswith('.'):
        return 'class'
    elif s.startswith('#'):
        return 'id'
    elif s.startswith('@'):
        return 'attr'
    else:
        return 'tag'

def parse_selettore(s):
    '''in base al tipo di selettore parsa il contenuto'''
    tipo = tipo_selettore(s)
    if tipo == 'class':
        return s[1:]
    elif tipo == 'id':
        return s[1:]
    elif tipo == 'attr':
        i = s.find('=')
        t = (s[2:i], s[i+2:-2])
        return t
    elif tipo == 'tag':
        return s

def lista_selettore(selettore):
    '''torna una lista di selettori in forma di tuple,
    se è un solo selettore la lista contiene solo il selettore'''
    ret = []
    l = []
    for e in selettore.split(' '):
        if e != '':
            l.append(e)
    if len(l) == 1:
        return l
    else:
        i = 0
        while i < len(l)-1:
            if l[i+1] == '>':
                ret.append(('pf', l[i], l[i+2]))
                i += 2
            else:
                ret.append(('ad', l[i], l[i+1]))
                i += 1
    return ret

def find_by_attr(node, at):
    '''torna una lista di nodi in base all'attr'''
    ret = []
    if at[0] in node.attr.keys():
        if at[1] in node.attr[at[0]]:
            ret += [node]
    if not node.istext():
        for child in node.content:
            ret += find_by_attr(child, at)
    return ret

def find_by_id(node, id):
    ''' torna una lista di  nodi in base all'id'''
    ret = []
    if 'id' in node.attr.keys():
        if id in node.attr['id']:
            ret += [node]
    if not node.istext():
        for child in node.content:
            ret += find_by_id(child, id)
    return ret

def find_by_class(node, clas):
    '''torna una lista di nodi in base alla classe'''
    ret = []
    if 'class' in node.attr.keys():
        if clas in node.attr['class']:
            ret += [node]
    if not node.istext():
        for child in node.content:
            ret += find_by_class(child, clas)
    return ret

def find_by_tag(node, tag):
    '''torna una lista di nodi che hanno il tag'''
    ret = []
    if node.tag == tag:
        ret += [node]
    if not node.istext():
        for child in node.content:
            ret += find_by_tag(child, tag)
    return ret


def find_node(l_node, sel):
    '''algoritmo che parte da una tripla del selettore ed una lista di nodi gia spulciata per il primo elemento del selettore'''
    l = []
    for node in l_node:
        tipo2 = tipo_selettore(sel[2])
        parse2 = parse_selettore(sel[2])
        if sel[0] == 'pf':
            if not node.istext():
                for child in node.content:
                    if tipo2 == 'tag':
                        if child.tag == parse2:
                            l += [child]
                    elif tipo2 == 'class':
                        if 'class' in child.attr.keys():
                            if parse2 in child.attr['class']:
                                l += [child]
                    elif tipo2 == 'attr':
                        if parse2[0] in child.attr.keys():
                            if parse2[1] == child.attr[parse2[0]]:
                                l += [child]
                    elif tipo2 == 'id':
                        if 'id' in child.attr.keys():
                            if parse2 == child.attr['id']:
                                l += [child]
        elif sel[0] == 'ad':
            if tipo2 == 'tag':
                l.extend(find_by_tag(node, parse2))
            elif tipo2 == 'class':
                l.extend(find_by_class(node, parse2))
            elif tipo2 == 'attr':
                l.extend(find_by_attr(node, parse2))
            elif tipo2 == 'id':
                l.extend(find_by_id(node, parse2))
    return l



'''funzione che conta i nodi'''
def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.
        richiama nel modo giusto le funzioni per contare i nodi'''
    node = fparse(fileIn)
    lista_sel = lista_selettore(selettore)
    l_node = []
    if type(lista_sel[0]) == tuple:
        tipo1 = tipo_selettore(lista_sel[0][1])
        parse1 = parse_selettore(lista_sel[0][1])
        if tipo1 == 'tag':
            l_node.extend(find_by_tag(node, parse1))
        elif tipo1 == 'class':
            l_node.extend(find_by_class(node, parse1))
        elif tipo1 == 'attr':
            l_node.extend(find_by_attr(node, parse1))
        elif tipo1 == 'id':
            l_node.extend(find_by_id(node, parse1))
        for sel in lista_sel:
            l_node = (find_node(l_node, sel))
    else:
        tipo1 = tipo_selettore(lista_sel[0])
        parse1 = parse_selettore(lista_sel[0])
        if tipo1 == 'tag':
            l_node.extend(find_by_tag(node, parse1))
        elif tipo1 == 'class':
            l_node.extend(find_by_class(node, parse1))
        elif tipo1 == 'attr':
            l_node.extend(find_by_attr(node, parse1))
        elif tipo1 == 'id':
            l_node.extend(find_by_id(node, parse1))
    return len(l_node)

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    node = fparse(fileIn)
    lista_sel = lista_selettore(selettore)
    l_node = []
    if type(lista_sel[0]) == tuple:
        tipo1 = tipo_selettore(lista_sel[0][1])
        parse1 = parse_selettore(lista_sel[0][1])
        if tipo1 == 'tag':
            l_node.extend(find_by_tag(node, parse1))
        elif tipo1 == 'class':
            l_node.extend(find_by_class(node, parse1))
        elif tipo1 == 'attr':
            l_node.extend(find_by_attr(node, parse1))
        elif tipo1 == 'id':
            l_node.extend(find_by_id(node, parse1))
        for sel in lista_sel:
            l_node = (find_node(l_node, sel))
    else:
        tipo1 = tipo_selettore(lista_sel[0])
        parse1 = parse_selettore(lista_sel[0])
        if tipo1 == 'tag':
            l_node.extend(find_by_tag(node, parse1))
        elif tipo1 == 'class':
            l_node.extend(find_by_class(node, parse1))
        elif tipo1 == 'attr':
            l_node.extend(find_by_attr(node, parse1))
        elif tipo1 == 'id':
            l_node.extend(find_by_id(node, parse1))
    for n in l_node:
        remove_node(node, n)
    ret = open(fileOut, 'w', encoding='utf8')
    ret.write(node.to_string())
    ret.close()

def remove_node(node, n):
    '''rimuove dall'albero tutti i nodi uguali ad n'''
    if node.istext(): return
    for child in node.content:
        remove_node(child, n)
    newcont = []
    for child in node.content:
        if child == n:
            if child.istext():
                newcont += child.content
        else:
            newcont += [child]
    node.content = newcont

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    node = fparse(fileIn)
    lista_sel = lista_selettore(selettore)
    l_node = []
    if type(lista_sel[0]) == tuple:
        tipo1 = tipo_selettore(lista_sel[0][1])
        parse1 = parse_selettore(lista_sel[0][1])
        if tipo1 == 'tag':
            l_node.extend(find_by_tag(node, parse1))
        elif tipo1 == 'class':
            l_node.extend(find_by_class(node, parse1))
        elif tipo1 == 'attr':
            l_node.extend(find_by_attr(node, parse1))
        elif tipo1 == 'id':
            l_node.extend(find_by_id(node, parse1))
        for sel in lista_sel:
            l_node = (find_node(l_node, sel))
    else:
        tipo1 = tipo_selettore(lista_sel[0])
        parse1 = parse_selettore(lista_sel[0])
        if tipo1 == 'tag':
            l_node.extend(find_by_tag(node, parse1))
        elif tipo1 == 'class':
            l_node.extend(find_by_class(node, parse1))
        elif tipo1 == 'attr':
            l_node.extend(find_by_attr(node, parse1))
        elif tipo1 == 'id':
            l_node.extend(find_by_id(node, parse1))
    for n in l_node:
        modify_node(node, n, chiave, valore)
    ret = open(fileOut, 'w', encoding='utf8')
    ret.write(node.to_string())
    ret.close()

def modify_node(node, n, chiave, valore):
    ''''modifica il valore dei nodi per qulla chiave ed attributo e se uguali al nodo n'''
    if node == n:
        node.attr[chiave] = valore
    if not node.istext():
        for child in node.content:
            modify_node(child, n, chiave, valore)