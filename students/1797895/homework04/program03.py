'''
Un documento HTML può essere rappresentato sotto forma di albero, come visto a lezione, che si chiama DOM (Document Object Model).

Un qualsiasi nodo di questo albero può essere individuato sulla base delle proprie caratteristiche:
    - tag                       un tag del tipo indicato
    - .classe                   una delle parole presenti nel valore dell'attributo "class"
    - #id                       il valore dell'attributo "id"
    - @[attributo="valore"]     valore di un attributo generico
ed in base alla sua relazione con i tag che lo contengono:
    - ova discendente           il tag 'ova' contiene un tag 'discendente' a qualsiasi profondità
    - padre > fiolo            il tag 'padre' contiene il tag 'fiolo' nel livello immediatamente sotto

Un selector CSS è una successione di selettori di tag separati da spazio che serve ad individuare uno o più nodi all'interno del DOM.
Esempio:
    div .class1 > #main_window
        seleziona un qualsiasi tag che ha                                       id="main_window"
        è il fiolo di un tag che ha                                            class="... class1 ..."
        e si trova all'interno (a qualsiasi livello di distanza) di un tag      div
Esempio2:
    p  table > tr > td > a
	seleziona un link (<a ...> </a>)
	fiolo di una casella (<td> ... </td>)
	figlia di una riga (<tr> ... </tr>)
	figlia di una tabella (<table> ... </table>)
	contenuta a qualsiasi livello in un paragrafo (<p> .... </p>)

NOTA: questa definizione del CSS è una versione ridottissima che non segue lo standard completo. 
In particolare, non è possibile usare più relazioni '>' consecutive o costruire selettori alternativi (in OR) e selettori in AND.

Le modifiche da attuare su un DOM possono essere di 3 tipi:
    - conteggio dei nodi che soddisfano il selector CSS
    - eliminazione di tutti i tag individuati da un selector CSS
    - modifica degli attributi di tutti i tag individuati da un selector CSS

Realizzate le funzioni che esplorano e modificano l'albero:
    conta_nodi(       fileIn, selector)				
    elimina_nodi(       fileIn, selector, fileOut)				
    cambia_attributo(	fileIn, selector, kiave, valore, fileOut)

ATTENZIONE: nei test verrà utilizzato un timout globale di 1*N secondi (se il grader fa N test)
'''

from  my_html import HTMLNode, fparse


def serchoplus(nodello,tag,millepiedi):
    if nodello.tag == tag:
        millepiedi+=[nodello]
    return millepiedi


def sercho(nodello,tag):
    millepiedi = []
    millepiedi=serchoplus(nodello,tag,millepiedi)
    if not nodello.istext():
        for fijjo in nodello.content:
            millepiedi +=sercho(fijjo,tag)
    return millepiedi



def trovatagplus(millepiedi,nodello,tag):
    for x in nodello.attr:
            if tag in nodello.attr[x]:
                millepiedi+=[nodello]
    return millepiedi



def trovatag(nodello, tag):
    millepiedi = []
    if nodello.tag == tag:
        millepiedi+= [nodello]
    else:
        millepiedi=trovatagplus(millepiedi,nodello,tag)
    if not nodello.istext():
        for fijjo in nodello.content:
            millepiedi+=trovatag(fijjo,tag)
    return millepiedi



def ricval(nodello,tag):
    millepiedi = []
    appoggio=''
    for x in nodello.attr:
        appoggio=x+'='+'"'+nodello.attr[x]+'"'
        if tag==appoggio:
            millepiedi+=[nodello]
    if not nodello.istext():
        for fijjo in nodello.content:
            millepiedi+=ricval(fijjo,tag)
    return millepiedi



def padrefiglio(nodello,padre,fiolo):
    millepiedi = []
    if not nodello.istext():
        for fijjo in nodello.content:
            if nodello.tag==padre:
                if fijjo.tag==fiolo:
                    millepiedi+=[nodello]
            millepiedi+=padrefiglio(fijjo,padre,fiolo)
    return millepiedi



def ova(nodello,padre,fiolo):
    millepiedi = []
    if nodello.tag == padre:
        if not nodello.istext():
            for fijjo in nodello.content:
                if fijjo.tag==fiolo:
                    millepiedi+=[nodello]
                millepiedi+=ova(fijjo,fijjo.tag,fiolo)
    else:
        if not nodello.istext():
            for fijjo in nodello.content:
                millepiedi+=ova(fijjo,padre,fiolo)
    
    return millepiedi

