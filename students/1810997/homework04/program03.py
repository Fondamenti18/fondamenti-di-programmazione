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

        
def cats(s):
   # if '|' in s:
   #     s=s.split('|')
    #    s=s[0]
    
    if '>' in s : return 'figlio'
    if '#' in s : return 'id'
    if '.' in s : return 'class'
    if '@' in s : return 'attr'
    return 'tag'


def formats(s1):
    s=''+s1
    if '#' in s:
        s=s[1:]
    if '.' in s:
        s=s[1:]
        
    if '@' in s:
        s=list(s)
        s.remove('@')
        s.remove('[')
        s.remove(']')
        #if ('id' in s) or ('class' in s) or ()
        s.remove('"')
        s.remove('"')
        s=''.join(s)
        s=s.split('=')
        if s[-1].isalpha() :
            app=[]
            ls=list(s[1])
            app+=ls
            app.insert(len(app),'"')
            app.insert(0,'"')
            app=''.join(app)
            s[1]=app
        
    return s


def stomat(selettore):
    s=''.join(selettore)
    s=s.split(' ')
    
    mat=[]
    for y in range(len(s)):
        ls=[formats(s[y]),cats(s[y])]
        mat.append(ls)
    mat.append(['end','end'])
    #print('*************')
    #print(mat)
    #print('*************')
    return mat

def check(sel,cats,nodo):
    if cats=='id':
        if 'id' in nodo.attr:
            if nodo.attr['id']==sel:
                return True
    if cats=='tag':
        if nodo.tag==sel:
            return True
    if cats=='class':
        if 'class' in nodo.attr:
            if  sel in nodo.attr['class']:
                return True
    if cats=='attr':
        if sel[0] in nodo.attr:
            if nodo.attr[sel[0]]==sel[1]:
                return True
    return False

def conta(nodo,sel,mess='',c=0):
    if mess=='end': return c
    if mess=='figlio':
        if check(sel[0][0],sel[0][1],nodo):
            if sel[1][0]=='end':
                c+=1
            if sel[1][0]=='>':
                mess='figlio'
                sel=sel[1:]
            if sel[1][0]!='end':
                sel=sel[1:]
        else:
            return c
    
    #if sel[1][0]=='end':
     #   mess='end'
        
    if check(sel[0][0],sel[0][1],nodo)==True and mess!='figlio':
        if sel[1][0]=='end':
            c+=1
        if sel[1][0]=='>':
            mess='figlio'
            sel=sel[1:]
        if sel[1][0]!='end':
            sel=sel[1:]
        
        
            
    if not nodo.istext():
    
        for figlio in nodo.content:
            c=conta(figlio,sel,mess,c)
        
    return c
        
        

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    
    ogg=fparse(fileIn)
    
    sel=stomat(selettore)
    #print(sel[0][0],sel[0][1])
    mess=''
    c=0
    c=conta(ogg,sel,mess,c)
    
    
    return c
    
def elimina(nodo,sel,mess=''):
    if nodo.istext(): return
    
    
    #if sel[1][0]=='end':
     #   mess='end'
        
    if check(sel[0][0],sel[0][1],nodo)==True and mess!='figlio':
        
        if sel[1][0]=='>':
            mess='figlio'
            sel=sel[1:]
        if sel[1][0]!='end':
            sel=sel[1:]
    
    
    
    for figlio in nodo.content:
        elimina(figlio,sel,mess)
    cont2=[]
    for figlio in nodo.content:
        if mess=='figlio':
            if check(sel[0][0],sel[0][1],figlio):
                if sel[1][0]=='end':
                    cont2+=''
                if sel[1][0]=='>':
                    mess='figlio'
                    sel=sel[1:]
                if sel[1][0]!='end':
                    sel=sel[1:]
           
            else:
                cont2+=[figlio]
            
            
            
        if check(sel[0][0],sel[0][1],figlio)==True and mess!='figlio':
            if sel[1][0]=='end':
                cont2+=''
            if sel[1][0]=='>':
                mess='figlio'
                sel=sel[1:]
            if sel[1][0]!='end':
                sel=sel[1:]   
      
    nodo.content =cont2
    
    
        
    

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    ogg=fparse(fileIn)
    
    sel=stomat(selettore)
    mess=''
    elimina(ogg,sel,mess)
    
    
    Html_file=open(fileOut,"w")
    Html_file.write(ogg.to_string())
    Html_file.close()
    
    
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

