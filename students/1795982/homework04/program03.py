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


def cerca(selettore,alb,nodi):
    if not alb.istext():
        c=alb.content
        if selettore[0]=='.':
            for x in c:
                if 'class' in x.attr:
                    if selettore[1:]in x.attr['class']:
                        nodi+=[x]
        elif selettore[0]=='#':
            for x in c:
                if 'id' in x.attr:
                    if x.attr['id']==selettore[1:]:
                        nodi+=[x]
        elif selettore.isalpha():
            for x in c:
                if x.tag==selettore:
                    nodi+=[x]
        elif selettore[0]=='@':
            attributo=''
            valore=''
            for y in selettore:
                for d in y:
                    if d.isalpha():
                        attributo+=d
                    if d.isnumeric():
                        valore+=d
            for x in c:
                if attributo in x.attr:
                    if x.attr[attributo]==valore:
                        nodi+=[x]
        for x in c:
            cerca(selettore,x,nodi)
    return nodi
        
    
def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    alb=fparse(fileIn)
    nodi=[]
    cerca(selettore,alb,nodi)
    return len(nodi)
    
        
def elimina(selettore,alb):
    if not alb.istext():
        c=alb.content
        if selettore[0]=='.':
            for x in c:
                if 'class' in x.attr:
                    if selettore[1:]in x.attr['class']:
                        del(x)
        elif selettore[0]=='#':
            for x in c:
                if 'id' in x.attr:
                    if x.attr['id']==selettore[1:]:
                        del(x)
        elif selettore.isalpha():
            for x in c:
                if x.tag==selettore:
                    del(x)
        elif selettore[0]=='@':
            attributo=''
            valore=''
            for y in selettore:
                for d in y:
                    if d.isalpha():
                        attributo+=d
                    if d.isnumeric():
                        valore+=d
            for x in c:
                if attributo in x.attr:
                    if x.attr[attributo]==valore:
                        del(x)
        for x in c:
            elimina(selettore,x)
    return alb
        

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    alb=fparse(fileIn)
    elimina(selettore,alb)
    ris=alb.to_string()
    with open(fileOut,'w') as out:
        out.write(ris)
    
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

