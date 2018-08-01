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
import my_html 
from bs4 import BeautifulSoup as Bsoup

def classe(albero,soup,selettore,cont):
    lista=[]
    for lettera in selettore:
        lista.append(lettera)
    lista.remove('.')
    classe=''.join(lista)
    taggo=albero.tag
    if classe in soup.taggo['class']:
        for k in albero.content:
            return 1+conto((my_html.HTMLNode(k,{},[])),soup,selettore,cont)
    return 0

def tags(albero,lista):
    lista.append(albero.tag)
    for el in albero.content:
        lista.append(el.tag)
    for k in albero.content:
        lista+=tags(k,lista)
    return lista

def conto(albero,soup,selettore,cont):
    if selettore.startswith('#'):
        lista=[]
        for lettera in selettore:
            lista.append(lettera)
        lista.remove('#')
        selettore1=''.join(lista)
        for x in soup.find_all(id=selettore1):
            cont+=1
        return cont
    if selettore.startswith('.'):
        lista=[]
        return classe(albero,soup,selettore,cont)
                            
                            
                            


def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    albero=my_html.fparse(fileIn)
    page=open(fileIn)
    soup=Bsoup(page,'html.parser')
    cont=0
    if selettore.startswith('#') or selettore.startswith('.'):
        return conto(albero,soup,selettore,cont)
    if selettore.startswith('@'):
        lista=[]
        for lett in selettore:
            lista.append(lett)
        lista.remove('@')
        lista.remove('[')
        lista.remove(']')
        selettore2=''.join(lista)
        b=selettore2.split('=')
        attributo=b[1]
        for elemento in soup.find_all(width=attributo):
            cont+=1
        return cont
        
    if len(selettore)==3:
        listaselettori=selettore.split(' ')
        avo=listaselettori[0]
        discendente=listaselettori[1]
        for elemento in soup.find_all(avo):
            for el in elemento.find_all(discendente):
                cont+=1
        return cont
    for k in soup.find_all(selettore):
        cont+=1
    return cont
        
    

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    albero=my_html.fparse(fileIn)
    lista=selettore.split(' ')
    lista1=[]
    
    for x in lista:
        lista1.append('<'+x+'>')
    for k in lista1:
        for nodo in albero.content:
            remove_by_tag(nodo, k)
    
    with open(fileOut, 'w') as f:
        f.write(albero.to_string())



def change(albero,selettore,chiave, valore):
    if type(albero)!=str:
        pass
    else:
        albero=my_html.HTMLNode(albero,{},[])
    lista=[]
    for lett in selettore:
        lista.append(lett)
    selettore2=''.join(lista)
    b=selettore2.split('=')
    for k in albero.content:
        return change(k,selettore,chiave, valore)



def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    albero=my_html.fparse(fileIn)
    return change(albero,selettore,chiave, valore)
    
        
        
    
    
def remove_by_tag(nodo, tag):
    '''Rimuove dall'albero tutti i nodi con il tag, esclusa la radice,
    cioè il nodo su cui è invocato il metodo.'''
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
                    