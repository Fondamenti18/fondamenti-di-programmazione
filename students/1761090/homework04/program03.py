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


def trova_nodi(lista, html_tree, indice=0, current_condition=None, current_operator=None, previous_condition=None):
    #print()
    #print('esploro nodo:', html_tree.tag)
    #print('attribute', html_tree.attr)
    #print('content', html_tree.content)
    #print('indice', indice)
    found = set()
    #   solo alla prima chiamata
    if html_tree.istext():
        #print('è di testo, ritorno')
        return found

    if not current_condition:
        try:
            current_condition = lista[indice]
        except IndexError:
            return found

    if not current_operator:
        try:
            current_operator = lista[indice+1]
        except IndexError:
            pass

    #print('condizione =', current_condition)
    #print('operatore =', current_operator)
    if not current_condition and not current_operator:
        #print('boh')
        return found


    '''         CASO BASE        '''
    #print('controllo se è un id...')
    stringa = current_condition.split('#')
    if stringa[0] == '':  # stiamo cercando un id
        #print('è un id')
        if html_tree.attr.get('id', None) == stringa[1]:
            found.add(html_tree)
    else:
        #print('non è un id')
        pass

    if not found:
        #print('non ho ancora trovato nulla')
        stringa = current_condition.split('@')
        #print('controllo se è un valore...')
        if stringa[0] == '':  # stiamo cercando un valore
            #print('è un valore')
            stringa = stringa[1]
            stringa = stringa.split("=")
            attributo = stringa[0][1:]
            valore = stringa[1][1:-2]
            if html_tree.attr.get(attributo, None) == valore:
                found.add(html_tree)
        else:
            #print('non è un valore')
            pass

    if not found:
        #print('non ho ancora trovato nulla')
        #print('controllo se è una parola in class...')
        stringa = current_condition.split(".")
        if stringa[0] == '':  # stiamo cercando una specifica parola nell'attributo class
            #print('è una parola in class')
            classe = html_tree.attr.get('class', None)
            if classe and stringa[1] in classe:
                found.add(html_tree)
        else:
            #print('non è una parola in class')
            pass

    if not found:
        #print('non ho ancora trovato nulla')
        #print('controllo se è un tag...')
        if html_tree.tag == current_condition:
            found.add(html_tree)

    if not found and previous_condition == '>':
        #print('non ho trovato nulla nei figli')
        return found


    #print('ho trovato', found)
    '''         RICORSIONE          '''
    #print('inizio ricorsione')
    if not found:
        #print('cerco primo selettore')
        # se ancora non ho trovato il primo elemento del selettore

        for figlio in html_tree.content:
            found = found.union(trova_nodi(lista, figlio, indice, current_condition, current_operator))
    else:
        #  se ho trovato il primo elemento del selettore
        if current_operator == '>':
            found = set()
            #print('cerco figli')
            #  se devo rispettare una gerarchia padre -> figlio
            for figlio in html_tree.content:
                found = found.union(trova_nodi(lista, figlio, indice+2, previous_condition=current_operator))

        elif current_operator == '':
            found = set()
            #print('cerco discendenti')
            #   se devo rispettare una gerarchia antenato -> discendente
            for figlio in html_tree.content:
                found = found.union(trova_nodi(lista, figlio, indice+2))
        else:
            #print('ritorno')
            #  ultimo livello del selettore (o selettore a un argomento)
            pass

    return found


def elabora_selettore(selettore):
    lista = selettore.split(' ')
    new_lista = []
    for i, el in enumerate(lista):

        new_lista.append(el)
        if i + 1 == len(lista):
            break
        if el != '' and el != '>' and lista[i + 1] != '>' and lista[i + 1] != '':
            new_lista.append('')

    return new_lista

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    html_tree = fparse(fileIn)
    #print('\n\n\n')

    new_lista = elabora_selettore(selettore)

    nodi = trova_nodi(new_lista, html_tree)


    return len(nodi)



def elimina_nodi(fileIn, selettore, fileOut, html_tree=None, nodi=None):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    gestisci_file = html_tree is None

    if gestisci_file:
        html_tree = fparse(fileIn)

        lista = elabora_selettore(selettore)

        nodi = trova_nodi(lista, html_tree)

    if html_tree.istext():
        return

    for figlio in html_tree.content[:]:
        if figlio in nodi:
            html_tree.content.remove(figlio)

    for figlio in html_tree.content:
        elimina_nodi(fileIn, selettore, fileOut, figlio, nodi)

    if gestisci_file:
        with open(fileOut, 'w') as f:
            f.write(html_tree.to_string())




def cambia_attributo(fileIn, selettore, chiave, valore, fileOut, html_tree=None, nodi=None):
    gestisci_file = html_tree is None

    if gestisci_file:
        html_tree = fparse(fileIn)

        lista = elabora_selettore(selettore)

        nodi = trova_nodi(lista, html_tree)

    if html_tree.istext():
        return

    for figlio in html_tree.content[:]:
        if figlio in nodi:
            figlio.attr[chiave] = valore

    for figlio in html_tree.content:
        cambia_attributo(fileIn, selettore, chiave, valore, fileOut, figlio, nodi)

    if gestisci_file:
        with open(fileOut, 'w') as f:
            f.write(html_tree.to_string())



