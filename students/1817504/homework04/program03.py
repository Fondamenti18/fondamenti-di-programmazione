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
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    radice=fparse(fileIn)
    selettore=selettore.split()
    risposta=fconta(radice,selettore)
    return risposta

def fpadre(css,i):
    if (i+1)<len(css)-1:
        if css[i+1]=='>':
            return True
    return False

def fconta(radice,css,risposta=0,figlio=False):
    
    if 'a'<=css[0][0]<='z':
        if css[0]==radice.tag:
            risposta=f(radice,css,risposta)

    elif css[0][0]=='.':
        if 'class' in radice.attr:
            if css[0][1:] in radice.attr['class']:
                risposta=f(radice,css,risposta)
                    
    elif css[0][0]=='#':
        if 'id' in radice.attr:
            if css[0][1:]==radice.attr['id']:
                risposta=f(radice,css,risposta)

    elif css[0][0]=='@':
        attributo=css[0][2:-1].split('=')
        attributo[1]=attributo[1].replace('"','')
        if attributo[0] in radice.attr:
            if attributo[1]==radice.attr[attributo[0]]:
                risposta=f(radice,css,risposta)            
    
    if figlio==False and radice.istext()==False:
        for nodo in radice.content:
            risposta=fconta(nodo,css,risposta,False)
    return risposta
                
def f(radice,css,risposta):
    if len(css)==1:
        risposta+=1
    elif radice.istext()==False:
        for nodo in radice.content:
            if css[1]=='>':
                risposta=fconta(nodo,css[2:],risposta,True)
            else: risposta=fconta(nodo,css[1:],risposta,False)
    return risposta
            
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    radice=fparse(fileIn)
    selettore=selettore.split()
    radice=fcancella(radice,selettore)
    with open(fileOut,'w') as f:
        f.write(radice.to_string())

def fcancella(radice,css):
    if css[0]=='>': fcancella(radice,css[1:])
    
    elif 'a'<=css[0][0]<='z':
        if radice.istext()==False:
            i=0
            while i<len(radice.content):
                if radice.content[i].tag==css[0]:
                    if len(css)==1:
                        del(radice.content[i])
                        i=i-1
                    else: fcancella(radice.content[i],css[1:])
                i+=1
                
    elif css[0][0]=='.':
        if radice.istext()==False:
            i=0
            while i<len(radice.content):
                if 'class' in radice.content[i].attr:
                    if css[0][1:] in radice.content[i].attr['class']:
                        if len(css)==1:
                            del(radice.content[i])
                            i=i-1
                        else: fcancella(radice.content[i],css[1:])
                i+=1

    elif css[0][0]=='#':
        if radice.istext()==False:
            i=0
            while i<len(radice.content):
                if 'id' in radice.content[i].attr:
                    if css[0][1:]==radice.content[i].attr['id']:
                        if len(css)==1:
                            del(radice.content[i])
                            i=i-1
                        else: fcancella(radice.content[i],css[1:])
                i+=1

    elif css[0][0]=='@':
        attributo=css[0][2:-1].split('=')
        attributo[1]=attributo[1].replace('"','')
        if radice.istext()==False:
            i=0
            while i<len(radice.content):
                if attributo[0] in radice.content[i].attr:
                    if attributo[1]==radice.content[i].attr[attributo[0]]:
                        if len(css)==1:
                            del(radice.content[i])
                            i=i-1
                        else: fcancella(radice.content[i],css[1:])
                i+=1
        
            
    if radice.istext()==False:
        if len(css)==1 or css[1]!='>':
            for nodo in radice.content:
                fcancella(nodo,css)
    return radice
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    radice=fparse(fileIn)
    selettore=selettore.split()
    radice=modifica(radice,selettore,chiave,valore)
    with open(fileOut,'w') as f:
        f.write(radice.to_string())

def modifica(radice,css,chiave,valore,figlio=False):
    if 'a'<=css[0][0]<='z':
        if css[0]==radice.tag:
            if len(css)==1:
                radice.attr[chiave]=valore
            elif radice.istext()==False:
                for nodo in radice.content:
                    if css[1]=='>':
                        modifica(nodo,css[2:],chiave,valore,True)
                    else: modifica(nodo,css[1:],chiave,valore,False)

    elif css[0][0]=='.':
        if 'class' in radice.attr:
            if css[0][1:] in radice.attr['class']:
                if len(css)==1:
                    radice.attr[chiave]=valore
                elif radice.istext()==False:
                    for nodo in radice.content:
                        if css[1]=='>':
                            modifica(nodo,css[2:],chiave,valore,True)
                        else: modifica(nodo,css[1:],chiave,valore,False)
                    
    elif css[0][0]=='#':
        if 'id' in radice.attr:
            if css[0][1:]==radice.attr['id']:
                if len(css)==1:
                    radice.attr[chiave]=valore
                elif radice.istext()==False:
                    for nodo in radice.content:
                        if css[1]=='>':
                            modifica(nodo,css[2:],chiave,valore,True)
                        else: modifica(nodo,css[1:],chiave,valore,False)

    elif css[0][0]=='@':
        attributo=css[0][2:-1].split('=')
        attributo[1]=attributo[1].replace('"','')
        if attributo[0] in radice.attr:
            if attributo[1]==radice.attr[attributo[0]]:
                if len(css)==1:
                    radice.attr[chiave]=valore
                elif radice.istext()==False:
                    for nodo in radice.content:
                        if css[1]=='>':
                            modifica(nodo,css[2:],chiave,valore,True)
                        else: modifica(nodo,css[1:],chiave,valore,False)
    
    if figlio==False and radice.istext()==False:
        for nodo in radice.content:
            modifica(nodo,css,chiave,valore,False)
    return radice
                

