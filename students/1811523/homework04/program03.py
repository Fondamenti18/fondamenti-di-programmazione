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

def find_by_tag(nodo,tag):
    ret=[]
    if nodo.tag==tag:ret+=[nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret+=find_by_tag(figlio,tag)
    return ret

def find_by_tag1(nodo, tag):
    ret=[]
    if nodo.tag==tag:ret+=[nodo]
    if nodo.tag!='_text_':
        if nodo.content[1].tag==tag:
            ret+=find_by_tag(nodo.content[1],tag)
    return ret

def find_by_attr(nodo,attr):
    attr=attr.replace('.','')
    ret=[]
    if attr in nodo.attr:ret+=[nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret+=find_by_attr(figlio,attr)
    return ret

def find_by_av(nodo,attr):
    attr=attr.replace('#','')
    ret=[]
    for k in nodo.attr:
        if nodo.attr[k]==attr:ret+=[nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret+=find_by_av(figlio,attr)
    return ret

def find_by_val(nodo,attr,val):
    ret=[]
    for k in nodo.attr:
        if k==attr and nodo.attr[k]==val:ret+=[nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret+=find_by_val(figlio,attr,val)
    return ret

def remove_by_tag(nodo, tag):
    if nodo.tag=='_text_': return
    for figlio in nodo.content:
        remove_by_tag(figlio,tag)
    newcontent = []
    for figlio in nodo.content:
        if figlio.tag == tag:
            newcontent += []
        else:
            newcontent += [figlio]
    nodo.content = newcontent


def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    nodo=fparse(fileIn)
    c=0
    tag=selettore.split()
    if len(tag)>1:
        if '>' in tag:
            d=tag.count('>')
            i=0
            while d>0:
                i=tag.index('>',i+1)
                t=find_by_tag(nodo,tag[i-1])
                for k in t:
                    t=find_by_tag1(k,tag[i+1])
                    c+=len(t)
                d-=1
        else:
            t=find_by_tag(nodo,tag[0])
            for k in t:
                t=find_by_tag(k,tag[1])
                c+=len(t)
    for k in tag:
        if '.' in k:
            t=find_by_attr(nodo,selettore)
            c+=len(t)
        if '#' in k:
            t=find_by_av(nodo,selettore)
            c+=len(t)
        if '@' in k:
            selettore=k.replace('[','')
            selettore=selettore.replace(']','')
            selettore=selettore.replace('=',' ')
            s=selettore.split()
            attr=s[0]
            val=s[1]
            attr=attr.replace('@','')
            val=val.replace('"','')
            t=find_by_val(nodo,attr,val)
            c+=len(t)
        if k.isalpha():
            t=find_by_tag(nodo,selettore)
            c+=len(t)
    return c

    
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    nodo=fparse(fileIn)
    tag=selettore.split()
    if len(tag)>1:
        if '>' in tag:
            d=tag.count('>')
            i=0
            while d>0:
                i=tag.index('>',i+1)
                t=find_by_tag(nodo,tag[i-1])
                for k in t:
                    remove_by_tag(k, tag[i+1])
                d-=1
        else:
            t=find_by_tag(nodo,tag[0])
            for k in t:
                remove_by_tag(k, tag[1])
                
    for k in tag:
        if '.' in k:
            remove_by_tag(nodo,k.replace('.',''))
        if '#' in k:
            remove_by_tag(nodo,k.replace('#',''))
        if '@' in k:
            selettore=k.replace('[','')
            selettore=selettore.replace(']','')
            selettore=selettore.replace('=',' ')
            s=selettore.split()
            attr=s[0]
            val=s[1]
            attr=attr.replace('@','')
            val=val.replace('"','')
            remove_by_tag(nodo,attr,val)
        if k.isalpha() and len(tag)==1:
            remove_by_tag(nodo,k)
    with open(fileOut,'w') as o:o.write(HTMLNode.to_string(nodo))
    o.close()

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    nodo=fparse(fileIn)
    tag=selettore.split()
    if len(tag)>1:
        if '>' in tag:
            d=tag.count('>')
            i=0
            while d>0:
                i=tag.index('>',i+1)
                t=find_by_tag(nodo,tag[i-1])
                for k in t:
                    t=find_by_tag1(k,tag[i+1])
                d-=1
        else:
            t=find_by_tag(nodo,tag[0])
            for k in t:
                t1=find_by_tag(k,tag[1])
                for k in t1:
                    k.attr[chiave]=valore
    for k in tag:
        if '.' in k:
            t=find_by_attr(nodo,selettore)
            for k in t:
                    k.attr[chiave]=valore
        if '#' in k:
            t=find_by_av(nodo,selettore)
            for k in t:
                    k.attr[chiave]=valore
        if '@' in k:
            selettore=k.replace('[','')
            selettore=selettore.replace(']','')
            selettore=selettore.replace('=',' ')
            s=selettore.split()
            attr=s[0]
            val=s[1]
            attr=attr.replace('@','')
            val=val.replace('"','')
            t=find_by_val(nodo,attr,val)
            for k in t:
                    k.attr[chiave]=valore
        if k.isalpha():
            t=find_by_tag(nodo,selettore)
            for k in t:
                    k.attr[chiave]=valore
    with open(fileOut,'w') as o:o.write(HTMLNode.to_string(nodo))
    o.close()