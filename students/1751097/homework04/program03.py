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

from my_html import HTMLNode, fparse


def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    doc = fparse(fileIn)

    #print(doc.to_string())
    
    # richiamo la funzione ricorsiva
    lista_nodi=set(conta_selettore(doc, selettore))
    print(len(lista_nodi))
    return len(lista_nodi)
    
    
 
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    doc = fparse(fileIn)
    # la conta selettore torna la lista dei nodi coinvolti in tutto l albero.
    lista_nodi_cancellare = conta_selettore(doc, selettore)
    
    # richiamo la funzione ricorsiva di eliminazione.
    elimina_selettore(doc, lista_nodi_cancellare)
    # scrivo il nuovo file DOM
    with open(fileOut, 'w', encoding = 'utf8') as f: f.write(doc.to_string())    
    
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    doc = fparse(fileIn)
    
    lista_nodi_modificare = conta_selettore(doc, selettore)
    # richiamo la funzione ricorsiva
    cambia_selettore(doc, chiave, valore, lista_nodi_modificare)
    # scrivo il nuovo file DOM
    with open(fileOut, 'w', encoding = 'utf8') as f: f.write(doc.to_string())    
    

''' ========================================================
Funzioni globali
    ======================================================== '''

'''
Funzione basica di controllo selettore
torna una lista di nodi che soddisfano la regola del selettore
es. nel caso dei casi secchi, come attributo, classe, tag, attributo=valore, torna il nodo
nel caso dei "padre figlio" o "padre > avo" torna una lista dei figli/avi coinvolti cosicchè possa
rimuoverli o cambiarli nelle funzioni 2  e 3 dell'esercizio 
'''
def check_selector(node, selettore):
    
    if '>' in selettore: # sto condizione padre > figlio
        # me ricavo padre e figlio.
        selettore = selettore.split(' > ')
        selettore_padre = selettore[0]
        selettore_figlio = selettore[1]
        padre_trovato = check_selector(node, selettore_padre)
        
        lista_trovati = []
        if padre_trovato and padre_trovato[0] == node:    
            figli = node.content     # analizzo i figli del nodo padre.
            if figli != '_text_':    # facendo attenzione non siano un nodo text.
                for child in figli:
                    lista_trovati += check_selector(child, selettore_figlio)   # aggiungo alla lista trovati.                   
        
        # Adesso analizzo il terzo selettore.
        # dalla lista_trovati ciclo per ogni nodo e becco se ci sono figli di questo nodo "pipe".
        if lista_trovati and len(selettore) == 3:
            selettore_nipote = selettore[2]
            lista_appoggio = lista_trovati.copy()
            lista_trovati = []
            for nodo in lista_appoggio:
                figli = nodo.content
                if figli != '_text_':
                    for bimbo in figli:
                        lista_trovati += check_selector(bimbo, selettore_nipote)

        return lista_trovati
    
    return check_selector_single(node, selettore)

def check_selector_single(node, selettore):

    ### CASO SELETTORE PADRE AVO ###
    if len(selettore.split()) == 2:    # caso padre - avi.
        selettore_padre, selettore_avo = selettore.split()[0], selettore.split()[1]

        # richiamo se stessa per gestire il caso singolo
        nodo_trovato=check_selector(node, selettore_padre)
        lista_trovati = []
        if nodo_trovato and nodo_trovato[0] == node: # sestesso rispetta il selettore
            # chiamo la funzione che restituisce la lista dei nodi collegati
            lista_trovati=find_by_selector(node, selettore_avo)
        return lista_trovati
    
    ### CASI SELETTORE SINGOLO ###
    elif '#' in selettore: # cerco la chiave negli attributi del nodo
        if node.attr.get('id', None) == selettore[1:]: return [node]  
        return [] #  non soddisfa il selettore per cui torna la lista di nodi vuota. 
    
    elif '.' in selettore:
        value = node.attr.get('class', None)
        if value == None: return []
        if selettore[1:] in value: 
            return [node]
        return []
    
    elif '@' in selettore:         #   @[width="300"]
        selettore=selettore.replace('@[','')
        selettore=selettore.replace(']','').split('=')
        chiave, valore = selettore[0], selettore[1]
        value = node.attr.get(chiave, None)
        if value == None: return []
        if '"'+value+'"' == valore: return [node]
        return []
    
    else:              # caso tag.
        if selettore == node.tag:
            return [node]
        return []

