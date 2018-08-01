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

from  my_html import HTMLNode, fparse, _MyHTMLParser

def parse(html):
    parser = _MyHTMLParser()
    parser.feed(html)
    return parser.root

def fparse(fhtml):
    with open(fhtml) as f:
        root = parse(f.read())
    return root

def find_by_tag(node, tag):
    ret = []
    if node.tag == tag: ret += [node]
    if not node.istext():
        for child in node.content:
            ret += find_by_tag(child,tag)

    return ret

def riconosci_info(selettore):
    if not selettore.isalnum():
        if selettore[:1]=='#':
            seleinfo=str('id="')+selettore[1:]+str('"')
        elif selettore[:1]=='.':
            seleinfo=str('class="')+selettore[1:]+str('"')
    else:
        seleinfo=str('<')+selettore
    return seleinfo

def conta_nodi(fileIn, selettore):
    cont=0
    doc = fparse(fileIn)
    node=fparse(fileIn)
    if not selettore.isalnum():
        if len(selettore.split(' '))!=1:
            indice=1
            if selettore.split(' ')[indice]=='>':
                indice=2
            seleinfo=riconosci_info(selettore.split(' ')[indice])
            for node in find_by_tag(doc,selettore[0]):
                parole=node.to_string().split(' ')
                for sez in parole:
                    if seleinfo in sez:
                        cont+=1
        else:   
            seleinfo=riconosci_info(selettore)
            
            parole=doc.to_string().split(' ')
            for sez in parole:
                if seleinfo in sez:
                    cont+=1
    else:        
        for node in find_by_tag(doc,selettore):
            cont+=1
    #print(cont)
    return cont
#conta_nodi('page1-3.html', 'p a')
           
def remove_by_tag(node, tag):
    if node.istext(): return
    for child in node.content:
        remove_by_tag(child,tag)
    newcont = []
    for child in node.content:
        if child.tag == tag:
            if not child.istext():
                newcont += child.content

        else:
            newcont += [child]
    node.content = newcont
    
def elimina_nodi(fileIn, selettore, fileOut):
    doc=fparse(fileIn)
    if ' ' in selettore:
        selettore=selettore.split(' ')[-1:]
    remove_by_tag(doc,selettore)
    f = open(fileOut,'w')
    f.write(doc.to_string())
    f.close()
    return doc.to_string()
#elimina_nodi('page1-3.html','p > em','prova.html')
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

