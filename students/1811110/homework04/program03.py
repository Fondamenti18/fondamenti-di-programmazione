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


def u_tag(tag,fin,node):
    if node.tag == tag:
        fin+= [node]


def faind_all(node,tag):
    fin = []
    u_tag(tag,fin,node)
    if not node.istext():
        for ch in node.content:
            fin +=faind_all(ch,tag)
    return fin







def f_b_t(node,tag,fin):
    if node.tag == tag:
        fin+= [node]
    else:
        for x in node.attr:
            if tag in node.attr[x]:
                fin+=[node]

def cerca_tag(node, tag):
    fin = []
    f_b_t(node,tag,fin)
    if not node.istext():
        for ch in node.content:
            fin+=cerca_tag(ch,tag)
    return fin







def c_a_v(node,ls,tag,fin):
    for x in node.attr:
        ls=x+'='+'"'+node.attr[x]+'"'
        if tag==ls:
            fin+=[node]

def find_av(node,tag):
    fin = []
    ls=''
    c_a_v(node,ls,tag,fin)
    if not node.istext():
        for ch in node.content:
            fin+=find_av(ch,tag)
    return fin




def rico_pf(node,padr,fig,fin):
    for ch in node.content:
            if node.tag==padr:
                if ch.tag==fig:
                    fin+=[node]
            fin+=r_pf(ch,padr,fig)

def r_pf(node,padr,fig):
    fin = []
    if not node.istext():
        rico_pf(node,padr,fig,fin)
    return fin






def if_avo(node,fig,fin):
    if not node.istext():
            for ch in node.content:
                if ch.tag==fig:
                    fin+=[node]
                fin+=rt(ch,ch.tag,fig)
def else_avo(node,fin,padr,fig):
    if not node.istext():
            for ch in node.content:
                fin+=rt(ch,padr,fig)
                
def rt(node,padr,fig):
    fin = []
    a=node.tag
    if node.tag == padr:
        if_avo(node,fig,fin)
    else:
        else_avo(node,fin,padr,fig)
    
    return fin







def del_bt(nco, node, tag):
    for ch in node.content:
        if ch.tag == tag:    
            nco +=''
        else:
            nco +=[ch]
    node.content = nco


def del_tag(node, tag):
    if node.istext():
        return
    for ch in node.content:
        del_tag(ch,tag)
    nco = []
    del_bt(nco, node, tag)
    




    

def cond_delnode(selettore,cond,sel):
    if ' ' in selettore:
        for x in selettore:
            if cond!=1:
                if x==' ':
                    cond=1
            else:
                sel+=x
    return selettore,cond,sel


def elimina_nodi(fileIn, selettore, fileOut):
    dom=fparse(fileIn)
    sel=''
    cond=0
    selettore,cond,sel=cond_delnode(selettore,cond,sel)
    del_tag(dom,sel)
    Html_file=open(fileOut,"w")
    Html_file.write(dom.to_string())
    Html_file.close()
    
    










def if_c_a(ch,fig,fin,node,chiave,val):
    if ch.tag==fig:
        fin+=[node]
        ch.attr[chiave]=val

def cambia_a(node,padr,fig,chiave,val):
    fin = []
    a=node.tag
    if a == padr:
        if not node.istext():
            for ch in node.content:
                if_c_a(ch,fig,fin,node,chiave,val)
                ct=ch.tag
                fin+=cambia_a(ch,ct,fig,chiave,val)
    else:
        if not node.istext():
            for ch in node.content:
                fin+=cambia_a(ch,padr,fig,chiave,val)
    
    return fin






def c_a_b_id_istxt(node,fin,chiave,val,tag):
    if not node.istext():
        for ch in node.content:
            fin+=change_att_by_id(ch,tag,chiave,val)
def cicl_changebyid(diz,tag,fin,chiave,val):
    for x in diz:
        if tag in diz[x]:
            fin+=[node]
            node.attr[chiave]=val
            
def change_att_by_id(node,tag,chiave,val):
    fin = []
    diz={}
    diz=node.attr.copy()
    cicl_changebyid(diz,tag,fin,chiave,val)
    c_a_b_id_istxt(node,fin,chiave,val,tag)
    
    return fin




    


def selett(selettore):
    selett=selettore[1:]
    return selett

def ver(dom, selettore):
    cont = 0
    guardia=''
    if selettore[0]=='#':
        guardia='id'
        selettore=selett(selettore)
    if selettore[0]=='.':
        guardia='class'
        selettore=selett(selettore)
    if selettore[0]=='@':
        guardia='@'
        selettore=selettore[2:-1]
        for node in find_av(dom,selettore):
            cont+=1
    return selettore, guardia, cont


def richiama(guardia,cont,dom,selettore):
    if guardia=='':
        for node in faind_all(dom,selettore):
            cont+=1
    else:
        for node in cerca_tag(dom,selettore):
            cont+=1
    return cont

def conta_nodi(fileIn, selettore):
    dom=fparse(fileIn)
    cond=0
    d=0
    padr=''
    fig=''
    figlio2=''
    nipote=''
    selettore, guardia, cont = ver(dom, selettore)
    if '>' in selettore:
        guardia='>'
        for x in selettore:
            if d==0:
                if x!='>':
                    if x.isalpha()==True:
                        padr+=x
                else:
                    d=1
            else:
                if x.isalpha()==True:
                    fig+=x
                    
        s=1
        for node in r_pf(dom,padr,fig):
            cont+=1
    
    else:
        if '>' not in selettore and ' ' in selettore:
            cond=3
            guardia='>'
            for x in selettore:
                if d==0:
                    if x!=' ':
                        if x.isalpha()==True:
                            padr+=x
                    else:
                        d=1
                else:
                    if x.isalpha()==True:
                        fig+=x
                        
        s=1
        for node in rt(dom,padr,fig):
            cont+=1
            
           
    if s==1:
        cont=richiama(guardia,cont,dom,selettore)
    return cont









def cond_c_a(selettore,d,padr,fig,guardia):
    if '#' in selettore:
        selettore=selett(selettore)
        guardia='id'
    else:
        for x in selettore:
            if d==0:
                if x!=' ':
                    if x.isalpha()==True:
                        padr+=x
                else:
                    d=1
            else:
                if x.isalpha()==True:
                    fig+=x
    return padr,fig,guardia
                    
def cambia_attributo(fileIn, selettore, chiave, val, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    dom=fparse(fileIn)
    d=0
    guardia=''
    cont=0
    padr=''
    fig=''
    padr,fig,guardia=cond_c_a(selettore,d,padr,fig,guardia)
    if guardia=='':
        for node in cambia_a(dom,padr,fig,chiave,val):
            cont+=1
    else:
        for node in change_att_by_id(dom,selettore,chiave,val):
            cont+=1
            
    Html_file=open(fileOut,"w")
    Html_file.write(dom.to_string())
    Html_file.close()







    
