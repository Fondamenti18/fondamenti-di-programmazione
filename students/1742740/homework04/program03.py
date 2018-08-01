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

from my_html import HTMLNode, fparse

def conta_nodi(fileIn, selettore): 
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    rad=fparse(fileIn)
    key,a=trova_ts(selettore)
    l=['avo','padre']
    c=0
    if key=='tag':
        c+=count_t(rad,a)
    elif key!='tag' and key not in l:
        c+=count_attr(rad,key,a)
    else:
        if key=='avo':
            a,d=trova_ad(selettore)
            c+=count_avi(rad,a,d)
        elif key=='padre':
            p,f=trova_pf(selettore)
            c+=conta_pf(rad,p,f)
    return c


def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    rad=fparse(fileIn)
    key,a=trova_ts(selettore)
    l = ['avo', 'padre']
    if key=='tag':
        remove_by_tag(rad,a)
    elif key!='tag' and key not in l:
        remove_by_attr(rad,key,a)
    else:
        if key=='avo':
            a, d = trova_ad(selettore)
            remove_by_ancestor(rad,a,d)
        elif key=='padre':
            p,f=trova_pf(selettore)
            remove_by_father(rad,p,f)
    with open(fileOut,'w') as w:
        w.write(rad.to_string())

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    rad=fparse(fileIn)
    key,a=trova_ts(selettore)
    l = ['avo', 'padre']
    if key == 'tag':
        change_by_tag(rad,a,chiave,valore)
    elif key != 'tag' and key not in l:
        change_by_attr(rad,key,a,chiave,valore)
    else:
        if key=='avo':
            a, d = trova_ad(selettore)
            change_by_ancestor(rad,a,d,chiave,valore)
        if key=='padre':
            p, f = trova_pf(selettore)
            change_by_father(rad,p,f,chiave,valore)
    with open(fileOut,'w') as w:
        w.write(rad.to_string())

def modifica_dizionario(diz,chiave,valore): #modifica l'istanza di un dizionario
    diz[chiave]=valore
    return diz

def change_by_attr(nodo,key,att,chiave,valore): #modifica un nodo basandosi sull'attributo 
    diz = nodo.attr
    if key != 'class':
        if key in diz.keys():
            if diz[key] == att:
                diz = nodo.attr
                nodo.attr = modifica_dizionario(diz, chiave, valore)
    else:
        if att in diz.keys():
            diz = nodo.attr
            nodo.attr = modifica_dizionario(diz, chiave, valore)
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            change_by_attr(figlio,key,att,chiave,valore)

def change_by_father(nodo,p,f,chiave,valore):#modifica un nodo basandosi sul rapporto padre>figlio
    if nodo.tag==p:
        if count_pf(nodo,p,f):
            diz = nodo.attr
            nodo.attr = modifica_dizionario(diz, chiave, valore)
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            change_by_father(figlio,p,f,chiave,valore)

def change_by_ancestor(nodo,a,d,chiave,valore):#modifica un nodo basandosi sul rapporto avo>>discendente
    if nodo.tag==d:
        if trova_disc(nodo,d)>0:
            diz = nodo.attr
            nodo.attr = modifica_dizionario(diz, chiave, valore)
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            change_by_ancestor(figlio, a, d, chiave, valore)

def change_by_tag(nodo,tag,chiave,valore):#modifica un nodo basandosi sul tag 
    if nodo.tag==tag:
        diz=nodo.attr
        nodo.attr=modifica_dizionario(diz,chiave,valore)
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            change_by_tag(figlio,tag,chiave,valore)


def remove_by_attr(nodo,chiave,att): #rimuove un nodo basandosi sull'attributo 
    if nodo.tag=='_text_': return
    for node in nodo.content:
        remove_by_attr(node, chiave, att)
    newcont=[]
    diz=nodo.attr
    for node in nodo.content:
        if chiave!='class':
            if chiave in diz.keys():
                if diz[chiave]==att:
                    if not node.tag=='_text_':
                        newcont+=node.content
                else:
                    newcont += [node]
            else:
                newcont+=[node]
        else:
            if att in diz.keys():
                if not node.tag=='_text_':
                    newcont += node.content
            else:
                newcont += [node]
    nodo.content = newcont

