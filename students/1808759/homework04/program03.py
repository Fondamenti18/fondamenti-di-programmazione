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

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    nodo=fparse(fileIn)
    c=0
    v=clean(selettore)
    nume=conta(nodo,c,v)
    return nume

def conta(nodo,c,v):
    if not nodo.istext(): 
        if v in nodo.attr.values():
            
            c+=1
            
        for figlio in nodo.content:
                print(cn)
            conta(figlio,c,v)
    return c

def clean(selettore):
    sel=selettore
    s=''
    if '#' in sel:
        a=sel.replace('#','')
        return a
    if '.' in sel:
        a=sel.replace('.','')
        return a
    if '@' in sel:
        b=sel.split('"')
        s+=b[1]
        return s
    


    































def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    nodo=fparse(fileIn)
    v=clean(selettore)
    alb=canc(nodo,v)
    f=open(fileOut,'w')
    f.write(albe)
    nodo.close
    f.close
    
    

def canc(nodo,v):
    if not nodo.istext():
        if v in nodo.attr.values():
            print(nodo)
            del(nodo)
        
        else:
            for x in nodo.content:
                canc(x,v)
    
        
        
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice






import html

class HTMLNode(object):
    def __init__(self,tag,attr,content,closed=True):
        self.tag = tag
        # dizionario degli attributi
        self.attr = attr
        # testo per nodi _text_ o lista dei figli
        self.content = content  
        # True se il nodo ha la chiusura
        self.closed = closed    
    
    # per distinguere i nodi testo
    def istext(self):           
        return self.tag == '_text_'
    
    def open_tag(self):
        '''Ritorna la stringa del tag di inizio.'''
        if self.istext():
            return self.tag
        s = '<'+self.tag
        for k in sorted(self.attr):
            v = self.attr[k]
            # usiamo escape per i valori 
            s += ' {}="{}"'.format(k, html.escape(v,True))
        s += '>'
        return s
    
    def close_tag(self):
        '''Ritorna la stringa del tag di fine.'''
        return '</'+self.tag+'>'
    
    def print_tree(self, level=0):
        '''Stampa l'albero mostrando la struttura
        tramite indentazione'''
        if self.istext():
            print('  '*level + '_text_ ' +
                repr(self.content))
        else:
            print('  '*level + str(self))
            for child in self.content:
                child.print_tree(level+1)
    
    def to_string(self):
        '''Ritorna la stringa del documento HTML che
        corrisponde all'albero di questo nodo.'''
        if self.istext():
            # usiamo escape per i caratteri speciali
            return html.escape(self.content,False)
        s = self.open_tag()
        doc = self.open_tag()
        if self.closed:
            for child in self.content:
                doc += child.to_string()
            doc += self.close_tag()
        return doc
                
    def __str__(self):
        '''Ritorna una rappresentazione semplice
        del nodo'''
        if self.istext(): return self.tag
        else: return '<{}>'.format(self.tag)

import html.parser

class _MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        '''Crea un parser per la class HTMLNode'''
        # inizializza la class base super()
        super().__init__()
        self.root = None
        self.stack = []
    def handle_starttag(self, tag, attrs):
        '''Metodo invocato per tag aperti'''
        closed = tag not in ['img','br','meta','link']
        node = HTMLNode(tag,dict(attrs),[],closed)
        if not self.root:
            self.root = node
        if self.stack: 
            self.stack[-1].content.append(node)
        if closed:
            self.stack.append(node)
    def handle_endtag(self, tag):
        '''Metodo invocato per tag chiusi'''
        if self.stack and self.stack[-1].tag == tag:
            self.stack[-1].opentag = False
            self.stack = self.stack[:-1]
    def handle_data(self, data):
        '''Metodo invocato per il testo'''
        if not self.stack: return
        self.stack[-1].content.append(
            HTMLNode('_text_',{},data))
    def handle_comment(self, data):
        '''Metodo invocato per commenti HTML'''
        pass
    def handle_entityref(self, name):
        '''Metodo invocato per caratteri speciali'''
        if name in name2codepoint:
            c = unichr(name2codepoint[name])
        else:
            c = '&'+name
        if not self.stack: return
        self.stack[-1].content.append(
            HTMLNode('_text_',{},c))
    def handle_charref(self, name):
        '''Metodo invocato per caratteri speciali'''
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        if not self.stack: return
        self.stack[-1].content.append(
            HTMLNode('_text_',{},c))
    def handle_decl(self, data):
        '''Metodo invocato per le direttive HTML'''
        pass

def parse(html):
    '''Esegue il parsing HTML del testo html e
    ritorna la radice dell'albero.'''
    parser = _MyHTMLParser()
    parser.feed(html)
    return parser.root

def fparse(fhtml):
    '''Esegue il parsing HTML del file fhtml e
    ritorna la radice dell'albero .'''
    with open(fhtml) as f:
        root = parse(f.read())
        return root

if __name__ == '__main__':
    doc = HTMLNode('html',{},[
                HTMLNode('body',{},[
                    HTMLNode('p',{},[
                        HTMLNode('_text_',{},'Un paragrafo con '),
                            HTMLNode('em',{},[
                                HTMLNode('_text_',{},'enfasi')
                            ]),
                        HTMLNode('_text_',{},' e un\'immagine'),
                        HTMLNode('img',{'src':'img_logo.png'}, [],closed=False)
                    ])
                ])
            ])

    # stampa la struttura nell'albero
    doc.print_tree()
    # Out: <html>
    # Out:   <body>
    # Out:     <p>
    # Out:       _text_ 'Un paragrafo con '
    # Out:       <em>
    # Out:         _text_ 'enfasi'
    # Out:       _text_ " e un'immagine"
    # Out:       <img>

    # stampa la stringa HTML corrispodente
    print(doc.to_string())
    # Out: <html><body><p>Un paragrafo con <em>enfasi</em> e un'immagine<img src="img_logo.png"></p></body></html>


    # Proviamo a fare il parsing del semplice file
    # che abbiamo visto sopra.
    doc = fparse('page.html')

    doc.print_tree()

    print(doc.to_string())

