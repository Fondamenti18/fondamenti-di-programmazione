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

def conta_id(nodo, tag, count):
    attributo = nodo.attr
    if('id' in attributo):
        if(attributo['id'] == tag):
            count += 1        
    if not nodo.istext():
        for child in nodo.content:
            count = conta_id(child, tag, count)    
    return(count)


def conta_tag(nodo, tag, count):
    if nodo.tag == tag:
        count += 1
    if not nodo.istext():
        for child in nodo.content:
            count = conta_tag(child, tag, count)
    return(count)
    
    
def conta_attributi(nodo, chiave, valore, count):
    attributo = nodo.attr
    if(chiave in attributo):
        if(attributo[chiave] == valore):
            count += 1        
    if not nodo.istext():
        for child in nodo.content:
            count = conta_attributi(child, chiave, valore, count)    
    return(count)
     
     
def conta_classi(nodo, tag, count):
    attributo = nodo.attr    
    if('class' in attributo):       
        if(tag in attributo['class']):
            
            count += 1        
    if not nodo.istext():
        for child in nodo.content:
            count = conta_classi(child, tag, count)    
    return(count)
    
def conta_padre_figlio(nodo, padre, figlio, count):
    if (nodo.tag == padre):
        for i in nodo.content:           
            if(i.tag == figlio):
                count += 1 
    if not nodo.istext():
        for child in nodo.content:
            count = conta_padre_figlio(child, padre, figlio, count)
    return(count)
    
def conta_avo_discendente(nodo, avo, discendente, count):
    if (nodo.tag == avo):
        for i in nodo.content:
            if(i.tag == discendente):                
                count += 1               
            else:
                if not i.istext():
                    for c in i.content:
                        if(c.tag == discendente):
                            count += 1                    
    if not nodo.istext():     
        for child in nodo.content:
            count = conta_avo_discendente(child, avo, discendente, count)
    return(count)    
    

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    albero = fparse(fileIn)
    count = 0
    if(selettore[0] == '#'):
        selettore = ''.join(selettore[1:])
        count = conta_id(albero, selettore, count)
        
    elif(selettore[0] == '.'): 
        selettore = ''.join(selettore[1:])
        count = conta_classi(albero, selettore, count)
        
    elif(selettore[0] == '@'):
        selettore = ''.join(selettore[2:-1])
        lst = selettore.split('=')
        chiave = lst[0]
        valore = ''.join(lst[1][1:-1])            
        count = conta_attributi(albero, chiave, valore, count)
    
    elif('>' in selettore):
        lst = selettore.split('>')
        padre = lst[0].strip()
        figlio = lst[1].strip()
        count = conta_padre_figlio(albero, padre, figlio, count)
        
    elif(len(selettore) > 1):
        lst = selettore.split()
        avo = lst[0]
        discendente = lst[1]
        count = conta_avo_discendente(albero, avo, discendente, count)
        
    else:
        count = conta_tag(albero, selettore, count)
    return(count)
        

def elimina_tag(nodo, tag):
    if nodo.istext():       #se il nodo è di testo
        return
    lst = []        #inizializzazione lista
    for child in nodo.content:      #scorre contenuto nodo
        if child.tag == tag:        #se il figlio del nodo è uguale al tag
            if not child.istext():      #se il figlio del nodo non è di testo
                lst += child.content        #aggiunge alla lista il contenuto
        else:       #altrimenti
            elimina_tag(child, tag)     #richiama funzione elimina_tag
            lst += [child]      #aggiunge alla lista il figlio
    nodo.content = lst      #contenuto del nodo è uguale alla lista
    return(nodo)        #ritorna il nodo
    
    
def elimina_avo_discendente(nodo, avo, discendente):
    if nodo.istext():       #se il nodo è di testo
        return
    lst = []        #inizializzazione lista
    for child in nodo.content:      #scorre contenuto nodo
        if child.tag == avo:        #se il figlio del nodo è uguale al tag
            if not child.istext():      #se il figlio del nodo non è di testo
                lst += child.content        #aggiunge alla lista il contenuto
        else:       #altrimenti
            elimina_avo_discendente(child, avo, discendente)     #richiama funzione elimina_tag
            lst += [child]      #aggiunge alla lista il figlio
    nodo.content = lst      #contenuto del nodo è uguale alla lista
    return(nodo)        #ritorna il nodo
        
                
def elimina_nodi(fileIn, selettore, fileOut):
    albero = fparse(fileIn)     
    if(len(selettore) > 1):
        lst = selettore.split()
        avo = lst[0]
        discendente = lst[1]
        albero_del = elimina_avo_discendente(albero, avo, discendente)
    #albero.print_tree()
    albero_del = albero_del.to_string() 
    with open (fileOut, 'w', encoding = 'utf8') as f:        
        f.write(albero_del)




def modifica_attr(nodo, avo, discendente, chiave, valore, level=0):
    ''''''


def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    albero = fparse(fileIn)
    if(len(selettore) > 1):
        lst = selettore.split()
        avo = lst[0]
        discendente = lst[1]
        albero_mod = modifica_attr(albero, avo, discendente, chiave, valore)
        
    albero_mod = albero.to_string()
    with open (fileOut, 'w', encoding = 'utf8') as f:        
        f.write(albero_mod)


if __name__ == '__main__':
    #conta_nodi('page1-3.html', 'p a')
    #print(elimina_nodi('page1-3.html', 'p a', 'test9.html'))
    print(cambia_attributo('page1-3.html', 'p a', 'style', 'background-color:red', 'test10.html', ))