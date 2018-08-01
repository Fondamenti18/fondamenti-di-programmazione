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
from re import split,search    

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    root=fparse(fileIn)
    sel=split(' (?!>)',selettore)
    bones=[]
    funcdic={'@':check_at,'#':check_hash,'.':check_point,'w':check_word}
    for el in sel:
        if el[0]=='@':
            l=search('(\w+)="(\w+)',el)
            bones.append((l.group(1),l.group(2)))   
        else:
            l=search('\w+-*\w*',el)
            bones.append(l.group())       
    l=cycling(root,bones,sel,funcdic)
    return len(l)

def cycling(root,bones,sel,funcdic):
    i=0
    l0=[root]
    while i<len(bones):
        l1=[]
        if sel[i][0].isalpha():c='w'
        else:c=sel[i][0]
        hound_tree(l0,bones[i],l1,funcdic,c)
        l0=l1
        if sel[i][-1]=='>':
            if sel[i+1][0].isalpha():c='w'
            else:c=sel[i+1][0]
            l2=hound_sons(l0,bones[i+1],funcdic,c)
            l0=l2
            i+=2
        else:
            i+=1
            
    return l0
    
    
def hound_sons(nodes,bone,dic,c):
    ls=[]
    for node in nodes:
        for i in node.content:
            if dic[c](i,bone):ls.append(i)
    return ls        
                
def hound_tree(nodes,bone,ls,dic,c):
    for node in nodes:
        if dic[c](node,bone):ls.append(node)
        if type(node)!=str:hound_tree(node.content,bone,ls,dic,c)
    return    

def check_word(node,bone):
    if type(node)!=str and bone==node.tag:return True
    else:return False

def check_point(node,bone):
    if type(node)!=str:
        for k,v in node.attr.items():
            if bone in v and k=='class':return True
    else:return False

  
def check_at(node,bone):
   if type(node)!=str and bone[0] in node.attr and bone[1]==node.attr[bone[0]]:return True
   else:return False

   
def check_hash(node,bone):
    if type(node)!=str and bone in node.attr.values():return True
    else:return False

       
    


def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    root=fparse(fileIn)
    sel=split(' (?!>)',selettore)
    bones=[]
    funcdic={'@':check_at,'#':check_hash,'.':check_point,'w':check_word}
    for el in sel:
        if el[0]=='@':
            l=search('(\w+)="(\w+)',el)
            bones.append((l.group(1),l.group(2)))   
        else:
            l=search('\w+-*\w*',el)
            bones.append(l.group())    
    ls=cycling(root,bones,sel,funcdic)
    delete(ls)
    f=open(fileOut,'w')
    f.write(root.to_string())
    f.close()
    
    return 
    
def delete(ls):
    for el in ls:
        el.content=''
        el.tag='_text_'
    return        
    
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    root=fparse(fileIn)
    sel=split(' (?!>)',selettore)
    bones=[]
    funcdic={'@':check_at,'#':check_hash,'.':check_point,'w':check_word}
    for el in sel:
        if el[0]=='@':
            l=search('(\w+)="(\w+)',el)
            bones.append((l.group(1),l.group(2)))   
        else:
            l=search('\w+-*\w*',el)
            bones.append(l.group())
    ls=cycling(root,bones,sel,funcdic)
    changes(ls,chiave,valore)
    f=open(fileOut,'w')
    f.write(root.to_string())
    f.close()
    return

def changes(ls,k,v):
    for el in ls:
        el.attr[k]=v
    return    

if __name__=='__main__':
    fileIn    = 'page1-3.html'
    selettore = '.title'
    expected  = 1
    args      = (fileIn, selettore)
    print(conta_nodi(*args))