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
import copy
def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    Nodo =fparse(fileIn)
    i = 0
    ris = []
    selector = selettore.split()
    #print(selector)
    a = ricorsione_conta_nodi(Nodo,selector,i,ris)
    return (a)
    
    
def ricorsione_conta_nodi(Nodo,selector,i,ris):
    if i < len(selector):
        contr = []
        lista = []
        word = selector[i]
        
        #return('cazzooooo',selector[i])
        if len(selector) == 1 and  word[0] != '.' and word[0] != '@' and word[0] != '#':
            sign = 'niente'
            op1 = selector[i]
            op2=''
            ris = controllo(Nodo,op1,op2,sign,word,contr,lista)
            
        
        if selector[i] == '>':

            
            if i +1 < len(selector) and i-1 < len(selector):
                op1 = selector[i-1]
                op2 = selector[i+1]
                sign= selector[i]
                
                             
                ris = controllo(Nodo,op1,op2,sign,word,contr,lista)
                #return (len(ris))
                
        if i +1 < len(selector) and i-1 < len(selector):
            if selector[i].isalpha() and selector[i+1].isalpha():
                op1 = selector[i]
                op2 = selector[i+1]
                sign = ''
                #print(op1,op2,sign)
                        
                ris = controllo(Nodo,op1,op2,sign,word,contr,lista)
                #return(len(ris))
        parola = selector[i]
        if parola[0] == '#':
            sign = parola[0]
            op1 = parola[1:]
            op2 = 'vuoto'
            #print(sign,op1)
            
            ris = controllo(Nodo,op1,op2,sign,word,contr,lista)
            #return(len(ris))
            #AGGIUNGERE FUNZIONE PER '#'
        if parola[0] == '.':
            
            sign = parola[0]
            op1 = parola[1:]
            op2 = 'vuoto'
            #AGGIUNGERE FUNZIONE PER '.'
            ris = controllo(Nodo,op1,op2,sign,word,contr,lista)
            #return(len(ris))
        if parola[0] == '@':
            op1 = ''
            op2 = ''
            
            sign = parola[0]
            
            #print(par,sign)
            for x in range(len(parola)):
                if parola[x] == '=':
                    
                    op1 = parola[2:x]
                    op2=parola[x+2:-2]  
            
            ris = controllo(Nodo,op1,op2,sign,word,contr,lista)
            #return(len(ris))
        return ricorsione_conta_nodi(Nodo,selector,i+1,ris)
    return (len(ris))
    
def controllo(Nodo,op1,op2,sign,word,contr,lista):
    ret = []
    
    #if Nodo.tag== word: ret+= [Nodo]
    if sign == 'niente':
        if op1 in Nodo.tag:
            ret+=[Nodo]
        
    if sign == '#':
            if 'id' in Nodo.attr:
                if Nodo.attr['id'] == op1:
                    ret += [Nodo]
    if sign == '.':
        
        if op1 in Nodo.attr:
            ret += [Nodo]
            
    if sign == '@':
        if op1 in Nodo.attr:
            if op2 == Nodo.attr[op1]:
                ret +=[Nodo]
                
    if sign == '>': 
        
        if Nodo.tag == op1: 
            for i in Nodo.content:
                
                if i.tag == op2:
                    ret+=[Nodo]
    if sign == '':
 
        
        if Nodo.tag == op1:
            
            lista.append('c')
        if len(lista) > 0 and Nodo.tag == op2:
            ret +=[Nodo]

    if not Nodo.istext():
        if len(contr)> 0 and Nodo.tag == op2:
            ret+=[Nodo]
            #print('afafdf')
        
        for child in Nodo.content:
            #print(child,lista)
            ret += controllo(child,op1,op2,sign,word,contr,lista)
    #print(ret)
    return ret
                
                
   
    
   
    
    
    
import json 

