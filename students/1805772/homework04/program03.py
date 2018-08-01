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
        e' il figlio di un tag che ha                                           class="... class1 ..."
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
    conta_nodi(fileIn, selettore) Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.
    elimina_nodi(fileIn, selettore, fileOut) Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)
    cambia_attributo(fileIn, selettore, chiave, valore, fileOut) Modifica tutti i nodi dell'albero che soddisfano il selettore CSS

ATTENZIONE: nei test verra' utilizzato un timout globale di 1*N secondi (se il grader fa N test)
'''

from  my_html import HTMLNode, fparse

def splitSelettore(selettore):
    # s e' una lista
    s = selettore.split(" ")
    risultato = dict()
    
    # Scandisco una copia della lista
    i = 'i'
    y = 'y'
    for valore in s[:]:
        # Se valore inizia con # e' proprio un id
        if valore[0] == '#':
            risultato['id'] = valore[1:]
        # Se valore inizia con . e' proprio una classe
        elif valore[0] == '.':
            risultato['class'] = valore[1:]
        # Se valore e' >
        #elif valore == '>':
        #    risultato.append(valore)
        # Se valore inizia con @ e' proprio un attributo generico
        elif valore[0] == '@':
            risultato[y] = valore[valore.index('=') + 2:-2]
            y += 'y'
        # Se valore e' una lettera
        elif valore != '>':
            risultato[i] = valore
            i += 'i'

    return risultato

def splitSelettorePadre(selettore):
    # s e' una lista
    s = selettore.split(" ")
    risultato = []
    
    # Scandisco una copia della lista
    for valore in s[:]:
        if valore == '>':
            pass
        else:
            risultato.append(valore)

    return risultato   
    
def scavaContando(albero , selettore , risultato):
    if not albero.istext():
        for figli in albero.content:
            valori = figli.attr.values()
            for i in valori:
                # i e' una stringa
                for x in selettore.values():
                    if x in i:
                        risultato += 1
            risultato = scavaContando(figli , selettore , risultato)

    return risultato

def scavaContandoTag(albero , selettore , risultato):
    if not albero.istext():
        for figli in albero.content:
            valori = figli.attr.values()
            for x in selettore.values():
                if figli.tag in x :
                    risultato += 1
            risultato = scavaContandoTag(figli , selettore , risultato)

    return risultato


def cerca(albero , x):
    if not albero.istext():
        for figli in albero.content:
            if x == figli.tag:
                return True
            #else:
            #    niente = cerca(figli,x)
    return False

def scavaContandoPadre(albero , selettore , risultato , contatore = 0):
    if not albero.istext():
        for figli in albero.content:
            if selettore[0] == figli.tag:
                bandiera = cerca(figli , selettore[1])
                if bandiera == True:
                    risultato += 1
            risultato = scavaContandoPadre(figli , selettore , risultato , contatore)

    return risultato


def cercaAvo(albero , x):
    risultato = 0
    if not albero.istext():
        for figli in albero.content:
            if x == figli.tag:
                return 1
            else:
                risultato += cercaAvo(figli,x)
    return risultato

def scavaContandoAvo(albero , selettore , risultato , contatore = 0):
    if not albero.istext():
        for figli in albero.content:
            if selettore[0] == figli.tag:
                bandiera = cercaAvo(figli , selettore[1])
                risultato += bandiera
            risultato = scavaContandoAvo(figli , selettore , risultato , contatore)

    return risultato







# ===========================
# ==== FUNZIONI HOMEWORK ====
# ===========================

def conta_nodi(fileIn, selettore):
    radice = fparse(fileIn)
    if '>' in selettore:
        selettore = splitSelettorePadre(selettore)
        risultato = scavaContandoPadre(radice , selettore , 0)
        return risultato
        
    elif ' ' in selettore:
        selettore = splitSelettorePadre(selettore)
        risultato = scavaContandoAvo(radice , selettore , 0)
        return risultato

    else:
        selettore = splitSelettore(selettore)
    
    if 'i' in selettore:
        risultato = scavaContandoTag(radice , selettore , 0)
    else:
        risultato = scavaContando(radice , selettore , 0)
        
    return risultato

def elimina_nodi(fileIn, selettore, fileOut):
    #Inserite qui il vostro codice
    pass

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    #Inserite qui il vostro codice
    pass

if __name__ == '__main__':
    print(conta_nodi('page1-3.html' , 'p a'))
