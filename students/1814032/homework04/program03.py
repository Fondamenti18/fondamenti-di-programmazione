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

checks_indexes = '.#@>'
arg_s = 'selector_check[progress][1]'
checks_functions = ['eval(["False","demn_quotes(selector_check,progress,node)"][node.attr.get("class") != None])',arg_s+' == node.attr.get("id")','node.attr.get(selector_check[progress][1][0]) == selector_check[progress][1][1]','[-progress-2,2][demn_sparkles(node,fathers,progress,selector_check)]','str(node) == '+arg_s]
checks_arguments = ['s[1:]','s[1:]','"".join(map(lambda c: [" ",c][c.isalnum()],s)).split()','"-"','"<"+s+">"']
execute_function = ['nodes_num[0] += 1','del(fathers[orig_node].content[fathers[orig_node].content.index(orig_node)])','orig_node.attr[chiave] = valore']

def conta_nodi(fileIn, selettore):
	nodes_num = [0]
	unifier(fileIn,selettore,nodes_num,0,0,0,0)
	return nodes_num[0]

def elimina_nodi(fileIn, selettore, fileOut):
	unifier(fileIn,selettore,0,0,0,1,fileOut)

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
	unifier(fileIn,selettore,0,chiave,valore,2,fileOut)

def unifier(fileIn,selettore,nodes_num,chiave,valore,f,fileOut):
	root = fparse(fileIn)
	fathers = dict()
	selector_check = []
	next(filter(lambda s: selector_check_builder(selector_check,s),selettore.split()[::-1]),True)
	scan_tree(f,root,selector_check,fathers,nodes_num,chiave,valore)
	exec(['pass','out = open(fileOut,"w",encoding="utf-8")\nout.write(root.to_string())'][f in [1,2]])

def selector_check_builder(selector_check,s):
	c_i = eval(['checks_indexes.index(s[0])','4'][s[0].isalpha()])
	selector_check.append((c_i,eval(checks_arguments[c_i])))

def scan_tree(f,node,selector_check,fathers,nodes_num,chiave,valore,father=None,progress=0):
	fathers[node] = father
	exec(['pass','analyze_nodes(fathers[node],fathers,selector_check,1,f,node,nodes_num,chiave,valore)'][eval(checks_functions[selector_check[progress][0]])])
	next(filter(lambda child: scan_tree(f,child,selector_check,fathers,nodes_num,chiave,valore,node),[[],node.content][str(node) != '_text_']),True)
	#exec(['','del(fathers[node])'][bool(d.get(fathers[node]))])
	del(fathers[node])

def analyze_nodes(node,fathers,selector_check,progress,f,orig_node,nodes_num,chiave,valore):
	exec([['analyze_nodes(fathers[node],fathers,selector_check,progress + eval(checks_functions[selector_check[progress][0]]),f,orig_node,nodes_num,chiave,valore)','pass'][(node == None) | (progress < 0)],execute_function[f]][progress == len(selector_check)])
	
def demn_quotes(selector_check,progress,node):
	return eval(arg_s+' in node.attr.get("class")')
	
def demn_sparkles(node,fathers,progress_ren,selector_check):
	progress = progress_ren+1
	return eval(checks_functions[selector_check[progress][0]])