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
    root=fparse(fileIn)
    if 0<(2*selettore.count(' > '))<selettore.count(' ') :
        listNodes=mixture(root,selettore.split(' > '))
    else:
        listNodes=findSon(root,selettore.split(' > '),0,[]) if selettore.find('>')!=-1 else findDescendent(root,selettore.split(' '),0,[])
    return len(listNodes)

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    root=fparse(fileIn)
    if 0<(2*selettore.count(' > '))<selettore.count(' ') :
        listNodes=mixture(root,selettore.split(' > '))
    else:
        listNodes=findSon(root,selettore.split(' > '),0,[]) if selettore.find('>')!=-1 else findDescendent(root,selettore.split(' '),0,[])
    delete(root,listNodes)
    with open(fileOut,'w',encoding='utf8') as file:    
        file.write(root.to_string())

        
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    root=fparse(fileIn)
    if 0<(2*selettore.count(' > '))<selettore.count(' ') :
        listNodes=mixture(root,selettore.split(' > '))
    else:
        listNodes=findSon(root,selettore.split(' > '),0,[]) if selettore.find('>')!=-1 else findDescendent(root,selettore.split(' '),0,[])
    for i in listNodes:
        i.attr[chiave]=valore
    with open(fileOut,'w',encoding='utf8') as file:    
        file.write(root.to_string())

def findSon(root,listSelettore,counter,listNodes):
    if root.istext():
        if counter==len(listSelettore)-1 and listSelettore[counter]=='_text_':
            listNodes.append(root)
        return listNodes
    control=check(root,listSelettore[counter])
    if counter!=0 and not(control):
        return listNodes
    else:
        if counter==len(listSelettore)-1 and control:
            listNodes.append(root)
            return listNodes
        else:
            if control:
                for i in root.content:
                    listNodes=findSon(i,listSelettore,counter+1,listNodes)
            else:
                for i in root.content:
                    listNodes=findSon(i,listSelettore,counter,listNodes)
    return listNodes 

def findDescendent(root,listSelettore,counter,listNodes):
    if root.istext():
        if counter==len(listSelettore)-1 and listSelettore[counter]=='_text_':
            listNodes.append(root)
        return listNodes
    control=check(root,listSelettore[counter])
    if counter==len(listSelettore)-1 and control:
        listNodes.append(root)
        return listNodes
    else:
        if control:
            for i in root.content:
                listNodes=findDescendent(i,listSelettore,counter+1,listNodes)
        else:
            for i in root.content:
                listNodes=findDescendent(i,listSelettore,counter,listNodes)
    return listNodes

def mixture(root,listSelettore):
    result=[]
    counter=[]
    for i in range(len(listSelettore)):
        if i==len(listSelettore)-1:
            if 0<(2*listSelettore[i].count(' > '))<listSelettore[i].count(' '):
                listSelettore.append(listSelettore[i][listSelettore[i].find(' ')+3:])
                listSelettore[i]=listSelettore[i][:listSelettore[i].rfind(' ')]
            break
        if listSelettore[i].find(' ')!=-1:
            listSelettore[i-1]+=' > '+listSelettore[i][:listSelettore[i].find(' ')]
            listSelettore[i+1]=listSelettore[i][listSelettore[i].find(' ')+1:]+' > '+listSelettore[i+1]
    for i in listSelettore:
        result.append(findDescendent(root,i.split(' '),0,[])) if i.find(' > ')==-1 else result.append(findSon(root,i.split(' > '),0,[]))
    for i in range(len(result)-1):
        for x in result[i]:
            isPath(x,result[i+1],result[i+1])
    result[i+1]=list(set(result[i+1]))
    return result[len(result)-1]
    
def isPath(root,listSons,result):
    if root in listSons:
        result.append(root)
        listSons.remove(root)
    if not(listSons) or root.istext():
        return result
    else:
        for i in root.content:
            result=isPath(i,listSons,result)
    return result
            
        
    
def delete(node,listNodes=[]):
    if type(node.content)==str:
        return None
    if not(listNodes):
            return None
    else:
        for i in range(len(listNodes)-1,-1,-1):
            if listNodes[i] in node.content:
                node.content.remove(listNodes[i])
                listNodes=listNodes[:-1]
        for i in node.content:
            delete(i,listNodes)



def check(root,selettore):
    starsWith=selettore[0]
    if starsWith=='.':
        return selettore[1:] in root.attr['class'] if 'class' in root.attr.keys() else False
    if starsWith=='#':
        return selettore[1:]==root.attr['id'] if 'id' in root.attr.keys() else False
    if starsWith=='@':
               return selettore[selettore.find('=')+2:-2]==root.attr[selettore[2:selettore.find('=')]] if selettore[2:selettore.find('=')] in (root.attr).keys() else False
    else:
        return selettore==root.tag


