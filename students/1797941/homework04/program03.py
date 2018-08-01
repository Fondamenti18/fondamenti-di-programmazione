#--------------------------------------------FUN RICERCA----------------------------------------------#
from  my_html import HTMLNode, fparse
import json

def switch_selettore(nodo,selettore,ls):
    ls = []
    if selettore[0]=='.':
#        print("class",selettore)
        return trova_attr(nodo,"class",selettore[1:],ls)
    elif selettore[0]=='#':
#        print("#   ",selettore)
        return trova_attr(nodo,"id",selettore[1:],ls)
    elif selettore[0]=="@":
#        print("@   ",selettore)
        attr = selettore[2:-2].split('="')
#        print(attr[0],"-",attr[1])
        return trova_attr(nodo,attr[0],attr[1],ls)
    else:
#        print('tag',selettore)
        return trova_tag(nodo,selettore,ls)
    

def trova_attr(nodo,tipo_attr,val_attr,ls=[]):
    if not(nodo.istext()):
        if tipo_attr in nodo.attr:
            if tipo_attr == 'class':
                if val_attr in nodo.attr[tipo_attr].split():
#                    print(nodo.tag,"   ",nodo.attr[tipo_attr])
                    ls.append(nodo)
            elif val_attr == nodo.attr[tipo_attr]:
#                print(nodo.tag,"   ",nodo.attr[tipo_attr])
                ls.append(nodo)
        for figlio in nodo.content:
            trova_attr(figlio,tipo_attr,val_attr,ls)
        return ls

def trova_tag(nodo,tag,ls=[],lvl=None):
    if not(nodo.istext()):
        if tag == nodo.tag:
#                print(nodo.tag)
            ls.append(nodo)
        for figlio in nodo.content:
            trova_tag(figlio,tag,ls)
        return ls
        
def fun_magg(ls_root,selettore,lvl):
    node_list=[]
    set_figli = set()
    for el in ls_root:
        node_list+=switch_selettore(el,selettore[lvl+1],[])
        set_figli.update(el.content)
    return list(set_figli.intersection(node_list))
    
def fun_AD(ls_root,selettore,lvl):
    node_list=[]
    for el in ls_root:
        node_list+=switch_selettore(el,selettore[lvl],[])
    return node_list

def main_fun(ls_root,selettore,lvl=0):
#    ls = switch_selettore(root,selettore[0],[])
#    ls = switch_selettore(root,'#img1',ls)
#    print("return: ",[l.tag for l in ls])
    node_list = []
    if selettore[lvl] == '>':
        node_list=fun_magg(ls_root,selettore,lvl)
        lvl+=1  
    else:
        node_list=fun_AD(ls_root,selettore,lvl)
            #print("-"*(lvl+1),[l.tag for l in node_list])
    if lvl == len(selettore)-1: return node_list
    else: return main_fun(node_list,selettore,lvl+1)
    
#--------------------------------------------CONTA-----------------------------------------------#

def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    dom = fparse(fileIn)
    ls_nodi = main_fun([dom],selettore.split())
#    print("ls_nodi: ",[l.tag for l in ls_nodi])
    return len(ls_nodi)

#--------------------------------------------ELIMINA-----------------------------------------------#

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    dom = fparse(fileIn)
    
    ls_nodi = main_fun([dom],selettore.split())
    elimina_albero(dom,ls_nodi)
    with open(fileOut,mode="w") as f:
        f.write(dom.to_string())

def elimina_albero(root,res_list,livello=0):
    if not(root.istext()):
        if root in res_list:
            res_list.remove(root)
            return True
        for figlio in root.content:
            if elimina_albero(figlio,res_list,livello+1):
                root.content.remove(figlio)
    

#--------------------------------------------MODIFICA----------------------------------------------#

        
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    dom = fparse(fileIn)
    ls_nodi = main_fun([dom],selettore.split())
    modifica_albero(dom,ls_nodi,chiave,valore)
    with open(fileOut,mode="w") as f:
        f.write(dom.to_string())

def modifica_albero(root,res_list,chiave,valore,livello=0):
    if not(root.istext()):
        if root in res_list:
            return True
        for figlio in root.content:
            if modifica_albero(figlio,res_list,chiave,valore,livello+1):
                figlio.attr[chiave] = valore
    

#root = fparse("page1-3.html")
#selettore= 'p > em'
#selettore=selettore.split()
#print("selettore: ",selettore.split(),"\n\n")
#print(switch_selettore(root,selettore,[])[0].attr['id'])         
#main_fun([root],selettore,0)
#print(conta_nodi("page1-3.html",selettore))











