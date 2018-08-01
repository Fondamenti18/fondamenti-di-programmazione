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

def conta(albero,selettore,tot):
    if selettore[0]=='#':
        try:
            if albero.attr['id']==selettore[1:]: tot.append(albero)
        except:pass
    elif selettore[0]=='.':
        try:
            if selettore[1:] in albero.attr['class']: tot.append(albero)
        except:pass        
    elif selettore[0]=='@':
        try:
            nome=selettore[2:].split('=')[0]
            if albero.attr[nome]==selettore[2:].split('=')[1].split('"')[1]: tot.append(albero)
        except:pass
    elif albero.tag==selettore: tot.append(albero)
    if not albero.istext():
        lista=albero.content
        for el in lista: tot=conta(el,selettore,tot)
    return tot

def ricorsiva(lista,selettore):
    '''questa funzione mi genera una lista con tutti i nodi dei nodi in lista
    che soddisfano il selettore '''
    ris=[]
    for el in lista:
        ris+=conta(el,selettore,[])
    return ris

def verificaFiglio(lista,selettore):
    tot=[]
    for nodo in lista:
        figli=nodo.content
        for figlio in figli:
            if selettore[0]=='#':
                try:
                    if figlio.attr['id']==selettore[1:]: tot.append(figlio)
                except:pass
            elif selettore[0]=='.':
                try:
                    if selettore[1:] in figlio.attr['class']: tot.append(figlio)
                except:pass        
            elif selettore[0]=='@':
                try:
                    nome=selettore[2:].split('=')[0]
                    if figlio.attr[nome]==selettore[2:].split('=')[1].split('"')[1]: tot.append(figlio)
                except:pass
            elif figlio.tag==selettore: tot.append(figlio)
    return tot

     
def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    albero=fparse(fileIn) # crea l'albero a partire dal file
    lista=[albero]
    k=selettore.split('>')
    tot=[]
    flag=False
    for j in k:
        if flag:
            sel=j.split()[0]
            lista1=[]
            lista1=verificaFiglio(lista,sel)
            lista=lista1
            l=j.split()[1:]
        else: l=j.split() # dentro l avro tutti i partenti del tag finale
        flag=True
        tot=[]
        for sel in l:
            lista=ricorsiva(lista,sel)
        tot+=lista
    return len(tot)

def elimina(albero,indice,lista,selettore,f):
    if selettore[0]=='#':
        try:
            if albero.attr['id']==selettore[1:]:
                del(lista[f-indice-1])
        except:pass
    elif selettore[0]=='.':
        try:
            if selettore[1:] in albero.attr['class']:
                del(lista[f-indice-1])
        except:pass        
    elif selettore[0]=='@':
        try:
            nome=selettore[2:].split('=')[0]
            if albero.attr[nome]==selettore[2:].split('=')[1].split('"')[1]:
                del(lista[f-indice-1])
        except:pass
    elif albero.tag==selettore:
        del(lista[f-indice-1])
    if not albero.istext():
        lista1=albero.content
        k=len(lista1)
        for indice,el in enumerate(lista1[::-1]): tot=elimina(el,indice,lista1,selettore,k)
    return

def ricorsiva2(lista,selettore,flag):
    ris=[]
    if flag:
        for indice,el in enumerate(lista[::-1]):
            elimina(el,indice,lista,selettore,0)
    else:
        for el in lista: 
            ris+=cambia2(el,selettore,[])
    return ris

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    albero=fparse(fileIn) # crea l'albero a partire dal file
    lista=[albero]
    k=selettore.split('>')
    flag=False
    for j in k[:-1]:
        if flag:
            sel=j.split()[0]
            lista1=[]
            lista1=verificaFiglio(lista,sel)
            lista=lista1
            l=j.split()[1:]
        else: l=j.split() # dentro l avro tutti i partenti del tag finale
        flag=True
        for sel in l:
            lista=ricorsiva2(lista,sel,False)
    #-----------------------------------------------------
    if flag:
        sel=k[-1].split()[0]
        lista1=[]
        lista1=verificaFiglio(lista,sel)
        lista=lista1
        l=k[-1].split()[1:]
    else: l=k[-1].split() # dentro l avro tutti i partenti del tag finale
    for sel in l[:-1]:
        lista=ricorsiva2(lista,sel,False)
    lista=ricorsiva2(lista,l[-1],True)
    #----------------------------------------------------
    with open(fileOut,'w') as f:
        f.write(albero.to_string())

def cambia(albero,selettore,tot,chiave,valore):
    if selettore[0]=='#':
        try:
            if albero.attr['id']==selettore[1:]:
                tot.append(albero)
                albero.attr[chiave]=valore
        except:pass
    elif selettore[0]=='.':
        try:
            if selettore[1:] in albero.attr['class']:
                tot.append(albero)
                albero.attr[chiave]=valore
        except:pass        
    elif selettore[0]=='@':
        try:
            nome=selettore[2:].split('=')[0]
            if albero.attr[nome]==selettore[2:].split('=')[1].split('"')[1]:
                tot.append(albero)
                albero.attr[chiave]=valore
        except:pass
    elif albero.tag==selettore:
        tot.append(albero)
        albero.attr[chiave]=valore
    if not albero.istext():
        lista=albero.content
        for el in lista: tot=cambia(el,selettore,tot,chiave,valore)
    return tot

def cambia2(albero,selettore,tot):
    if selettore[0]=='#':
        try:
            if albero.attr['id']==selettore[1:]:
                tot.append(albero)
        except:pass
    elif selettore[0]=='.':
        try:
            if selettore[1:] in albero.attr['class']:
                tot.append(albero)
        except:pass        
    elif selettore[0]=='@':
        try:
            nome=selettore[2:].split('=')[0]
            if albero.attr[nome]==selettore[2:].split('=')[1].split('"')[1]:
                tot.append(albero)
        except:pass
    elif albero.tag==selettore:
        tot.append(albero)
    if not albero.istext():
        lista=albero.content
        for el in lista: tot=cambia2(el,selettore,tot)
    return tot
        
def ricorsiva3(lista,selettore,chiave,valore,flag):
    ris=[]
    for el in lista:
        if flag:
            ris+=cambia(el,selettore,[],chiave,valore)
        else: ris+=cambia2(el,selettore,[])
    return ris

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    albero=fparse(fileIn) # crea l'albero a partire dal file
    lista=[albero]
    k=selettore.split('>')
    flag=False
    for j in k:
        if flag:
            sel=j.split()[0]
            lista1=[]
            lista1=verificaFiglio(lista,sel)
            lista=lista1
            l=j.split()[1:]
        else: l=j.split() # dentro l avo tutti i partenti del tag finale
        flag=True
        for sel in l[:-1]:
            lista=ricorsiva3(lista,sel,chiave,valore,False)
        lista=ricorsiva3(lista,l[-1],chiave,valore,True)
    with open(fileOut,'w') as f:
        f.write(albero.to_string())
