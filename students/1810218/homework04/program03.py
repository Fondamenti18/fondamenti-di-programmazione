# -*- coding: utf-8 -*-
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

from  my_html import HTMLNode, parse, fparse

import codecs
def fparse(fhtml):
    with codecs.open(fhtml, 'r', "utf-8") as f:
        root = parse(f.read())
        return root










def tipo(s):
    if s.startswith('.'):
        return 'c'
    elif s.startswith('#'):
        return 'id'
    elif s.startswith('@'):
        return 'a'
    else:
        return 't'
                      
                      
def discendenti(nodo,l=[]):
    
    if not nodo.istext():    
        for figlio in nodo.content:
            l.append(figlio)
            discendenti(figlio,l)
    return l
    







def soddisfa(nodo,selettore,ris=[],indice=0):
    
    if indice<len(selettore):
        sel=selettore[indice]
    else:
        indice=0
        sel=selettore[indice]
    
    if sel[-1]=='>':
        
        if tipo(sel)=='t': #controllo se sel e' un tag
            if nodo.tag==sel[:-1]: # se i tag coincidono
                if indice==len(selettore)-1:
                    ris.append(nodo)
                for figlio in nodo.content:
                     if not figlio.istext():   
                        soddisfa(figlio,selettore,ris,indice+1)#ricerca in tutti i figli con indice +1
            else:
                for figlio in nodo.content:#se non coincide cerca con indice non aumentato
                    if not figlio.istext():
                        soddisfa(figlio,selettore,ris,0)
                
               
        elif tipo(sel)=='c':    #se e' classe
            if 'class' in nodo.attr.keys():
                if sel[1:-1] in nodo.attr['class']: #se soddisfa il sel
                    if indice==len(selettore)-1:
                        ris.append(nodo)
                    for figlio in nodo.content:
                        if not figlio.istext():
                            soddisfa(figlio,selettore,ris,indice+1) #ricerca in tutti i figli con indice +1
                else:
                    for figlio in nodo.content:
                        if not figlio.istext():
                            soddisfa(figlio,selettore,ris,0)
            else:
                for figlio in nodo.content:
                    if not figlio.istext():
                        soddisfa(figlio,selettore,ris,0)
                    
        elif tipo(sel)=='id':
            if 'id' in nodo.attr.keys():
                if sel[1:-1] in nodo.attr['id']:
                    if indice==len(selettore)-1:
                        ris.append(nodo)
                    for figlio in nodo.content:
                        if not figlio.istext():
                            soddisfa(figlio,selettore,ris,indice+1)
                else:
                    for figlio in nodo.content:
                        if not figlio.istext():
                            soddisfa(figlio,selettore,ris,0)
            else:
                for figlio in nodo.content:
                    if not figlio.istext():
                        soddisfa(figlio,selettore,ris,0)
                    
        else:
            if sel[sel.find('[')+1:sel.find('=')] in nodo.attr.keys(): #se l'attributo e' nelle chiavi
                if sel[sel.find('"')+1:-3] in nodo.attr[sel[sel.find('[')+1:sel.find('=')]]: #se il valore e' nei valori della chiave
                    if indice==len(selettore)-1:
                        ris.append(nodo)
                    for figlio in nodo.content:
                        if not figlio.istext():
                            soddisfa(figlio,selettore,ris,indice+1)
                else:
                    for figlio in nodo.content:
                        if not figlio.istext():
                            soddisfa(figlio,selettore,ris,0)
            else:
                for figlio in nodo.content:
                    if not figlio.istext():
                        soddisfa(figlio,selettore,ris,0)
    
    else:
        if tipo(sel)=='t': #controllo se sel e' un tag
            if nodo.tag==sel: # se i tag coincidono
                if indice==len(selettore)-1:
                    ris.append(nodo)
                for figlio in discendenti(nodo,[]):
                    if not figlio.istext():
                        soddisfa(figlio,selettore,ris,indice+1)#ricerca in tutti i figli con indice +1
            else:
                for figlio in discendenti(nodo,[]):#se non coincide cerca con indice non aumentato
                    if not figlio.istext():
                        soddisfa(figlio,selettore,ris,indice)
                
               
        elif tipo(sel)=='c':    #se e' classe
            if 'class' in nodo.attr.keys():
                if sel[1:] in nodo.attr['class']: #se soddisfa il sel
                    if indice==len(selettore)-1:
                        ris.append(nodo)
                    for figlio in discendenti(nodo,[]):
                        if not figlio.istext():
                            soddisfa(figlio,selettore,ris,indice+1) #ricerca in tutti i figli con indice +1
                else:
                    for figlio in discendenti(nodo,[]):
                        if not figlio.istext():
                            soddisfa(figlio,selettore,ris,indice)
            else:
                for figlio in discendenti(nodo,[]):
                    if not figlio.istext():
                        soddisfa(figlio,selettore,ris,indice)
                    
        elif tipo(sel)=='id':
            if 'id' in nodo.attr.keys():
                if sel[1:] in nodo.attr['id']:
                    if indice==len(selettore)-1:
                        ris.append(nodo)
                    for figlio in discendenti(nodo,[]):
                        if not figlio.istext():
                            soddisfa(figlio,selettore,ris,indice+1)
                else:
                    for figlio in discendenti(nodo,[]):
                        if not figlio.istext():
                            soddisfa(figlio,selettore,ris,indice)
            else:
                for figlio in discendenti(nodo,[]):
                    if not figlio.istext():
                        soddisfa(figlio,selettore,ris,indice)
                    
        else:
            if sel[sel.find('[')+1:sel.find('=')] in nodo.attr.keys(): #se l'attributo e' nelle chiavi
                if sel[sel.find('"')+1:-2] in nodo.attr[sel[sel.find('[')+1:sel.find('=')]]: #se il valore e' nei valori della chiave
                    if indice==len(selettore)-1:
                        ris.append(nodo)
                    for figlio in discendenti(nodo,[]):
                        if not figlio.istext():
                            soddisfa(figlio,selettore,ris,indice+1)
                else:
                    for figlio in discendenti(nodo,[]):
                        if not figlio.istext():
                            soddisfa(figlio,selettore,ris,indice)
            else:
                for figlio in discendenti(nodo,[]):
                    if not figlio.istext():
                        soddisfa(figlio,selettore,ris,indice)
                    
    return ris
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    for nodo in nodi:
    
    
    
    
    
        sel=selettore[indice]
        if tipo(sel)=='t':
            for figlio in nodo.content:
                if sel[-1]=='>' and sel[:-1]==nodo.tag:
                    l.append(figlio)
                elif sel[-1]!='>' and sel==nodo.tag: 
                    l.append(figlio)
                soddisfa(l,selettore,[],indice+1)
                
            
        
    elif tipo(sel[indice])=='c':
    elif tipo(sel[indice])=='id':
    else:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if tipo(sel[indice])=='t':
        if indice==len(sel)-1 and 
    elif tipo(sel[indice])=='c':
    elif tipo(sel[indice])=='id':
    else:
    
    
    
    
    if sel[indice][-1]=='>':
        if tipo(sel[indice])=='t': #controllo se sel[indice] e' un tag
            if nodo.tag==sel[indice][:-1]: # se i tag coincidono
                for figlio in nodo.content:
                    soddisfa(figlio,sel,indice+1)#ricerca in tutti i figli con indice +1
            else:
                for figlio in nodo.content:#se non coincide cerca con indice non aumentato
                    soddisfa(figlio,sel,indice)
                
               
        elif tipo(sel[indice])=='c':    #se e' classe
            if 'class' in nodo.attr.keys():
                if sel[indice][1:-1] in nodo.attr['class']: #se soddisfa il sel
                    for figlio in nodo.content:
                        soddisfa(figlio,sel,indice+1) #ricerca in tutti i figli con indice +1
                else:
                    for figlio in nodo.content:
                        soddisfa(figlio,sel,indice)
            else:
                for figlio in nodo.content:
                    soddisfa(figlio,sel,indice)
                    
        elif tipo(sel[indice])=='id':
            if 'id' in nodo.attr.keys():
                if sel[indice][1:-1] in nodo.attr['id']:
                    for figlio in nodo.content:
                        soddisfa(figlio,sel,indice+1)
                else:
                    for figlio in nodo.content:
                        soddisfa(figlio,sel,indice)
            else:
                for figlio in nodo.content:
                    soddisfa(figlio,sel,indice)
                    
        else:
            if sel[sel.find('[')+1:sel.find('=')] in nodo.attr.keys(): #se l'attributo e' nelle chiavi
                if sel[sel.find('"')+1:-3] in nodo.attr[sel[sel.find('[')+1:sel.find('=')]]: #se il valore e' nei valori della chiave
                    for figlio in nodo.content:
                        soddisfa(figlio,sel,indice+1)
                else:
                    for figlio in nodo.content:
                        soddisfa(figlio,sel,indice)
            else:
                for figlio in nodo.content:
                    soddisfa(figlio,sel,indice)
            
    else:
    
    
    
    
    
    
    
    
    
    

    if sel[indice][-1]=='>':
        for figlio in nodo.content:
            
            if tipo(sel)=='t':
                if nodo.tag==sel[:-1]:
                    soddisfa(figlio,sel,indice+1)
            elif tipo(sel)=='c':    
                if 'class' in nodo.attr.keys():
                    if sel[1:-1] in nodo.attr['class']:
                        soddisfa(figlio,sel,indice+1)
            elif tipo(sel)=='id':
                if 'id' in nodo.attr.keys():
                    if sel[1:-1] in nodo.attr['id']:
                        soddisfa(figlio,sel,indice+1)
            else:
                if sel[sel.find('[')+1:sel.find('=')] in nodo.attr.keys():
                    if sel[sel.find('"')+1:-3] in nodo.attr[sel[sel.find('[')+1:sel.find('=')]]:
                        soddisfa(figlio,sel,indice+1)
                        
         '''   
def elimina(nodo,compat):
    if not nodo.istext():
        for figlio in nodo.content:
            if figlio in compat: 
                
                nodo.content.remove(figlio)
                for x in figlio.content:
                    if not x.istext():
                        
                        nodo.content.append(x)
                figlio.content=[]
            elimina(figlio,compat)
    return nodo
                
def cambia(nodo,compat,chiave,valore):
    if nodo in compat:
        
        nodo.attr[chiave]=valore
    if not nodo.istext():
        for figlio in nodo.content:
            cambia(figlio,compat,chiave,valore)
    return nodo
            
    
        
                    
                    
                    
                    
    



def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    rad=fparse(fileIn)
    selettore=selettore.split(' ')
    for x in range(len(selettore)):
        if selettore[x]=='>':
            selettore[x-1]+='>'
    for x in selettore:
        if x=='>':
            selettore.remove(x)
    selettore[-1]+='>'
        
    return len(set(soddisfa(rad,selettore,[],0)))
    

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    rad=fparse(fileIn)
    selettore=selettore.split(' ')
    for x in range(len(selettore)):
        if selettore[x]=='>':
            selettore[x-1]+='>'
    for x in selettore:
        if x=='>':
            selettore.remove(x)
    selettore[-1]+='>'
    compat=set(soddisfa(rad,selettore,[],0))
    ris=elimina(rad,compat)
    
    f=codecs.open(fileOut, "w", "utf-8")
    
    f.write(ris.to_string())
    f.close()
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    rad=fparse(fileIn)
    selettore=selettore.split(' ')
    for x in range(len(selettore)):
        if selettore[x]=='>':
            selettore[x-1]+='>'
    for x in selettore:
        if x=='>':
            selettore.remove(x)
    selettore[-1]+='>'
    compat=set(soddisfa(rad,selettore,[],0))
    ris=cambia(rad,compat,chiave,valore)
    f=codecs.open(fileOut, "w", "utf-8")
    f.write(ris.to_string())
    f.close()
    
    
    
