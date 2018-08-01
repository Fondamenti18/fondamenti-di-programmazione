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

def counttag(albero,tag):
    cnt=0
    if albero.tag == tag:
        cnt+=1
    if not albero.istext():
        for figlio in albero.content:
            cnt+=counttag(figlio,tag)
    return cnt


def countid(albero,selettore):
    cnt=0
    if 'id' in albero.attr:
        if albero.attr['id']==selettore:
            cnt+=1
    if not albero.istext():
        for figlio in albero.content:
            cnt+=countid(figlio,selettore)
    return cnt


def countclass(albero,selettore):
    cnt=0
    if 'class' in albero.attr:
        if selettore in albero.attr['class']:
            cnt+=1
    if not albero.istext():
        for figlio in albero.content:
            cnt+=countclass(figlio,selettore)
    return cnt

def countatt(albero,att_val):
    cnt=0
    if att_val[0] in albero.attr:
        if att_val[1] == albero.attr[att_val[0]]:
            cnt+=1
    if not albero.istext():
        for figlio in albero.content:
            cnt+=countatt(figlio,att_val)
    return cnt


def tiposelettore(selettore):
    if selettore[0]=='#':
        return (selettore[1:],'id')
    if selettore[0]=='.':
        return (selettore[1:],'classe')
    if selettore[0]=='@':
        a=selettore[2:-1].replace('=',' ').replace('"','').split()
        return (a,'att-valore')
    return (selettore,'tag')

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    albero=fparse(fileIn)
    tipo=tiposelettore(selettore)
    if tipo[1]=='tag':
        return counttag(albero,tipo[0])
    if tipo[1]=='id':
        return countid(albero,tipo[0])
    if tipo[1]=='classe':
        return countclass(albero,tipo[0])
    if tipo[1]=='att-valore':
        return countatt(albero,tipo[0])

    
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