def remove_by_father(nodo,p,f): #rimuove un nodo basandosi sul rapporto padre>figlio
    if nodo.tag == '_text_': return
    for node in nodo.content:
        remove_by_father(node, p, f)
    newcont = []
    for node in nodo.content:
        if node.count_pf(node,p,f):
            if not node.tag=='_text_':
                newcont += node.content
        else:
                newcont += [node]
    nodo.content=newcont

def remove_by_ancestor(nodo,a,d): #rimuove un nodo basandosi sul rapporto avo>>discendente
    if nodo.tag == '_text_': return
    for node in nodo.content:
        remove_by_ancestor(node,a,d)
    newcont=[]
    for node in nodo.content:
        if trova_disc(node,d)>0:
            if node.tag == '_text_':
                newcont += node.content
        else:
            newcont += [node]
    nodo.content = newcont


def remove_by_tag(nodo, tag): #rimuove un nodo basandosi sul tag
    if nodo.tag=='_text_': return
    for node in nodo.content:
        remove_by_tag(node, tag)
    newcont=[]
    for node in nodo.content:
        if node.tag == tag:
            if node.tag!='_text_':
                newcont += node.content
        else:
            newcont += [node]
    nodo.content = newcont

def trova_ad(selettore): #se un selettore e' a>>d allora lo divide in avo e discendente
    l=selettore.lstrip().split()
    return l[0],l[1]

def trova_pf(selettore): #se un selettore e' p>f allora lo divide in padre e figlio
    l=selettore.lstrip().split()
    return l[0],l[2]

def conta_pf(nodo,p,f): #funzione che conta il numero di nodi con determinato rapporto p>f
    tot=0
    if count_pf(nodo,p,f):
            tot+=1
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            tot+=conta_pf(figlio,p,f)
    return tot

def count_pf(nodo,p,f): #funzione che indica se un nodo padre p ha tra i suoi figli f
    if nodo.tag==p:
        for i in nodo.content:
            if i.tag==f:
                return True
                break
        return False
    else:
        return False

def count_avi(nodo,avo,disc): #funzione che conta il numero di nodi che hanno rapporto tra avo >> discendente
    tot=0
    if nodo.tag==avo:
        if trova_disc(nodo,disc)>0:
            tot+=1
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            tot+=count_avi(figlio,avo,disc)
    return tot

def trova_disc(nodo,disc): #se questa funzione torna un numero >0 significa che ci sono discendenti nel sottoalbero di avo corrispondenti al discendende da cercare
    t=0
    if nodo.tag==disc:
        t+=1
    else:
        if nodo.tag!='_text_':
            for figlio in nodo.content:
                t+=trova_disc(figlio,disc)
    return t



def count_attr(nodo,key,att): #funzione che conta il numero di nodi con determinato attributo
    tot=0
    diz=nodo.attr
    if key!='class':
        if key in diz.keys():
            if diz[key]==att:
                tot+=1
    else:
        if att in diz.keys():
            tot+=1
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            tot += count_attr(figlio,key,att)
    return tot

def count_t(nodo,sel): #funzione che conta il numero di nodi con determinato tag
    tot = 0
    if nodo.tag==sel:
        tot+=1
    if nodo.tag != '_text_':
        for figlio in nodo.content:
            tot += count_t(figlio,sel)
    return tot

def trova_ts(selettore): #funzione che trova il tipo di selettore
    if selettore[0]=='.':
        return 'class',selettore[1:]
    elif selettore[0]=='#':
        return 'id',selettore[1:]
    elif selettore[0]=='@':
        i=2
        while selettore[i]!='=':
            i+=1
        c=selettore[2:i]
        r=selettore[i+2:len(selettore)-2]
        return c,r
    else:
        l=selettore.split()
        if len(l)==1:
            return 'tag',selettore
        elif len(l)==2:
            return 'avo',l[0]
        else: return 'padre',l[0]
