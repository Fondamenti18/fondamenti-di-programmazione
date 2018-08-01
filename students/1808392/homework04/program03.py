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
import sys
sys.setrecursionlimit = 99999999

def conta_nodi(fileIn, selettore,Doc=None,count=None,tipo=0):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    if Doc is None:
        Doc = fparse(fileIn)
        count=0
    
    for el in Doc.content:
        if not isinstance(el.content, str): # non cerco il testo
            if '>' not in selettore:
                if ' ' in selettore: #avo
                    
                    lst = selettore.split(' ')
                    padre=lst[0]
                    figlio = lst[1]
                    
                    if tipo == 1 and figlio.strip() == el.tag.strip():
                        tipo = 0
                        count +=1
                        
                    else:
                        
                        if padre.strip() == el.tag.strip():
                            tipo = 1
                            
                            
                            
                    if tipo == 1 :      
                        count = conta_nodi(fileIn,selettore,el,count,1)
                    else:
                        count = conta_nodi(fileIn,selettore,el,count)
                    
                elif selettore[0] == '#':
                    if selettore[1:] in el.attr.values():
                        count+= 1
                    count = conta_nodi(fileIn,selettore,el,count)
                    
                elif selettore[0].isalpha(): #tag
                    if selettore == el.tag:
                        count +=1
                    count = conta_nodi(fileIn,selettore,el,count)
                    
                elif selettore[0] == '.':
                    if 'class' in el.attr.keys():
                        if selettore[1:] in el.attr['class']:
                            count +=1
                            
                    count = conta_nodi(fileIn,selettore,el,count)
                    
                elif selettore[0] == '@':
                    lst = selettore[2:-1].split("=")
                    lst[1] = lst[1][1:-1]
                    if lst[0] in el.attr.keys() and lst[1] in el.attr.values():
                        count +=1
                    count = conta_nodi(fileIn,selettore,el,count)
                
                    
            else:
                lst = selettore.split('>')
                padre=lst[0]
                figlio = lst[1]
                
                if tipo == 1 and figlio.strip() == el.tag.strip():
                    count +=1
                    count = conta_nodi(fileIn,selettore,el,count)
                else:
                    
                    if padre.strip() == el.tag.strip():
                        count = conta_nodi(fileIn,selettore,el,count,1)
                    
                count = conta_nodi(fileIn,selettore,el,count)
    
    return count
       


