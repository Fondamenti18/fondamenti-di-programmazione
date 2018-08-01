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

def getAttrKeyValue(attr):
    s = attr.split('=')
    return s[0][2:], s[1][1:-2]

def isGood(node, sel):
    if sel[0] == '.': #class
        return 'class' in node.attr and sel[1:] in set(node.attr['class'].split())
    elif sel[0] == '#': #id
        return 'id' in node.attr and sel[1:] == node.attr['id']
    elif sel[0] == '@': #attribute
        k, v = getAttrKeyValue(sel)
        return k in node.attr and node.attr[k] == v
    else: #tag
        return node.tag == sel

def checkPath(path, indp, selettore, indsel, mt): #percorso, indice_percorso, selettore, indice_selettore, mt = sono obbligato a prendere il nodo?
    if indsel < 0: #finiti i dati del selettore, c'e' soluzione
        return True
    if indp < 0: #finiti i nodi sul path... non c'e' soluzione
        return False

    if (indsel, mt) in path[indp]['memo']: #memoization: se sono passato gia' in questo stato, non ricalcolo la soluzione
        return path[indp]['memo'][(indsel, mt)]

    ret = False
    if isGood(path[indp]['n'], selettore[indsel]): #lo prendo
        ret = ret or checkPath(path, indp-1, selettore, indsel - (1 if selettore[indsel-1] != '>' else 2), selettore[indsel-1] == '>')
    if not mt: #non lo prendo
        ret = ret or checkPath(path, indp-1, selettore, indsel, False)

    path[indp]['memo'][(indsel, mt)] = ret
    return ret

def getNodes(node, selettore, ls, path): #salva tutti i nodi che rispettano il selettore
    path.append({'n':node, 'memo':{}})
    if isGood(node, selettore[-1]) and checkPath(path, len(path)-1, selettore, len(selettore)-1, True):
        ls.append(node)
    if node.tag != '_text_':
        for v in node.content:
            getNodes(v, selettore, ls, path)
    del path[-1]

def deleteSel(node, selettore, path):
    path.append({'n':node, 'memo':{}})
    if isGood(node, selettore[-1]) and checkPath(path, len(path)-1, selettore, len(selettore)-1, True):
        del path[-1]
        return True
    if node.tag != '_text_':
        for i in range(len(node.content)-1, -1, -1):
            if deleteSel(node.content[i], selettore, path):
                del node.content[i]
    del path[-1]
    return False

def conta_nodi(fileIn, selettore):
    root = fparse(fileIn)
    n = []
    getNodes(root, selettore.split(), n, [])
    return len(n)

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    root = fparse(fileIn)
    with open(fileOut, 'w') as f:
        if not deleteSel(root, selettore.split(), []): #quando e' vera, devo cancellare la radice, quindi non rimane nulla
            f.write(root.to_string())

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    root = fparse(fileIn)
    n = []
    getNodes(root, selettore.split(), n, [])
    for v in n:
        v.attr[chiave] = valore
    with open(fileOut, 'w') as f:
        f.write(root.to_string())

def debugPrint(node, sel):
    print(node.tag, node.attr, sel, isGood(node, sel))
    for v in node.content:
        if v.tag != '_text_':
            debugPrint(v, sel)

if __name__ == '__main__':
    #print(conta_nodi('page1-3.html', 'p > em'))
    elimina_nodi('page1-3.html', 'p', 'out.html')
