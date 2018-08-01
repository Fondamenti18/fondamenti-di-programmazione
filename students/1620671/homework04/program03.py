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
    if fileIn[-5:] == '.html':
        doc = fparse(fileIn)
        doc = doc.to_string()
        return conta_nodi(doc,selettore)
    else:
        count = 0
        for i in fileIn.splitlines():
            if soddisfa_sel(i, selettore) == True:
                count += 1
    return count

def soddisfa_sel(i, selettore):
    sel = selettore[0]
    if sel == '#':
        if 'id=' not in i:
            return False
        else:
            s = i.split('id="')[1]
            s = s.split('"')[0]
            if s == selettore[1:]:
                return True
    elif len(selettore) == 1:
        if '<'+sel in i:
            return True
        else:
            return False
    elif sel == '.':
        if selettore[1:]+'=' not in i:
            return False
        else:
            return True
    elif sel == '@':
        if selettore[2:].split(']')[0] not in i:
            return False
        else:
            return True
    elif selettore[1] == ' ' and selettore[2] != '>':
        if soddisfa_sel(i, selettore[0]) == True:
            if '<'+selettore[2] in i:
                return True
            else:
                return False
        else:
            return False
    elif selettore[2] == '>':
        if soddisfa_sel(i, selettore[0]) == True:
            if '<'+selettore[4:] in i and 'testo'in i:
                return True
            else:
                return False
        else:
            return False

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    if conta_nodi(fileIn, selettore) == 0:
        fileOut = fileIn
    else:
        doc = fparse(fileIn)
        doc = doc.to_string()
        for i in doc.splitlines():
            if soddisfa_sel(i, selettore) == False:
                with open(fileOut, 'w') as of:
                    of.write(i)



def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    if conta_nodi(fileIn, selettore) == 0:
        fileOut = fileIn