def elimina_nodi(fileIn, selettore, fileOut, Doc=None, string = None, stringDoc = None,tipo=None):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    if Doc is None:
        Doc = fparse(fileIn)
        stringDoc = Doc.to_string()
        string = []

    
    for el in Doc.content:
        if not isinstance(el.content, str): # non cerco il testo
            if '>' not in selettore:
                if ' ' in selettore: #avo
                    
                    lst = selettore.split(' ')
                    padre=lst[0]
                    figlio = lst[1]
                    
                    if tipo == 1 and figlio.strip() == el.tag.strip():
                        tipo = 0
                        string.append(el.to_string)                
                    else:
                        if padre.strip() == el.tag.strip():
                            tipo = 1
                            
                            
                            
                    if tipo == 1 :      
                        elimina_nodi(fileIn,selettore,fileOut,el,string,stringDoc,1)
                    else:
                        elimina_nodi(fileIn,selettore,fileOut,el,string,stringDoc)
                    
                elif selettore[0] == '#':
                    if selettore[1:] in el.attr.values():
                        string.append(el.to_string)
                    elimina_nodi(fileIn,selettore,fileOut,el,string,stringDoc)
                    
                elif selettore[0].isalpha(): #tag
                    if selettore == el.tag:
                        string.append(el.to_string)
                    elimina_nodi(fileIn,selettore,fileOut,el,string,stringDoc)
                    
                elif selettore[0] == '.':
                    if 'class' in el.attr.keys():
                        if selettore[1:] in el.attr['class']:
                            string.append(el.to_string)
                            
                    elimina_nodi(fileIn,selettore,fileOut,el,string,stringDoc)
                    
                elif selettore[0] == '@':
                    lst = selettore[2:-1].split("=")
                    lst[1] = lst[1][1:-1]
                    if lst[0] in el.attr.keys() and lst[1] in el.attr.values():
                        string.append(el.to_string)
                        elimina_nodi(fileIn,selettore,fileOut,el,string,stringDoc)
                
                    
            else:
                lst = selettore.split('>')
                padre=lst[0]
                figlio = lst[1]
                
                if tipo == 1 and figlio.strip() == el.tag.strip():
                    string.append(el.to_string)
                    elimina_nodi(fileIn,selettore,fileOut,el,string,stringDoc)
                else:
                    
                    if padre.strip() == el.tag.strip():elimina_nodi(fileIn,selettore,fileOut,el,string,stringDoc,1)
                    elimina_nodi(fileIn,selettore,fileOut,el,string,stringDoc)
    
    for rim in string:
        b = rim()
        stringDoc = stringDoc.replace(b,'')
        
    with open (fileOut,'w') as f:
        f.write(stringDoc)
    
    return string

    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut,Doc = None,StringDoc = None,tipo=None):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    
    if Doc is None:
        Doc = fparse(fileIn)
        StringDoc = Doc.to_string()
        with open("C:\prova.txt",'w',encoding='utf-8') as f:
            f.write(StringDoc)
    for el in Doc.content:
        if not isinstance(el.content, str): # non cerco il testo
            if '>' not in selettore:
                if ' ' in selettore: #avo
                    
                    lst = selettore.split(' ')
                    padre=lst[0]
                    figlio = lst[1]
                    if tipo == 1 and figlio.strip() == el.tag.strip():
                        el.attr[chiave] = valore
                        if len(el.content) == 1 and str(el.content[0]) == '_text_':
    
                            tipo = 0
                        
                    elif padre.strip() == el.tag.strip():
                        tipo = 1
                            
                            
                            
                    
                    cambia_attributo(fileIn, selettore, chiave, valore, fileOut,el,StringDoc,tipo)
                
                    
                elif selettore[0] == '#':
                    if selettore[1:] in el.attr.values():
                        el.attr[chiave] = valore
                    cambia_attributo(fileIn, selettore, chiave, valore, fileOut,el,StringDoc)
                    
                elif selettore[0].isalpha(): #tag
                    if selettore == el.tag:
                        el.attr[chiave] = valore
                    cambia_attributo(fileIn, selettore, chiave, valore, fileOut,el,StringDoc)
                    
                elif selettore[0] == '.':
                    if 'class' in el.attr.keys():
                        if selettore[1:] in el.attr['class']:
                            el.attr[chiave] = valore
                            
                    cambia_attributo(fileIn, selettore, chiave, valore, fileOut,el,StringDoc)
                    
                elif selettore[0] == '@':
                    lst = selettore[2:-1].split("=")
                    lst[1] = lst[1][1:-1]
                    if lst[0] in el.attr.keys() and lst[1] in el.attr.values():
                        el.attr[chiave] = valore
                    cambia_attributo(fileIn, selettore, chiave, valore, fileOut,el,StringDoc)
                
                    
            else:
                lst = selettore.split('>')
                padre=lst[0]
                figlio = lst[1]
                
                if tipo == 1 and figlio.strip() == el.tag.strip():
                    el.attr[chiave] = valore
                    cambia_attributo(fileIn, selettore, chiave, valore, fileOut,el,StringDoc)
                else:
                    
                    if padre.strip() == el.tag.strip():
                        cambia_attributo(fileIn, selettore, chiave, valore, fileOut,el,StringDoc,1)
                    
                cambia_attributo(fileIn, selettore, chiave, valore, fileOut,el,StringDoc)
    
    StringDoc = Doc.to_string()
    with open(fileOut,'w',encoding='utf8') as f:
        f.write(StringDoc)
        
    return StringDoc
    
