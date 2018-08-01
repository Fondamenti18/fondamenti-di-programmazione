'''
Un documento HTML può essere rappresentato sotto forma di albero, come visto a lezione, che si chiama DOM (Document Object Model).

Un qualsiasi nodo di questo albero può essere individuato sulla base delle proprie caratteristiche:
    - tag                       un tag del tipo indicato
    - .classe                   una delle parole presenti nel valore dell'attributo "class"
    - #id                       il valore dell'attributo "id"
    - @[attributo="valore"]     valore di un attributo generico
ed in base alla sua relazione con i tag che lo contengono:
    - avo discendente           il tag 'avo' contiene un tag 'discendente' a qualsiasi profondità
    - padre > figlio            il tag 'padre' contiene il tag 'figlio' nel livello immediatamente sotto

Un selettore CSS è una successione di selettori di tag separati da spazio che serve ad individuare uno o più nodi all'interno del DOM.
Esempio:
    div .class1 > #main_window
        seleziona un qualsiasi tag che ha                                       id="main_window"
        è il figlio di un tag che ha                                            class="... class1 ..."
        e si trova all'interno (a qualsiasi livello di distanza) di un tag      div
Esempio2:
    p  table > tr > td > a
	seleziona un link (<a ...> </a>)
	figlio di una casella (<td> ... </td>)
	figlia di una riga (<tr> ... </tr>)
	figlia di una tabella (<table> ... </table>)
	contenuta a qualsiasi livello in un paragrafo (<p> .... </p>)

NOTA: questa definizione del CSS è una versione ridottissima che non segue lo standard completo. 
In particolare, non è possibile usare più relazioni '>' consecutive o costruire selettori alternativi (in OR) e selettori in AND.

Le modifiche da attuare su un DOM possono essere di 3 tipi:
    - conteggio dei nodi che soddisfano il selettore CSS
    - eliminazione di tutti i tag individuati da un selettore CSS
    - modifica degli attributi di tutti i tag individuati da un selettore CSS

Realizzate le funzioni che esplorano e modificano l'albero:
    conta_nodi(       fileIn, selettore)				
    elimina_nodi(       fileIn, selettore, fileOut)				
    cambia_attributo(	fileIn, selettore, chiave, valore, fileOut)

ATTENZIONE: nei test verrà utilizzato un timout globale di 1*N secondi (se il grader fa N test)
'''

from  my_html import HTMLNode, fparse



def cercatutto(node,tag):
    ret = []
    if node.tag == tag:
        ret+= [node]
    if not node.istext():
        for child in node.content:
            ret +=cercatutto(child,tag)
    return ret


def find_by_tag(node, tag):
    ret = []
    if node.tag == tag:
        ret+= [node]
    else:
        for x in node.attr:
            if tag in node.attr[x]:
                ret+=[node]
    if not node.istext():
        for child in node.content:
            ret+=find_by_tag(child,tag)
    return ret



def cerca_att_val(node,tag):
    ret = []
    ls=''
    for x in node.attr:
        ls=x+'='+'"'+node.attr[x]+'"'
        if tag==ls:
            ret+=[node]
    if not node.istext():
        for child in node.content:
            ret+=cerca_att_val(child,tag)
    return ret



def rel_padre_figlio(node,padre,figlio):
    ret = []
    if not node.istext():
        for child in node.content:
            if node.tag==padre:
                if child.tag==figlio:
                    ret+=[node]
            ret+=rel_padre_figlio(child,padre,figlio)
    return ret



def avo(node,padre,figlio):
    ret = []
    if node.tag == padre:
        if not node.istext():
            for child in node.content:
                if child.tag==figlio:
                    ret+=[node]
                ret+=avo(child,child.tag,figlio)
    else:
        if not node.istext():
            for child in node.content:
                ret+=avo(child,padre,figlio)
    
    return ret



    

def conta_nodi(fileIn, selettore):
    doc=fparse(fileIn)
    count=0
    talpa=''
    c=0
    d=0
    padre=''
    figlio=''
    if selettore[0]=='#':
        talpa='id'
        selettore=selettore[1:]
    if selettore[0]=='.':
        talpa='class'
        selettore=selettore[1:]
    if selettore[0]=='@':
        c=1
        talpa='@'
        selettore=selettore[2:-1]
    if '>' in selettore:
        c=2
        talpa='>'
        for x in selettore:
            if d==0:
                if x!='>':
                    if x.isalpha()==True:
                        padre+=x
                else:
                    d=1
            else:
                if x.isalpha()==True:
                    figlio+=x
    
    else:
        if '>' not in selettore and ' ' in selettore:
            c=3
            talpa='>'
            for x in selettore:
                if d==0:
                    if x!=' ':
                        if x.isalpha()==True:
                            padre+=x
                    else:
                        d=1
                else:
                    if x.isalpha()==True:
                        figlio+=x
            

    if talpa=='':
        for node in cercatutto(doc,selettore):
            count+=1
    elif c==1:
        for node in cerca_att_val(doc,selettore):
            count+=1
    elif c==2:
        for node in rel_padre_figlio(doc,padre,figlio):
            count+=1
    elif c==3:
        for node in avo(doc,padre,figlio):
            count+=1
    else:
        for node in find_by_tag(doc,selettore):
            count+=1

    return count

def remove_by_tag(node, tag):
    if node.istext(): return
    for child in node.content:
        remove_by_tag(child,tag)
    newcont = []
    for child in node.content:
        if child.tag == tag:    
            newcont +=''
        else:
            newcont +=[child]
    node.content = newcont
            
def elimina_nodi(fileIn, selettore, fileOut):
    doc=fparse(fileIn)
    sel=''
    c=0
    if ' ' in selettore:
        for x in selettore:
            if c!=1:
                if x==' ':
                    c=1
            else:
                sel+=x            
    remove_by_tag(doc,sel)
    Html_file=open(fileOut,"w")
    Html_file.write(doc.to_string())
    Html_file.close()


def change_attr(node,padre,figlio,chiave,valore):
    ret = []
    if node.tag == padre:
        if not node.istext():
            for child in node.content:
                if child.tag==figlio:
                    ret+=[node]
                    child.attr[chiave]=valore
                ret+=change_attr(child,child.tag,figlio,chiave,valore)
    else:
        if not node.istext():
            for child in node.content:
                ret+=change_attr(child,padre,figlio,chiave,valore)
    
    return ret

    
def change_att_by_id(node,tag,chiave,valore):
    ret = []
    diz={}
    diz=node.attr.copy()
    for x in diz:
        if tag in diz[x]:
            ret+=[node]
            node.attr[chiave]=valore
    if not node.istext():
        for child in node.content:
            ret+=change_att_by_id(child,tag,chiave,valore)
    return ret
    

   
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    doc=fparse(fileIn)
    d=0
    talpa=''
    count=0
    padre=''
    figlio=''
    if '#' in selettore:
        selettore=selettore[1:]
        talpa='id'
    else:
        for x in selettore:
            if d==0:
                if x!=' ':
                    if x.isalpha()==True:
                        padre+=x
                else:
                    d=1
            else:
                if x.isalpha()==True:
                    figlio+=x
    if talpa=='':
        for node in change_attr(doc,padre,figlio,chiave,valore):
            count+=1
    else:
        for node in change_att_by_id(doc,selettore,chiave,valore):
            count+=1
    Html_file=open(fileOut,"w")
    Html_file.write(doc.to_string())
    Html_file.close()









    
