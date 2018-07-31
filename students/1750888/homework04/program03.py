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
    n, L = decodifica(selettore)
    x = 9999
    if len(L) == 1:
       x = conta(root, n, L)
    elif len(L) == 3:
       x = conta3(root, L)
    elif len(L) == 2:
       x = conta2(root, L)
    return x

def conta(root, n, L):
    x = 0
    if not root.istext():
       if e_contenuto(root, n, L):
          x = 1
       for y in root.content:
           x = x + conta(y, n, L)
    return x

def conta2(root, L):
    x = 0
    if root.tag == L[0]:
       if not root.istext():
          for y in root.content:
              x = x + trovaDiscendente(y, L[1])
    if not root.istext():
       for y in root.content:
          x = x + conta2(y, L)
    return x

def trovaDiscendente(root, k):
    x = 0
    if root.tag == k:
       x = 1
    else:
       if not root.istext():
          for z in root.content:
             x = x + trovaDiscendente(z, k)
    return x

def conta3(root, L):
    x = 0
    if root.tag == L[0]:
       if not root.istext():
          for y in root.content:
             if y.tag == L[2]:
                x = 1
    if not root.istext():
       for y in root.content:
           x = x + conta3(y, L)
    return x

def decodifica(selettore):
    L = []
    n = ""
    if selettore[0] == '#':    
        n = 'id'
        L.append(selettore[1:])
    elif selettore[0] == '.':          
        n = 'title'
        L.append('*')
    elif selettore[0] == '@':     
        n = 'width'
        x = selettore.index('"')
        y = selettore.index('"', x+1)
        L.append(selettore[x+1: y])
    else:
        n = "tag"
        L = selettore.split()
    return n, L

def e_contenuto(root, n, L):
    t = False
    if n == "tag" and L[0] == root.tag:
       t = True
    else:
       if n in root.attr and (root.attr[n] == L[0] or L[0] == '*'):
          t = True
    return t

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    
    root = fparse(fileIn)
    
    L = decodifica(selettore)
    
    if len(L) == 2:
       root = elimina(root, L)
    
    S = root.to_string()
    with open(fileOut, 'w') as f:
         f.write(S)
    return root

def elimina(root, L):
    x = False
    if root.tag == L[0]:
       if not root.istext():
          for y in root.content:
             cancella(root, y, L)
    else:
         if not root.istext():
            for y in root.content:
                elimina(y, L)
    return root

def cancella(genitore, figlio, L):
    if figlio.tag == L[1]:
       i = genitore.content.index(figlio)
       genitore.content.pop(i)
    else:
       if not figlio.istext():
           for x in figlio.content:
               cancella(figlio, x, L)


def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    root = fparse(fileIn)
    n, L = decodifica(selettore)
    if len(L) == 2:
       cambia(root, L, chiave, valore)
    S = root.to_string()
    with open(fileOut, 'w', encoding="utf8") as f:
         f.write(S)
    return root

def cambia(root, L, chiave, valore):
    if root.tag == L[0]:
       if not root.istext():
          for y in root.content:
              cambia2(y, L, chiave, valore)
    else:
       if not root.istext():
          for y in root.content:
              cambia(y, L, chiave, valore)

def cambia2(root, L, chiave, valore):
    if root.tag == L[1]:
       root.attr[chiave] = valore
    if not root.istext():
       for y in root.content:
          cambia2(y, L, chiave, valore)


