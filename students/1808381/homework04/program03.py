# -*- coding: ISO-8859-1 -*-
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
    file = fparse(fileIn)
    ris1 = alberi.findSelector(file, selettore)
    return ris1

    
    
    
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    doc = fparse(fileIn)
    alberi.removeTag(doc, selettore)
    with open(fileOut,'w') as f: f.write(doc.to_string())
    
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''

    doc = fparse(fileIn)
    a = selettore.split(' ')
    discendente = a[1]
    avo = a[0]
    for x in alberi.find_by_tag(doc, avo):
        for y in alberi.find_by_tag(x, discendente):
            dizio = y.attr
            dizio[chiave] = valore
    with open(fileOut,'w') as f: f.write(doc.to_string())


class alberi:
    
    def __init__(self, tag, attr, content, closed=True):
        
        self.tag = tag
        self.attr = attr
        self.content = content
        self.closed = closed

    def findSelector(albero, tag):
        '''Ritorna il numero dei nodi che hanno il tag''' 

        result = 0
        
        if tag[0] != '.' and tag[0] != '#'  and tag[0] != '@' and ' ' not in tag and '>' not in tag:
            if albero.tag == tag: 
                result += 1
            if albero.tag != '_text_':
                for figlio in albero.content:
                    
                    result += alberi.findSelector(figlio,tag)      
       
        elif albero.tag != '_text_' and ' ' not in tag and '>' not in tag:
            if tag[0] == '@': 
                tag = tag[2:-1]
            else:
                tag = tag[1:]
            for figlio in albero.content:
                if tag in figlio.to_string():
                    result += 1
                alberi.findSelector(figlio, tag)
                
        elif ' ' in tag and '>' not in tag:
            a = tag.split(' ')
            
            avo = a[0]
            discendente = '<'+a[1]
            for nodo in alberi.find_by_tag(albero, avo):
                b = nodo.to_string()
                if discendente in b:
                    result += 1
                                       
        elif '>' in tag:
            a = tag.split(' > ')
            padre = a[0]
            figlio = a[1]
            
            for nodo in alberi.find_by_tag(albero, padre):
                for el in nodo.content:
                    if el.tag != '_text_':
                        if figlio == el.tag:
                            result += 1
                        break
        return result

    def find_by_tag(nodo, tag):
        '''Ritorna una lista dei nodi che hanno il tag''' 
        ret = []
        if nodo.tag == tag: ret += [nodo]
        if nodo.tag!='_text_':
            for figlio in nodo.content:
                ret += alberi.find_by_tag(figlio,tag)
        return ret
    
    
    def removeTag(nodo, tag):
        '''Rimuove dall'albero tutti i nodi con il tag, esclusa la radice, cioè il nodo su cui è invocato il metodo.'''
        
        a = tag.split(' ')
        discendente = a[1]
        avo = a[0]
        newcontent = []
        for x in alberi.find_by_tag(nodo, avo):           
            alberi.remove(x, discendente)
        
        
    def remove(nodo,tag):
        
        if nodo.tag=='_text_': return
        for figlio in nodo.content:
            alberi.remove(figlio,tag)
        newcontent = []
        for figlio in nodo.content:
            
            if figlio.tag == tag:
                if nodo.tag!='_text_':
                    newcontent += ''
            else:
                newcontent += [figlio]
        nodo.content = newcontent
                
                
if __name__ == '__main__':
    elimina_nodi('page1-3.html', 'p a', 'ciao.html')
