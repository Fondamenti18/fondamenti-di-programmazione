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
        seleziona un qualsiasi tag che ha id="main_window" , e' il figlio di un tag che ha class="... class1 ..." e si trova all'interno (a qualsiasi livello di distanza) di un tag      div
        
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

from  my_html import HTMLNode, fparse, parse

def pulisci_sel(nodo):
    '''Restituisce una lista i cui elementi sono i nodi che il selettore contiene separati tra di loro e sottoforma di stringhe (se sono tag semplici), tuple (attributo, valore) o simbolo '>'.'''
    primoCar = nodo[0]
    #se si tratta di un nodo della forma: @[attributo="valore"], si divide attraverso l'= e si levano i caratteri inutili
    if not nodo.isalpha() and primoCar == '@':
        sel = nodo[2:-1].split('=')
        sel[1] = sel[1][1:-1]
        return (sel[0], sel[1])
    #se si tratta di un nodo della forma: #nomeId, si aggiunge 'id' come attributo e si mette come valore il nodo senza #
    elif not nodo.isalpha() and primoCar == '#':
        return ('id', nodo[1:])
    #se si tratta di un nodo della forma: .nomeattributo, si aggiunge 'classe' come attrivuto e si mette come valore il nodo senza .
    elif not nodo.isalpha() and primoCar == '.':
        return ('class', nodo[1:])
    else:
        return nodo
    
def conta_nodi(fileIn, selettore):
    '''Ritorna il numero di nodi che soddisfano il selettore dato in input'''
    dom = fparse(fileIn)
    selettore = selettore.split(' ')
    
    listaSel = list()
    for nodo in selettore:
        listaSel.append(pulisci_sel(nodo))
    if len(listaSel)==1:
        return conta_lun1(dom, listaSel)
#    print(listaSel, '--->', conta_ricors(dom, listaSel, 0))
    return conta_ricors(dom, listaSel, 0)

def conta_lun1(self, listaSel):
    '''Funzione che esegue la ricerca analoga a quella di conta_ricors() ma lavora con listaSel di un solo elemento'''
    count = 0
    if type(listaSel[0]) == tuple:
        attr, value = listaSel[0]
        if attr in self.attr and value in self.attr[attr]:
            count += 1
    elif type(listaSel[0]) == str and self.tag == listaSel[0]: 
            count += 1

    if not self.istext():
        for c in self.content:
            count += conta_lun1(c, listaSel)
    return count
    
def conta_ricors(self, listaSel, i):
    '''Funzione ricorsiva che calcola quanti nodi del file soddisfano la sequenza di quelli contenuti nella listaSel.'''
    count = 0
    #si controlla se gli elementi da cercare sono finiti, nel caso si ritorna 1 per il conteggio
    if i == len(listaSel):
        return 1
    
#Se l'elemento in posizione i è '>', si aumenta l'indice i (per studiare l'elemento successivo) e si esegue la stessa ricerca che sta nell'elif/else sotto, con la differenza che si cerca solo nel nodo in questione (ovvero il figlio di quello precedente). Questo per assicurarsi che il nodo in posizione i+1 sia figlio stretto di quello in posizione i-1 (compreso il simbolo di maggiore).
#Nel caso in cui si trovi una corrispondenza, si aumenta l'indice e si andrà a rieseguire la funzione con l'elemento in posizione i+2, altrimenti si returna 0 perché il selettore richiesto non è stato trovato.
    if listaSel[i]=='>' and not self.istext():
        i+=1 #si incrementa l'indice per saltare l'elemento '>'
    
        if type(listaSel[i]) == str and self.tag == listaSel[i]:
            i += 1
        elif type(listaSel[i]) == tuple:
            key, value = listaSel[i]
            if key in self.attr and value in self.attr[key]:
                i += 1
        else:
            return 0
    
#In base al tipo dell'elemento in posizione i, si cerca il tag o l'attributo-valore, se si trova, si incrementa i per la chiamata successiva:
#       se è una stringa (escluso caso listaSel=='>'), si cerca il tag; 
#       se è una tupla, si unpacka e si cerca l'attributo come chiave e il valore corrispondente.
    elif type(listaSel[i])== str:
        if self.tag == listaSel[i]: 
            i += 1
    else:
        attribute, value = listaSel[i]
        if attribute in self.attr and value in self.attr[attribute]:
            i += 1
    
#In qualunque caso, si procede con il controllo dei figli (CHIAMATA DELLA FUNZIONE RICORSIVA) con la differenza che se l'elemento è stato trovato (come tag o come attributo-valore) l'indice è aumentato di 1, altrimenti continua la ricerca dello stesso elemento.
    if not self.istext():
        for figlio in self.content:
            count += conta_ricors(figlio, listaSel, i)
    return count
    
    
