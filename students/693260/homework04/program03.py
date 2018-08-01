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

from my_html import HTMLNode, fparse

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def __init__(self):
        '''Crea un parser per la class HTMLNode'''
        super().__init__()
        
        self.root = None
        
        self.stack = []
    
        self.htmltree = {}
        
    def handle_starttag(self, tag, attrs):
        '''Metodo invocato per tag aperti'''
                     
        closed = tag not in ['img','br']
        
        node = HTMLNode(tag, dict(attrs), [], closed)
        
        if not self.root:
            
            self.root = node
            
            #self.htmltree[node] = (dict(attrs), [], 'root')
                        
        if self.stack:
            
            self.stack[-1].content.append(node)
                        
        if closed:
            
            self.stack.append(node)
            
            if node != self.root:
           
                if closed:
                    
                    self.htmltree[node] = (tag, dict(attrs), [], self.stack[-2])
                
                else:
                    
                    self.htmltree[node] = (tag, dict(attrs), [], self.stack[-1])
                
            else:
                
                self.htmltree[node] = (tag, dict(attrs), [], None)
                
        else:
            
            self.htmltree[node] = (tag, dict(attrs), [], self.stack[-1])
        
        if node != self.root:
            
            if closed:
                
                self.htmltree[self.stack[-2]][2].append(node)
                
            else:
                
                self.htmltree[self.stack[-1]][2].append(node)
    
    def restituiscialbero(self):
        
        return self.htmltree
    
    def restituiscielencofoglie(self):
        
        elencofoglie = []
        
        for elemento in self.htmltree:
            
            if self.htmltree[elemento][2] == []:

                elencofoglie.append(elemento)
                
        return elencofoglie
    
    def handle_endtag(self, tag):
        
        '''Metodo invocato per tag chiusi'''
        
        if self.stack and self.stack[-1].tag == tag:
            
            self.stack[-1].opentag = False
            
            self.stack = self.stack[:-1]
                        
    def handle_data(self, data):
        
        '''Metodo invocato per il testo'''
        if not self.stack: return
        
        self.stack[-1].content.append(HTMLNode('_text_',{},data))
                       
def fparse(fhtml):
    
    '''Esegue il parsing HTML del file fhtml e ritorna la radice dell'albero .'''
    
    with open(fhtml) as f: html=f.read()
    
    htmlparser = MyHTMLParser()

    htmlparser.feed(html)
    
    return htmlparser

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    #Inserite qui il vostro codice
        
    albero = fparse(fileIn)

    alberohtml = albero.restituiscialbero()
    
    selettoreCSS = selettore.split(" ")
    
    selettoreCSS = invertiselettore(selettoreCSS)
    
    contatoreselettoritrovati = 0
    
    elencofoglie = albero.restituiscielencofoglie()
    
    elenconodigiatrovati = []
    
    for foglia in elencofoglie:
        
        np = foglia
        
        for elementoselettore in range(0, len(selettoreCSS)):
            
            if selettoreCSS[elementoselettore] == '>':
                
                nodotrovato = trovanodo(alberohtml, np, selettoreCSS[elementoselettore + 1])
                
                elementoselettore + 1
                
                if nodotrovato != elenconodigiatrovati[-1][3]:
                        
                        break
                    
            else:
                
                nodotrovato = trovanodo(alberohtml, np, selettoreCSS[elementoselettore])
                               
            if nodotrovato == None:
                
                break
            
            else:
            
                if nodotrovato in elenconodigiatrovati:
                    
                    nodotrovato = None
                    
                else:
                    
                    elenconodigiatrovati.append(nodotrovato)
            
        if nodotrovato != None:
            
            contatoreselettoritrovati += 1
            
        nodotrovato = None
        
    return contatoreselettoritrovati   
    
    
       
def contanodi(selettore, risultato, nomeattributocercato = "class"):
    
    return risultato
    

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

def invertiselettore(selettore):
    
    tmpselettore = []
    
    for indiceselettore in range(len(selettore) - 1, -1, -1):
        
        tmpselettore.append(selettore[indiceselettore])
        
    return tmpselettore
       
    
def trovanodo(alberohtml, np, ndt):
    
    npadre = alberohtml[np][3]
    
    if npadre != None:
        
        #print("Sono qui e sto analizzando:", alberohtml[np][0])
        
        if ndt.startswith('.'):
            
            attributi = alberohtml[np][1]
            
            for attributo in attributi:
                
                if attributo == 'class':
                    
                    elencovaloriclasse = attributi[attributo].split(" ")
                    
                    if ndt[1:] in elencovaloriclasse:
                    
                        return alberohtml[np]
                    
            return None
                   
        elif ndt.startswith('#'):
            
            attributi = alberohtml[np][1]
            
            for attributo in attributi:
                
                if attributi[attributo] == ndt[1:]:
                    
                    return alberohtml[np]
                    
                else:
        
                    return trovanodo(alberohtml, npadre, ndt)      
                          
        elif ndt.startswith('@'):
           
            proprieta = ndt[1:].replace("[","").replace("]","")
                        
            proprieta = proprieta.split('=')
          
            attributi = alberohtml[np][1]
            
            for attributo in attributi:
                
                if attributo == proprieta[0] and attributi[attributo] == proprieta[1].replace("\"", ""):
                    
                    return alberohtml[np]
                
            return None
            
            
            
            
            
            
            
        else:
            
            if alberohtml[np][0] == ndt:
                
                return alberohtml[np]
            
            else:
            
                return trovanodo(alberohtml, npadre, ndt) 
            
                          
    else:
        
        if alberohtml[np][0] == ndt:
            
            return alberohtml[np]
        
        else:
        
            return None
        
