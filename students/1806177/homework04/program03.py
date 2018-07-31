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

def selezione(selettore):
    varia=selettore[0]
    if varia=='#':
        jack=selettore[1:]
        return 'id',jack
    elif varia=='.':
        jack=selettore[1:]      
        return 'class',jack
    elif varia=='@':
        jack=selettore[2:len(selettore)-1]
        jack=jack.replace(' ','')
        jack=jack.replace('\"','')
        jack=jack.split('=')
        return jack[0],jack[1]
    else:
        return 'tag',selettore 




def children(varia,selettore):
    vittoria=[]
    for bello in varia:
       if not bello.istext():
           if selettore[0]=='tag' and selettore[1]==bello.tag:
            vittoria+=[bello]
           elif selettore[0] in list(bello.attr.keys()):
              if selettore[1] in bello.attr[selettore[0]]:
                  vittoria+=[bello]
    return vittoria           
           

def studio(file,selettore): 
    vittoria=[]
    if not file.istext():
        if selettore[0]=='tag' and selettore[1]==file.tag:
            return [file]
        elif selettore[0] in list(file.attr.keys()):  
              if  selettore[1] in file.attr[selettore[0]] :
                  return [file]               
        for i in file.content:
           vittoria+= studio(i,selettore)
    return vittoria



def sistema(varia):
    for bello in range(len(varia)):
        varia[bello]=varia[bello].split('>')
    for variazione in range(len(varia)):
        for j in range(len(varia[variazione])):
            varia[variazione][j] = selezione(varia[variazione][j])
      
    return varia   

            


def norm(selettore): 
    varia=[]
    while True:
        sel=selettore.find(' ')
        if sel!=-1:
            if '>' not in [selettore[sel-1],selettore[sel+1]]:
                varia.append(selettore[:sel])
                selettore=selettore[sel+1:]
            else:
                selettore=selettore.replace(" ","",1)
        else:
            break
    varia.append(selettore)
    varia=sistema(varia)
    return varia   



def crescendo(selettor,varia):
        for bello in range(len(selettor)):
            conto=[]
            for y in range(len(varia)):
                conto+=studio(varia[y],selettor[bello][0])
            if len(selettor[bello])>1:
                varia=conto[:]
                conto=[]
                conto=finale(selettor[bello],varia,conto)
            varia=conto[:]
        return varia    
            

     
def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    file=fparse(fileIn)
    varia=[file]
    selettor=norm(selettore)
    varia=crescendo(selettor, varia)
    return len(varia)
    



def finale(selettore, nodi,conto=[]):
    for bello in range(1, len(selettore)):
        for y in range(len(nodi)):
            conto+=children(nodi[y].content,selettore[bello])
    return conto
  
    

def elimina(file, veloce):
    if not file.istext():
        if veloce in file.content:
            del file.content[file.content.index(veloce)]
            return
        else:
            for i in file.content:
                elimina(i,veloce) 
    return
    
    
   
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dallalbero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    file=fparse(fileIn)
    varia=[file]
    selettor=norm(selettore)
    varia=crescendo(selettor, varia)
    for j in varia:
       elimina(file,j)
    with open (fileOut, 'w', encoding='utf-8') as f:
        f.write(file.to_string())


    
def cambia(veloce,chiave,valore):
    if not veloce.istext():
        veloce.attr[chiave]=valore
    return veloce
 
    
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice
    file=fparse(fileIn)
    varia=[file]
    selettor=norm(selettore)
    varia=crescendo(selettor, varia)
    for j in varia:
       cambia(j,chiave,valore)
    with open (fileOut, 'w', encoding='utf-8') as f:
        f.write(file.to_string())

