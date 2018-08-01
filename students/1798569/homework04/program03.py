'''
Un documento HTML può essere rappresentato sotto forma di albero, come visto a lezione, 
che si chiama DOM (Document Object Model).

Un qualsiasi nodo di questo albero può essere individuato sulla base delle proprie 
caratteristiche:
    - tag                       un tag del tipo indicato
    - .classe                   una delle parole presenti nel valore dell'attributo "class"
    - #id                       il valore dell'attributo "id"
    - @[attributo="valore"]     valore di un attributo generico
ed in base alla sua relazione con i tag che lo contengono:
    - avo discendente           il tag 'avo' contiene un tag 'discendente' a qualsiasi 
    profondità
    - padre > figlio            il tag 'padre' contiene il tag 'figlio' nel livello 
    immediatamente sotto

Un selettore CSS è una successione di selettori di tag separati da spazio che serve 
ad individuare uno o più nodi all'interno del DOM.
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
In particolare, non è possibile usare più relazioni '>' consecutive o costruire selettori 
alternativi (in OR) e selettori in AND.

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

def find_by_tag(nodo, tag):
    '''Ritorna una lista dei nodi che hanno il tag'''
    ret = []
    if nodo.tag == tag: ret += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret += find_by_tag(figlio,tag)
    return ret

def find_by_id(nodo, tag):
    '''Ritorna una lista dei nodi che hanno il tag'''
    ret = []
    d=nodo.attr
    if 'id' in d:      
        if d['id'] == tag: 
            ret += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret += find_by_id(figlio,tag)
    return ret


def find_by_class(nodo, tag):
    '''Ritorna una lista dei nodi che hanno il tag'''
    ret = []
    l=[]
    d=nodo.attr
    if 'class' in d: 
        l=d['class'].split()
        for x in l:            
            if x == tag: 
                ret += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret += find_by_class(figlio,tag)
    return ret

def find_by_attr(nodo, tag, tag2):
    '''Ritorna una lista dei nodi che hanno il tag'''
    ret = []
    d=nodo.attr     
    if tag in d: 
        if d[tag]== tag2:         
            ret += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret += find_by_attr(figlio,tag,tag2)
    return ret

def find_by_par(nodo, tag, tag2):
    '''Ritorna una lista dei nodi che hanno il tag'''
    ret = []
    if nodo.tag == tag:
        for x in nodo.content:            
            if tag2 == x.tag:
                ret += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret += find_by_par(figlio,tag, tag2)
    return ret

lista2=[]
cnt=0
def find_by_anc(nodo,tag,tag2):
    global cnt
    global lista2
    cnt=0
    lista=find_by_tag(nodo,tag)
    listaDiz=[]
    dizFin={}
    dizDef={}
    conta=0
    for x in lista:
        listaDiz+=[{}]
        dizFin[x]=gen (listaDiz[conta],x.content,tag2,x)
        conta+=1
    for y in lista2:
        dizDef[y]=dizFin[y]
    return dizDef
    
def gen (dizOut, listaFigli,tag2,y):
    global cnt
    global lista2
    for x in listaFigli:
        if x.tag!='_text_':
            dizOut[x.tag]=x.content
            if x.tag==tag2:
                cnt+=1
                lista2+=[y]
            gen(dizOut, x.content,tag2,y)
    return dizOut
            
            

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    doc= fparse(fileIn)
    if selettore[0].isalpha(): 
        x=selettore.split()
        if len(x)==1:
            return len(find_by_tag(doc,selettore))
        if len(x)==2:
            return len (find_by_anc(doc,x[0],x[1]))
        if len(x)==3:
            return len(find_by_par(doc,x[0],x[2]))
    if selettore[0]=='#':
        return len(find_by_id(doc,selettore[1:]))
    if selettore[0]=='.':
        return len(find_by_class(doc,selettore[1:]))
    if selettore[0]=='@':
        selettore=selettore[2:-1].split('=')
        x=selettore[1]
        selettore[1]=x[1:-1]
        return len(find_by_attr(doc,selettore[0],selettore[1]))

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il 
                                                                         loro contenuto)'''
    doc= fparse(fileIn)
    if selettore[0].isalpha(): 
        x=selettore.split()
        if len(x)==1:
            k = find_by_tag(doc,selettore)
        if len(x)==2:
            k= find_by_anc2(doc,x[0],x[1])
        if len(x)==3:
           k= find_by_par(doc,x[0],x[2])
    if selettore[0]=='#':
        k= find_by_id(doc,selettore[1:])
    if selettore[0]=='.':
        k=find_by_class(doc,selettore[1:])
    if selettore[0]=='@':
        selettore=selettore[2:-1].split('=')
        x=selettore[1]
        selettore[1]=x[1:-1]
        k=find_by_attr(doc,selettore[0],selettore[1])


lista3=[]
cnt2=0
def find_by_anc2(nodo,tag,tag2,chiave, valore, fileOut):
    global cnt2
    global lista3
    cnt2=0
    lista3=[]
    lista=find_by_tag(nodo,tag)
    listaDiz=[]
    dizFin={}
    dizDef={}
    conta=0
    for x in lista:
        listaDiz+=[{}]
        dizFin[x]=gen2 (listaDiz[conta],x.content,tag2,x, chiave, valore, fileOut)
        conta+=1
    for y in lista3:
        dizDef[y]=dizFin[y]
    with open(fileOut,'w',encoding='utf-8') as f:
        f.write(nodo.to_string())
    return dizDef
    
def gen2 (dizOut, listaFigli,tag2,y,chiave, valore, fileOut):
    global cnt2
    global lista3
    for x in listaFigli:
        if x.tag!='_text_':
            dizOut[x.tag]=x.content
            if x.tag==tag2:
                x.attr[chiave]=valore
                #print (x.to_string())
                cnt2+=1
                lista3+=[y]
            gen2(dizOut, x.content,tag2,y,chiave, valore, fileOut)
    return dizOut
            
            

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    doc= fparse(fileIn)
    if selettore[0].isalpha(): 
        x=selettore.split()
        if len(x)==1:
            y= len(find_by_tag(doc,selettore))
        if len(x)==2:
            y= len (find_by_anc2(doc,x[0],x[1],chiave, valore, fileOut))
        if len(x)==3:
            y= len(find_by_par(doc,x[0],x[2]))
    if selettore[0]=='#':
        y= len(find_by_id(doc,selettore[1:]))
    if selettore[0]=='.':
        y= len(find_by_class(doc,selettore[1:]))
    if selettore[0]=='@':
        selettore=selettore[2:-1].split('=')
        x=selettore[1]
        selettore[1]=x[1:-1]
        y= len(find_by_attr(doc,selettore[0],selettore[1],chiave, valore, fileOut))
      

