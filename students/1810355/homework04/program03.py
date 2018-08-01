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
import copy


from  my_html import HTMLNode, fparse

def find_by_tag(node): 
    ret= []     
    ret.append(node.tag)
    if not node.istext():         
        for child in node.content:             
            ret+=find_by_tag(child)
    return (ret)

def find_id(node,sel,ret=[]):
         
    nsel=sel[1:]
     
    try:
        if node.attr["id"]==nsel:ret.append(node)
    except:
        KeyError
    if not node.istext():         
        for child in node.content:             
            find_id(child,sel,ret)
   
    return (ret)
def find_class(sel,node,ret=[]):
    
    nsel=sel[1:]
   
    try:
        if nsel in node.attr["class"]:ret.append(node)
    except:
        KeyError                         
    if not node.istext():
        for child in node.content:             
            find_class(sel,child)
        
    
    return (ret)
def find_attributi(sel,node,ret=[]):#semplice conteggio degli attributi
    nsel=sel[1:]
    nsel1=nsel.split("=")
    a=""
    b=""
    a=nsel1[0].translate({ord(c): "" for c in '"!@#$%^&*()[]{};:,./<>?\|`~-=_+'})
    b= nsel1[1].translate({ord(c): "" for c in '"!@#$%^&*()[]{};:,./<>?\|`~-=_+'})
        
   # print(a,b)
    try:
        if node.attr[a]==b:ret.append(node)
    except:
        KeyError
    if not node.istext():
        for child in node.content:
            find_attributi(sel,child)           
    return ret

def padretag(sel,node,ret):
    
    lista=sel.split(">")
    a=lista[0].replace(" ","")
    b=lista[1].replace(" ","")    
    if node.tag==a: 
        for el in node.content:                 
            if b == el.tag  :      
                ret.append(node)
   
    if not node.istext():
        for child in node.content:
            padretag(sel,child,ret)
        
    return ret          
def avo(node,ricerca,lista):
    
    if node.tag==ricerca:
        lista.append(node)
    if not node.istext():
        for child in node.content:
            avo(child,ricerca,lista)
    return lista
def avo2(sel,node,ret):
    lista=sel.split(" ")
    if node.tag==lista[0]:
        a=avo(node,lista[1],[])                
        
        if a!=[]:                                          
            ret.append(a)
    if not node.istext():
        for child in node.content:
            avo2(sel,child,ret)
    flat_list = [item for sublist in ret for item in sublist] 
    return flat_list

def elaboratore(sel,node):
    if sel in find_by_tag(node):
        contatore=0
        for el in find_by_tag(node):
            if el == sel:
                contatore+=1
        return contatore   
    elif sel[0]=="#":
        return len(find_id(node,sel))
    elif sel[0]==".":
       
        return len(find_class(sel,node))
    elif sel[0]=="@":    
       
        return len(find_attributi(sel,node))
    elif ">" in sel:
        if sel.count(">")==1:
            return len(padretag(sel,node,[]))
    elif " " in sel:
        return len(avo2(sel,node,[]))
##############################################################################
def Elimina_Tag(node,tag):
    
    if not node.istext():
        a=copy.copy(node.content)
        for child in node.content:
            if child.tag==tag:
                a.remove(child)
            
    if not node.istext():
      
        for child in node.content:
            Elimina_tag(child,ricerca)
    

def elimina_id(sel,node):
    nsel=sel[1:]
    if not node.istext():
        a=copy.copy(node.content)
        for child in node.content:
            if child.attr["id"]==nsel:
                a.remove(child)
        node.content=a    
    if not node.istext():
      
        for child in node.content:
            elimina_id(sel,child)
def elimina_class(sel,node):
    nsel=sel[1:]
    if not node.istext():
        a=copy.copy(node.content)
        for child in node.content:
            if child.attr["class"]==nsel:
                a.remove(child)
        node.content=a    
    if not node.istext():
      
        for child in node.content:
            elimina_class(sel,child)    
def elimina_attr(sel,node):
    nsel=sel[1:]
    nsel1=nsel.split("=")
    a=""
    b=""
    a=nsel1[0].translate({ord(c): "" for c in '"!@#$%^&*()[]{};:,./<>?\|`~-=_+'})
    b= nsel1[1].translate({ord(c): "" for c in '"!@#$%^&*()[]{};:,./<>?\|`~-=_+'})
    if not node.istext():    
        for child in node.content:
            a=copy.copy(node.content)
            try:
                if node.attr[a]==b:a.remove(child)
            except:
                KeyError
        node.content=a
    if not node.istext():
        for child in node.content:
            elimina_attr(sel,child)           