def elimina_nodi(fileIn, selettore, fileOut):
    selector = selettore.split()
    Nodo = fparse(fileIn)
    i =0
    lis =[]
    ris=[]
    ris2 = splitta2(Nodo,selector,i,ris)
    #print(ris2)
    for i in ris2:
        print(i)
        lis.append(i.tag)
        #print(i,ris)
    
    for lista in lis:
        print('cacc')
        a = ricorsione_elimina_nodi(Nodo,lista)
    
    
    testo = ''
    
    testo=Nodo.to_string()
    #print(testo)
    with open(fileOut, 'w',encoding = 'utf-8') as f:
        f.write(testo)
    
def ricorsione_elimina_nodi(Nodo,lista):   
    #'''Rimuove dall'albero tutti i nodi con il tag,
    #esclusa la radice, cioè il nodo su cui è invocato
    #il metodo.'''
    
    if Nodo.istext(): 
        #print(Nodo.to_string())
        return
    for child in Nodo.content:
        #print(child)
        ricorsione_elimina_nodi(child,lista)
    newcont=[]
    for child in Nodo.content:
        #print(child.tag)
        if child.tag == lista: 
            for i in child.content:
                
                if not i.istext():
                       newcont += i.content

        else:
            #print(child)
            newcont += [child]
    
    Nodo.content = newcont[:]
    
    
    
def splitta2(Nodo,selector,i,ris):
    if i < len(selector):
        
        contr = []
        lista = []
        word = selector[i]
        if selector[i] == '>':
            if i +1 < len(selector) and i-1 < len(selector):
                op1 = selector[i-1]
                op2 = selector[i+1]
                sign= selector[i]
                #print(op1,sign,op2)
                ris = controllo(Nodo,op1,op2,sign,word,contr,lista)
                #return(ris)
                
        if i +1 < len(selector) and i-1 < len(selector):
            if selector[i].isalpha() and selector[i+1].isalpha():
                op1 = selector[i]
                op2 = selector[i+1]
                sign = ''
                #print(op1,op2,sign)
                        
                ris = controllo(Nodo,op1,op2,sign,word,contr,lista)
                #return(ris)
        parola = selector[i]
        if parola[0] == '#':
            sign = parola[0]
            op1 = parola[1:]
            op2 = 'vuoto'
            #print(sign,op1)
            
            ris = controllo(Nodo,op1,op2,sign,word,contr,lista)
            #return(ris)
            #AGGIUNGERE FUNZIONE PER '#'
        if parola[0] == '.':
            sign = parola[0]
            op1 = parola[1:]
            op2 = 'vuoto'
            #AGGIUNGERE FUNZIONE PER '.'
            ris = controllo(Nodo,op1,op2,sign,word,contr,lista)
            #return(ris)
        if parola[0] == '@':
            op1 = ''
            op2 = ''
            
            sign = parola[0]
            
            #print(par,sign)
            for x in range(len(parola)):
                if parola[x] == '=':
                    
                    op1 = parola[2:x]
                    op2=parola[x+2:-2]  
            
            ris = controllo(Nodo,op1,op2,sign,word,contr,lista)
            #return(ris)
        splitta2(Nodo,selector,i+1,ris)    
    return(ris)
    


def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    selector = selettore.split()
    Nodo = fparse(fileIn)
    #print(Nodo)
    ris =[]
    lis=[]
    ret =[]
    i = 0
    a = splitta2(Nodo,selector,i,ris)
    for i in a:
        #print(i)
        lis.append(i.tag)
        #print(i,ris)
    
    for lista in lis:
        
        a = ric_cambia(Nodo,lista,chiave,valore,ret)
    
    
    testo = ''
    
    testo=Nodo.to_string()
    #print(testo)
    with open(fileOut, 'w',encoding = 'utf-8') as f:
        f.write(testo)
    
    
    
def ric_cambia(Nodo,lista,chiave,valore,ret):
    
    if Nodo.istext(): 
        #print(Nodo.to_string())
        return
    for child in Nodo.content:
        #print(child.tag)
        if child.tag == lista: 
            if chiave in child.attr:
                child.attr[chiave] = valore
            else:#se non è presente la chiave nel dizionario
                child.attr[chiave] = valore
                
                #print('niente')
                       
        
    for child in Nodo.content:
        #print(child)
        ric_cambia(child,lista,chiave,valore,ret)
    
    
    #Nodo.content = newcont[:]
    
    
    
    
    
    
    

