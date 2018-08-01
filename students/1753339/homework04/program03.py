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

def parti(selettore):
    # Ritorna un dizionario che ha come chiavi i determinati attributi in selettore e come chiavi i valori richiesti
    diz = {}
    i = 0
    figlio = False
    simboli = ['.','#','@']
    lista = selettore.split()
    for el in lista:
        s = el[0]
        if s == simboli[0]:
            diz['class'] = el[1:]
        elif s == simboli[1]:
            diz['id'] = el[1:]
        elif s == simboli[2]:
            diz['attr'] = {}
            k,v = '',''
            for c in el[2:]:
                if c.isalpha():
                    k += c
                    continue
                if not c.isalnum():
                    pass
                else:
                    v += c
            diz['attr'][k] = v
        elif s == '>':
            figlio = True
            pass
        else:
            i += 1
            if i > 1 and figlio == True:
                diz['tag_f'] = el # tag figlio
            elif i > 1 and figlio != True:
                diz['tag_d'] = el # tag discendente
            else:
                diz['tag'] = el
    return diz

def n_nodi(doc):
    #preso un nodo aggiunge alla lista finale i nodi-figli del nodo
    # lo fa ricorsivamente
    n = [doc]
    if not doc.istext():
        for child in doc.content:
            n += n_nodi(child)
    return n

def trova(nodi,rit,select):
    #ritorna una lista di nodi che soddisfano il selettore
    for nodo in nodi:
        x = nodo.attr
        for key, val in select.items():
            if key == 'tag':
                if str(nodo.tag) == val:
                    rit.append(nodo)
            elif key == 'class' or key == 'id':
                if key not in nodo.attr.keys():
                    pass
                elif val in nodo.attr[str(key)]:
                    rit.append(nodo)
            elif key == 'attr':
                for k,v in x.items():
                    for k1,v1 in val.items():
                        if k == k1 and v == v1:
                            rit.append(nodo)
            elif key == '>':
                pass
    # GESTISCE IL PROBLEMA DI TAG-PADRE, TAG-FIGLIO  E TAG-DISCENDENTE
    if not 'tag_f' in select.keys() and 'tag_d' not in select.keys():
        return rit
    rit_2 = []
    for nodo in rit:
        if nodo.tag == select['tag']:
            rit_2 = ric(rit_2,nodo,select)
    return rit_2

def ric(rit_2,nodo,select):
    #funzione ricorsiva legata alla funzione trova
    if 'tag_f' in select.keys():
        for child in nodo.content:
            if child.tag == select['tag_f']:
                rit_2.append(nodo)
    elif 'tag_d' in select.keys():
        if not nodo.istext():
            for child in nodo.content:
                if child.tag == select['tag_d']:
                    rit_2.append(nodo)
                    break
                else:
                    rit_2 = ric(rit_2,child,select)
        else:
            if nodo.tag == select['tag_d']:
                rit_2.append(nodo.content)
    return rit_2

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    doc = fparse(fileIn)
    select = parti(selettore) # lista contenente cio' che devo cercare in doc (richiesto dal selettore)
    nodi = n_nodi(doc)
    rit = []
    rit = trova(nodi,rit,select)
    return len(rit)

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    doc = fparse(fileIn)
    select = parti(selettore)  # dizionario contenente cio' che devo cercare in doc (richiesto dal selettore)
    nodi = n_nodi(doc)
    rit = []
    rit = trova(nodi,rit,select) # nodi che soddisfano il selettore CSS
    for nodo in nodi:
        if nodo in rit:
            for el in nodo.content:
                if not el.istext():
                    nodo.content.remove(el)
    with open(fileOut,'w',encoding = 'utf-8') as f:
        f.write(nodi[0].to_string())

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    doc = fparse(fileIn)
    select = parti(selettore)
    nodi = n_nodi(doc)
    rit = []
    rit = trova(nodi,rit,select)
    c = rit[0].content
    for nodo in nodi:
        if nodo in c:
            nodo.attr[chiave] = valore
    radice = nodi[0]
    with open(fileOut,'w') as f:
        f.write(radice.to_string())
