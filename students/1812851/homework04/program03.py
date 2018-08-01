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

ATTENZIONE: nei test verrÃ  utilizzato un timout globale di 1*N secondi (se il grader fa N test)

aprire file json
json.load()
nodo.istext()
'''

from  my_html import HTMLNode, fparse

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    fileIn='page1-3.html'
    file=fparse(fileIn)
    risfunz=det_selettore(file,selettore)
    
    return risfunz

def det_selettore(file,selettore): #tag .classe #id  @[attributo="valore"]  avo discendente  padre > figlio  
    ris=None
    risfunz=None
    if '#' in selettore:
        ris='id'
        selettore=selettore[1:]
        risfunz=conta_id(file,selettore,0)
    elif '.' in selettore:
        ris='class'
        selettore=selettore[1:]
        risfunz=conta_class(file,selettore,0)
    elif '@' in selettore:
        ris='attr'
        selettore=selettore[1:] #leva chiocciola
        selettore=str(selettore) 
        selettore=selettore[1:-1]
        selettore=selettore.split('=')
        att=selettore[0]
        val=selettore[1]
        val=val[1:-1]
        #print(att,val)
        risfunz=conta_attr(file,0,att,val)
        
    elif ' ' in selettore and not '>' in selettore:
        ris='avo'
    elif '>' in selettore and ' ' in selettore:
        ris='pafi'
        selettore=selettore.split('>')
        pad=selettore[0]
        fig=selettore[1]
        
    elif ris==None:
        ris='tag'
        risfunz=conta_tag(file,selettore,0)
    return risfunz

def conta_tag(file,x,c):
    #print(file.tag,c)
    if file.tag==x:
        c+=1
    for i in range(len(file.content)):
        if i%2!=0:
            c=conta_tag(file.content[i],x,c)
    return c

def conta_id(file,selettore,c):
    #print(file.tag,c)
    try:
        if selettore in file.attr.values():
            c+=1
    except:
        c=c
    for i in range(len(file.content)):
        #print(file,file.content[i].tag)
        if file.content[i].tag!='_text_':
            c=conta_id(file.content[i],selettore,c)
            
    return c
 
def conta_class(file,selettore,c):
    try:
        #☻print(file.attr)
        if selettore in str(file.attr['class']):
            c+=1
            
    except:
        c=c
   
    for i in range(len(file.content)):
        #print(file,file.content[i].tag)
        if file.content[i].tag!='_text_':
            c=conta_class(file.content[i],selettore,c)
    return c


def conta_attr(file,c,att,val):
    #print(file.tag,file.attr)
    try:
        if val == file.attr[att]:
            c+=1
    except:
        c=c
    for i in range(len(file.content)):
        if file.content[i].tag!='_text_':
            c=conta_attr(file.content[i],c,att,val)
    return c

def conta_padfig(file,c,pad,fig):
    print(file.tag,file.attr)
    for i in range(len(file.content)):
        if file.content[i].tag!='_text_':
            c=conta_padfig(file.content[i],c,pad,fig)
    return c

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

