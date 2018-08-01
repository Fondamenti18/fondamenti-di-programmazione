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
import re
from  my_html import HTMLNode, fparse

def atts(sel):
    att = sel.split(" ")
    for el in att:
        if '#' in el:
            tag = ('id', el.replace('#', '')) 
            return tag
        if '.' in el:
            tag = ('class', el.replace('.', ""))
            return tag
        if '@' in el:
            words = el.split('=')
            tag = (re.sub(r'[^a-zA-Z]', '', words[0]), re.sub(r'[^a-zA-Z0-9]', '', words[-1]) )
            return tag
   

def is_att(sel):
    atts = ['.', '#', '@']
    for a in atts:
        if a in sel:
            return True
    return False
    
def find_tags(nodo, tag):
    tags = []
    if nodo.tag == tag: 
        tags += [nodo]
    if not nodo.istext():
        for child in nodo.content:
            tags += find_tags(child, tag)
    return tags

def find_dir_childs(nodo, sel):
    att = sel.split(" ")
    tag = att[0]
    sub = att[-1]
    chs = []
    if not nodo.istext():
        if nodo.tag == tag: 
            for n in nodo.content:
                if n.tag == sub:
                    chs += [n]
        for child in nodo.content:
            chs += find_dir_childs(child, sel)
    return chs

def find_subnodes(nodo, sel, s = []):
    if isinstance(sel, tuple):
        tag = sel[0]
        sub = sel[1]
    else:
        tags = sel.split(" ")
        tag = tags[0]
        sub = tags[-1]
    l = find_tags(nodo, tag)
    for n in l:
        s.extend(find_tags(n, sub))
    return s

def find_atts(nodo, sel):
    nodi = []
    k, v = atts(sel)
    if v in nodo.attr.get(k, ""): 
        nodi.append(nodo)
    if not nodo.istext():
        for child in nodo.content:
            nodi += find_atts(child, sel)
    return nodi       

def remove_nodes(nodo, tag):
    if nodo.istext(): 
        return
    for child in nodo.content:
        remove_nodes(child, tag)
    figli = []
    for child in nodo.content:
        if child.tag == tag:
            child.content = []
        else:
            figli += [child]
    nodo.content = figli 

def parse_sel(sel):
    sels = sel.split(">")
    parsed = []
    ret = []
    for s in sels:
        parsed.append(s.strip())
    for el in parsed:
        if " " in el:
            r = el.split(" ")
            r1 = (r[0], r[1])
            ret.append(r1)
        else:
            ret.append(el)
    return ret

def find_complex(root, sel, i = 0, nodes = []):
    sels = parse_sel(sel)
    s = sels[i]
    temp = []
    if is_att(s) and not isinstance(s, tuple):
        temp += find_atts(root, s)
    elif not is_att(s) and isinstance(s, tuple):
        temp += find_subnodes(root, s)
    elif is_att(s) and isinstance(s, tuple):
        for n in find_atts(root, s):
            temp += find_atts(n, s)
    else:
        temp += find_tags(root, s)
    for n in temp:
        nodes += find_complex(n, sel, i+1, nodes)
    return nodes        
    
def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    root = fparse(fileIn) 
    if len(selettore) == 1:
        res = find_tags(root, selettore)
        return len(res)
    if is_att(selettore):
        ret = find_atts(root, selettore)
        return len(ret)
    if '>' in selettore:
        ret = find_dir_childs(root, selettore)
        return len(ret)
    else:
        ret = find_subnodes(root, selettore)
        return len(ret)   

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    root = fparse(fileIn)
    att = ""
    if is_att(selettore):
        att = atts(selettore)
    s = selettore.split(" ")
    tag = s[0]
    sub = s[-1]
    if att:
        nodi = find_atts(root, selettore)
    nodi = find_tags(root, tag)
    for n in nodi:
        remove_nodes(n, sub)
    with open(fileOut, 'w', encoding = 'utf8') as f:
        f.write(root.to_string())
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    root = fparse(fileIn)
    if is_att(selettore):
        nodi = find_atts(root, selettore)
    else:
        nodi = find_subnodes(root, selettore)
    for n in nodi:
        n.attr[chiave] = valore
    with open(fileOut, 'w', encoding = 'utf8') as f:
        f.write(root.to_string())    
        

    