def condizioni(selector,draft,c):
    if selector[0]=='#':
        draft='id'
        selector=selector[1:]
    if selector[0]=='@':
        c=1
        draft='@'
        selector=selector[2:-1]
    if selector[0]=='.':
        draft='class'
        selector=selector[1:]
    return selector,draft,c


def contacount(draft,c,documento,selector,padre,fiolo,count):
    if draft=='':
        for nodello in sercho(documento,selector):
            count+=1
    elif c==1:
        for nodello in ricval(documento,selector):
            count+=1
    elif c==2:
        for nodello in padrefiglio(documento,padre,fiolo):
            count+=1
    elif c==3:
        for nodello in ova(documento,padre,fiolo):
            count+=1
    else:
        for nodello in trovatag(documento,selector):
            count+=1

    return count


def conta_nodi(fileIn, selector):
    documento=fparse(fileIn)
    count=0
    draft=''
    c=0
    d=0
    padre=''
    fiolo=''
    selector,draft,c=condizioni(selector,draft,c)
    if '>' in selector:
        c=2
        draft='>'
        for x in selector:
            if d==0:
                if x!='>':
                    if x.isalpha()==True:
                        padre+=x
                else:
                    d=1
            else:
                if x.isalpha()==True:
                    fiolo+=x
    
    else:
        if '>' not in selector and ' ' in selector:
            c=3
            draft='>'
            for x in selector:
                if d==0:
                    if x!=' ':
                        if x.isalpha()==True:
                            padre+=x
                    else:
                        d=1
                else:
                    if x.isalpha()==True:
                        fiolo+=x
    count=contacount(draft,c,documento,selector,padre,fiolo,count)
    return count

def remove_by_tag(nodello, tag):
    if nodello.istext(): return
    for fijjo in nodello.content:
        remove_by_tag(fijjo,tag)
    newcont = []
    for fijjo in nodello.content:
        if fijjo.tag == tag:    
            newcont +=''
        else:
            newcont +=[fijjo]
    nodello.content = newcont
            
def elimina_nodi(fileIn, selector, fileOut):
    documento=fparse(fileIn)
    sel=''
    c=0
    if ' ' in selector:
        for x in selector:
            if c!=1:
                if x==' ':
                    c=1
            else:
                sel+=x            
    remove_by_tag(documento,sel)
    Html_file=open(fileOut,"w")
    Html_file.write(documento.to_string())
    Html_file.close()


def change_attr(nodello,padre,fiolo,kiave,valore):
    millepiedi = []
    if nodello.tag == padre:
        if not nodello.istext():
            for fijjo in nodello.content:
                if fijjo.tag==fiolo:
                    millepiedi+=[nodello]
                    fijjo.attr[kiave]=valore
                millepiedi+=change_attr(fijjo,fijjo.tag,fiolo,kiave,valore)
    else:
        if not nodello.istext():
            for fijjo in nodello.content:
                millepiedi+=change_attr(fijjo,padre,fiolo,kiave,valore)
    
    return millepiedi

    
def cambioid(nodello,tag,kiave,valore):
    millepiedi = []
    dizzio={}
    dizzio=nodello.attr.copy()
    for x in dizzio:
        if tag in dizzio[x]:
            millepiedi+=[nodello]
            nodello.attr[kiave]=valore
    if not nodello.istext():
        for fijjo in nodello.content:
            millepiedi+=cambioid(fijjo,tag,kiave,valore)
    return millepiedi
    

   
def cambia_attributo(fileIn, selector, kiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selector CSS'''
    documento=fparse(fileIn)
    d=0
    draft=''
    count=0
    padre=''
    fiolo=''
    if '#' in selector:
        selector=selector[1:]
        draft='id'
    else:
        for x in selector:
            if d==0:
                if x!=' ':
                    if x.isalpha()==True:
                        padre+=x
                else:
                    d=1
            else:
                if x.isalpha()==True:
                    fiolo+=x
    if draft=='':
        for nodello in change_attr(documento,padre,fiolo,kiave,valore):
            count+=1
    else:
        for nodello in cambioid(documento,selector,kiave,valore):
            count+=1
    Html_file=open(fileOut,"w")
    Html_file.write(documento.to_string())
    Html_file.close()









    
