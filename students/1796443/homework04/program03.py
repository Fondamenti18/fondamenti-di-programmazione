'''
Un documento HTML può essere rappresentato sotto forma di albero, come visto a lezione, che si chiama DOM (Document Object Model).

Un qualsiasi nodo di questo albero può essere individuato sulla base delle proprie caratteristiche:
    - tag                       un tag del tipo indicato
    - .classe                   una delle parole presenti nel valore dell'attributo "class"
    - #id                       il valore dell'attributo "id"
    - @[attributo="valore"]     valore di un attributo generico
ed in base alla sua relazione con i tag che lo contengono:
    - avo discendente           il tag 'avo' contiene un tag 'discendente' a qualsiasi profondità
    - padre > figlio            il tag 'padre' contiene il tag 'figlio' nel livello immediatamente sotto

Un selettore CSS è una successione di selettori di tag separati da spazio che serve ad individuare uno o più nodi all'interno del DOM.
Esempio:
    div .class1 > #main_window
        seleziona un qualsiasi tag che ha                                       id="main_window"
        è il figlio di un tag che ha                                            class="... class1 ..."
        e si trova all'interno (a qualsiasi livello di distanza) di un tag      div
Esempio2:
    p  table > tr > td > a
	seleziona un link (<a ...> </a>)
	figlio di una casella (<td> ... </td>)
	figlia di una riga (<tr> ... </tr>)
	figlia di una tabella (<table> ... </table>)
	contenuta a qualsiasi livello in un paragrafo (<p> .... </p>)

NOTA: questa definizione del CSS è una versione ridottissima che non segue lo standard completo. 
In particolare, non è possibile usare più relazioni '>' consecutive o costruire selettori alternativi (in OR) e selettori in AND.

Le modifiche da attuare su un DOM possono essere di 3 tipi:
    - conteggio dei nodi che soddisfano il selettore CSS
    - eliminazione di tutti i tag individuati da un selettore CSS
    - modifica degli attributi di tutti i tag individuati da un selettore CSS

Realizzate le funzioni che esplorano e modificano l'albero:
    conta_nodi(       fileIn, selettore)				
    elimina_nodi(       fileIn, selettore, fileOut)				
    cambia_attributo(	fileIn, selettore, chiave, valore, fileOut)

ATTENZIONE: nei test verrà utilizzato un timout globale di 1*N secondi (se il grader fa N test)
'''

from  my_html import HTMLNode, fparse

def conta(doc,sel,lista):
    if sel[0]!='>':
        trova(doc,sel,lista)
    else:
        if sel[1][0]=='.':
            if 'class' in doc.attr.keys():
                if sel[1][1:] in doc.attr['class']:
                    if len(sel)==2: lista+=[doc]
                    else:
                        for d in doc.content:
                            conta(d,sel[2:],lista)
        elif sel[1][0]=='#':
            if 'id' in doc.attr:
                if doc.attr['id']==sel[1][1:]:
                    if len(sel)==2: lista+=[doc]
                    else:
                        for d in doc.content:
                            conta(d,sel[2:],lista)
        elif sel[1][0]=='@':
            if sel[1][2:sel[1].find('=')] in doc.attr.keys():
                if doc.attr[sel[1][2:sel[1].find('=')]]==sel[1][sel[1].find('=')+2:len(sel[1])-2]:
                    if len(sel)==2: lista+=[doc]
                    else:
                        for d in doc.content:
                            conta(d,sel[2:],lista)
        elif sel[1]=='_text_':
            if doc.tag=='_text_':
                lista+=[doc]
        elif doc.tag== sel[1]:
            if len(sel)==2: lista+=[doc]
            else:
                for d in doc.content:
                    conta(d,sel[2:],lista)
    
