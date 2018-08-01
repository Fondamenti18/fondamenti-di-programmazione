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

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    doc=fparse(fileIn)  
    trovati=selettore_css(doc, selettore)
    return len(trovati)
    

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    doc=fparse(fileIn)  
    trovati=selettore_css_non(doc, selettore)
    return new
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    doc=fparse(fileIn)  
    trovati=selettore_css(doc, selettore)
    

def selettore_css(nodo, selettore):
    trovati = []
    # indentificatore del selettore
    tipo_selettore = selettore[:1]
    if tipo_selettore == '#':
        # selettore id  
        if 'id' in nodo.attr and nodo.attr['id'] == selettore[1:]:
            trovati.append(nodo)
    elif tipo_selettore == '.':
        # selettore class
        if 'class' in nodo.attr and selettore[1:] in nodo.attr['class'].split(' '):
            trovati.append(nodo)
    elif tipo_selettore == '@':
        # selettore attribute
        nome_attributo, valore_attributo = selettore[2:-1].split('=')
        valore_attributo = valore_attributo.replace('"', '')
        if nome_attributo in nodo.attr and nodo.attr[nome_attributo] == valore_attributo:
            trovati.append(nodo)
    elif selettore == nodo.tag:
        # selettore tag
        trovati.append(nodo)
    # caso base
    if nodo.tag == '_text_': return trovati
    # caso ricorsivo
    for nodo_figlio in nodo.content:
        trovati += selettore_css(nodo_figlio, selettore)
    return trovati

    
def selettore_css_non(nodo, selettore):
    trovati = []
    # indentificatore del selettore
    tipo_selettore = selettore[:1]
    if tipo_selettore == '#':
        # selettore id  
        if 'id' in nodo.attr and nodo.attr['id'] == selettore[1:]:
            trovati.append(nodo)
    elif tipo_selettore == '.':
        # selettore class
        if 'class' in nodo.attr and selettore[1:] in nodo.attr['class'].split(' '):
            trovati.append(nodo)
    elif tipo_selettore == '@':
        # selettore attribute
        nome_attributo, valore_attributo = selettore[2:-1].split('=')
        valore_attributo = valore_attributo.replace('"', '')
        if nome_attributo in nodo.attr and nodo.attr[nome_attributo] == valore_attributo:
            trovati.append(nodo)
    elif selettore == nodo.tag:
        # selettore tag
        trovati.append(nodo)
    # caso base
    new=[]
    for figlio in nodo.content:
        selettore_css_non(figlio,selettore)
        if figlio.selettore==selettore:
            if nodo.selettore!='_text_':
                new+=figlio.content
        else:
            new+= [figlio]
            nodo.content = new
    return new

        
