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
str1=''
str2=''
conta=0
def conta_nodi(fileIn, selettore):
    d= fparse(fileIn)
    global str1
    global str2
    global conta    
    str1=''
    str2=''
    t=''
    si=''
    conta=0
    si=simbo(selettore,t,si)
    cont(d,si)
    return(conta)
def simbo(selettore,t,si):    
    for i in selettore:
        if i=='=':
            t=i
        if i==' ':
            t=i    
        if not i.isalpha():
            if not i.isnumeric():
                if si!='@':
                    if si!='>': 
                        if si!='#':
                            if si!='.':               
                                si=i
            else:
                sim(i,t)                
        else:
            sim(i,t)
    return(si)
def sim(i,t):
    global str1
    global str2
    if t!='=' and t!=' ':
        str1+=(i)
    elif t=='=' or t==' ':                
        if i.isalpha():
            str2+=(i)
        elif i.isnumeric():
            str2+=(i)
def cont(d,si):
    for i in d.content:
        if i.tag != '_text_':
            tip(i,si)            
def tip(i,si):
    global conta
    l=[o for o in i.attr.keys()]
    l2=[k for k in i.attr.values()]
    if si=='>':
        maggio(i)        
    if si=='.':
        punt(i,l,l2)                          
    if si=='#':
        canc(i,l,l2)
    if si=='@':
        chio(i,l,l2)    
    if si=='':
        spa(i)        
    cont(i,si)
def spa(i):
    global conta
    if str1 in i.tag:
            conta+=1
def maggio(i):
    global conta
    if str1 in i.tag:
        if len(str1)==len(i.tag):
            for h in i.content:
                if h.tag!='_text_':
                      if conta==0:            
                          if str2 in h.tag :
                              conta+=1
def punt(i,l,l2):
    global conta
    if 'class' in l:
            if str1 in i.attr['class']:
                conta+=1
def canc(i,l,l2):
    global conta
    if 'id' in l:
        if str1 in l2:            
                conta+=1
def chio(i,l,l2):
    global conta
    if str2 in l2:
        if str1 in l:                    
            conta+=1

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

