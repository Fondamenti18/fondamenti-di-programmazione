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
    albero = fparse(fileIn)
    chiave,valore = analisi_selettore(selettore)
    nodi = []
    if chiave == 'class' or chiave == 'id' or '@' in selettore:
        nodi = ricerca_per_attributi(chiave,valore,albero,nodi)
        return len(nodi)
    elif valore == None:
        nodi = ricerca_per_tag(chiave,albero,nodi)
        return len(nodi)
    elif '>' in selettore:
        nodi = ricerca_padre_figlio(chiave,valore,albero,nodi)
        return len(nodi)
    else:
        nodi = ricerca_avo_discendente(chiave,valore,albero,nodi)
        return len(nodi)
        

def elimina_nodi(fileIn, selettore, fileOut):
    albero = fparse(fileIn)
    chiave,valore = analisi_selettore(selettore)
    nodi = []
    if chiave == 'class' or chiave == 'id' or '@' in selettore:
        nodi = ricerca_per_attributi(chiave,valore,albero,nodi)
    elif valore == None:
        nodi = ricerca_per_tag(chiave,albero,nodi)
    elif '>' in selettore:
        nodi = ricerca_padre_figlio(chiave,valore,albero,nodi)
    else:
        nodi = ricerca_avo_discendente(chiave,valore,albero,nodi)
    remove_node(nodi,albero)
    nuova_pag = albero.to_string()
    with open(fileOut,'w',encoding='utf8') as f:
        f.write(nuova_pag)
        
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    albero = fparse(fileIn)
    chia,val = analisi_selettore(selettore)
    nodi = []
    if chia == 'class' or chia == 'id' or '@' in selettore:
        nodi = ricerca_per_attributi(chia,val,albero,nodi)
    elif valore == None:
        nodi = ricerca_per_tag(chia,albero,nodi)
    elif '>' in selettore:
        nodi = ricerca_padre_figlio(chia,val,albero,nodi)
    else:
        nodi = ricerca_avo_discendente(chia,val,albero,nodi)
    modifica_nodi(nodi,albero,chiave,valore)
    nuova_pag = albero.to_string()
    with open(fileOut,'w',encoding = 'utf8') as f:
        f.write(nuova_pag)


#conta_nodi('page1-3.html','.title')

def analisi_selettore(selettore):
    chiave = ''
    valore = ''
    if selettore[0] == '@':
        for x in selettore:
            if x.isalpha():
                chiave += x
            elif x.isnumeric():
                valore += x
        return chiave,valore
    elif selettore[0] == '.':
        chiave = 'class'
        valore = selettore[1:]
        return chiave,valore
    elif selettore[0] == '#':
        chiave = 'id'
        valore = selettore[1:]
        return chiave,valore
    elif '>' in selettore:
        padre = ''
        figlio = ''
        sel = selettore.split()
        padre = sel[0]
        figlio = sel[2]
        return padre,figlio
    elif ' ' in selettore:
        sel = selettore.split()
        avo = sel[0]
        discendente = sel[1]
        return avo,discendente
    else:
        tag = selettore
        return tag,None
    
def ricerca_per_attributi(chiave,valore,nodo,nodi):
    if not nodo.istext():
        if chiave in nodo.attr:
            diz = nodo.attr
            if valore in diz[chiave]:
                nodi += [nodo]
        for x in nodo.content:
            nodi = ricerca_per_attributi(chiave,valore,x,nodi)
    return nodi

def ricerca_per_tag(chiave,nodo,nodi):
    if not nodo.istext():
        if nodo.tag == chiave:
            nodi += [nodo]
        for x in nodo.content:
            nodi = ricerca_per_tag(chiave,x,nodi)
    return nodi

def ricerca_padre_figlio(chiave,valore,nodo,nodi):
    if not nodo.istext():
        if nodo.tag == chiave:
            for x in nodo.content:
                if x.tag == valore:
                    nodi += [x]
        for x in nodo.content:
            nodi = ricerca_padre_figlio(chiave,valore,x,nodi)
    return nodi

def ricerca_avo_discendente(chiave,valore,nodo,nodi):
    if not nodo.istext():
        if nodo.tag == chiave:
            for x in nodo.content:
                n = ricerca_per_tag(valore,x,nodi)
                if n != nodi:
                    nodi += n
        else:
            for x in nodo.content:
                n = ricerca_avo_discendente(chiave,valore,x,nodi)
                if n != nodi:
                    nodi += n
    return nodi

def remove_node(nodi,nodo):
    if not nodo.istext():
        for x in nodi:
            if x in nodo.content:
                nodo.content.remove(x)
        for x in nodo.content:
            nodo = remove_node(nodi,x)

def modifica_nodi(nodi,nodo,chiave,valore):
    if not nodo.istext():
        for x in nodi:
            if x in nodo.content:
                x.attr[chiave] = valore
        for x in nodo.content:
            nodo = modifica_nodi(nodi,x,chiave,valore)