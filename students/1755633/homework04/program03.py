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

def print_tree(nodo,level):
    if nodo.istext():
        print('   '*level+'__text__'+repr(nodo.content))
    else:
        print('   '*level+str(nodo))
        for child in nodo.content:
            print_tree(child,level+1)





def create_d(selettore):  #per creare il dizionario attributi
    spec_ch=['.','#','@']
    d=dict()
    #lista=list()
    #lista_2=list()
    lista=selettore.split()
    for attr in lista:
        #print(attr)
        for elemento in spec_ch:
            if elemento in attr[0]: #se trovo un spec_ch in attr->lista splitatta da spazio
                #print('attr',attr,type(attr))
                lista_2=attr.split(elemento)
                if elemento=='.':
                    d['class']=lista_2[-1]
                if elemento=='#':
                    d['id']=lista_2[-1]
                if elemento=='@':
                    app=str()
                    for c in lista_2[-1]:
                        if c not in '][':
                            app+=c
                    app1=app.split('=')
                    appfinal=app1[1].split('\"')
                    appfinal.remove(appfinal[0])
                    appfinal.remove(appfinal[-1])
                    #print('appfinal',appfinal)
                    d[app1[0]]=appfinal[0]
                break
    return d

def conta_attr(nodo,d,lista,cont):
    '''Funzione che conta i nodi con dato attributo'''
    if not nodo.istext():
        #print('entro con', nodo.tag)
        state=0
        for k in lista:   #lista=d.keys
            #print('dizionario attr:',nodo.attr)
            if nodo.attr!={} and k in nodo.attr:
                d_nodo=nodo.attr
                #print('valori:',d_nodo.get(k))
                if d[k] in d_nodo.get(k):
                    state+=1
                    #print('attr',nodo.attr,state)
            if state==len(lista):
                #print('uguale')
                cont+=1
        for child in nodo.content:
            if not child.istext():
                cont=conta_attr(child,d,lista,cont)

    return cont

def con_padre_figlio(nodo,selettore,ind,cont): #selettore E una lista
    '''Funzione che conta i nodi con relazione padre figlio'''
    if not nodo.istext():
        #print('nodotag',nodo.tag,'=',selettore[ind])
        if nodo.tag==selettore[ind]:
            #print('si')
            if ind==(len(selettore)-1) :
                #print('incrementato',cont)
                cont+=1
                return cont
            for child in nodo.content:
                if not child.istext():
                    cont=con_padre_figlio(child,selettore,ind+1,cont)



        for child in nodo.content:
            if not child.istext():
                cont=con_padre_figlio(child,selettore,0,cont)

    return cont

def con_avo_disc(nodo,selettore,ind,cont): #selettore e una lista
    '''Funzione che CONTA i nodi con relazione avo discendente'''
    if not nodo.istext():
        for child in nodo.content:
            if not child.istext():
                #print('tag',child.tag,'=',selettore[ind])
                if child.tag==selettore[ind]:
                    if ind==(len(selettore)-1):
                        cont+=1
                        print('arrivato',cont)
                        #---return cont stesso motivo
                    #print('si, call')
                    cont=con_avo_disc(child,selettore,ind+1,cont)
                else:
                    #print('no')
                    cont=con_avo_disc(child,selettore,ind,cont)

    return cont


def rem_avo_disc(nodo,selettore,ind,dad): #selettore e una lista
    '''Funzione che RIMUOVE i nodi con relazione avo discendente'''
    if not nodo.istext():
        for child in nodo.content:
            if not child.istext():
                #print('tag',child.tag,'=',selettore[ind])
                if child.tag==selettore[ind]:
                    if ind==(len(selettore)-1):
                        print_tree(dad,0)
                        #print('arrivato',child)
                        dad_schild=dad.content
                        #####
                        child_schild=child.content
                        c=0
                        for x in dad_schild: #elimino figlio a da padre
                            #print(x,child)
                            if x==child:
                                dad_schild.remove(x)
                                '''for el_listacont_child in child.content:#inserisco filgio del figlio
                                #nel conent del padre, allo stesso posto(indice) in cui era il figlio
                                    dad_schild.insert(c,el_listacont_child)'''


                            c+=1
                        #####
                        #---dad_schild+=child.content
                        #---dad.content=dad_schild
                        #print('nuovi figli',dad,dad.content)
                        print('\nelimo',child,'\n')
                        print_tree(dad,0)
                        #print('op ef.')
                        #return nodo #levato il return perche senno non continuava a scorrere
                    #print('si, call')
                    nodo=rem_avo_disc(child,selettore,ind+1,dad)
                else:
                    #print('no')
                    dad=child
                    #print('padre',dad)
                    nodo=rem_avo_disc(child,selettore,ind,dad)
    #print('ritorno',nodo)

    return nodo