def trova(doc,sel,lista):
    if sel[0][0]=='.':
        if 'class' in doc.attr.keys():
            if sel[0][1:] in doc.attr['class']:
                if len(sel)==1: lista+=[doc]
                else:
                    for d in doc.content:
                        conta(d,sel[1:],lista)
    elif sel[0][0]=='#':
        if 'id' in doc.attr:
            if doc.attr['id']==sel[0][1:]:
                if len(sel)==1: lista+=[doc]
                else:
                    for d in doc.content:
                        conta(d,sel[1:],lista)
    elif sel[0][0]=='@':
        if sel[0][2:sel[0].find('=')] in doc.attr.keys():
            if doc.attr[sel[0][2:sel[0].find('=')]]==sel[0][sel[0].find('=')+2:len(sel[0])-2]:
                if len(sel)==1: lista+=[doc]
                else:
                    for d in doc.content:
                        conta(d,sel[1:],lista)
    elif sel[0]=='_text_':
        if doc.tag=='_text_':
            lista+=[doc]
    elif doc.tag== sel[0]:
        if len(sel)==1: lista+=[doc]
        else:
            for d in doc.content:
                conta(d,sel[1:],lista)
    if doc.tag!='_text_':
        for d in doc.content:
            trova(d,sel,lista)

def conta2(doc,sel,lista):
    if sel[0]!='>':
        trova2(doc,sel,lista)
    else:
        if sel[1][0]=='.':
            if 'class' in doc.attr.keys():
                if sel[1][1:] in doc.attr['class']:
                    if len(sel)==2:
                        lista+=[1]
                    else:
                        i=0
                        for d in doc.content:
                            conta2(doc,sel[2:],lista)
                            if 1 in lista:
                                del doc.content[i]
                                lista=[]
                            else:
                                i+=1
        elif sel[1][0]=='#':
            if 'id' in doc.attr:
                if doc.attr['id']==sel[1][1:]:
                    if len(sel)==2:
                        lista+=[1]
                    else:
                        i=0
                        for d in doc.content:
                            conta2(doc,sel[2:],lista)
                            if 1 in lista:
                                del doc.content[i]
                                lista=[]
                            else:
                                i+=1
        elif sel[1][0]=='@':
            if sel[1][2:sel[1].find('=')] in doc.attr.keys():
                if doc.attr[sel[1][2:sel[1].find('=')]]==sel[1][sel[1].find('=')+2:len(sel[1])-2]:
                    if len(sel)==2:
                        lista+=[1]
                    else:
                        i=0
                        for d in doc.content:
                            conta2(doc,sel[2:],lista)
                            if 1 in lista:
                                del doc.content[i]
                                lista=[]
                            else:
                                i+=1
        elif sel[1]=='_text_':
            if doc.tag=='_text_':
                lista+=[1]
        elif doc.tag== sel[1]:
            if len(sel)==2:
                lista+=[1]
            else:
                i=0
                for d in doc.content:
                    conta2(doc,sel[2:],lista)
                    if 1 in lista:
                        del doc.content[i]
                        lista=[]
                    else:
                        i+=1
    
def trova2(doc,sel,lista=[]):
    if sel[0][0]=='.':
        if 'class' in doc.attr.keys():
            if sel[0][1:] in doc.attr['class']:
                if len(sel)==1:
                    lista+=[1]
                else:
                    i=0
                    for d in doc.content:
                        conta2(doc,sel[1:],lista)
                        if 1 in lista:
                            del doc.content[i]
                            lista=[]
                        else:
                            i+=1
    elif sel[0][0]=='#':
        if 'id' in doc.attr:
            if doc.attr['id']==sel[0][1:]:
                if len(sel)==1:
                    lista+=[1]
                else:
                    i=0
                    for d in doc.content:
                        conta2(doc,sel[1:],lista)
                        if 1 in lista:
                            del doc.content[i]
                            lista=[]
                        else:
                            i+=1
    elif sel[0][0]=='@':
        if sel[0][2:sel[0].find('=')] in doc.attr.keys():
            if doc.attr[sel[0][2:sel[0].find('=')]]==sel[0][sel[0].find('=')+2:len(sel[0])-2]:
                if len(sel)==1:
                    lista+=[1]
                else:
                    i=0
                    for d in doc.content:
                        conta2(doc,sel[1:],lista)
                        if 1 in lista:
                            del doc.content[i]
                            lista=[]
                        else:
                            i+=1
    elif sel[0]=='_text_':
        if doc.tag=='_text_':
            lista+=[1]
    elif doc.tag== sel[0]:
        if len(sel)==1:
            lista+=[1]
        else:
            i=0
            for d in doc.content:
                conta2(doc,sel[1:],lista)
                if 1 in lista:
                    del doc.content[i]
                    lista=[]
                else:
                    i+=1
    if doc.tag!='_text_':
        for d in doc.content:
            i=0
            for d in doc.content:
                trova2(d,sel,lista)
                if 1 in lista:
                    del doc.content[i]
                    lista=[]
                else:
                    i+=1


