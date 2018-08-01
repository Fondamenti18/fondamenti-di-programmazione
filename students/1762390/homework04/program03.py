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
    albero = fparse(fileIn)
    a = b = c = x = ""
    if selettore[0] == '#' or selettore[0] == '.':
        a = selettore[1:]
        x = contaId(albero, a)
    elif selettore[0] == '@':
         T = ""
         for h in selettore:
            if h.isalpha() or h.isdigit():
                T = T + h
            else:
                T = T + " "
         lista = T.split()
         x = contaId(albero, '@', lista[0], lista[1])
    elif selettore[0].isalpha() and len(selettore)==1:
         lista = selettore.split()
         if len(lista)==1:
            x = contaId(albero, lista[0])
    elif selettore[0].isalpha() and len(selettore)==3:   
         T = ""
         for h in selettore:
            if h.isalpha():
                T = T + h
            else:
                T = T + " "
         lista = T.split()   
         x = trovaAvoDiscendente(albero, lista[0], lista[1])
    elif selettore[0].isalpha() and '>' in selettore:  
         T = ""
         for h in selettore:
            if h.isalpha() or h == '>':
                T = T + h
            else:
                T = T + " "
         lista = T.split()   
         x = trovaGenitoreFiglio(albero, lista[0], lista[2])
    return x

def contaId(albero, a, b = None, c = None):
    x = 0
    if not albero.istext():
       if albero.tag==a:
          x = 1
          b = c = None
       elif a in albero.attr.keys():
            x = 1
            b = c = None
       elif a in albero.attr.values():
            x = 1
            b = c = None
       elif a[0] == "@":
            if b in albero.attr and albero.attr[b] == c:
               x = 1
       elif b == '>':    
            x = trovaGenitoreFiglio(albero, a, c)

       for figlio in albero.content:
           x = x + contaId(figlio, a, b, c)
    return x

def trovaGenitoreFiglio(albero, a, c):
    x = 0
    if albero.tag == a:
       if not albero.istext():
          for figlio in albero.content:
             if figlio.tag == c:
                x = 1
    if not albero.istext():
       for figlio in albero.content:
           x = x + trovaGenitoreFiglio(figlio, a, c)
    return x

def trovaAvoDiscendente(albero, a, c):   
    x = 0
    if albero.tag == a:
       if not albero.istext():
          for figlio in albero.content:    
              x = x + trovaDiscendente(figlio, c)
    if not albero.istext():
       for figlio in albero.content:
           x = x + trovaAvoDiscendente(figlio, a, c)
    return x

def trovaDiscendente(albero, c):
    x = 0
    if albero.tag == c:
       
       x = 1
    if not albero.istext():
       for figlio in albero.content:
           x = x + trovaDiscendente(figlio, c)
    return x

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    albero = fparse(fileIn)
    T = ""
    for h in selettore:
        if h.isalpha():
           T = T + h
        else:
           T = T + " "
    lista = T.split()
    if len(lista) == 2:
       eliminaAvoDiscendenti(albero, lista[0], lista[1])

    with open(fileOut, 'w') as f:
         f.write(albero.to_string())

def eliminaAvoDiscendenti(albero, a, b):
    if albero.tag == a:
       if not albero.istext():
          for figlio in albero.content:
             eliminaDiscendente(albero, figlio, b)
    else:
         if not albero.istext():
            for figlio in albero.content:
                eliminaAvoDiscendenti(figlio, a, b)
    return albero

def eliminaDiscendente(genitore, figlio, b):
    if figlio.tag == b:
       i = genitore.content.index(figlio)
       genitore.content.pop(i)  
    else:
       if not figlio.istext():
           for nipote in figlio.content:
               eliminaDiscendente(figlio, nipote, b)    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    albero = fparse(fileIn)
    T = ""
    for h in selettore:
        if h.isalpha():
           T = T + h
        else:
           T = T + " "
    lista = T.split()
    if len(lista) == 2:
       cambiaAvoDiscendenti(albero, lista[0], lista[1], chiave, valore)

    with open(fileOut, 'w') as f:
         f.write(albero.to_string())
         
def cambiaAvoDiscendenti(albero, a, b, chiave, valore):
    if albero.tag == a:
       if not albero.istext():
          for figlio in albero.content:
              cambiaDiscendente(figlio, b, chiave, valore)
    else:
       if not albero.istext():
          for figlio in albero.content:
              cambiaAvoDiscendenti(figlio, a, b, chiave, valore)

def cambiaDiscendente(albero, b, chiave, valore):
    if albero.tag == b:
       albero.attr[chiave] = valore
    if not albero.istext():
       for figlio in albero.content:
          cambiaDiscendente(figlio, b, chiave, valore)


