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
    '''Ritorna il numero di nodi dell'albero di questo nodo'''
    radice=fparse(fileIn)
    insieme=find_selector(radice,selettore)
   # print(len(insieme))
    return len(insieme)
    
def find_selector(radice,selettore):
    insieme=set()
    if radice.tag!='_text_':
        if selettore[0]=='#':
            if 'id' in radice.attr:
                if radice.attr['id'] == selettore[1:]:
                    insieme.add(radice)
        elif selettore[0]=='.':
            if 'class' in radice.attr:
                if selettore[1:] in radice.attr['class']:
                    insieme.add(radice)
        elif selettore[0]=='@':
            attributo=selettore[2:selettore.find('=')]
            valore=selettore[selettore.find('=')+2:-2]
            if attributo in radice.attr:
                if radice.attr[attributo] == valore:
                    insieme.add(radice)
        elif radice.tag==selettore:
            insieme.add(radice)
        for figlio in radice.content:
            insieme.update(find_selector(figlio,selettore))
    return insieme

def elimina_nodi(fileIn, selettore, fileOut):
    radice=fparse(fileIn)
    insieme=find_selector(radice,selettore)
    for elementi in insieme:
        elimina_nodo(elementi)
    with open(fileOut,'w') as f:
        f.write(radice.to_string())

def elimina_nodo(elementi):
    for figlio in elementi.content:
        elimina_nodo(figlio)
    del (elementi)

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    radice=fparse(fileIn)
    insieme=find_selector(radice,selettore)
    for elemento in insieme:
        elemento.attr[chiave]=valore
    with open(fileOut,'w') as f:
        f.write(radice.to_string())





    
    
#conta_nodi('page1-3.html', 'p')
