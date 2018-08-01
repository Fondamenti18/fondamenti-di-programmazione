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

def trovaselettore(nodo, criterio,cosacerco):
    contatore=0
    if cosacerco=="lista":
        if not nodo.istext():
            if nodo.tag==criterio[0]:
                for figlio in nodo.content:
                    if figlio.tag==criterio[1]:
                        return 1
            else:
                for figlio in nodo.content:
                    contatore=contatore+trovaselettore(figlio,criterio,cosacerco)
        
    if cosacerco=="@":
        listacriterio=criterio.split("=")
        poggino=listacriterio[1]
        a=poggino
        listacriterio[1]=a[1:-1]
        if not nodo.istext():
            if listacriterio[0] in nodo.attr:
                if nodo.attr[listacriterio[0]]==listacriterio[1]:
                    return 1
            else:
                for figlio in nodo.content:
                    contatore=contatore+trovaselettore(figlio,criterio,cosacerco)
    if cosacerco=="id" or cosacerco=="class":
        if cosacerco in nodo.attr:
            if nodo.attr[cosacerco].find(criterio)!=-1:
                return 1
        else:
            if not nodo.istext():
                for figlio in nodo.content:
                    contatore=contatore+trovaselettore(figlio, criterio, cosacerco)
    elif cosacerco=="tag":
        if nodo.tag==criterio:
            return 1
        else:
            if not nodo.istext():
                for figlio in nodo.content:
                    contatore=contatore+trovaselettore(figlio,criterio,cosacerco)
    return contatore



def conta_nodi(fileIn, selettore):
    counter=0
    radice=fparse(fileIn)
    if selettore.find(">")!=-1:
        listaselettori=selettore.split(" > ")
    if selettore[0]=="@":
        selettore2=selettore[2:-1]
        selettorestandard="@"
    elif selettore[0]=="#":
        selettore2=selettore[1:]
        selettorestandard="id"
    elif selettore[0]==".":
        selettore2=selettore[1:]
        selettorestandard="class"
    else:
        if selettore.find(">")!=-1:
            selettorestandard="lista"
            selettore2=listaselettori
        else:
            selettorestandard="tag"
            selettore2=selettore
    counter=0
    counter=trovaselettore(radice,selettore2,selettorestandard)
    return counter
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

