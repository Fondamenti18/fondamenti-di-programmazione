
'''
Un documento HTML puÃ² essere rappresentato sotto forma di albero, come visto a lezione, che si chiama DOM (Document Object Model).

Un qualsiasi nodo di questo albero puÃ² essere individuato sulla base delle proprie caratteristiche:
    - tag                       un tag del tipo indicato
    - .classe                   una delle parole presenti nel valore dell'attributo "class"
    - #id                       il valore dell'attributo "id"
    - @[attributo="valore"]     valore di un attributo generico
ed in base alla sua relazione con i tag che lo contengono:
    - avo discendente           il tag 'avo' contiene un tag 'discendente' a qualsiasi profonditÃ 
    - padre > figlio            il tag 'padre' contiene il tag 'figlio' nel livello immediatamente sotto

Un selettore CSS Ã¨ una successione di selettori di tag separati da spazio che serve ad individuare uno o piÃ¹ nodi all'interno del DOM.
Esempio:
    div .class1 > #main_window
        seleziona un qualsiasi tag che ha                                       id="main_window"
        Ã¨ il figlio di un tag che ha                                            class="... class1 ..."
        e si trova all'interno (a qualsiasi livello di distanza) di un tag      div
Esempio2:
    p  table > tr > td > a
	seleziona un link (<a ...> </a>)
	figlio di una casella (<td> ... </td>)
	figlia di una riga (<tr> ... </tr>)
	figlia di una tabella (<table> ... </table>)
	contenuta a qualsiasi livello in un paragrafo (<p> .... </p>)

NOTA: questa definizione del CSS Ã¨ una versione ridottissima che non segue lo standard completo. 
In particolare, non Ã¨ possibile usare piÃ¹ relazioni '>' consecutive o costruire selettori alternativi (in OR) e selettori in AND.

Le modifiche da attuare su un DOM possono essere di 3 tipi:
    - conteggio dei nodi che soddisfano il selettore CSS
    - eliminazione di tutti i tag individuati da un selettore CSS
    - modifica degli attributi di tutti i tag individuati da un selettore CSS

Realizzate le funzioni che esplorano e modificano l'albero:
    conta_nodi(       fileIn, selettore)				
    elimina_nodi(       fileIn, selettore, fileOut)				
    cambia_attributo(	fileIn, selettore, chiave, valore, fileOut)

ATTENZIONE: nei test verrÃ  utilizzato un timout globale di 1*N secondi (se il grader fa N test)
'''

from  my_html import HTMLNode, fparse

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''

    albero = fparse(fileIn)
    risultato = ricerca(albero, selettore)    
    return risultato

    
    
    
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''

    
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    albero = fparse(fileIn)
    lista = selettore.split(' ')
    elemento1 = lista[1]
    elemento = lista[0]
    controllo_text=True if albero.tag!='_text_' else False
    lista1=ricercaAvi(albero,elemento,controllo_text)
    for x in lista1:
        lista2=ricercaAvi(x,elemento1,controllo_text)
        for y in lista2:       
            dizionario = y.attr                     
            dizionario[chiave] = valore            
    with open(fileOut,'w') as file:
        file.write(albero.to_string())




def ricerca(nodo, selettore):
    risultato = 0
    controllo_punto= True if selettore[0] != '.' else False
    controllo_valore=True if selettore[0]!='#' else False
    controllo_valore_generico=True if selettore[0]!='@' else False
    controllo_discendenza=True if ' ' not in selettore else False
    controllo_padre_figlio=True if '>' not in selettore else False
    controllo_text=True if nodo.tag!='_text_' else False
    
    if  controllo_valore   and controllo_discendenza and  controllo_punto and controllo_padre_figlio and controllo_valore_generico:
        if nodo.tag==selettore:
           risultato+=1
        if controllo_text:
           for figlio in nodo.content:

               risultato += ricerca(figlio,selettore)
       
    
                
    elif not controllo_padre_figlio and not  controllo_discendenza :   
            lista = selettore.split(' ')
            if not controllo_padre_figlio:
            
                discendente = '<'+lista[1]
                avo = lista[0] 
                lista=ricercaAvi(nodo, avo,controllo_text)
                for nodo in lista:
                    if discendente in nodo.to_string():
                    
                        risultato += 1
                    
                    
    elif controllo_text:
        if   controllo_padre_figlio and controllo_discendenza:
        
            if selettore[0] == '@':
                selettore = selettore[2:-1]
            else:
                selettore= selettore[1:]
                for figlio in nodo.content:
                    if selettore in figlio.to_string():   
                        risultato += 1
                        risultato+=ricerca(figlio, selettore)    
    elif controllo_padre_figlio  and (not controllo_text   and not controllo_discendenza):
        lista = selettore.split(' > ')
        figlio = lista[1]
        lista1=ricercaAvi(nodo,selettore,controllo_text)    
        for nodi in lista1:
            for el in nodi.content:
                if el.tag != '_text_':
                    if figlio == el.tag:
                        risultato += 1
                        break
    return risultato

def ricercaAvi(nodo, tag,controllo_text):
        controllo_text=True if nodo.tag!='_text_' else False
        lista = []
        if nodo.tag == tag:
            lista += [nodo]
        if controllo_text:
            for figlio in nodo.content:
                lista +=ricercaAvi(figlio,tag,controllo_text)
        return lista
    
    
    
