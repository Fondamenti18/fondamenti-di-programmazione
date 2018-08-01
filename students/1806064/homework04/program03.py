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
import html
import copy

with open("page1-3.html") as f:
    f=BeautifulSoup(f,"lxml")

def conta_nodi(fileIn, selettore):
    f=fparse(fileIn)
    f=f.to_string()
    f=BeautifulSoup(f,"lxml")
    selettore=clean(selettore)
    return len(f.select(selettore))

def clean(stringa):
    if stringa.startswith("@"):
        return stringa[1:]
    else:
        return stringa
    
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    with open(fileIn) as f:
        f=BeautifulSoup(f,"lxml")
    stringa=fparse(fileIn)
    stringa=stringa.to_string()
    selettore=clean(selettore)
    nodi_da_eliminare=f.select(selettore)
    stringa=scorri_tag(nodi_da_eliminare,stringa,[])
    with open(fileOut,"w",encoding="utf-8") as d:
        d.write(stringa)
        
def scorri_tag(lista,stringa,output):
    if lista==[]:
        return output[0]
    if str(lista[0]) in stringa:
        stringa=stringa.replace(str(lista[0]),"")
        output.append(stringa)
    scorri_tag(lista[1:],stringa,output)
    return output[-1]

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    with open(fileIn) as f:
        f=BeautifulSoup(f,"lxml")
    selettore=clean(selettore)
    stringa=fparse(fileIn)
    stringa=stringa.to_string()
    lista=f.select(selettore)
    lista_attributes=[]
    c=0
    lista_attributes=copia_nodi(lista)
    lista=cambia_attributi(lista,chiave,valore)
    for i in lista_attributes:
        i=i.split("\n")
        if i[0] in stringa:
            stringa=stringa.replace(i[0],str(lista[c]).split("\n")[0])
        c+=1
    with open(fileOut,"w",encoding="utf-8") as j:
        j.write(stringa)

def cambia_attributi(lista,chiave,valore):
    if lista==[]:
        return lista
    lista[0][chiave]=valore
    cambia_attributi(lista[1:],chiave,valore)
    return lista

def copia_nodi(lista):
    lista_copiata=[]
    for i in lista:
        lista_copiata.append(str(i))
    return lista_copiata
        
    



   
    
    
    
        
    
    
    
    
    

