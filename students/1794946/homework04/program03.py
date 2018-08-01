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
import copy
from  my_html import HTMLNode, fparse
from bs4 import BeautifulSoup
def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    root=BeautifulSoup(open(fileIn), "html.parser")
    s=str(root.find('html'))
    t=s.replace('<html>','')
    d=t.replace('</html>','')
    g=gen_diz(['html'], [d],{})
    testo_lista_figli=g[1]
    lista_figli=g[2]
    f=gen_tree(g[0],testo_lista_figli,{'html'})
    cont=0
    selettore=pulito(selettore)
    if ' ' in selettore:
        if '>' in selettore:
            return sele(list(f.keys()), f, selettore.split(' > '),0)
        else:
            diz=crea_diz(f)
            return avi(list(diz.keys()), diz, selettore.split(' '),0)
    else:
        if len(selettore)==1:
            return ciao(list(f.keys()), selettore)
        else:
            return sele(list(f.keys()), f, [selettore],0)
def ciao(lista_chiavi, selettore):
    cont=0
    for i in lista_chiavi:
        c=i.split()
        if selettore in c:
            cont+=1
    return cont

def sele(lista_chiavi, dizionario, lista_selettori,cont):
    controllo=[]
    if cont+1!=len(lista_selettori):
        for el in lista_chiavi:
            if len( (lista_selettori)[cont])==1:
                c=el.split()
                if lista_selettori[cont] in c:
                    controllo+=dizionario[el]
            else:
                if lista_selettori[cont] in el:
                    controllo+=dizionario[el]
        return sele(controllo, dizionario, lista_selettori,cont+1)
    else:
        for el in lista_chiavi:
            if len( (lista_selettori)[cont])==1:
                c=el.split()
                if lista_selettori[cont] in c:
                    controllo.append(el)
            else:
                if lista_selettori[cont] in el:
                    controllo.append(el)
        return len(controllo)


def avi(lista_chiavi, dizionario, lista_selettori,cont):
    controllo=[]
    if cont+1!=len(lista_selettori):
        for el in lista_chiavi:
            if len( (lista_selettori)[cont])==1:
                c=el.split()
                if lista_selettori[cont] in c:
                    controllo+=dizionario[el]
            else:
                if lista_selettori[cont] in el:
                    controllo+=dizionario[el]
        return avi(controllo, dizionario, lista_selettori,cont+1)
    else:
        for el in lista_chiavi:
            if len((lista_selettori)[cont])==1:
                c=el.split()
                if lista_selettori[cont] in c:
                    controllo.append(el)
            else:
                if lista_selettori[cont] in el:
                    controllo.append(el)
        return len(controllo)



def discendenti(dizionario, elemento,lista):
    lista.append(elemento)
    for i in dizionario[elemento]:
        discendenti(dizionario, i, lista)
    return lista

def crea_diz(dizionario):
    diz2={}
    for el in dizionario:
        z=discendenti(dizionario, el,[])
        z.remove(el)
        diz2[el]=z
    return diz2



def pulito(selettore):
    lista=['#','[',']','@','.']
    q=''
    for x in selettore:
        if x not in lista:
            q+=x
    return q

def find_children(s,lista_figli, lista_figli_text):
    s=s.replace('\n','')
    if s==''or '<' and '>' not in s:
        return (lista_figli,lista_figli_text)
    nodo= (s.split('<'))[1].split('>')[0]
    nodo2=(nodo.split(' '))[0]
    nodo_text=(s.split('<'+nodo+'>'))[1].split('</'+nodo2+'>')[0]
    lista_figli_text+=[nodo_text]
    lista_figli+=[nodo]
    if nodo[-1]=='/':
        t=s.replace('<'+nodo+'>','')
        return find_children(t,lista_figli, lista_figli_text)
    t=s.replace('<'+nodo+'>'+nodo_text+'</'+nodo2+'>','')
    return find_children(t,lista_figli, lista_figli_text)

def gen_tree(dizionario,testo_lista_figli,insieme):
    c=[]
    try:
        for x in insieme:
            if dizionario[x]!=[]:
                c=gen_diz(dizionario[x], testo_lista_figli,{})
                y=list(c[0].keys())
                dizionario.update(c[0])
        return gen_tree(dizionario,c[1],y)
    except IndexError:
        return dizionario



def gen_diz(lista_figli, lista_figli_text,diz):
    children=[]
    cont=0
    c=[]
    b=[]
    for el in lista_figli:
        i=lista_figli_text[cont]
        f=find_children(i,[], [])
        c+=f[1]
        if '<' and '>' in i and i!='': 
            children+=f[0]
        else:
            children=[]
        b+=copy.deepcopy(children)
        diz[el]=copy.deepcopy(children)
        children=[]
        cont+=1
    return (diz,c,b)



def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    s= BeautifulSoup(open(fileIn), "html.parser")
    try:
        lista=s.select(selettore)
        conta=delete(lista, 0, str(s))
    except ValueError:
        lista2=['=','[',']','>',' ']
        sele=''.join(e for e in selettore if e.isalnum() or e in lista2)
        lista=s.select(sele)
        conta=delete(lista, 0, str(s))
    f=open(fileOut,'w',encoding='utf-8')
    f.write(conta)
    f.close()

def delete(lista, cont,s):
    if cont>=len(lista):
        return s
    if lista[cont]!=[]:
        o=str(lista[cont])
        if o in s:
            t=s.replace(o,'')
            cont+=1
        return delete(lista, cont,t)
    

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    s= BeautifulSoup(open(fileIn), "html.parser")
    lista=s.select(selettore)
    cambia=edit(lista, 0, str(s),chiave, valore)
    f=open(fileOut,'w',encoding='utf-8')
    f.write(cambia)
    f.close()


def edit(lista, cont,s, chiave, valore):
    if cont>=len(lista):
        return s
    if lista[cont]!=[]:
        tag=lista[cont]
        c=str(lista[cont])
        tag[chiave]=valore
        new_tag=str(tag)
        t=s.replace(c,new_tag)
        cont+=1
        return edit(lista, cont,t,chiave, valore)

