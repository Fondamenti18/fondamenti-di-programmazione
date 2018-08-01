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
    a=open(fileIn)
    a=a.readlines()
    cont=0
    sel=''
    for i in selettore:
        if i not in ' ':
            sel+=i
        else:
            sel=''
    if sel[0]=='.' or sel[0]=='@':
        stato='non_tag'
    else:
        stato='tag'
    return conta_tag(a,cont, sel, stato)

def conta_tag(a, cont, selettore, stato):
    if len(a)==0:
        return cont
    if len(a)>0:
        if stato=='tag':
            if a[0].find('<'+selettore)!=-1:
                return conta_tag(a[1:], cont+1, selettore,stato)
        if stato!='tag':
            if a[0].find(selettore.replace('.','').replace('@','').replace('[','').replace(']',''))!=-1:
                return conta_tag(a[1:], cont+1, selettore,stato)
        return conta_tag(a[1:], cont, selettore,stato)

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    a=open(fileIn, encoding='utf-8')
    a=a.readlines()
    sel=''
    for i in selettore:
        if i!=' ':
            sel+=i
        else:
            sel=''
    ind=trova_tag(a, sel, 0)
    tag=isola_tag(a[ind], sel)
    a[ind]=a[ind].replace(tag, '')
    stringa=''
    for i in a:
        stringa+=i
    p=open(fileOut, 'w')
    p.write(stringa)

def trova_tag(a,selettore, cont):
    if len(a)==0:
        return 0
    if len(a)>0:
        if a[0].find('<'+selettore)!=-1:
            return cont
    return trova_tag(a[1:], selettore, cont+1)

def isola_tag(riga, tag):
    inizio=riga.find('<'+tag)
    stringa=''
    for i in range(inizio, len(riga)):
        stringa+=riga[i]
    fine=stringa.find('/'+tag+'>')
    if fine==-1:
        fine=stringa.find('/>')
    stringa2=''
    if fine!=-1:
        for i in range(fine):
            stringa2+=stringa[i]
    stringa2+='/'+tag+'>'
    return stringa2
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

