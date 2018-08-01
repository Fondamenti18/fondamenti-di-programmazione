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

def selettore_split(sel):
    if '>' not in sel:
        s = sel.split(' ')
    else:
        s = sel.split('>')
    return s

def crea_nodo(li):
    tagOpen=False
    sonOpen=False
    nomeSon=''
    figli=[]
    attr={}
    nome=''
    nome2=''
    closed = ['$&/img','$&/br','$&/meta','$&/link', '$&/input', '$&/br', '$&/hr','$&img','$&br','$&meta','$&link', '$&input', '$&br', '$&hr']
    for i,el in enumerate(li):
        if '$&' in el:
            #primo padre
            if not tagOpen and el not in closed:
                tagOpen=True
                el=el.split('"')
                if len(el)==1:
                     nome=el[0]
                     nome = nome.replace('$&','$&/')
                else:
                     nome2 = el[0].split(' ')
                     nome = nome2[0]
                     nome = nome.replace('$&','$&/')
                     nome2=nome2[1:]
                     for att in nome2:
                         dividi=att.split("=")
                         attr[dividi[0]]=dividi[1].replace('"','')
                #print('\nNodo: ', nome)
            #tagOpen == true
            elif nome in el and nome not in closed:
                nome=nome.replace('$&/','')
                #print('--Chiudo nodo ',nome,sonOpen,tagOpen)
                tagOpen=False
                return HTMLNode(nome,attr,figli)
            #tagOpen == true and Not SonOpen
            #ho trovato il primo figlio
            elif not sonOpen: 
                        el2=el.split(' ')
                        nomeSon=el2[0]
                        #print('\nTrovato figlio "',nomeSon,'" di ',nome)
                        if nomeSon in closed:
                            nomeSon = nomeSon.replace('$&','')
                            attributes={}
                            el2=el2[1:]
                            for att in el2:
                                dividi=att.split("=")
                                attributes[dividi[0]]=dividi[1]
                            figli.append(HTMLNode(nomeSon,attributes,[]))
                        else:    
                            nomeSon = nomeSon.replace('$&','$&/')
                            sonOpen=True  
                            figli.append(crea_nodo(li[i:]))
            #tagOpen==true and sonOpen=True e c'è il nome
            #ho chiuso il figlio
            elif sonOpen and nomeSon in el:
                #print('\n---Chiudo il figlio ',nomeSon," di ",nome,"---")
                sonOpen=False
        #l'elemnto corrento non è un nodo, ma il padre è aperto,ma il figlio è chiusp
        elif tagOpen and not sonOpen:
            #print("\nTrovato un figlio '",el,"' di'",nome)
            figli.append(HTMLNode("_text_",{},el))
                
            

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    with open(fileIn, encoding='utf-8-sig') as f:
        fa = f.read()
        sel = selettore_split(selettore)
        fr=  fa.replace('<','<$&')
        fr = fr.replace('>','<')
        fr = fr.split('<')
        while '' in fr:
            fr.remove('')     
        while ' ' in fr:
            fr.remove(' ')
        
        root=crea_nodo(fr)
        if len (sel[0].split('  '))>1:
            father=sel[0].split('  ')[0]
            sel[0]=sel[0].split('  ')[1]
            for elem in sel:
                elem=elem.replace(' ','')
            print( conta(root,father,False,sel))
        else:
            for elem in sel:
                elem=elem.replace(' ','')
            print( conta(root,root.attr,True,sel))
            
def conta(nodo,p,bul,sel):
    c=0
    if bul==True:
        if len(sel)==1:
            if nodo.tag.replace(' ','')==sel[0].replace(' ',''):
                return 1
        else:
            cerco=sel[0]
            if nodo.tag.replace(' ','')==cerco.replace(' ',''):
                for figli in nodo.content:
                    if figli.tag != "_text_":
                        c+=conta(figli,p,bul,sel[1:])
            else:
                 for figli in nodo.content:
                    if figli.tag != "_text_":
                        c+=conta(figli,p,bul,sel)
    elif nodo.tag==p:
        for figli in nodo.content:
            c+=conta(figli,p,True,sel)
    
    return c
        
    
    
    
    
    
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    with open(fileIn, encoding='utf-8-sig') as f:
        fr = f.read()
        fr = fr.split('\n')
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    with open(fileIn, encoding='utf-8-sig') as f:
        fr = f.read()
        fr = fr.split('\n')
    



if __name__ == '__main__':
    conta_nodi('page1-3.html', 'p > em')
    #'page1-3.html'