def check_selettore(root,selettore,choice,zipp=0):
    '''Funzione che richiama la funzione apposita per ogni relazione'''
    spec_ch=['@','#','.']
    for elemento in spec_ch:
        if elemento in selettore:
            d=create_d(selettore)
            #print(d)
            if choice=='count':
                print('relazione tag - choice->',choice,d)
                cont=conta_attr(root,d,d.keys(),0)
                return cont
            elif choice=='remove':
                print('funz rimuovi')
            elif choice=='edit':
                print('relazione attributo - choice->',choice,d)
                k,v=zipp
                change_attr(root,d,d.keys(),0,k,v)
                return


    if '>' in selettore:
        lista=selettore.split('>')
        #print('inizio con lista',lista)
        contatore=0
        for elemento in lista:
            #print('elemento',elemento)
            c1=str()
            for c in elemento:
                if c!=' ':
                    c1+=c
            lista[contatore]=c1
            contatore+=1
        print('Relazione padre-figlio ->', lista)
        cont=con_padre_figlio(root,lista,0,0)
        return cont


    else:
        single_tag=True
        for c in selettore:
            if c==' ':
                single_tag=False
        if single_tag==False:
            lista=selettore.split(' ')

            if choice=='count':
                print('Relazione avo-discendente ->',choice,lista)
                cont=con_avo_disc(root,lista,0,0)
                return cont

            elif choice=='remove':
                print('Relazione avo-discendente ->',choice,lista)
                cont=rem_avo_disc(root,lista,0,0)
                #print_tree(root,0)


            elif choice=='edit':
                print('Relazione avo-discendente ->',choice,lista)
                k,v=zipp
                a=change_avo_disc(root,lista,0,k,v)
        else:
            lista=list()
            lista.append(selettore)
            print('Relazione tag-',lista)
            cont=con_padre_figlio(root,lista,0,0)
            return cont



def change_attr(nodo,d,lista,cont,k1,v):
    '''Funzione che conta i nodi con dato attributo'''
    if not nodo.istext():
        #print('entro con', nodo.tag)
        state=0
        for k in lista:   #lista=d.keys
            #print('dizionario attr:',nodo.attr)
            if nodo.attr!={} and k in nodo.attr:
                d_nodo=nodo.attr
                #print('valori:',d_nodo.get(k))
                if d[k] in d_nodo.get(k):
                    state+=1
                    #print('attr',nodo.attr,state)
            if state==len(lista):
                print('uguale')
                print(nodo.attr)
                diz_nodo=nodo.attr
                diz_nodo[k1]=v
                print(nodo.attr)

                cont+=1
        for child in nodo.content:
            if not child.istext():
                change_attr(child,d,lista,cont,k1,v)

    return





def change_avo_disc(nodo,selettore,ind,k,v): #selettore e una lista
    '''Funzione che CAMBIA attributi dei nodi con relazione avo discendente'''
    if not nodo.istext():
        for child in nodo.content:
            if not child.istext():
                print('tag',child.tag,'=',selettore[ind])
                if child.tag==selettore[ind]:
                    if ind==(len(selettore)-1):
                        #print('attr di',child,'-',child.attr)
                        d_nodo=child.attr
                        d_nodo[k]=v
                        #print('attr di',child,',modificati -',child.attr)
                        #----return
                    #print('si, call')
                    change_avo_disc(child,selettore,ind+1,k,v)
                else:
                    #print('no')
                    change_avo_disc(child,selettore,ind,k,v)

    return



def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    choice='count'
    root=fparse(fileIn)
    cont=check_selettore(root,selettore,choice)
    print('res',cont)
    return cont



#conta_nodi('page1-3.html','p a')

def save_HTML(root,fileOut):
    '''FUNZIONE PER SCRIVERE .HTML SU DISCO'''
    s=root.to_string()
    #print(s)
    f=open(fileOut,'w')
    f.write(s)
    f.close


def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dallalbero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    choice='remove'
    root=fparse(fileIn)
    check_selettore(root,selettore,choice)
    #print_tree(root,0)
    save_HTML(root,fileOut)

#elimina_nodi('page1-3.html','p a','prova.html')




def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    choice='edit'
    root=fparse(fileIn)
    #print_tree(root,0)
    zipp=(chiave,valore)
    check_selettore(root,selettore,choice,zipp)
    save_HTML(root,fileOut)


cambia_attributo('slashdot.html','#slashdot_deals-title','style','background-color:red','prova.html')
