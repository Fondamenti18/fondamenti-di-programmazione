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


def match(albero,selettore):
    if selettore.startswith('.'):
        return selettore[1:] in  albero.attr.get('class', '').split(' ')
    elif(selettore.startswith('#')):
         return selettore[1:] == albero.attr.get('id')
    elif(selettore.startswith('@[')):
         k,v = selettore[2:-1].split('=')
         return albero.attr.get(k)==v.strip('"')
    else:
         return albero.tag==selettore
         
    


def cerca(albero,selettori):
    nodi=[]

    if(albero.istext()):
        return nodi

    if ( len(selettori)==1):
         selettore=selettori[0]
         if( match(albero,selettore)):
             nodi.append(albero)
         for figlio in albero.content:
             if(figlio.istext()):
                 continue
             nodi_figlio=cerca(figlio,selettori)
             nodi+=nodi_figlio
         return nodi

    primo,secondo=selettori[0:2]
    if(secondo=='>' and match(albero, primo)):
        terzo=selettori[2]
        for figlio in albero.content:
            if(figlio.tag==terzo and not figlio.istext()):
                nodi+=cerca(figlio,selettori[2:])
    elif(primo[0].isalpha() and secondo[0].isalpha() and albero.tag==primo):
            for figlio in albero.content:
                if(figlio.istext()):
                    continue
                else:
                    nodi+=cerca(figlio,selettori[1:])
    else:
        for figlio in albero.content:
            nodi+=cerca(figlio,selettori)

    return nodi


def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    root = fparse(fileIn)
    lista_selettori=selettore.split()
    return len(cerca(root,lista_selettori))


def bfs(root, delete):
    root.content=[ n for n in root.content if n not in delete]
    for n in root.content:
        if( not n.istext() ):
            bfs(n,delete)
               

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    root = fparse(fileIn)
    lista_selettori=selettore.split()
    lista=set(cerca(root,lista_selettori))
    bfs(root, lista)
    with open(fileOut,'w',encoding='utf8') as t :
        t.write(root.to_string())    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    root = fparse(fileIn)
    lista_selettori=selettore.split()
    lista=set(cerca(root,lista_selettori))

    for n in lista:
        n.attr[chiave]=valore

    with open(fileOut,'w',encoding='utf8') as t :
        t.write(root.to_string())    

        

