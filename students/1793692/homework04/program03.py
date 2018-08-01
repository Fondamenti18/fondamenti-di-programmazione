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
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    doc=fparse(fileIn)
    selettori=selettore.split(' ')
    if len(selettori)==1 and tiposelettoreid(selettori[0]):
        return conta_attr_singolo(doc,selettori)
    if len(selettori)==1 and not tiposelettoreid(selettori[0]):
        return conta_tag_singolo(doc,selettori)
    if len(selettori)>1 and '>' in selettori:
        return conta_padre_figlio(doc,selettori)
    if len(selettori)>1 and '>' not in selettori:
        return conta_avo_discendente(doc,selettori)

    
def conta_attr_singolo(doc,selettori):
    for x in selettori:
        if tiposelettoreid(x):
            sel=tipoid(x)
            return (len(conta_attr(doc,sel)))
def conta_tag_singolo(doc,selettori):
    return len(conta_tag(doc, selettori[0]))

def conta_padre_figlio(doc,selettori):
    p=None
    return len(conta_pf(doc,selettori[2],selettori[0],p))
def conta_avo_discendente(doc,selettori):
    p=None
    return len(conta_ad(doc,selettori[1],selettori[0],p))        
    
def conta_attr(nodo, attributo):
    ret = []
    if attributo[0] in nodo.attr.keys():
        if attributo[1] in nodo.attr[attributo[0]]:
            ret += [nodo.attr[attributo[0]]]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret += conta_attr(figlio,attributo)
    return ret
def conta_tag(nodo, tag):
    ret = []
    if nodo.tag == tag: ret += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret += conta_tag(figlio,tag)
    return ret
def conta_pf(nodo, tag, padre,p):
    ret = []
    if nodo.tag == tag:
        if p==padre:
            ret += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            p=nodo.tag
            ret += conta_pf(figlio,tag,padre,p)
    return ret
def conta_ad(nodo, tag, avo,p):
    ret = []
    if nodo.tag == tag:
        if p==avo:
            ret += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            if nodo.tag==avo:
                p=nodo.tag
            ret += conta_ad(figlio,tag,avo,p)
    return ret
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    doc=fparse(fileIn)
    selettori=selettore.split(' ')
    if len(selettori)>1 and '>' not in selettori:
        elimina_avo_discendente(doc,selettori)
        with open(fileOut,'w',encoding='utf-8') as f:
            f.write(doc.to_string())
    
def elimina_avo_discendente(doc,selettori):
    rimuovi_tag(doc,selettori[1])
def rimuovi_tag(nodo, tag):
    if nodo.tag=='_text_': return
    for figlio in nodo.content:
        rimuovi_tag(figlio,tag)
    newcontent = []
    for figlio in nodo.content:
        if figlio.tag == tag:
            if nodo.tag!='_text_':
                pass
        else:
            newcontent += [figlio]
    nodo.content = newcontent

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    doc=fparse(fileIn)
    selettori=selettore.split(' ')
    if len(selettori)>1 and '>' not in selettori:
        cambia_avo_discendente(doc,selettori,chiave,valore)
        with open(fileOut,'w',encoding='utf-8') as f:
            f.write(doc.to_string())
    if len(selettori)==1 and tiposelettoreid(selettori[0]):
        cambia_attr_singolo(doc,selettori, chiave, valore)
        with open(fileOut,'w',encoding='utf-8') as f:
            f.write(doc.to_string())
    
def cambia_avo_discendente(doc,selettori,chiave,valore):
    p=None
    cambia_ad(doc,selettori[1],selettori[0],p,chiave,valore)
def cambia_attr_singolo(doc,selettori, chiave, valore):
    for x in selettori:
        if tiposelettoreid(x):
            sel=tipoid(x)
            cambia_attr(doc,sel, chiave, valore)
def cambia_ad(nodo, tag, avo,p,chiave,valore):
    ret = []
    if nodo.tag == tag:
        if p==avo:
            nodo.attr[chiave]=valore
            ret += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            if nodo.tag==avo:
                p=nodo.tag
            ret += cambia_ad(figlio,tag,avo,p,chiave,valore)
    return ret  
def cambia_attr(nodo, attributo, chiave, valore):
    ret = []
    if attributo[0] in nodo.attr.keys():
        if attributo[1] in nodo.attr[attributo[0]]:
            nodo.attr[chiave]=valore
            ret += [nodo.attr[attributo[0]]]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret += cambia_attr(figlio,attributo, chiave, valore)
    return ret  


def tiposelettoreid(selettore):
    if '#' in selettore or '.' in selettore or '@' in selettore:
        return True
    return False
def tipoid(selettore):
    if '#' in selettore:
        return ['id',selettore.replace('#','')]
    if '.' in selettore:
        return ['class',selettore.replace('.','')]
    if '@' in selettore:
        selettore=selettore.replace('@','')
        selettore=selettore.replace('[','')
        selettore=selettore.replace(']','')
        selettore=selettore.replace('"','')
        return selettore.split('=')
