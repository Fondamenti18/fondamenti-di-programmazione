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
    root = fparse(fileIn)
    rootList = [root]
    select = selettore.split()
    return len(ricorsione1(rootList, select))

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    root = fparse(fileIn)
    rootList = [root]
    select = selettore.split()
    nodi = ricorsione1(rootList, select)
    for nodo in nodi:
        remove(nodo)
        

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

def ricorsione1(lstN, lstSelect):
    if lstN == [] or lstSelect == []: return lstN
    if lstSelect[0] == '>':
        newN = []
        for nodo in lstN:
            if nodo.tag != '_text_':
                for child in nodo.content:
                    newN += ctrl(child, lstSelect[1])
        newSelect = lstSelect[2:]
        return ricorsione1(newN, newSelect)
    else:
        for nodo in lstN:
            newN = []
            if nodo.tag != '_text_':
                for child in nodo.content:
                    if lstSelect[0][0].isalpha(): newN += find_by_tag(child, lstSelect[0])
                    elif lstSelect[0][0] == '.': newN += find_by_class(child, lstSelect[0])
                    elif lstSelect[0][0] == '#': newN += find_by_id(child, lstSelect[0])
                    elif lstSelect[0][0] == '@': newN += find_by_attr(child, lstSelect[0])
        newSelect = lstSelect[1:]
        return ricorsione1(newN, newSelect)
    
def ctrl(nodo, word):
    if word[0].isalpha() and nodo.tag == word: return [nodo]
    elif nodo.attr != {}:
        if word[0] == '.' and word[1:] in nodo.attr['class']: return [nodo]
        elif word[0] == '#' and word[1:] == nodo.attr['id']: return [nodo]
        elif word[0] == '@':
            wordlst = word.split('=')
            if nodo.attr[wordlst[0][2:]] == wordlst[1][1:-2]: return [nodo]
            else: return []
    else: return []

    
def find_by_tag(nodo, tag):
    ret = []
    if nodo.tag == tag: ret += [nodo]
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            ret += find_by_tag(figlio,tag)
    return ret
    
def find_by_class(nodo, cl):
    ret = []
    if 'class' in nodo.attr:
        if cl[1:] in nodo.attr['class']: ret += [nodo]
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            ret += find_by_class(figlio,cl)
    return ret

def find_by_id(nodo, i):
    ret = []
    if 'id' in nodo.attr:
        if nodo.attr['id'] ==  i[1:]: ret += [nodo] 
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            ret += find_by_id(figlio,i)
    return ret

def find_by_attr(nodo, attr):
    ret = []
    wordlst = attr.split('=')
    if wordlst[0][2:] in nodo.attr:
        if nodo.attr[wordlst[0][2:]] == wordlst[1][1:-2]: ret += [nodo]
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            ret += find_by_attr(figlio,attr)
    return ret

def remove(nodo):
    if nodo.tag =='_text_': return
for figlio in nodo.content:
remove_by_tag(figlio,tag)
newcontent = []
for figlio in nodo.content:
if figlio.tag == tag:
if nodo.tag!='_text_':
newcontent += figlio.content
else:
newcontent += [figlio]
nodo.content = newcontent
        
                
        
    

        
    