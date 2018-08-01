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

def trova_tag_nodo(nodo,selettore):
    ins=set()
    if selettore in nodo.tag:
        ins=ins.union(set([nodo]))
    for figlio in nodo.content:
        if type(figlio)!=str:
            ins=ins.union(set(trova_tag_nodo(figlio,selettore)))
    return ins


def trova_attr_id(nodo):
    lista=set()
    if nodo.attr!=[] and 'id' in nodo.attr.keys():
        a=[nodo.attr['id']]
        lista=lista.union(set(a))
    
    for figlio in nodo.content:
        if type(figlio)!=str:
            lista=lista.union(set(list(trova_attr_id(figlio))))
            

    return lista
    
def trova_attr_class(nodo):
    lista=set()
    if nodo.attr!=[] and 'class' in nodo.attr.keys():
        a=[nodo.attr['class']]
        lista=lista.union(set(a))
    
    for figlio in nodo.content:
        if type(figlio)!=str:
            lista=lista.union(set(list(trova_attr_class(figlio))))
            

    return lista

def sel(selettore):
    selettore=selettore[2:len(selettore)-1]
    chiave=''
    for x in selettore:
        if x!='=':
            chiave+=x
        else: break
            
    valore=selettore[len(chiave)+2:len(selettore)-1]
    return chiave,valore

def trova_attr_values(nodo,selettore,lista):
    chiave_sel=sel(selettore)[0]
    valore_sel=sel(selettore)[1]
    if chiave_sel in nodo.attr.keys():       
        if valore_sel in nodo.attr[chiave_sel]:
            lista+=[valore_sel]
            print(lista)
    for figlio in nodo.content:
        if type(figlio)!=str:
            trova_attr_values(figlio,selettore,lista)
            
                   
    return lista
            
    
    
    
def conta_nodi(fileIn, selettore):
    pag=fparse(fileIn)
    
    
    if selettore[0] not in '.#@' and '>' not in selettore:
        lista=[pag]
        selettori=selettore.split()
        lun=len(selettori)
        esito=[]
        cont=0
        for x in range(lun):
            for nodo in lista:
                esito+=list(trova_tag_nodo(nodo,selettori[x]))
                lista.remove(nodo)
            lista+=esito
        for el in lista:
            if selettori[-1] in el.tag:
                cont+=1        
        return cont
        
        
    if '>' in selettore:
        selettori=selettore.split(' > ')
        lista1=list(trova_tag_nodo(pag,selettori[0]))
        cont=0
        for el in lista1:
            for figlio in el.content:
                if selettori[1] in figlio.tag:
                    cont+=1                   
        return cont
    
    if selettore[0] in '#':
        n=[]
        selettore=selettore[1:len(selettore)]
        lista=trova_attr_id(pag)
        return contat(lista,selettore)
    
    if selettore[0] in '.':
        selettore=selettore[1:len(selettore)]
        lista=trova_attr_class(pag)
        return contat(lista,selettore)
    
    if selettore[0] in '@':
        lista=[]
        lista=trova_attr_values(pag,selettore,lista)
        return len(lista)
    
            
    
def contat(lista,selettore):
    c=0
    for el in lista:
        if selettore in el:
            c+=1
    return c
def elimina_nodi(fileIn, selettore,fileOut):

    pag=fparse(fileIn)
    selettori=selettore.split()
    lista=[pag]
    esito=[]
    text=pag.to_string()
    s_out=''
    if selettore[0] not in '.#@' and '>' not in selettore:
        lista=[pag]
        selettori=selettore.split()
        esito=[]
        for x in range(len(selettori)):
            for nodo in lista:
                esito+=list(trova_tag_nodo(nodo,selettori[x]))
                lista.remove(nodo)
            lista+=esito
        for el in lista:
            if selettori[-1] in el.tag and el.to_string() in text:
                l_text=text.split(el.to_string())
                for x in l_text:
                    s_out+=x
                        
        chiusura(fileOut,s_out)
        
    
def chiusura(fileOut,s):
    f=open(fileOut,'w')
    f.write(s)
    f.close()
    
    
    
    
    
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

#pagina=fparse('page1-3.html')
#print(conta_nodi('page1-3.html','p a'))        
        