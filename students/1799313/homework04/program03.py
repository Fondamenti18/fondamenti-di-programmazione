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


def search_id(element, tag):
    new_lst = []
    if element.tag == tag:
        new_lst+= [element]
    else:
        for k in element.attr:
            if tag in element.attr[k]:
                new_lst+=[element]
    if not element.istext():
        for fig in element.content:
            new_lst+=search_id(fig,tag)
    return new_lst

def searchvalues(element,tag):
    new_lst = []
    lst=''
    for i in element.attr:
        lst=i +'='+ '"'+ element.attr[i] + '"'
        if tag==lst:
            new_lst+=[element]
    if not element.istext():
        for fig in element.content:
            new_lst+=searchvalues(fig,tag)
    return new_lst


def searchtag(element,tag):
    new_lst = []
    if element.tag == tag:
        new_lst+=[element]
    if not element.istext():
        for fig in element.content:
            new_lst+=searchtag(fig,tag)
    return new_lst



def daddy_son(element,daddy,son):
    new_lst = []
    if not element.istext():
        for fig in element.content:
            if element.tag==daddy:
                if fig.tag==son:
                    new_lst+=[element]
            new_lst+=daddy_son(fig,daddy,son)
    return new_lst



def avocat(element,daddy,son):
    new_lst = []
    if element.tag == daddy:
        if not element.istext():
            for fig in element.content:
                if fig.tag==son:
                    new_lst+=[element]
                new_lst+=avocat(fig,fig.tag,son)
    else:
        if not element.istext():
            for fig in element.content:
                new_lst+=avocat(fig,daddy,son)
    return new_lst


def conta_nodi(fileIn, selettore):
    alb=fparse(fileIn)
    contatore=0
    fox=''
    riconoscitore=0
    di=0
    daddy=''
    son=''
    mod=''
    if selettore[0]=='#':
        fox='id'
        mod=selettore[1:]
    if selettore[0]=='.':
        fox='class'
        mod=selettore[1:]
    if selettore[0]=='@':
        riconoscitore="scelta1"
        fox='@'
        mod=selettore[2:-1]
    if '>' in selettore:
        riconoscitore="scelta2"
        fox='>'
        for o in selettore:
            if di==0:
                if o!='>':
                    if o.isalpha()==1:
                        daddy+=o
                else:
                    di=1
            else:
                if o.isalpha()==1:
                    son+=o
    
    else:
        if '>' not in selettore and ' ' in selettore:
            riconoscitore="scelta3"
            fox='>'
            for o in selettore:
                if di==0:
                    if o!=' ':
                        if o.isalpha()==1:
                            daddy+=o
                    else:
                        di=1
                else:
                    if o.isalpha()==1:
                        son+=o
    if fox=='':
        contatore=len(searchtag(alb,selettore))
    elif riconoscitore=="scelta1":
        contatore=len(searchvalues(alb,mod))
    elif riconoscitore=="scelta2":
        contatore=len(daddy_son(alb,daddy,son))
    elif riconoscitore=="scelta3":
        contatore=len(avocat(alb,daddy,son))
    else:
        contatore=len(search_id(alb,mod))
    return contatore

def rimuoversi_tag(element, tag):
    if element.istext():
        return
    for fig in element.content:
        rimuoversi_tag(fig,tag)
    nuovocont = []
    for fig in element.content:
        if fig.tag == tag:    
            nuovocont +=''
        else:
            nuovocont +=[fig]
    element.content = nuovocont
            
def elimina_nodi(fileIn, selettore, fileOut):
    f=open(fileOut,"w")
    alb=fparse(fileIn)
    select=''
    riconoscitore=0
    if ' ' in selettore:
        for x in selettore:
            if riconoscitore!=1:
                if x==' ':
                    riconoscitore=1
            else:
                select+=x            
    rimuoversi_tag(alb,select)
    f.write(alb.to_string())


def cambiattrib(element,daddy,son,chiave,valore):
    new_lst = []
    if element.tag == daddy:
        if not element.istext():
            for fig in element.content:
                if fig.tag==son:
                    new_lst+=[element]
                    fig.attr[chiave]=valore
                new_lst+=cambiattrib(fig,fig.tag,son,chiave,valore)
    else:
        if not element.istext():
            for fig in element.content:
                new_lst+=cambiattrib(fig,daddy,son,chiave,valore)
    return new_lst

    
def riconoscimenti_att_and_change(element,tag,chiave,valore):
    diz={}
    diz=element.attr.copy()
    new_lst = []
    for x in diz:
        if tag in diz[x]:
            new_lst+=[element]
            element.attr[chiave]=valore
    if not element.istext():
        for fig in element.content:
            new_lst+=riconoscimenti_att_and_change(fig,tag,chiave,valore)
    return new_lst
    

   
def cambia_attributo(fileIn,selettore,chiave,valore,fileOut):
    alb=fparse(fileIn)
    f=open(fileOut,"w")
    di=0
    daddy=''
    fox=''
    contatore=0
    son=''
    if '#' in selettore:
        selettore=selettore[1:]
        fox='id'
    else:
        for i in selettore:
            if di==0:
                if i!=' ':
                    if i.isalpha()==1:
                        daddy+=i
                else:
                    di=1
            else:
                if i.isalpha()==1:
                    son+=i
    
    if fox=='':
        contatore=len(cambiattrib(alb,daddy,son,chiave,valore))
    else:
        contatore=len(riconoscimenti_att_and_change(alb,selettore,chiave,valore))
    f.write(alb.to_string())









    
