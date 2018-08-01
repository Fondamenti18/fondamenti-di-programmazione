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
from  my_html import fparse
from copy import copy 

def hasRule(actSel, n):
    if actSel[0] == '.':
        if 'class' in n.attr:
            attr = n.attr['class'].split(' ')
            for a in attr:
                if a == actSel[1:]: return True
    elif actSel[0] == '#' and 'id' in n.attr and n.attr['id'] == actSel[1:]: return True
    elif actSel[0] == '@':
        attr = actSel.replace('[', '').replace(']','').replace('"','').split('=')
        index = attr[0][1:]
        value = attr[1]
        if index in n.attr:
            attr = n.attr[index].split(' ')
            for a in attr:
                if a == value: return True
    return actSel == n.tag

def recursiveCount1(n, sel, mbe=False):
    if n.istext(): return 0
    res, b = hasRule(sel[0], n), 0
    if mbe:
        if not res: return 0
        mbe = False
    if len(sel) and res:
        del sel[0]
        if len(sel) and sel[0] == '>':
            mbe = True
            del sel[0]
    if not len(sel): return 1
    for t in n.content:
        b += recursiveCount1(t, copy(sel), mbe)
    return b 


def recursiveCount2(n, sel, mbe=False):
    if n.istext(): return 0
    res = hasRule(sel[0], n)
    if mbe:
        if not res: return 0
        mbe = False
    if len(sel) and res:
        del sel[0]
        if len(sel) and sel[0] == '>':
            mbe = True
            del sel[0]
    if not len(sel): 
        n.content.clear()
        return 1
    for i in range(len(n.content)-1, -1, -1):
        if recursiveCount2(n.content[i], copy(sel), mbe):
            n.content.pop(i)
    return 0

def recursiveCount3(n, sel, chiave, valore, mbe=False):
    if n.istext(): return 
    res = hasRule(sel[0], n)
    if mbe:
        if not res: return 
        mbe = False
    if len(sel) and res:
        del sel[0]
        if len(sel) and sel[0] == '>':
            mbe = True
            del sel[0]      
    if not len(sel):
        n.attr[chiave] = valore
        return
    for t in n.content:
        recursiveCount3(t, copy(sel), chiave, valore, mbe)
        
def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    Root = fparse(fileIn) 
    return recursiveCount1(Root, selettore.split(' '))

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    Root = fparse(fileIn) 
    recursiveCount2(Root, selettore.split(' '))
    with open(fileOut, 'w') as f:
        f.write(Root.to_string())
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    Root = fparse(fileIn) 
    recursiveCount3(Root, selettore.split(' '), chiave, valore)
    with open(fileOut, 'w') as f:
        f.write(Root.to_string())