'''
ritorna il numero di nodi che hanno quel selettore
'''
def conta_selettore(node, selettore):
    '''Ritorna il numero di nodi albero di questo nodo'''
    # i nodi toccati me li metto in una lista ret
    ret = []
    ret += check_selector(node, selettore) # richiamo una funzione generia che stabilisce come controllare il selettore
    if node.tag != '_text_':
        for figlio in node.content:
            ret += conta_selettore(figlio, selettore)
    return ret


'''
ritorna il numero di nodi che hanno quel selettore
'''
def elimina_selettore(node, lista_nodi):
    if node.tag == '_text_': return 
    lista_figli = []
    for child in node.content:
        if child not in lista_nodi:
            lista_figli.append(child)
            elimina_selettore(child, lista_nodi)
    node.content = lista_figli
    

'''
Questa funzione ricorsiva cambia i valori passati sul selettore 
'''
def cambia_selettore(node, chiave, valore, lista_nodi):
    '''cambia i nodi con un determinato selettore'''
    if node in lista_nodi:   # devo cambiare gli attr del nodo.
       node.attr[chiave] = str(valore)
    if node.tag != '_text_': 
        for child in node.content:
            cambia_selettore(child, chiave, valore, lista_nodi)    


def find_by_selector(node, selettore):
    '''Ritorna una lista dei nodi che soddisfano il selettore'''
    
    ret = []

    if '#' in selettore: # cerco la chiave negli attributi del nodo
        if node.attr.get('id', None) == selettore[1:]: ret+= [node]  
    
    elif '.' in selettore:
        value = node.attr.get('class', None)
        if value != None: 
            if selettore[1:] in value: ret+= [node]
    
    elif '@' in selettore:         #   @[width="300"]
        selettore=selettore.replace('@[','')
        selettore=selettore.replace(']','').split('=')
        chiave, valore = selettore[0], selettore[1]
        value = node.attr.get(chiave, None)
        if value != None: 
            if '"'+value+'"' == valore: ret+= [node]
    else:              # caso tag.
        if selettore == node.tag: ret += [node]

    if node.tag != '_text_':
        for figlio in node.content:
            ret += find_by_selector(figlio, selettore)
    
    return ret


if __name__ == '__main__':
    fileIn    = 'page1-3.html'
    selettore = '#id1'
    selettore = '#intestazione'
    selettore = 'p'
    selettore = '.title'
    selettore = '@[width="300"]'
    selettore = 'p > em'
    selettore = 'p'
    selettore = 'p > a'
    selettore = 'p a'
    #expected  = 0
    #args      = (fileIn, selettore)
    #ris       = conta_nodi(*args)
    #print(ris)
    
    selettore = 'p a'
    fileIn    = 'page1-3.html'
    fileOut   = 'test9.html'

    #fileIn    = 'slashdot.html'
    #fileOut   = 'test12.html'
    #fileExp   = 'risTest12-3.html'
    #selettore = '@[class="container"] > .main-wrap #firehose > .row strong'

    #ris       = elimina_nodi(fileIn, selettore, fileOut)

    fileIn    = 'page1-3.html'
    fileOut   = 'test10.html'
    fileExp   = 'risTest10-3.html'
    selettore = 'p a'
    chiave    = 'style'
    valore    = 'background-color:red'

    fileIn    = 'python.org.html'
    fileOut   = 'test11.html'
    fileExp   = 'risTest11-3.html'
    selettore = 'p a'
    chiave    = 'style'
    valore    = 'background-color:red'
    #ris       = cambia_attributo(fileIn, selettore, chiave, valore, fileOut)    

    
    fileIn    = 'slashdot.html'
    fileOut   = 'test13.html'
    fileExp   = 'risTest13-3.html'
    selettore = '#slashdot_deals-title'
    chiave    = 'style'
    valore    = 'background-color:red'
    
    #ris       = cambia_attributo(fileIn, selettore, chiave, valore, fileOut)
    
    fileIn    = 'slashdot.html'
    selettore = '@[id="slashboxes"] > article h2 > a'
    expected  = 3
    args      = (fileIn, selettore)
    #ris       = conta_nodi(*args)
    
    fileIn    = 'slashdot.html'
    fileOut   = 'test12.html'
    fileExp   = 'risTest12-3.html'
    selettore = '@[class="container"] > .main-wrap #firehose > .row strong'
    ris       = elimina_nodi(fileIn, selettore, fileOut)