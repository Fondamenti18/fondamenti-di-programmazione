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
from bs4 import BeautifulSoup

def conta_nodi(fileIn, selettore):
    doc = fparse(fileIn)
    c = 0
    l = []
    s = []
    if ">" in selettore or "<" in selettore:
        selettore1 = maggiore(selettore)
        selettore2 = maggiore2(selettore)
        return conta_selettore_speciale1(doc,selettore1,selettore2,c,l,s)
    if " " in selettore :
        if not ">" in selettore :
            selettore1 = maggiore(selettore)
            selettore2 = maggiore2(selettore)
            return conta_selettore_speciale2(doc,selettore1,selettore2,c,l,s)
    else:
        selettore,verifica = pulizia(selettore)
        if verifica == True :
            return attributo(doc,doc,selettore,l,c)
        else:
            return conta_selettore(doc,selettore,c,l,)
###############VERIFICA DEL PADRE E FIGLIO E LO SPIRITO SANTO###############
def maggiore(selettore):
    a = ""
    for x in selettore :
        if x.isalpha() :
            a = a + x
        else :
            return a
def maggiore2(selettore):
    a = ""
    selettore = selettore[::-1]
    for x in selettore:
        if x.isalpha() :
            a = a + x
        else :
            return a[::-1]
###############PULIZIA CARATTERI SPECIALI############################
def pulizia(selettore):
    if selettore.startswith(".") == True:
        selettore = selettore.replace(".","")
        return (selettore , True)
    elif selettore.startswith("#") :
        selettore = selettore.replace("#","")
        return (selettore , True)
    elif selettore.startswith('@'):
        for x in selettore:
            if x != '"':
                selettore = selettore.replace(x,"")
            else :
                break
        selettore = selettore[::-1]
        for y in selettore:
            if y != '"' :
                selettore = selettore.replace(y,"")
            else:
                selettore = selettore.replace(y,"")
                return (selettore[::-1],True)
    else :
        return (selettore , False)
##############CONTEGGIO SELETTORE NORMALE OPPURE PULITO###############
def conta_selettore(node,selettore,c,l):
    if not node.istext():
        for child in node.content:
            if child.tag == selettore :
                c = c + 1
            else :
                conta_selettore(child,selettore,c,l)
        l.append(c)
        l.sort()
        return l[-1]
##############CONTEGGIO CON RELAZIONE PADRE E FIGLI PLURALE############
def conta_selettore_speciale2(node,selettore1,selettore2,c,l,s):
    if not node.istext():
        for child in node.content:
            if child.tag == selettore1 :
                a = trova_selettore(child,selettore2,s)
                if a !=[]:
                    c = c + 1
            else :
                conta_selettore_speciale2(child,selettore1,selettore2,c,l,s)
        l.append(c)
        l.sort()
        return l[-1]
def trova_selettore(node,selettore2,s):
    if not node.istext():
        for child in node.content:
            if child.tag == selettore2 :
                s.append(1)
            else :
                trova_selettore(child,selettore2,s)
        return s
############CONTEGGIO CON RELAZIONE PADRE E FIGLIO STRETTO#############
def conta_selettore_speciale1(node,selettore1,selettore2,c,l,s):
    if not node.istext():
        for child in node.content:
            if child.tag == selettore1 :
                a = trova_selettore1(child,selettore2,s)
                if a !=[]:
                    c = c + 1
                    break
            else :
                conta_selettore_speciale1(child,selettore1,selettore2,c,l,s)
        l.append(c)
        l.sort()
        return l[-1]
def trova_selettore1(node,selettore2,s):
    if not node.istext():
        for child in node.content:
            if child.tag == selettore2 :
                s.append(1)
            if child.tag == "_text_" :
                trova_selettore1(child,selettore2,s)
            else :
                return s
        return s
###########CONTEGGIO CON ATTRIBUTI#################
def attributo(capo,doc , selettore,l,c):
    for node in doc.content :
        if not node.istext():
            if selettore in str((list((node.attr).values()))) :
                for x in  conta(capo,node.tag):
                    c = c + 1
                    l.append(c)
            else :
                attributo(capo,node,selettore,l,c)
    l.sort()
    if l == [] :
        return 0
    else :
        return l[-1]
def conta(node,selettore):
    ret = []
    if node.tag == selettore:
        ret = ret + [node]
    if not node.istext():
        for child in node.content:
            ret = ret + conta(child,selettore)
    return ret
           
    
                        
       
      
                

def elimina_nodi(fileIn, selettore, fileOut):
    doc = fparse(fileIn)
    if "@" in selettore :
        selettore = selettore.replace("@","")
    return elimina (doc,selettore,fileOut)
def elimina(doc,selettore,fileOut):
    doc = doc.to_string()
    soup = BeautifulSoup(doc,"lxml")
    lista = soup.select(selettore)
    c = 0
    ricorsiva1(doc,lista,c,fileOut)
def ricorsiva1(t,lista,c,fileOut):
    if c == len(lista):
        with open(fileOut,"w",encoding = "utf-8") as f :
            f.write(t)
    else:
        x = lista[c]
        c = c + 1
        z = str(x)
        if z in t:
            t = t.replace(z,"")
        ricorsiva1(t,lista,c,fileOut)          
    
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    doc = fparse(fileIn)
    if "@" in selettore :
        selettore = selettore.replace("@","")
    return colora (doc,selettore,chiave,valore,fileOut)
def colora(doc,selettore,chiave,valore,fileOut):
    doc = doc.to_string()
    soup = BeautifulSoup(doc,"lxml")
    lista = soup.select(selettore)
    c = 0
    ricorsiva(doc,lista,c,chiave,valore,fileOut)
    
def ricorsiva(t,lista,c,chiave,valore,fileOut):
    if c == len(lista):
        with open(fileOut,"w",encoding = "utf-8") as f :
            f.write(t)
    else:
        x = lista[c]
        c = c + 1
        z = str(x)
        z = z.split("\n")
        if len(z) > 0 :
            z = str(z[0])
            if z in t :
                x[chiave] = valore
                x = str(x)
                x = x.split("\n")
                x = str(x[0])
                t = t.replace(z,str(x))
            ricorsiva(t,lista,c,chiave,valore,fileOut)
            
        else :
            z = str(z[0])
            if z in t:
                x[chiave] = valore
                t = t.replace(z,str(x))
            ricorsiva(t,lista,c,chiave,valore,fileOut)
    
  


