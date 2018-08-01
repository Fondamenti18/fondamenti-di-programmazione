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
   if padre[0] == '@':
        coconut=x.strip('@[ ]')
            #print(coconut)
        coconut=coconut.split('=')
        coconuut=coconut[1].strip('"')
        coconuts=coconut[0]
'''

from  my_html import HTMLNode, fparse
from copy import copy
def vis(c,selettore,count):
    box=0
    if c.tag != '_text_':
        #print(c.tag)
        #print(c.attr.keys())
        for x in list(c.attr.keys()):
            if x == 'id':
                if selettore.strip('#') in c.attr[x]:
            #print(c.attr)
                    return selettore
        for x in c.content:
            count+=[(vis(x,selettore,count))]

    return count
def vis2(c,selettore,count):
    box=0
    if c.tag != '_text_':
        #print(c.tag)
        #print(c.attr.keys())
        for x in list(c.attr.keys()):
            if x == 'class':
                if selettore.strip('.') in c.attr[x]:
            #print(c.attr)
                    return selettore
        for x in c.content:
            count+=[(vis2(x,selettore,count))]

    return count
def vis3(c,selettore,count,att):
    box=0
    if c.tag != '_text_':
        #print(c.attr)
        #print(c.attr.keys())
        for x in list(c.attr.keys()):
            if x == att:
                #print(x)
                if selettore in c.attr[x]:
            #print(c.attr)
                    #print(selettore)
                    return selettore
        for x in c.content:
            count+=[(vis3(x,selettore,count,att))]

    return count

def vis1(c,selettore,count):
    box=0
    #print(c.tag)
    if c.tag != '_text_':
        #print(c.tag)
        #print(c.attr.values())
        if selettore == c.tag:
            #print(c.attr)
            #print('ciao')
            return selettore
        for x in c.content:
            #print(x.tag)
            count+=[(vis1(x,selettore,count))]

    return count

def unity(selettore,count,c):
    if selettore[0] == '#':
        (vis(c,selettore,count))
        
    if selettore[0] != '#' and selettore[0] != '.' and selettore[0] != '@':
        vis1(c,selettore,count)
    if selettore[0] == '.':
        vis2(c,selettore,count)
    if selettore[0] == '@':
        coconut=selettore.strip('@[ ]')
        coconut=coconut.split('=')
        coconuut=coconut[1].strip('"')
        coconuts=coconut[0]
        vis3(c,coconuut,count,coconuts)
        selettore=coconuut
    
    
    return count.count(selettore)

def prova(c,selettore,count,padre,figlioO,padreO,lv):
    box=0
    #print(lv)
    #print(c.tag)
 
    if c.tag != '_text_':
        #print(c.tag)
        
        if c.tag == figlioO and padreO == padre:
            #print(c.tag,padre) #idea yasssuo
            #print(c.tag,padre)
            return c.tag
        for x in c.content:
            #print(x.tag)
            count+=[(prova(x,selettore,count,c.tag,figlioO,padreO,lv))]
            
    return count

def baba(x,c,lv,avo,disc,lvl):
    if x.tag != '_text_':
        #print(x.tag,lv,c.tag)
        #print(lvl)
        #lvl=lv
        #print(lvl,lv)
        #if x.tag == avo:
            #print(avo)
            #lvl = lv
        if x.tag == disc and c.tag == avo:
            return x.tag
            #print('fatto')
            #print(x.tag)
        #print(x.close_tag())
        for y in x.content:
            #print(y.tag)
            #lvl=lv
            if lv == 0:
                lvl+=[baba(y,x,lv+1,avo,disc,lvl)]
            else:
                lvl+=[baba(y,c,lv+1,avo,disc,lvl)]
    return lvl
def antenati(c,avo1,disc,count,avo):
    box=0
    #print(c.tag)
    if c.tag != '_text_':
        #print(c.tag)
        if c.tag == avo1:
            count=baba(c,c,0,avo1,disc,count)
            
        for x in c.content:
            #print(x.tag)
            #if x.tag == 'p':
            antenati(x,avo1,disc,count,c.tag)
            #baba(x,c,0,avo,disc,0)
            #print(c.tag)
            #count+=[(antenati(x,avo1,disc,count,c.tag))]

    return count
def decomponi(stringa):

    coconut=stringa.strip('@[ ]')
    coconut=coconut.split('=')
    coconuut=coconut[1].strip('"')
    coconuts=coconut[0]
    return [coconuts,coconuut]

def link(padre,figlio,padre0,c):
    if c.tag != '_text_':
        #if c.tag == 'article':
            
            #print(c.tag)
        #if c.tag in figlio:
            #print(c.tag)
        for y in list(padre0.attr.keys()):
            if padre[0] == y:
               # print(padre[1])
                if padre[1] == padre0.attr[y]:
                    #print(c.tag)
                    #print(padre[1],c)
                    if c.tag == figlio:
                        return c
        
        for x in c.content:
            popo= link(padre,figlio,c,x)
            if popo is not None:
                return popo
                    
                    
def parentela(avo,disc,avo1,lv,padrone):             
    if avo.tag != '_text_':
       # print(avo.tag,lv,padrone)
        #print(avo)
        if avo.tag == disc and avo1 == padrone:
            #print(avo)
            return avo
        for x in avo.content:
            if lv == 0:
                popo=parentela(x,disc,avo1,lv+1,avo)
                if popo is not None:
                    return popo
            else:
                popo=parentela(x,disc,avo1,lv+1,padrone)
                if popo is not None:
                    return popo
def hdlink(supremo,figlio,padre):
    if supremo.tag != '_text_':
        if figlio == supremo.tag:
            return supremo
        for x in supremo.content:
            
            hdlink(x,figlio,padre)
    return 0

def linkE(padre,figlio,padre0,c,E):
    if c.tag != '_text_':
        #if c.tag == 'article':
            
            #print(c.tag)
        #if c.tag in figlio:
            #print(c.tag)
        for y in list(padre0.attr.keys()):
            if padre[0] == y:
               # print(padre[1])
                if padre[1] == padre0.attr[y]:
                    #print(c.tag)
                    #print(padre[1],c)
                    if c.tag == figlio and c not in  E:
                        #print(c.tag,E)
                        return c
        
        for x in c.content:
            popo= linkE(padre,figlio,c,x,E)
            if popo is not None:
                return popo
def mostro(selex,c):
    print(selex)
    x=0
    if selex[x][0] == '@':
        ls=decomponi(selex[x])
        if selex[x+1][0] == '@':
            lx=decomponi(selex[x+1])
        if ' ' in selex[x+1].rstrip().lstrip():
            pelo=selex[x+1].rstrip().lstrip()
            figlio=pelo.split(' ')
            #print(figlio)
            lelo=link(ls,figlio[0],c,c)
            pepepe=parentela(lelo,figlio[1],lelo,0,lelo)
            supremo=pepepe
            #print(supremo.tag)
            if 0 == hdlink(supremo,selex[x+2],supremo):
                E=[lelo]
                panda=linkE(ls,figlio[0],c,c,E)
                #print(panda)
                pepepe=parentela(panda,figlio[1],panda,0,panda)
                #print(pepepe)
                supremo=pepepe
                pene=hdlink(supremo,selex[x+2],supremo)
                if pene == 0:
                    E+=[panda]
                    panda=linkE(ls,figlio[0],c,c,E)
                #print(panda)
                    pepepe=parentela(panda,figlio[1],panda,0,panda)
                #print(pepepe)
                    supremo=pepepe
                    pene=hdlink(supremo,selex[x+2],supremo)
                            
                            #print(pene)          
                    #print(pene)
                #if panda == lelo:
                    #print('coglione')
                
          
def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
    c=fparse(fileIn)
    #print(selettore)
    #print(c.tag)
    if selettore.count('>') >1:
        #print('ciao')
        selex=selettore.split('>')
        mostro(selex,c)
        #pappa(c,poro,selettore.count('>'),selettore.count('>'),c,padre)
        #pappa(c)
    #☺print(c.print_tree())
    #print(c.to_string())
    #☺print('\n')
    #trasfomare padre in una lista di padri
    #print(selettore)
    #cane=selettore.split('>')
    #print(cane)
    #prova(c,selettore,count,)
    #print(cane)
    #for x in cane:
     #   if x[0] == '@':
            #print(x)
            
            #print(coconuut,coconuts)
    #idea per il test 14, contare i figli padre, e contare poi dopo averli splittati gli avi disc
    #dopo aver ricavato padri figli, avi disc,  fare in modo ricorsivo per tot figli e solo quando, arriva a 0 il contatore del lv restit il count delle occorrenze 
    count=[]
    if ' ' in selettore and '>' not in selettore:
        poppo=selettore.split()
        pepe=antenati(c,poppo[0],poppo[1],count,c.tag)
        #baba(c,c,0,poppo[0],poppo[1],0)
        return pepe.count(poppo[1])
        #for x in pepe:
            #if x != [...]:
                #print(x)
    if '>' in selettore:
        #print('ciao')
        popo = selettore.split('>')
        #print()
        padre=popo[0].strip(' ')
        figlio=popo[1].strip(' ')
        #print(padre)
        papa=prova(c,selettore,count,c.tag,figlio,padre,selettore.count('>'))
        return papa.count(figlio)
    else:
    
    
    
        return unity(selettore,count,c)
    #print(coconuut)

    #for x in c.content:
     #   print(x.tag)
      #  if x.tag != '_text_':
       #     print(x.attr)
    #print(c.content)
    
def find_by_tag(nodo, tag):
    '''Ritorna una lista dei nodi che hanno il tag'''
    ret = []
    if nodo.tag == tag: ret += [nodo]
    if nodo.tag!='_text_':
        for figlio in nodo.content:
            ret += find_by_tag(figlio,tag)
    return ret
def remove_by_tag(nodo, tag):
    if nodo.tag=='_text_': return
    for figlio in nodo.content:
        remove_by_tag(figlio,tag)
    newcontent = []
    for figlio in nodo.content:
        if figlio.tag == tag:
            if nodo.tag!='_text_':
                newcontent += figlio.content
        else:
            newcontent += [figlio]
        nodo.content = newcontent

def cdiscen(c,disc,x):
    if c.tag != '_text_':
        #print(c.tag,x)
        newcontenet=[]
        if c.tag == disc:
            #print(c.content)
            #c.content=[' ']
            #HTMLNode('a','',['cane'])
            x.content.remove(c)
            
            
            
            #x.content=[' ']
            return
            #remove_by_tag(x,c.tag)
            #print(c.content)
            #print(x)
            #del c
            #print(c)
            #del c
            
            #c.tag=''
            #c.attr=''
            #c.content=newcontenet
            
            #return
            #print(c.attr)
        for x in c.content:
            cdiscen(x,disc,c)
            
            
def cvis4(c,selettore,y):
    box=0
    if c.tag != '_text_':
        #print(c.tag)
        #print(c.attr.keys())
        for x in list(c.attr.keys()):
            if x == 'id':
                if selettore.strip('#') in c.attr[x]:
            #print(c.attr)
                    
                    y.content.remove(c)
                    #print(c.attr)
        for x in c.content:
            (vis4(x,selettore,c))
def cvis5(c,selettore,y):
    box=0
    if c.tag != '_text_':
        #print(c.tag)
        #print(c.attr.keys())
        for x in list(c.attr.keys()):
            if x == 'class':
                if selettore.strip('.') in c.attr[x]:
            #print(c.attr)
                    y.content.remove(c)
                    
        for x in c.content:
            (cvis5(x,selettore,c))
            
            
def cvis6(c,selettore,att,y):
    box=0
    if c.tag != '_text_':
        #print(c.attr)
        #print(c.attr.keys())
        for x in list(c.attr.keys()):
            if x == att:
                #print(x)
                if selettore in c.attr[x]:
            #print(c.attr)
                    #print(selettore)
                    y.content.remove(c)
                    
                    #return selettore
        for x in c.content:
           (cvis6(x,selettore,att,c))
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice
    c=fparse(fileIn)
    Html_file= open(fileOut,"w")
    #print(c)
    if ' ' in selettore.rstrip().lstrip():
        #print('cacca')
        cane=selettore.rstrip().lstrip().split()
        #print(cane)
        cavallo=find_by_tag(c,cane[0])
        for x in cavallo:
            #print(x)
            cdiscen(x,cane[1],cane[1])
        #print(c.to_string())
        Html_file.write(c.to_string())
    if selettore[0] == '@':
        coconut=selettore.strip('@[ ]')
        coconut=coconut.split('=')
        coconuut=coconut[1].strip('"')
        coconuts=coconut[0]
        cvis6(c,selettore,coconuts)
        Html_file.write(c.to_string())
    if selettore[0] == '#':
        cvis4(c,selettore,selettore)
        Html_file.write(c.to_string())
    if selettore[0] == '.':
        cvis5(c,selettore,selettore)
        Html_file.write(c.to_string())   
     
    
    
    
    
    

def discen(c,disc,chiave,valore):
    if c.tag != '_text_':
        #print(c.tag)
        if c.tag == disc:
            #print(c.attr)
            c.attr[chiave] = valore
            #print(c.attr)
        for x in c.content:
            discen(x,disc,chiave,valore)
            
def vis4(c,selettore,chiave,valore):
    box=0
    if c.tag != '_text_':
        #print(c.tag)
        #print(c.attr.keys())
        for x in list(c.attr.keys()):
            if x == 'id':
                if selettore.strip('#') in c.attr[x]:
            #print(c.attr)
                    
                    c.attr[chiave]=valore
                    #print(c.attr)
        for x in c.content:
            (vis4(x,selettore,chiave,valore))
def vis5(c,selettore,chiave,valore):
    box=0
    if c.tag != '_text_':
        #print(c.tag)
        #print(c.attr.keys())
        for x in list(c.attr.keys()):
            if x == 'class':
                if selettore.strip('.') in c.attr[x]:
            #print(c.attr)
                    c.attr[chiave],valore
                    
        for x in c.content:
            (vis5(x,selettore,chiave,valore))
            
            
def vis6(c,selettore,chiave,valore,att):
    box=0
    if c.tag != '_text_':
        #print(c.attr)
        #print(c.attr.keys())
        for x in list(c.attr.keys()):
            if x == att:
                #print(x)
                if selettore in c.attr[x]:
            #print(c.attr)
                    #print(selettore)
                    c.attr[chiave]=valore
                    #return selettore
        for x in c.content:
           (vis6(x,selettore,chiave,valore,att))

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    c=fparse(fileIn)
    Html_file= open(fileOut,"w")
    #print(fileOut)
    #print(selettore)
    if selettore[0] == '@':
        coconut=selettore.strip('@[ ]')
        coconut=coconut.split('=')
        coconuut=coconut[1].strip('"')
        coconuts=coconut[0]
        vis6(c,selettore,chiave,valore,coconuts)
        Html_file.write(c.to_string())
    if selettore[0] == '#':
        vis4(c,selettore,chiave,valore)
        Html_file.write(c.to_string())
    if selettore[0] == '.':
        vis5(c,selettore,chiave,valore)
        Html_file.write(c.to_string())
    if ' ' in selettore.rstrip().lstrip():
        #print('cacca')
        cane=selettore.rstrip().lstrip().split()
        #print(cane)
        cavallo=find_by_tag(c,cane[0])
        for x in cavallo:
            discen(x,cane[1],chiave,valore)    
        Html_file.write(c.to_string())
    #Inserite qui il vostro codice
   
    
  
fileIn    = 'page1-3.html'
   
fileOut   = 'test9.html'
    
fileExp   = 'risTest9-3.html'
    
selettore = 'p a'


elimina_nodi(fileIn, selettore, fileOut)
#cambia_attributo(fileIn, selettore, chiave, valore, fileOut)
#fileOut   = 
#print(conta_nodi(fileIn,selettore))
#elimina_nodi(fileIn,selettore,fileOut)