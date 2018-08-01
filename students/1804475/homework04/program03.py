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
    #Inserite qui il vostro codice
    nodo=fparse(fileIn)
    search_nodi=search_nodo(nodo,selettore)
    return len(search_nodi)

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    nodo=fparse(fileIn)
    search_nodi=search_nodo(nodo,selettore)
    for x in search_nodi:
        ricorsive_elimina(x)
    testo=open (fileOut,'w')
    testo.write(nodo.to_string())
    testo.close()
        

def ricorsive_elimina(nodo):
    figli_nodi=nodo.content
    for x in figli_nodi:
        ricorsive_elimina(x)
    del (nodo)
    
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    nodo=fparse(fileIn)
    search_nodi=search_nodo(nodo,selettore)
    for x in search_nodi:
        ricorsive_elimina(x)
    testo=open (fileOut,'w')
    testo.write(nodo.to_string())
    testo.close()
    nodo.attr[chiave]=valore

def search_nodo(nodo,selettore):
    lista=list()
    if selettore[0]=='#':
        if 'id' in nodo.attr:
            if '#' + nodo.attr['id'] == selettore:
                lista.append(nodo)

    elif selettore[0]=='.':
        if 'class' in nodo.attr:
            if selettore[1:] in nodo.attr['class']:
                lista.append(nodo)

    elif selettore[0]=='@':
        x= selettore.split('=')
        variabile1= x[0][2:]
        variabile2=x[1][1:-2]
        if variabile1 in nodo.attr:
            if nodo.attr[variabile1] == variabile2:
                lista.append(nodo)

    elif selettore==nodo.tag:
        lista.append(nodo)
    for testo in nodo.content:
        if testo.tag != '_text_':
            lista+=search_nodo(testo,selettore)
    return lista