def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    dom = fparse(fileIn)
    selettore = selettore.split(' ')
    
    listaSel = list()
    for nodo in selettore:
        listaSel.append(pulisci_sel(nodo))
    elimina_ricors(dom, listaSel, 0)
    
    toSave = dom.to_string()
    with open (fileOut, 'w', encoding='utf=8') as fout:
        fout.write(toSave)

def elimina_ricors(self, listaSel, i):
    '''Funzione ricorsiva che elimina i nodi del file che soddisfano la sequenza di quelli contenuti nella listaSel.'''
    if self.istext(): return
    
    #si controlla se gli elementi da cercare sono finiti, nel caso si ritorna 1 per il conteggio
    if i==len(listaSel)-1:
        eliminazione(self, listaSel[i])
    
#Se l'elemento in posizione i è '>', si aumenta l'indice i (per studiare l'elemento successivo) e si esegue la stessa ricerca che sta nell'elif/else sotto, con la differenza che si cerca solo nel nodo in questione (ovvero il figlio di quello precedente). Questo per assicurarsi che il nodo in posizione i+1 sia figlio stretto di quello in posizione i-1 (compreso il simbolo di maggiore).
#Nel caso in cui si trovi una corrispondenza, si aumenta l'indice e si andrà a rieseguire la funzione con l'elemento in posizione i+2, altrimenti si returna 0 perché il selettore richiesto non è stato trovato.
    if listaSel[i]=='>':
        i+=1 #si incrementa l'indice per saltare l'elemento '>'
        
        if type(listaSel[i]) == str and self.tag == listaSel[i]:
            i += 1
        elif type(listaSel[i]) == tuple:
            key, value = listaSel[i]
            if key in self.attr and value in self.attr[key]:
                i += 1
        else:
            return
    
#In base al tipo dell'elemento in posizione i, si cerca il tag o l'attributo-valore, se si trova, si incrementa i per la chiamata successiva:
#       se è una stringa (escluso caso listaSel=='>'), si cerca il tag; 
#       se è una tupla, si unpacka e si cerca l'attributo come chiave e il valore corrispondente.
    elif type(listaSel[i])== str:
        if self.tag == listaSel[i]: 
            i += 1
    elif type(listaSel[i]) == tuple:
        attribute, value = listaSel[i]
        if attribute in self.attr and value in self.attr[attribute]:
            i += 1
    
    for figlio in self.content:
        elimina_ricors(figlio, listaSel, i)
    
def eliminazione(self, tag):
    '''Preso in input il tag, elimina il tag che lo contiene.'''
    if self.istext():
        return

    newContent = list()
    for child in self.content:
        eliminazione(child, tag)
        if child.tag == tag:
            if not child.istext():
                pass
        else:
            newContent += [child]
            
    self.content = newContent
        
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    dom = fparse(fileIn)
    selettore = selettore.split(' ')
    
    listaSel = list()
    for nodo in selettore:
        listaSel.append(pulisci_sel(nodo))
    
    cambia_ricors(dom, listaSel, 0, chiave, valore)
    
    toSave = dom.to_string()
    with open (fileOut, 'w', encoding='utf=8') as fout:
        fout.write(toSave)

def cambia_ricors(self, listaSel, i, chiave, valore):
    '''Funzione ricorsiva che seleziona i nodi del file che soddisfano la sequenza di quelli contenuti nella listaSel e ne cambia l'attributo.'''
    if self.istext():
        return
    #si controlla se gli elementi da cercare sono finiti, nel caso si ritorna 1 per il conteggio
    if i==len(listaSel)-1 and self.tag == listaSel[i]:
        self.attr[chiave] = valore

#In base al tipo dell'elemento in posizione i, si cerca il tag o l'attributo-valore, se si trova, si incrementa i per la chiamata successiva:
#       se è una stringa (escluso caso listaSel=='>'), si cerca il tag; 
#       se è una tupla, si unpacka e si cerca l'attributo come chiave e il valore corrispondente.
    if type(listaSel[i])== str:
        if self.tag == listaSel[i] and len(listaSel)==1:
            self.attr[chiave] = valore
        elif self.tag == listaSel[i]: 
            i += 1
    elif type(listaSel[i]) == tuple:
        attribute, value = listaSel[i]
        if attribute in self.attr and value in self.attr[attribute] and len(listaSel)==1:
            self.attr[chiave] = valore
        elif attribute in self.attr and value in self.attr[attribute]:
            i += 1
    
    for figlio in self.content:
        cambia_ricors(figlio, listaSel, i, chiave, valore)



if __name__=='__main__':
    fileIn    = 'slashdot.html'
    fileOut   = 'test13.html'
    fileExp   = 'risTest13-3.html'
    selettore = '#slashdot_deals-title'
    chiave    = 'style'
    valore    = 'background-color:red'
    cambia_attributo(fileIn, selettore, chiave, valore, fileOut)