def conta3(doc,sel,chiave,valore):
    if sel[0]!='>':
        trova3(doc,sel,chiave,valore)
    else:
        if sel[1][0]=='.':
            if 'class' in doc.attr.keys():
                if sel[1][1:] in doc.attr['class']:
                    if len(sel)==2:
                        doc.attr[chiave]=valore
                    else:
                        for d in doc.content:
                            conta3(d,sel[2:],chiave,valore)
        elif sel[1][0]=='#':
            if 'id' in doc.attr:
                if doc.attr['id']==sel[1][1:]:
                    if len(sel)==2:
                        doc.attr[chiave]=valore
                    else:
                        for d in doc.content:
                            conta3(d,sel[2:],chiave,valore)
        elif sel[1][0]=='@':
            if sel[1][2:sel[1].find('=')] in doc.attr.keys():
                if doc.attr[sel[1][2:sel[1].find('=')]]==sel[1][sel[1].find('=')+2:len(sel[1])-2]:
                    if len(sel)==2:
                        doc.attr[chiave]=valore
                    else:
                        for d in doc.content:
                            conta3(d,sel[2:],chiave,valore)
        elif sel[1]=='_text_':
            if doc.tag=='_text_':
                doc.attr[chiave]=valore
        elif doc.tag== sel[1]:
            if len(sel)==2:
                doc.attr[chiave]=valore
            else:
                for d in doc.content:
                    conta3(d,sel[2:],chiave,valore)
    
def trova3(doc,sel,chiave,valore):
    if sel[0][0]=='.':
        if 'class' in doc.attr.keys():
            if sel[0][1:] in doc.attr['class']:
                if len(sel)==1:
                    doc.attr[chiave]=valore
                else:
                    for d in doc.content:
                        conta3(d,sel[1:],chiave,valore)
    elif sel[0][0]=='#':
        if 'id' in doc.attr:
            if doc.attr['id']==sel[0][1:]:
                if len(sel)==1:
                    doc.attr[chiave]=valore
                else:
                    for d in doc.content:
                        conta3(d,sel[1:],chiave,valore)
    elif sel[0][0]=='@':
        if sel[0][2:sel[0].find('=')] in doc.attr.keys():
            if doc.attr[sel[0][2:sel[0].find('=')]]==sel[0][sel[0].find('=')+2:len(sel[0])-2]:
                if len(sel)==1:
                    doc.attr[chiave]=valore
                else:
                    for d in doc.content:
                        conta3(d,sel[1:],chiave,valore)
    elif sel[0]=='_text_':
        if doc.tag=='_text_':
            doc.attr[chiave]=valore
    elif doc.tag== sel[0]:
        if len(sel)==1:
            doc.attr[chiave]=valore
        else:
            for d in doc.content:
                conta3(d,sel[1:],chiave,valore)
    if doc.tag!='_text_':
        for d in doc.content:
            trova3(d,sel,chiave,valore)

    
def stampa(s):
    doc=fparse(s)
    doc.print_tree()
    print()
    print()
    print(doc.to_string())                        
        
    
def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    doc=fparse(fileIn)
    lsel=selettore.split()
    lista=[]
    trova(doc,lsel,lista)
    return len(lista)

    
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    doc=fparse(fileIn)
    lsel=selettore.split()
    trova2(doc,lsel)
    f=open(fileOut,'w',encoding='utf-8')
    f.write(doc.to_string())
    f.close()
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    doc=fparse(fileIn)
    lsel=selettore.split()
    trova3(doc,lsel,chiave,valore)
    f=open(fileOut,'w',encoding='utf-8')
    f.write(doc.to_string())
    f.close()