def Elimina_avo(node,ricerca):
    if not node.istext():
        for child in node.content:
            a=copy.copy(node.content)
            if child.tag==ricerca:               
                a.remove(child)               
            node.content=a      
    if not node.istext():     
        for child in node.content:
            Elimina_avo(child,ricerca)
    
    
    
def Elimina_avo2(sel,node,ret):
    lista=sel.split(" ")       
    if not node.istext():
        if node.tag==lista[0]:
            Elimina_avo(node,lista[1])            
    if not node.istext():
        for child in node.content:
            Elimina_avo2(sel,child,ret)




def padre_figlio(sel,node):
    lista=sel.split(">")
    a=lista[0].replace(" ","")
    b=lista[1].replace(" ","")    
    if not node.istext():
        for child in node.content: 
            if child.tag==a:             
                copia=copy.copy(child.content)
                for el in child.content:                 
                
                    if el.tag==b:      
                        copia.remove(el)
                child.content=copia
    if not node.istext():
        for child in node.content:
            padre_figlio(sel,child)
        
    
           

def elaboratore2(sel,node):
    if sel in find_by_tag(node):
        return elimina_tag(node,sel)
    elif sel.startswith("#") is True:
        return elimina_id(sel,node)
    elif sel.startswith(".") is True: 
        return elimina_class(sel,node)
    elif sel.startswith("@") is True:
        return elimina_attr(sel,node)
                  
    elif ">" in sel:
        return padre_figlio(sel,node)
    elif " " in sel:
        return Elimina_avo2(sel,node,[])
###############################################################################       
def elaboratore3(sel,node,chiave,valore):
    if sel in find_by_tag(node):
        return modifica1(child,chiave,valore,ricerca)
    elif sel.startswith("#") is True:
        return modifica_id(node,chiave,valore,sel)
    elif sel.startswith(".") is True:
        return modifica_class(node,chiave,valore,sel)
    elif sel.startswith("@") is True:
        return modifica_attr(node,chiave,valore,sel)            
    elif " " in sel :
        return modifica2(sel,node,chiave,valore)
        
def modifica1(node,chiave,valore,ricerca):
    if not node.istext():
        for child in node.content:
            if child.tag==ricerca:
                
                try:
                    child.attr[chiave]=valore
                    
                except:
                    KeyError
    if not node.istext():
         for child in node.content:
             modifica1(child,chiave,valore,ricerca)
    
    
def modifica2(sel,node,chiave,valore):
    lista=sel.split(" ")
    if not node.istext():
        if node.tag==lista[0]:
            modifica1(node,chiave,valore,lista[1])
    if not node.istext():
        for child in node.content:
            modifica2(sel,child,chiave,valore)
def modifica_id(node,chiave,valore,ricerca):
    ric=ricerca[1:]
    if not node.istext():
        for child in node.content:
            try:
                if child.attr["id"]==ric:
                                    
                    child.attr[chiave]=valore
                    
            except:
                KeyError
    if not node.istext():
         for child in node.content:
             modifica_id(child,chiave,valore,ricerca)
def modifica_class(node,chiave,valore,ricerca):
    ric=ricerca[1:]
    if not node.istext():
        for child in node.content:
            try:
                if child.attr["class"]==ric:
                                    
                    child.attr[chiave]=valore                    
            except:
                KeyError
    if not node.istext():
         for child in node.content:
             modifica_class(child,chiave,valore,ricerca)
def modifica_attr(node,chiave,valore,ricerca): 
    nsel=ricerca[1:]
    nsel1=nsel.split("=")
    a=""
    b=""
    a=nsel1[0].translate({ord(c): "" for c in '"!@#$%^&*()[]{};:,./<>?\|`~-=_+'})
    b= nsel1[1].translate({ord(c): "" for c in '"!@#$%^&*()[]{};:,./<>?\|`~-=_+'})
    for child in node.content:
            try:
                if child.attr[a]==b:                                    
                    child.attr[chiave]=valore                    
            except:
                KeyError
    if not node.istext():
         for child in node.content:
             modifica_id(child,chiave,valore,ricerca)         
      
 ##################################################################################           

def conta_nodi(fileIn,selettore):    
    g=fparse(fileIn)        
    ty=elaboratore(selettore,g)           
    return ty
    
        
def elimina_nodi(fileIn, selettore, fileOut):
    g=fparse(fileIn)
       
    elaboratore2(selettore,g)        
    with open (fileOut,"w")as f:
        f.write(g.to_string())
        
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    g=fparse(fileIn)
    elaboratore3(selettore,g,chiave,valore)
    with open(fileOut,"w",encoding="utf-8")as f:
        f.write(g.to_string())
