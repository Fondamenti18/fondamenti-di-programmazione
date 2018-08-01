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

def find_nodes(lista, albero, i=0, cc=None, co=None, pc=None):
    trovato = set()
    if albero.istext(): return trovato
    # print(cc)
    # print(co)
    # print(pc)
    if not cc:
        try: cc = lista[i]
        except: return trovato
    if not co:
        try: co = lista[i+1]
        except:
            ""
            #print(errore)
    if not cc and not co: return trovato
    sel = cc.split('#')
    if sel[0] == '':
        # print(sel)
        if albero.attr.get('id', []) == sel[1]: trovato.add(albero)
    if not trovato:
        # print(sel)
        sel = cc.split(".")
        if sel[0] == '':
            classe = albero.attr.get('class', [])
            # print(classe)
            if classe and sel[1] in classe: trovato.add(albero)
    if not trovato:
        # print(albero.tag)
        if albero.tag == cc: trovato.add(albero)
    if not trovato:
        # print(sel)
        sel = cc.split('@')
        if sel[0] == '':
            sel = sel[1]
            # print(sel)
            sel = sel.split("=")
            valore = sel[1][1:-2]; attributo = sel[0][1:]
            if albero.attr.get(attributo, []) == valore: trovato.add(albero)
    if not trovato and pc == '>': return trovato
    if not trovato:
        for child in albero.content: trovato = trovato.union(find_nodes(lista, child, i, cc, co))
        # print(trovato)
    else:
        # print(co)
        # print(trovato)
        if co == '':
            trovato = set()
            for child in albero.content: trovato = trovato.union(find_nodes(lista, child, i+2))
            # print(trovato)
        elif co == '>':
            trovato = set()
            for child in albero.content: trovato = trovato.union(find_nodes(lista, child, i + 2, pc=co))
            # print(trovato)
    # print(trovato)
    return trovato


def conta_nodi(fileIn, selettore):
    i = 0; nlst = []; lista = selettore.split(' ')
    for el in lista:
        nlst.append(el)
        if len(lista) == i + 1: break
        if el != '>' and el != '' and lista[i + 1] != '' and lista[i + 1] != '>': nlst.append('')
        i += 1
    lista = nlst; albero = fparse(fileIn)
    nodes = find_nodes(lista, albero)
    ret = len(nodes)
    return ret


def my_elimina_nodi(fileIn, selettore, fileOut, albero, nodes):
    if albero.istext(): return
    # print(albero)
    for child in albero.content[:]:
        if child in nodes: albero.content.remove(child)
    for child in albero.content:
        # print(child)
        my_elimina_nodi(fileIn, selettore, fileOut, child, nodes)

def elimina_nodi(fileIn, selettore, fileOut):
    i = 0; nlst = []; lista = selettore.split(' ')
    for el in lista:
        #print(el)
        nlst.append(el)
        # print(len(lista))
        if len(lista) == i + 1: break
        if el != '>' and el != '' and lista[i + 1] != '' and lista[i + 1] != '>': nlst.append('')
        i+=1
        # print(i)
    lista = nlst; albero = fparse(fileIn)
    # print(lista)
    nodes = find_nodes(lista, albero)
    # print(nodes)
    my_elimina_nodi(fileIn, selettore, fileOut, albero, nodes)
    with open(fileOut, 'w') as file: file.write(albero.to_string())


def my_cambia_attributo(fileIn, selettore, chiave, valore, fileOut, albero, nodes):
    if albero.istext(): return
    for child in albero.content[:]:
        #print(child)
        if child in nodes: child.attr[chiave] = valore
    for child in albero.content:
        #print(child)
        my_cambia_attributo(fileIn, selettore, chiave, valore, fileOut, child, nodes)

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    i = 0; nlst = []; lista = selettore.split(' ')
    for el in lista:
        nlst.append(el)
        if len(lista) == i + 1: break
        if el != '>' and el != '' and lista[i + 1] != '' and lista[i + 1] != '>': nlst.append('')
        i+=1
    lista = nlst; albero = fparse(fileIn)
    #print(lista)
    #print(albero)
    nodes = find_nodes(lista, albero)
    #print(nodes)
    my_cambia_attributo(fileIn, selettore, chiave, valore, fileOut, albero, nodes)
    with open(fileOut, 'w') as file: file.write(albero.to_string())

