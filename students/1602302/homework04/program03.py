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

def lavoro_sel(sito,selector):
    if selector[0]==0:
        if selector[1] in sito.attr:
            return True
    elif selector[0]==1:
        if "id" in sito.attr and sito.attr["id"]==selector[1]:
            return True
    elif selector[0]==2:
        if selector[1] in sito.attr and sito.attr[selector[1]]==selector[2]:
            return True
    elif selector[0]==3:
        if selector[1]==sito.tag:
            return True
    return False

def codifica_select(sel):
    
    if sel[0]== ".":
        #se e' una attributo la identifico con 0 e il nome dell' attributo
        return (0,sel[1:])
    elif sel[0]=="#":
        #se e' il valore di un id lo identifico con 1 e il valore
        return (1,sel[1:])
    elif sel[0]== "@" :
        #se e' un attributo generico lo identifico con 2, il tipo di attributo ed il valore
        attr=sel[2:sel.find("=")]
        value=sel[sel.find("=")+2:-2]
        return(2,attr,value)
    else:
        #se e' una tag la identifico con 3 e la tag stessa
        return(3,sel)
        
        
def determina_selettore(select):
    listasel=[]
    appoggio=select.split()
    if len(appoggio)>1:
        prev=appoggio[0]
        for elem in appoggio:
            if prev!=">" and elem!=prev and elem !=">" :
                listasel.append(" ")
            if elem!=">":
                listasel.append(codifica_select(elem))
            else:
                listasel.append(">")
            prev=elem
    else:
        listasel.append(codifica_select(select))
    return listasel

def ricorsione_avo(node,sele,out=[False,None]):
    
    if lavoro_sel(node,sele):
        out[0]=True
        out[1]=node
        return out
    
    for figlio in node.content:
        if not figlio.istext():
            out=ricorsione_avo(figlio,sele,out)
        
    return out

def ricorsione_cont(sito,selector,cont=0):

    latest= None
    flagM=0
    flagS=0
    check=False
    appoggio=None
    for selec in selector:
        if selec==">":
            flagM=1
            continue
        elif selec==" ":
            flagS=1
            continue        
        
        if selec!=">" and selec != " ":
            #se il prossimo e' un figlio di padre
            if flagM==1:
                for son in latest.content:
                    if lavoro_sel(son,selec):
                        latest=son
                        flagM=0
                else:
                    if flagM==1:
                        break
            #se il prossimo e' un discendente di avo, la funzione ricorsione_avo ritorna una lista dove al primo valore ce' true se ce' la presenza di un discendente e al secondo posto il discendente stesso        
            elif flagS==1:
                appoggio=ricorsione_avo(latest,selec)
                if appoggio[0]:
                    latest=appoggio[1]
                    flagS=0
                else:
                    break
            #se nessuno dei due e' il primo
            else:
                if lavoro_sel(sito,selec):
                    latest=sito
                    continue
                else:
                    #reset
                    break
        #se selec non e' un selettore alza flag per prossimo ciclo

    else:
        check=True
    if check:
        cont+=1
        

        
    for figlii in sito.content:
        if not figlii.istext():
            cont=ricorsione_cont(figlii,selector,cont)
    return cont



def ricorsione_del(sito,selector):
    latest= None
    flagM=0
    flagS=0
    check=False
    appoggio=None
    padrelatest=None
    for selec in selector:
        if selec==">":
            flagM=1
            continue
        elif selec==" ":
            flagS=1
            continue        
        
        if selec!=">" and selec != " ":
            #se il prossimo e' un figlio di padre
            if flagM==1:
                for son in latest.content:
                    if lavoro_sel(son,selec):
                        padrelatest=latest
                        latest=son
                        flagM=0
                else:
                    if flagM==1:
                        break
            #se il prossimo e' un discendente di avo, la funzione ricorsione_avo ritorna una lista dove al primo valore ce' true se ce' la presenza di un discendente e al secondo posto il discendente stesso        
            elif flagS==1:
                appoggio=ricorsione_avo_del(latest,selec)
                if appoggio[0]:
                    latest=appoggio[1]
                    padrelatest=appoggio[2]
                    flagS=0
                else:
                    break
            #se nessuno dei due e' il primo
            else:
                if lavoro_sel(sito,selec):
                    latest=sito
                    continue
                else:
                    #reset
                    break
        #se selec non e' un selettore alza flag per prossimo ciclo

    else:
        check=True
    if check:
        padrelatest.content.remove(latest)

        
    for figlii in sito.content:
        if not figlii.istext():
            ricorsione_del(figlii,selector)
    return sito

def ricorsione_change(sito,selector,chiave,valore):

    latest= None
    flagM=0
    flagS=0
    check=False
    appoggio=None
    for selec in selector:
        if selec==">":
            flagM=1
            continue
        elif selec==" ":
            flagS=1
            continue        
        
        if selec!=">" and selec != " ":
            #se il prossimo e' un figlio di padre
            if flagM==1:
                for son in latest.content:
                    if lavoro_sel(son,selec):
                        latest=son
                        flagM=0
                else:
                    if flagM==1:
                        break
            #se il prossimo e' un discendente di avo, la funzione ricorsione_avo ritorna una lista dove al primo valore ce' true se ce' la presenza di un discendente e al secondo posto il discendente stesso        
            elif flagS==1:
                appoggio=ricorsione_avo(latest,selec)
                if appoggio[0]:
                    latest=appoggio[1]
                    flagS=0
                else:
                    break
            #se nessuno dei due e' il primo
            else:
                if lavoro_sel(sito,selec):
                    latest=sito
                    continue
                else:
                    #reset
                    break
        #se selec non e' un selettore alza flag per prossimo ciclo

    else:
        check=True
    if check:
        latest.attr[chiave]=valore

        
    for figlii in sito.content:
        if not figlii.istext():
            ricorsione_change(figlii,selector,chiave,valore)
    return sito

def ricorsione_avo_del(node,sele,out=[False,None,None]):
    
    for son in node.content:
        if lavoro_sel(son,sele):
            out[0]=True
            out[1]=son
            out[2]=node
            return out

    for figlio in node.content:
        if not figlio.istext():
            out=ricorsione_avo_del(figlio,sele,out)
        
    return out        

def conta_nodi(fileIn, selettore):
    site=fparse(fileIn)
    selector=determina_selettore(selettore)
    out=ricorsione_cont(site,selector)
    return out

def elimina_nodi(fileIn, selettore, fileOut):
    site=fparse(fileIn)
    selector=determina_selettore(selettore)
    siteout=ricorsione_del(site,selector)
    output=open(fileOut,"w")
    output.write(siteout.to_string())
    output.close()
    return 0
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    site=fparse(fileIn)
    selector=determina_selettore(selettore)
    siteout=ricorsione_change(site,selector,chiave,valore)
    output=open(fileOut,"w")
    output.write(siteout.to_string())
    output.close()
    return 0






















