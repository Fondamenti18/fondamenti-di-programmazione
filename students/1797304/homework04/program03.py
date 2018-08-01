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
from copy import *
from  my_html import HTMLNode, fparse

def conta_nodi(fileIn, selettore):
        radice=fparse(fileIn)
        d=decodifica_selettore(selettore)
        lista=[radice]
        if len(d)==1:
            ris=(cerca_nodi(d,lista,[]))
            return len(ris)
        else:
            nodi=cerca_nodi(d,lista,[])
            ris=check_rapporti(d[1:],nodi)
            return len(ris)
                
            
                
            
        
def cerca_nodi(selettore,lista,nodi):
    if lista==[]:
        return nodi
    else:
        lista2=[]
        if len(selettore[0])==1:
           for x in lista:
               if x.istext():
                  next
               else:
                  lista2+=x.content
                  if x.tag == (selettore[0])[0]:
                    nodi.append(x)
           return cerca_nodi(selettore,lista2,nodi)
        else:
           s=selettore[0]
           if s[0]=='.':
               for x in lista:
                 if x.istext():
                    next
                 else:
                    lista2+=x.content
                    diz=x.attr
                    if 'class' in diz.keys():
                       if s[1] in diz['class']:
                         nodi.append(x)
               return cerca_nodi(selettore,lista2,nodi)
           elif s[0]=='#':
                for x in lista:
                 if x.istext():
                    next
                 else:
                    lista2+=x.content
                    diz=x.attr
                    if 'id' in diz.keys():
                       if s[1] == diz['id']:
                         nodi.append(x)
                return cerca_nodi(selettore,lista2,nodi)
           elif s[0]=='@':
                for x in lista:
                 if x.istext():
                    next
                 else:
                    lista2+=x.content
                    diz=x.attr
                    if s[1] in diz.keys():
                       if diz[s[1]] == s[2]:
                         nodi.append(x)
                return cerca_nodi(selettore,lista2,nodi)

def check_rapporti(selettore,lista):
    lista2=lista
    selettore2=deepcopy(selettore)
    while selettore2 != []:
           s=selettore2[0]
           if len(s)==1:
               if s[0]=='>':
                   nodi=[]
                   selettore2=selettore2[1:]
                   s=selettore2[0]
                   for n in lista2:
                       if n.istext():
                           next
                       else:
                           nodi+=n.content
                   ris=check_nodi(nodi,s)
                   if ris==[]:
                       selettore2=selettore2[1:]
                       lista2=[]
                   else:
                       lista2=ris
                       selettore2=selettore2[1:]
               else:
                   risultati=[]
                   for n in lista2:
                      ris=cerca_nodi([s],[n],[])
                      risultati+=ris
                   if risultati==[]:
                        selettore2=selettore2[1:]
                        lista2=[]
                   else:
                        selettore2=selettore2[1:]
                        lista2=risultati 
           else:
                risultati=[]
                for n in lista2: 
                      ris=cerca_nodi([s],[n],[])
                      risultati+=ris
                if ris==[]:
                    selettore2=selettore2[1:]
                    lista2=[]
                else:
                   selettore2=selettore2[1:]
                   lista2=risultati        
    return lista2
                        
                   
                       
            
            
    

def check_nodi(lista,selettore):
    risultato=[]
    if len (selettore) ==1:
           for x in lista:
               if x.istext():
                  next
               else:
                  if x.tag == selettore[0] :
                    risultato.append(x)
    else:
          if selettore[0]=='.':
               for x in lista:
                 if x.istext():
                    next
                 else:
                    diz=x.attr
                    if 'class' in diz.keys():
                       if selettore[1] in diz['class']:
                         risultato.append(x)
          elif selettore[0]=='#':
                for x in lista:
                 if x.istext():
                    next
                 else:
                    diz=x.attr
                    if 'id' in diz.keys():
                       if selettore[1] == diz['id']:
                         risultato.append(x)
          elif selettore[0]=='@':
                for x in lista:
                 if x.istext():
                    next
                 else:
                    diz=x.attr
                    if selettore[1] in diz.keys():
                       if diz[selettore[1]] == selettore[2]:
                         risultato.append(x) 
    return risultato          
                
            
                  
                    
                
                
                
            
        
        
def decodifica_selettore(sel):
    selettore=sel.split()
    decodificato=[]
    indicatori=('.','@','#',)
    for i in range(len(selettore)):
       if selettore[i]=='>':
           decodificato.append(['>'])
       elif selettore[i].isalnum():
           decodificato.append([selettore[i]])
       else:
          for c in selettore[i]:
             if c  in indicatori:
                 if c=='@':
                     x= selettore[i].split(c)
                     x.remove('')
                     x=list(x[0])
                     x.remove('[')
                     x.remove(']')
                     if '"'in x:
                         x.remove('"')
                         x.remove('"')
                     x=('').join(x)
                     x=x.split('=')
                     x.insert(0,c)
                     decodificato.append(x)
                 else:    
                     x= selettore[i].split(c)
                     x.insert(0,c)
                     x.remove('')
                     decodificato.append(x)
                     break
               
    return decodificato
    
    
def elimina_nodi(fileIn, selettore, fileOut):
        radice=fparse(fileIn)
        d=decodifica_selettore(selettore)
        lista=[radice]
        if len(d)==1:
            ris=(cerca_nodi(d,lista,[]))
            elimina(ris,lista)
        else:
            nodi=cerca_nodi(d,lista,[])
            ris=check_rapporti(d[1:],nodi)
            elimina(ris,lista)
        with open(fileOut,mode='w',encoding='utf-8') as d:
            risultato=radice.to_string()
            d.write(risultato)   
            
        
        
            
        
        
def elimina(d,lista):
    if d==[]:
        return 
    else:
        lista2=[]
        for x in lista:
             if x.istext():
                  next
             else:
                  contenuto=x.content
                  for n in contenuto:
                    if n in d:
                      x.content.remove(n)
                      d=d[1:]
                    else:
                        next
                  lista2+=x.content
        return elimina(d,lista2)
    
def elimina_contenuto(nodo):
    if nodo==[]:
        return
    else:
        lista=[]
        for n in nodo:
            n.content=[]
            lista+=n.content
        return elimina_contenuto(lista)
    
        
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
        radice=fparse(fileIn)
        d=decodifica_selettore(selettore)
        lista=[radice]
        nodi=cerca_nodi(d,lista,[])
        ris=check_rapporti(d[1:],nodi)
        cambia(ris,chiave,valore)
        with open(fileOut,mode='w',encoding='utf-8') as d:
            risultato=radice.to_string()
            d.write(risultato)
            
       
        
    
def cambia(lista,k,v):
    if lista==[]:
        return
    else:
       nodo=lista[0]
       diz=nodo.attr
       diz.update({k:v})
       return cambia(lista[1:],k,v)
        
